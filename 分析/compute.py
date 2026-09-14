import json, numpy as np
from scipy import stats
codes = [(0,0,0),(0,2,2),(1,2,2),(2,0,2),(2,1,2),(2,2,2),(2,3,2),(2,2,0),(2,2,1),(2,2,3),(3,2,2),(1,1,2),(1,2,1),(2,1,1)]
labels = [f"N{c[0]}P{c[1]}K{c[2]}" for c in codes]
plot = np.array([19.8,20.5,22.8,23.6,25.1,27.6,28.9,26.2,27.8,30.6,27.5,23.9,24.7,24.8])
Nlv=np.array([0,135,270,405.]); Plv=np.array([0,90,180,270.]); Klv=np.array([0,112.5,225,337.5])
N=np.array([Nlv[c[0]] for c in codes]); P=np.array([Plv[c[1]] for c in codes]); K=np.array([Klv[c[2]] for c in codes])
y=plot*10000/30; ymu=plot*667/30
# prices
urea, ssp, kcl = 2.10, 0.80, 3.20     # 元/kg 实物
pN, pP, pK = urea/0.463, ssp/0.12, kcl/0.60
py = 2.58
ck=y[0]; full=y[5]
eff=np.array([13.9,14.0,15.3,16.3,16.9,17.6,18.2,18.1,18.1,18.4,19.1,15.9,16.1,16.8])
tot=np.array([187.5,189.7,192.1,194.6,195.9,202.5,203.8,196.1,201.3,208.9,202.5,194.4,196.8,195.3])
fg=np.array([161.3,165.1,167.5,164.6,167.1,175.2,176.7,165.1,172.5,183.1,163.0,169.1,171.7,166.0])
sr=np.array([86.0,87.0,87.2,84.6,85.3,86.5,86.7,84.2,85.7,87.6,80.5,87.0,87.2,85.0])
tgw=np.array([23.2,23.3,23.3,23.1,23.4,23.5,23.6,23.1,23.3,23.8,23.1,23.4,23.5,23.3])
ph=np.array([115.2,116.1,118.1,118.5,118.6,118.9,118.9,118.9,119.0,119.2,120.7,118.7,118.8,118.6])
pl=np.array([23.8,23.9,24.1,24.2,24.3,24.7,24.8,24.5,24.6,25.1,25.8,24.2,24.4,24.3])
def fit(X, yy):
    b,*_=np.linalg.lstsq(X,yy,rcond=None); yhat=X@b; ssr=((yy-yhat)**2).sum(); sst=((yy-yy.mean())**2).sum()
    n,p=X.shape; dfr=n-p; R2=1-ssr/sst; F=((sst-ssr)/(p-1))/(ssr/dfr) if dfr>0 else float('nan'); pv=1-stats.f.cdf(F,p-1,dfr) if dfr>0 else float('nan')
    return b,R2,F,pv,dfr
out={}
out['prices']={'urea':urea,'ssp':ssp,'kcl':kcl,'N':round(pN,2),'P2O5':round(pP,2),'K2O':round(pK,2),'rice':py}
rows=[]
for i in range(14):
    cost=N[i]*pN+P[i]*pP+K[i]*pK; val=y[i]*py; inc=y[i]-ck; incval=inc*py
    rows.append({'no':i+1,'label':labels[i],'N':N[i],'P':P[i],'K':K[i],'plot_kg':plot[i],'y_hm2':round(y[i],1),'y_mu':round(ymu[i],1),
      'inc_vs_ck':round(inc,1),'inc_pct':round(inc/ck*100,1),'rank':0,
      'ph':ph[i],'pl':pl[i],'eff_hm2':round(eff[i]*15,1),'tot':tot[i],'fg':fg[i],'sr':sr[i],'tgw':tgw[i],
      'theory_hm2':round(eff[i]*15e4*fg[i]*tgw[i]/1e6,0),
      'value':round(val,1),'cost':round(cost,1),'net':round(val-cost,1),'incval':round(incval,1),'incnet':round(incval-cost,1),'ratio':(round(incval/cost,2) if cost>0 else None)})
order=sorted(range(14), key=lambda i:-y[i])
for r,i in enumerate(order): rows[i]['rank']=r+1
out['rows']=rows
# ternary
X3=np.column_stack([np.ones(14),N,P,K,N**2,P**2,K**2,N*P,N*K,P*K]); b,R2,F,pv,dfr=fit(X3,y)
H=np.array([[2*b[4],b[7],b[8]],[b[7],2*b[5],b[9]],[b[8],b[9],2*b[6]]]); g=b[1:4]; xs=np.linalg.solve(H,-g)
out['ternary']={'coef':[round(v,6) for v in b],'R2':round(R2,4),'F':round(F,3),'p':round(pv,4),'df':dfr,'stationary':[round(v,1) for v in xs],'eigH':[round(v,5) for v in np.linalg.eigvals(H)]}
# single factor quadratics
sf={}
for f,idx,x,pr in [('N',[1,2,5,10],N,pN),('P',[3,4,5,6],P,pP),('K',[7,8,5,9],K,pK)]:
    xx=x[idx]; yy=y[idx]; X1=np.column_stack([np.ones(4),xx,xx**2]); b1,R21,F1,pv1,d1=fit(X1,yy)
    xmax=-b1[1]/(2*b1[2]); ymax=b1[0]+b1[1]*xmax+b1[2]*xmax**2; xe=(pr/py-b1[1])/(2*b1[2]); ye=b1[0]+b1[1]*xe+b1[2]*xe**2
    sf[f]={'x':list(xx),'y':[round(v,1) for v in yy],'coef':[round(v,6) for v in b1],'R2':round(R21,4),'F':round(F1,2),'p':round(pv1,3),'xmax':round(xmax,1),'ymax':round(ymax,1),'xeco':round(xe,1),'yeco':round(ye,1),'typical':bool(b1[1]>0 and b1[2]<0)}
out['single']=sf
# N linear plus plateau
xN=np.array([0,135,270,405.]); yN=y[[1,2,5,10]]
best=None
for x0 in np.arange(135,405,0.5):
    A=np.column_stack([np.ones(4),np.minimum(xN,x0)]); c,*_=np.linalg.lstsq(A,yN,rcond=None); ss=((yN-A@c)**2).sum()
    if best is None or ss<best[0]: best=(ss,x0,c)
ss,x0,c=best; sst=((yN-yN.mean())**2).sum()
out['N_lpp']={'a':round(c[0],1),'b':round(c[1],3),'x0':round(x0,1),'plateau':round(c[0]+c[1]*x0,1),'R2':round(1-ss/sst,4)}
# linear fits P, K
for f,xx,yy in [('P',np.array([0,90,180,270.]),y[[3,4,5,6]]),('K',np.array([0,112.5,225,337.5]),y[[7,8,5,9]])]:
    A=np.column_stack([np.ones(4),xx]); cc,*_=np.linalg.lstsq(A,yy,rcond=None); ss=((yy-A@cc)**2).sum(); sst=((yy-yy.mean())**2).sum(); r=np.corrcoef(xx,yy)[0,1]
    out[f+'_lin']={'a':round(cc[0],1),'b':round(cc[1],3),'R2':round(1-ss/sst,4),'r':round(r,4)}
# deficiency
de={}
for nm,t,amt in [('N',2,270),('P',4,180),('K',8,225)]:
    de[nm]={'yield':round(y[t-1],1),'rel':round(y[t-1]/full*100,1),'contrib':round((full-y[t-1])/full*100,1),'ae':round((full-y[t-1])/amt,2)}
de['CK']={'yield':round(ck,1),'rel':round(ck/full*100,1),'contrib':round((full-ck)/full*100,1)}
out['deficiency']=de
# marginal
mg=[]
for nm,seq,amt,pr in [('N',[2,3,6,11],135,pN),('P',[4,5,6,7],90,pP),('K',[8,9,6,10],112.5,pK)]:
    ys=[y[i-1] for i in seq]
    for j in range(1,4):
        dy=ys[j]-ys[j-1]; mg.append({'f':nm,'from':j-1,'to':j,'dy':round(dy,1),'dval':round(dy*py,1),'cost':round(amt*pr,1),'ratio':round(dy*py/(amt*pr),2)})
out['marginal']=mg
# correlations
cor={}
for nm,v in [('株高',ph),('穗长',pl),('有效穗',eff),('每穗总粒数',tot),('每穗实粒数',fg),('结实率',sr),('千粒重',tgw)]:
    r=np.corrcoef(v,y)[0,1]; t=r*np.sqrt(12/(1-r*r)); p=2*(1-stats.t.cdf(abs(t),12)); cor[nm]={'r':round(r,3),'p':round(p,4)}
out['corr']=cor
# ranges of traits
out['trait_range']={k:[float(v.min()),float(v.max())] for k,v in [('ph',ph),('pl',pl),('eff',eff*15),('tot',tot),('fg',fg),('sr',sr),('tgw',tgw)]}
json.dump(out,open('data.json','w'),ensure_ascii=False,indent=1)
print(json.dumps({k:out[k] for k in ['prices','ternary','single','N_lpp','P_lin','K_lin','deficiency','marginal','corr']},ensure_ascii=False,indent=1))
print("\nrows:")
for r in rows: print(r)
