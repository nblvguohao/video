import numpy as np
from scipy import stats
np.set_printoptions(precision=4, suppress=True)

# ---- data ----
codes = [(0,0,0),(0,2,2),(1,2,2),(2,0,2),(2,1,2),(2,2,2),(2,3,2),(2,2,0),(2,2,1),(2,2,3),(3,2,2),(1,1,2),(1,2,1),(2,1,1)]
plot = np.array([19.8,20.5,22.8,23.6,25.1,27.6,28.9,26.2,27.8,30.6,27.5,23.9,24.7,24.8])  # kg / 30 m2
Nlv = np.array([0,135,270,405.]); Plv=np.array([0,90,180,270.]); Klv=np.array([0,112.5,225,337.5])
N = np.array([Nlv[c[0]] for c in codes]); P=np.array([Plv[c[1]] for c in codes]); K=np.array([Klv[c[2]] for c in codes])
y_hm = plot*10000/30           # kg/hm2
y_mu = plot*667/30             # kg/667m2
print("yield kg/hm2:", np.round(y_hm,1))
print("yield kg/667m2:", np.round(y_mu,1))

# prices 元/kg
pN, pP, pK, py = 5.0, 7.0, 5.5, 2.6

def fit(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    yhat = X@b; ss_res = ((y-yhat)**2).sum(); ss_tot=((y-y.mean())**2).sum()
    n,p = X.shape; df_r = n-p
    R2 = 1-ss_res/ss_tot
    F = ((ss_tot-ss_res)/(p-1))/(ss_res/df_r) if df_r>0 else np.nan
    pval = 1-stats.f.cdf(F, p-1, df_r) if df_r>0 else np.nan
    return b, R2, F, pval, df_r, yhat

# ---- ternary quadratic ----
X3 = np.column_stack([np.ones(14), N, P, K, N**2, P**2, K**2, N*P, N*K, P*K])
b, R2, F, pv, dfr, yhat = fit(X3, y_hm)
names = ['b0','N','P','K','N2','P2','K2','NP','NK','PK']
print("\n=== ternary quadratic (kg/hm2) ===")
for n_,v in zip(names,b): print(f"{n_:>3} = {v: .6f}")
print(f"R2={R2:.4f} F={F:.3f} p={pv:.4f} df_res={dfr}")
print("fitted:", np.round(yhat,0))
# stationary point
H = np.array([[2*b[4], b[7], b[8]],[b[7],2*b[5],b[9]],[b[8],b[9],2*b[6]]])
g = np.array([b[1],b[2],b[3]])
xs = np.linalg.solve(H, -g)
print("stationary point (N,P,K):", xs, "eig(H):", np.linalg.eigvals(H))
def y3(n,p,k): return b[0]+b[1]*n+b[2]*p+b[3]*k+b[4]*n*n+b[5]*p*p+b[6]*k*k+b[7]*n*p+b[8]*n*k+b[9]*p*k
print("y at stationary:", y3(*xs))
# economic optimum: grad = price ratio
xe = np.linalg.solve(H, np.array([pN/py,pP/py,pK/py])-g)
print("econ optimum (N,P,K):", xe, "y:", y3(*xe))
# constrained grid search within domain
best=None; bestE=None
for n_ in np.arange(0,405.1,1.5):
    for p_ in np.arange(0,270.1,1.5):
        for k_ in np.arange(0,337.6,1.5):
            yy=y3(n_,p_,k_)
            prof = yy*py - (n_*pN+p_*pP+k_*pK)
            if best is None or yy>best[3]: best=(n_,p_,k_,yy)
            if bestE is None or prof>bestE[4]: bestE=(n_,p_,k_,yy,prof)
print("grid max in domain:", best)
print("grid econ in domain:", bestE)

# ---- single factor ----
print("\n=== single-factor quadratics (kg/hm2) ===")
sets = {'N':([1,2,5,10], N), 'P':([3,4,5,6], P), 'K':([7,8,5,9], K)}
prices = {'N':pN,'P':pP,'K':pK}
for f,(idx,x) in sets.items():
    xx = x[idx]; yy = y_hm[idx]
    X1 = np.column_stack([np.ones(4), xx, xx**2])
    b1,R21,F1,pv1,dfr1,_ = fit(X1, yy)
    xmax = -b1[1]/(2*b1[2]); ymax = b1[0]+b1[1]*xmax+b1[2]*xmax**2
    xeco = (prices[f]/py - b1[1])/(2*b1[2]); yeco = b1[0]+b1[1]*xeco+b1[2]*xeco**2
    print(f"{f}: y = {b1[0]:.4f} + {b1[1]:.4f}x {b1[2]:+.6f}x^2  R2={R21:.4f} F={F1:.2f} p={pv1:.3f}")
    print(f"   x={list(xx)} y={list(np.round(yy,1))}")
    print(f"   xmax={xmax:.1f} ymax={ymax:.1f} | xeco={xeco:.1f} yeco={yeco:.1f}")

# ---- binary quadratics ----
print("\n=== binary quadratics (kg/hm2) ===")
pairs = {'NP':(lambda c: c[2]==2, N, P, pN, pP), 'NK':(lambda c: c[1]==2, N, K, pN, pK), 'PK':(lambda c: c[0]==2, P, K, pP, pK)}
for nm,(cond,x1,x2,p1,p2) in pairs.items():
    idx=[i for i,c in enumerate(codes) if cond(c)]
    a=x1[idx]; c_=x2[idx]; yy=y_hm[idx]
    X2=np.column_stack([np.ones(len(idx)),a,c_,a**2,c_**2,a*c_])
    b2,R22,F2,pv2,dfr2,_=fit(X2,yy)
    H2=np.array([[2*b2[3],b2[5]],[b2[5],2*b2[4]]]); g2=np.array([b2[1],b2[2]])
    xs2=np.linalg.solve(H2,-g2); xe2=np.linalg.solve(H2,np.array([p1/py,p2/py])-g2)
    f2=lambda u,v: b2[0]+b2[1]*u+b2[2]*v+b2[3]*u*u+b2[4]*v*v+b2[5]*u*v
    print(f"{nm}: n={len(idx)} b={np.round(b2,5)} R2={R22:.4f} F={F2:.2f} p={pv2:.3f} eig={np.linalg.eigvals(H2)}")
    print(f"   max at {xs2} y={f2(*xs2):.1f}; econ at {xe2} y={f2(*xe2):.1f}")

# ---- deficiency evaluation & efficiency ----
print("\n=== deficiency / efficiency ===")
yT = dict(zip(range(1,15), y_hm))
full=yT[6]; ck=yT[1]
for nm,t,amt in [('N',2,270),('P',4,180),('K',8,225)]:
    rel = yT[t]/full*100; contrib=(full-yT[t])/full*100; ae=(full-yT[t])/amt
    print(f"缺{nm}区 T{t}: yield={yT[t]:.1f} 相对产量={rel:.1f}% 贡献率={contrib:.1f}% 农学效率={ae:.2f} kg/kg 依存度={(full-yT[t])/full*100:.1f}")
print(f"空白区相对产量={ck/full*100:.1f}% 全肥增产={(full-ck)/ck*100:.1f}% 地力贡献率={ck/full*100:.1f}%")
# T10 best
print(f"T10 vs T1: +{yT[10]-ck:.1f} ({(yT[10]-ck)/ck*100:.1f}%), T10 vs T6: +{yT[10]-full:.1f} ({(yT[10]-full)/full*100:.1f}%)")

# ---- economics per treatment ----
print("\n=== economics per treatment (元/hm2) ===")
print("T  N   P   K   yield  产值   肥料成本  纯收益  增产  增产值  增收  产投比")
for i,c in enumerate(codes):
    cost=N[i]*pN+P[i]*pP+K[i]*pK; val=y_hm[i]*py; net=val-cost
    inc=y_hm[i]-ck; incval=inc*py; incnet=incval-cost; ratio=incval/cost if cost>0 else float('nan')
    print(f"{i+1:>2} {N[i]:>5.1f} {P[i]:>5.1f} {K[i]:>6.1f} {y_hm[i]:>7.1f} {val:>8.1f} {cost:>7.1f} {net:>8.1f} {inc:>7.1f} {incval:>7.1f} {incnet:>7.1f} {ratio:>5.2f}")

# theoretical yields from components
eff=[13.9,14.0,15.3,16.3,16.9,17.6,18.2,18.1,18.1,18.4,19.1,15.9,16.1,16.8] # 万穗/667m2
fg=[161.3,165.1,167.5,164.6,167.1,175.2,176.7,165.1,172.5,183.1,163,169.1,171.7,166]
tgw=[23.2,23.3,23.3,23.1,23.4,23.5,23.6,23.1,23.3,23.8,23.1,23.4,23.5,23.3]
print("\n=== theoretical yield (kg/hm2) & 有效穗 万/hm2 ===")
for i in range(14):
    th = eff[i]*1e4*fg[i]*tgw[i]/1e6 *15  # kg/hm2 (×15 from 667m2)
    print(f"T{i+1}: 有效穗={eff[i]*15:.1f}万/hm2 理论产量={th:.0f} 实产={y_hm[i]:.0f} 比={y_hm[i]/th*100:.1f}%")
