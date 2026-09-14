import numpy as np
from scipy import stats, optimize
codes = [(0,0,0),(0,2,2),(1,2,2),(2,0,2),(2,1,2),(2,2,2),(2,3,2),(2,2,0),(2,2,1),(2,2,3),(3,2,2),(1,1,2),(1,2,1),(2,1,1)]
plot = np.array([19.8,20.5,22.8,23.6,25.1,27.6,28.9,26.2,27.8,30.6,27.5,23.9,24.7,24.8])
Nlv = np.array([0,135,270,405.]); Plv=np.array([0,90,180,270.]); Klv=np.array([0,112.5,225,337.5])
N = np.array([Nlv[c[0]] for c in codes]); P=np.array([Plv[c[1]] for c in codes]); K=np.array([Klv[c[2]] for c in codes])
y = plot*10000/30
def fit(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    yhat = X@b; ss_res = ((y-yhat)**2).sum(); ss_tot=((y-y.mean())**2).sum()
    n,p = X.shape; df_r = n-p; R2 = 1-ss_res/ss_tot
    F = ((ss_tot-ss_res)/(p-1))/(ss_res/df_r); pval = 1-stats.f.cdf(F, p-1, df_r)
    return b, R2, F, pval, df_r
print("=== reduced ternary (no interactions) ===")
X = np.column_stack([np.ones(14),N,P,K,N**2,P**2,K**2]); b,R2,F,pv,dfr=fit(X,y)
print(np.round(b,5), f"R2={R2:.4f} F={F:.2f} p={pv:.4f} df={dfr}")
print("=== ternary linear ===")
X = np.column_stack([np.ones(14),N,P,K]); b,R2,F,pv,dfr=fit(X,y)
print(np.round(b,5), f"R2={R2:.4f} F={F:.2f} p={pv:.4f} df={dfr}")
# t-tests for linear model
Xl=X; n,p=Xl.shape; res=y-Xl@b; s2=(res**2).sum()/(n-p); cov=s2*np.linalg.inv(Xl.T@Xl); se=np.sqrt(np.diag(cov)); t=b/se
print(" se=",np.round(se,4)," t=",np.round(t,3)," p=",np.round(2*(1-stats.t.cdf(abs(t),n-p)),4))
print("=== N quadratic + P linear + K linear ===")
X = np.column_stack([np.ones(14),N,N**2,P,K]); b,R2,F,pv,dfr=fit(X,y)
print(np.round(b,5), f"R2={R2:.4f} F={F:.2f} p={pv:.4f} df={dfr}")
n,p=X.shape; res=y-X@b; s2=(res**2).sum()/(n-p); cov=s2*np.linalg.inv(X.T@X); se=np.sqrt(np.diag(cov)); t=b/se
print(" se=",np.round(se,4)," t=",np.round(t,3)," p=",np.round(2*(1-stats.t.cdf(abs(t),n-p)),4))
print(" N max=", -b[1]/(2*b[2]), " N econ=", (5.0/2.6-b[1])/(2*b[2]))
# linear plus plateau for N (T2,T3,T6,T11)
print("=== N linear-plus-plateau ===")
xN=np.array([0,135,270,405.]); yN=np.array([6833.3,7600,9200,9166.7])
def lpp(x,a,b,x0): return np.where(x<x0, a+b*x, a+b*x0)
best=None
for x0 in np.arange(150,405,0.5):
    A=np.column_stack([np.ones(4), np.minimum(xN,x0)]); c,*_=np.linalg.lstsq(A,yN,rcond=None)
    ss=((yN-A@c)**2).sum()
    if best is None or ss<best[0]: best=(ss,x0,c)
ss,x0,c=best; sst=((yN-yN.mean())**2).sum()
print(f" a={c[0]:.1f} b={c[1]:.3f} x0={x0:.1f} plateau={c[0]+c[1]*x0:.1f} R2={1-ss/sst:.4f}")
# Also LPP for P and K
for nm,xx,yy in [('P',np.array([0,90,180,270.]),np.array([7866.7,8366.7,9200,9633.3])),('K',np.array([0,112.5,225,337.5]),np.array([8733.3,9266.7,9200,10200]))]:
    A=np.column_stack([np.ones(4),xx]); c,*_=np.linalg.lstsq(A,yy,rcond=None); ss=((yy-A@c)**2).sum(); sst=((yy-yy.mean())**2).sum()
    r=np.corrcoef(xx,yy)[0,1]; 
    print(f" {nm} linear: a={c[0]:.1f} b={c[1]:.3f} R2={1-ss/sst:.4f} r={r:.4f} p={2*(1-stats.t.cdf(abs(r)*np.sqrt(2/(1-r*r)),2)):.3f}")
# Marginal analysis between adjacent levels
print("=== marginal returns (元/hm2), prices N5.0 P7.0 K5.5 rice2.6 ===")
for nm,seq,amt,pr in [('N',[2,3,6,11],135,5.0),('P',[4,5,6,7],90,7.0),('K',[8,9,6,10],112.5,5.5)]:
    ys=[y[i-1] for i in seq]
    for j in range(1,4):
        dy=ys[j]-ys[j-1]; print(f" {nm} level{j-1}->{j}: dy={dy:.0f} kg, 增值={dy*2.6:.0f}, 成本={amt*pr:.0f}, 边际产投比={dy*2.6/(amt*pr):.2f}")
# Yield component correlations with yield
eff=np.array([13.9,14.0,15.3,16.3,16.9,17.6,18.2,18.1,18.1,18.4,19.1,15.9,16.1,16.8])*15
tot=np.array([187.5,189.7,192.1,194.6,195.9,202.5,203.8,196.1,201.3,208.9,202.5,194.4,196.8,195.3])
fg=np.array([161.3,165.1,167.5,164.6,167.1,175.2,176.7,165.1,172.5,183.1,163,169.1,171.7,166])
sr=np.array([86,87,87.2,84.6,85.3,86.5,86.7,84.2,85.7,87.6,80.5,87,87.2,85])
tgw=np.array([23.2,23.3,23.3,23.1,23.4,23.5,23.6,23.1,23.3,23.8,23.1,23.4,23.5,23.3])
ph=np.array([115.2,116.1,118.1,118.5,118.6,118.9,118.9,118.9,119.0,119.2,120.7,118.7,118.8,118.6])
pl=np.array([23.8,23.9,24.1,24.2,24.3,24.7,24.8,24.5,24.6,25.1,25.8,24.2,24.4,24.3])
print("=== correlation with yield (n=14) ===")
for nm,v in [('株高',ph),('穗长',pl),('有效穗',eff),('总粒数',tot),('实粒数',fg),('结实率',sr),('千粒重',tgw)]:
    r=np.corrcoef(v,y)[0,1]; t=r*np.sqrt(12/(1-r*r)); p=2*(1-stats.t.cdf(abs(t),12))
    print(f" {nm}: r={r:.3f} p={p:.4f}")
print("r0.05(12)=0.532 r0.01(12)=0.661")
