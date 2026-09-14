# Proposal D (mechanism angle) -- all preliminary tests reported in plan/proposals/proposal_D_mechanism.md
# Concatenation of an1-an6 run on 2026-09-14. Intermediate CSVs are written to the scratchpad path below;
# change SCRATCH before re-running elsewhere.

import pandas as pd, numpy as np, statsmodels.formula.api as smf, warnings
warnings.filterwarnings('ignore')
pd.set_option('display.width',220)

d = pd.read_csv('/home/user/video/evidence/data/analysis_national_rice.csv')
st = d[(d.subspecies=='籼') & (d.breeding_system.isin(['Two-line hybrid','Three-line hybrid'])) &
       (d.season=='Single/Mid') & (d.region.isin(['Middle-Lower Yangtze','Upper Yangtze'])) &
       (d.approval_year>=2005) & (d.approval_year<=2024)].copy()
st['yr']=st.approval_year.astype(int).astype(str)
st['W']=st.winall.astype(int)

TRAITS = dict(
  head_rice_pct='Head rice rate (%)', chalkiness_deg_pct='Chalkiness degree (%)',
  lw_ratio='Length-width ratio', amylose_pct='Amylose (%)', gel_mm='Gel consistency (mm)',
  yield_2yr_kg_mu='Trial yield (kg/mu)', yield_gain_pct='Yield gain over check (%)',
  duration_d='Growth duration (d)', tgw_g='1000-grain weight (g)',
  plant_height_cm='Plant height (cm)', panicles_10k_mu='Panicles (10k/mu)',
  panicle_len_cm='Panicle length (cm)', grains_per_panicle='Grains per panicle',
  seed_setting_pct='Seed setting (%)')

def fe(df, y, rhs='W'):
    sub = df.dropna(subset=[y]).copy()
    if sub[y].notna().sum()<40: return None
    f = f"Q('{y}') ~ {rhs} + C(yr) + C(region) + C(breeding_system)"
    try:
        m = smf.ols(f, data=sub).fit(cov_type='HC1')
    except Exception as e:
        return None
    return m

print("="*100)
print("TABLE A. BASELINE REPLICATION: Winall vs all other applicants, stratum 2005-2024, FE(year, region, breeding system), HC1")
print("="*100)
rows=[]
for y,lab in TRAITS.items():
    m = fe(st,y)
    if m is None: continue
    rows.append([lab, int(m.nobs), round(m.params['W'],4), round(m.bse['W'],4), round(m.pvalues['W'],4)])
print(pd.DataFrame(rows, columns=['trait','n','beta_Winall','SE','p']).to_string(index=False))
import pandas as pd, numpy as np, statsmodels.formula.api as smf, warnings
warnings.filterwarnings('ignore'); pd.set_option('display.width',240)
d = pd.read_csv('/home/user/video/evidence/data/analysis_national_rice.csv')
st = d[(d.subspecies=='籼') & (d.breeding_system.isin(['Two-line hybrid','Three-line hybrid'])) &
       (d.season=='Single/Mid') & (d.region.isin(['Middle-Lower Yangtze','Upper Yangtze'])) &
       (d.approval_year>=2005) & (d.approval_year<=2024)].copy()
st['yr']=st.approval_year.astype(int).astype(str); st['W']=st.winall.astype(int)
st['POST19']=(st.approval_year>=2019).astype(int)
st['POST22']=(st.approval_year>=2022).astype(int)   # 3-yr breeding/trial lag version

TR = dict(head_rice_pct='Head rice (%)', chalkiness_deg_pct='Chalkiness (%)', lw_ratio='L/W ratio',
          gel_mm='Gel consistency (mm)', amylose_pct='Amylose (%)',
          yield_2yr_kg_mu='Trial yield (kg/mu)', yield_gain_pct='Yield gain vs CK (%)',
          duration_d='Duration (d)', tgw_g='TGW (g)',
          plant_height_cm='Plant height (cm)', panicles_10k_mu='Panicles (10k/mu)',
          panicle_len_cm='Panicle length (cm)')

def run(y, post):
    sub = st.dropna(subset=[y]).copy()
    f = f"Q('{y}') ~ W + W:{post} + C(yr) + C(region) + C(breeding_system)"
    m = smf.ols(f, data=sub).fit(cov_type='HC1')
    k = f'W:{post}'
    return [int(m.nobs), m.params['W'], m.pvalues['W'], m.params[k], m.bse[k], m.pvalues[k],
            int(sub[(sub.W==1)&(sub[post]==0)].shape[0]), int(sub[(sub.W==1)&(sub[post]==1)].shape[0])]

for post,lab in [('POST19','H1a: interaction with approval year >= 2019 (order-grain scale-up)'),
                 ('POST22','H1b: interaction with approval year >= 2022 (3-yr breeding/trial lag)')]:
    print("="*120); print(lab); print("="*120)
    rows=[]
    for y,nm in TR.items():
        r = run(y,post)
        rows.append([nm, r[0], round(r[1],3), round(r[2],3), round(r[3],3), round(r[4],3), round(r[5],4), r[6], r[7]])
    print(pd.DataFrame(rows, columns=['trait','n','W_pre','p(W_pre)','W x post','SE','p(inter)','n_W_pre','n_W_post']).to_string(index=False))
    print()

# Winall share & period means
print("Winall records per period in stratum:")
st['per']=pd.cut(st.approval_year,[2004,2010,2015,2018,2021,2024],labels=['2005-10','2011-15','2016-18','2019-21','2022-24'])
print(pd.crosstab(st.per, st.W))
import pandas as pd, numpy as np, statsmodels.formula.api as smf, warnings, re
warnings.filterwarnings('ignore'); pd.set_option('display.width',240)
d = pd.read_csv('/home/user/video/evidence/data/analysis_national_rice.csv')
st = d[(d.subspecies=='籼') & (d.breeding_system.isin(['Two-line hybrid','Three-line hybrid'])) &
       (d.season=='Single/Mid') & (d.region.isin(['Middle-Lower Yangtze','Upper Yangtze'])) &
       (d.approval_year>=2005) & (d.approval_year<=2024)].copy()
st['yr']=st.approval_year.astype(int).astype(str); st['W']=st.winall.astype(int)

A = st.applicant.fillna('')
# --- downstream-integrated (contract farming / seed-grain integration) applicants ---
# documented in Xie et al. 2023 Agribusiness Table 2 (seed-enterprise-led contract farming) + listed-firm annual reports
LP  = A.str.contains('袁隆平农业高科技|隆平高科|湖南亚华种业|安徽隆平')          # Longping High-Tech
FL  = A.str.contains('丰乐种业')                                              # Fengle Seed
NFZ = A.str.contains('农发种业|中国农业发展集团|中农发')                        # Nongfa Seed
DH  = A.str.contains('敦煌种业')
DBN = A.str.contains('大北农')
JJ  = A.str.contains('金健')                    # Jinjian Seed - sub of listed rice miller Jinjian Rice
ZZ  = A.str.contains('中国种子集团')             # Sinochem/China National Seed (parent of Winall since 2021)
st['INT_peer'] = (LP|FL|NFZ|DH|DBN|JJ).astype(int)
st['INT_peer_strict'] = (LP|FL|NFZ|DH|DBN).astype(int)   # drop Jinjian
st['ZZ']=ZZ.astype(int)
st['INT_any'] = ((st.W==1)|(st.INT_peer==1)).astype(int)

lab = st[st.applicant.notna()].copy()
print('applicant-labelled records in stratum:', len(lab))
print('by group: Winall %d | INT_peer %d | ZZ %d | other-enterprise %d | public %d | joint %d' % (
    (lab.W==1).sum(), (lab.INT_peer==1).sum(), (lab.ZZ==1).sum(),
    ((lab.applicant_type=='Enterprise')&(lab.W==0)&(lab.INT_peer==0)).sum(),
    (lab.applicant_type=='Public').sum(), (lab.applicant_type=='Joint').sum()))
print(pd.crosstab(lab.approval_year, [lab.W, lab.INT_peer]))
# group variable
def grp(r):
    if r.W==1: return '1_Winall'
    if r.INT_peer==1: return '2_IntegratedPeer'
    if r.applicant_type=='Enterprise': return '3_NonIntegratedFirm'
    if r.applicant_type=='Public': return '4_PublicInstitute'
    return '5_Other'
lab['G']=lab.apply(grp,axis=1)
print(lab.G.value_counts())
lab.to_csv('/tmp/claude-0/-home-user-video/00691716-191f-5e67-a5b5-7f0d0f6e696d/scratchpad/labelled.csv',index=False)
st.to_csv('/tmp/claude-0/-home-user-video/00691716-191f-5e67-a5b5-7f0d0f6e696d/scratchpad/stratum.csv',index=False)
import pandas as pd, numpy as np, statsmodels.formula.api as smf, warnings
warnings.filterwarnings('ignore'); pd.set_option('display.width',250)
lab = pd.read_csv('/tmp/claude-0/-home-user-video/00691716-191f-5e67-a5b5-7f0d0f6e696d/scratchpad/labelled.csv')
lab = lab[lab.G!='5_Other'].copy()
lab['yr']=lab.approval_year.astype(int).astype(str)
lab['G']=pd.Categorical(lab.G, categories=['3_NonIntegratedFirm','1_Winall','2_IntegratedPeer','4_PublicInstitute'])

TR = dict(head_rice_pct='Head rice (%) [REV]', chalkiness_deg_pct='Chalkiness (%) [REV]',
          lw_ratio='L/W ratio [REV]', gel_mm='Gel consistency (mm) [REV]', amylose_pct='Amylose (%) [REV]',
          yield_2yr_kg_mu='Trial yield (kg/mu) [REG]', yield_gain_pct='Yield gain vs CK (%) [REG]',
          duration_d='Duration (d) [BOTH]', tgw_g='TGW (g) [REV/REG]',
          plant_height_cm='Plant height (cm) [PLACEBO]', panicles_10k_mu='Panicles 10k/mu [PLACEBO]',
          panicle_len_cm='Panicle length (cm) [PLACEBO]', grains_per_panicle='Grains/panicle [PLACEBO]',
          seed_setting_pct='Seed setting (%) [PLACEBO]')

print("="*135)
print("TABLE B (H2/H3/H4). Group contrasts vs NON-INTEGRATED SEED FIRMS (reference). FE: year, region, breeding system. HC1 SE.")
print("Sample: applicant-labelled records only, indica hybrid single/mid-season, M-L + Upper Yangtze, 2005-2024")
print("="*135)
rows=[]
for y,nm in TR.items():
    sub=lab.dropna(subset=[y])
    m=smf.ols(f"Q('{y}') ~ C(G) + C(yr) + C(region) + C(breeding_system)", data=sub).fit(cov_type='HC1')
    r=[nm,int(m.nobs)]
    for g,gl in [('1_Winall','Winall'),('2_IntegratedPeer','IntPeer'),('4_PublicInstitute','Public')]:
        k=f"C(G)[T.{g}]"
        r += [round(m.params[k],3), round(m.pvalues[k],4)]
    rows.append(r)
print(pd.DataFrame(rows,columns=['trait','n','Winall_b','p','IntPeer_b','p','Public_b','p']).to_string(index=False))

print()
print("="*135)
print("TABLE C (H2 pooled). ANY downstream-integrated firm (Winall + integrated peers) vs non-integrated firms + public")
print("="*135)
lab['INT_any']=lab.G.isin(['1_Winall','2_IntegratedPeer']).astype(int)
lab['PUB']=(lab.G=='4_PublicInstitute').astype(int)
rows=[]
for y,nm in TR.items():
    sub=lab.dropna(subset=[y])
    m=smf.ols(f"Q('{y}') ~ INT_any + PUB + C(yr) + C(region) + C(breeding_system)", data=sub).fit(cov_type='HC1')
    rows.append([nm,int(m.nobs),round(m.params['INT_any'],3),round(m.bse['INT_any'],3),round(m.pvalues['INT_any'],4),
                 round(m.params['PUB'],3),round(m.pvalues['PUB'],4)])
print(pd.DataFrame(rows,columns=['trait','n','INTany_b','SE','p','PUB_b','p']).to_string(index=False))

print()
print("="*135)
print("TABLE D (H2 peers only, Winall EXCLUDED). Integrated peers vs non-integrated firms -- the out-of-sample test of the mechanism")
print("="*135)
nw = lab[lab.G!='1_Winall'].copy()
nw['INT']=(nw.G=='2_IntegratedPeer').astype(int); nw['PUB']=(nw.G=='4_PublicInstitute').astype(int)
rows=[]
for y,nm in TR.items():
    sub=nw.dropna(subset=[y])
    m=smf.ols(f"Q('{y}') ~ INT + PUB + C(yr) + C(region) + C(breeding_system)", data=sub).fit(cov_type='HC1')
    rows.append([nm,int(m.nobs),round(m.params['INT'],3),round(m.bse['INT'],3),round(m.pvalues['INT'],4),
                 int(sub.INT.sum())])
print(pd.DataFrame(rows,columns=['trait','n','IntPeer_b','SE','p','n_IntPeer']).to_string(index=False))
import pandas as pd, numpy as np, statsmodels.formula.api as smf, warnings
warnings.filterwarnings('ignore'); pd.set_option('display.width',250)
lab = pd.read_csv('/tmp/claude-0/-home-user-video/00691716-191f-5e67-a5b5-7f0d0f6e696d/scratchpad/labelled.csv')
lab = lab[lab.G!='5_Other'].copy(); lab['yr']=lab.approval_year.astype(int).astype(str)
lab['INT']=lab.G.isin(['1_Winall','2_IntegratedPeer']).astype(int)
lab['PUB']=(lab.G=='4_PublicInstitute').astype(int)
lab['WIN']=(lab.G=='1_Winall').astype(int); lab['PEER']=(lab.G=='2_IntegratedPeer').astype(int)

print("### R1. Cluster-robust SE by VARIETY (a variety approved in several regions = several rows)")
TR=['head_rice_pct','chalkiness_deg_pct','lw_ratio','gel_mm','yield_2yr_kg_mu','yield_gain_pct',
    'plant_height_cm','panicles_10k_mu','panicle_len_cm','grains_per_panicle']
rows=[]
for y in TR:
    sub=lab.dropna(subset=[y,'variety'])
    m=smf.ols(f"Q('{y}') ~ WIN + PEER + PUB + C(yr) + C(region) + C(breeding_system)",data=sub).fit(
        cov_type='cluster',cov_kwds={'groups':sub.variety})
    rows.append([y,int(m.nobs),sub.variety.nunique(),round(m.params['WIN'],3),round(m.pvalues['WIN'],4),
                 round(m.params['PEER'],3),round(m.pvalues['PEER'],4),round(m.params['PUB'],3),round(m.pvalues['PUB'],4)])
print(pd.DataFrame(rows,columns=['trait','n','n_var','WIN_b','p','PEER_b','p','PUB_b','p']).to_string(index=False))

print("\n### R2. COMPOSITE INDICES. Within-year z-scores. QualityIdx = mean(z_headrice, -z_chalk, -z_lwratio-dev?);")
print("    QualityIdx = z(head rice) - z(chalkiness)  (both enter the miller's payoff directly)")
print("    YieldIdx   = z(trial yield);  RelYieldIdx = z(yield gain vs check)")
g=lab.groupby('yr')
for c in ['head_rice_pct','chalkiness_deg_pct','yield_2yr_kg_mu','yield_gain_pct','plant_height_cm','panicles_10k_mu']:
    lab['z_'+c]=g[c].transform(lambda s:(s-s.mean())/s.std(ddof=0) if s.std(ddof=0)>0 else np.nan)
lab['QualIdx']=lab[['z_head_rice_pct']].mean(axis=1)-lab['z_chalkiness_deg_pct']
lab['QualIdx']=lab['QualIdx']/2
lab['PlaceboIdx']=(lab['z_plant_height_cm']+lab['z_panicles_10k_mu'])/2
for y,nm in [('QualIdx','Quality index (revenue-relevant)'),('z_yield_2yr_kg_mu','Trial yield (z)'),
             ('z_yield_gain_pct','Relative yield gain (z)'),('PlaceboIdx','Placebo index (height+panicles)')]:
    sub=lab.dropna(subset=[y,'variety'])
    m=smf.ols(f"{y} ~ WIN + PEER + PUB + C(region) + C(breeding_system)",data=sub).fit(
        cov_type='cluster',cov_kwds={'groups':sub.variety})
    print(f"{nm:38s} n={int(m.nobs):4d}  WIN={m.params['WIN']:+.3f}(p={m.pvalues['WIN']:.4f})  "
          f"PEER={m.params['PEER']:+.3f}(p={m.pvalues['PEER']:.4f})  PUB={m.params['PUB']:+.3f}(p={m.pvalues['PUB']:.4f})")

print("\n### R3. Formal mechanism test: is the integration effect LARGER on quality than on relative yield?")
st_=lab.dropna(subset=['QualIdx','z_yield_gain_pct']).copy()
long=pd.concat([st_.assign(Y=st_.QualIdx,DIM='Q'),st_.assign(Y=st_.z_yield_gain_pct,DIM='Y')])
m=smf.ols("Y ~ INT*C(DIM,Treatment('Y')) + PUB*C(DIM,Treatment('Y')) + C(region) + C(breeding_system)",
          data=long).fit(cov_type='cluster',cov_kwds={'groups':long.variety})
k=[p for p in m.params.index if p.startswith('INT:')][0]
print(f"  n(pairs)={len(st_)}  INT x Quality-vs-RelYield interaction = {m.params[k]:+.3f}  SE={m.bse[k]:.3f}  p={m.pvalues[k]:.4f}")
print(f"  INT main (on relative yield) = {m.params['INT']:+.3f} (p={m.pvalues['INT']:.4f})")
import pandas as pd, numpy as np, statsmodels.formula.api as smf, warnings
from scipy import stats
warnings.filterwarnings('ignore'); pd.set_option('display.width',250)
st = pd.read_csv('/tmp/claude-0/-home-user-video/00691716-191f-5e67-a5b5-7f0d0f6e696d/scratchpad/stratum.csv')
st['yr']=st.approval_year.astype(int).astype(str); st['W']=st.winall.astype(int)

# ---- R4 dose-response: yearly Winall-vs-rest gap regressed on order-grain revenue share (lagged) ----
share={2018:5.87,2019:15.65,2020:26.2,2021:28.73,2022:25.6,2023:20.1,2024:25.3}  # % of revenue, evidence/04
print("### R4. Dose-response: annual Winall-minus-rest quality gap vs order-grain revenue share")
rows=[]
for yv in sorted(st.approval_year.unique()):
    sub=st[st.approval_year==yv]
    if (sub.W==1).sum()<5: continue
    for trait in ['head_rice_pct','chalkiness_deg_pct','lw_ratio','yield_gain_pct']:
        a=sub.loc[sub.W==1,trait].dropna(); b=sub.loc[sub.W==0,trait].dropna()
        if len(a)<5 or len(b)<10: continue
        rows.append([int(yv),trait,a.mean()-b.mean(),len(a),len(b)])
gap=pd.DataFrame(rows,columns=['year','trait','gap','nW','nO'])
print(gap.pivot(index='year',columns='trait',values='gap').round(3).to_string())
for trait in ['head_rice_pct','chalkiness_deg_pct','lw_ratio','yield_gain_pct']:
    gg=gap[gap.trait==trait].copy()
    gg['sh']=gg.year.map(share)          # contemporaneous
    gg['sh3']=(gg.year-3).map(share)     # 3-year lag (decision-to-approval)
    for k,lb in [('sh','contemp'),('sh3','3-yr lag')]:
        v=gg.dropna(subset=[k])
        if len(v)>=5:
            r,p=stats.pearsonr(v[k],v.gap)
            print(f"  {trait:20s} {lb:9s} n_years={len(v)}  r={r:+.3f}  p={p:.3f}")

# ---- R5 economic magnitude ----
print("\n### R5. Economic magnitude of the head-rice differential")
base=st.head_rice_pct.mean(); print(f"  stratum mean head rice rate = {base:.2f}%")
for b,nm in [(1.356,'Winall vs all (Table A)'),(0.797,'Integrated peer vs non-integrated (Table B)')]:
    rel=b/base*100
    print(f"  {nm}: +{b:.3f} pp = +{rel:.2f}% relative milling output per tonne of paddy")
og=981414760.16; cost=994255695.14
print(f"  2025 Winall order-grain revenue {og/1e8:.2f} x1e8 CNY, cost {cost/1e8:.2f}, gross margin {(og-cost)/og*100:.2f}%")
print(f"  A +2.19% relative milling gain on that revenue base = {og*0.0219/1e6:.1f} m CNY of extra saleable-rice value")
print(f"  Actual 2025 gross LOSS on the same business = {(og-cost)/1e6:.1f} m CNY")

# ---- R6 robustness ----
print("\n### R6. Robustness of the Winall quality effect")
lab=pd.read_csv('/tmp/claude-0/-home-user-video/00691716-191f-5e67-a5b5-7f0d0f6e696d/scratchpad/labelled.csv')
lab=lab[lab.G!='5_Other'].copy(); lab['yr']=lab.approval_year.astype(int).astype(str)
lab['INT']=lab.G.isin(['1_Winall','2_IntegratedPeer']).astype(int); lab['PUB']=(lab.G=='4_PublicInstitute').astype(int)
g=lab.groupby('yr')
for c in ['head_rice_pct','chalkiness_deg_pct','plant_height_cm','panicles_10k_mu']:
    lab['z_'+c]=g[c].transform(lambda s:(s-s.mean())/s.std(ddof=0) if s.std(ddof=0)>0 else np.nan)
lab['QualIdx']=(lab.z_head_rice_pct-lab.z_chalkiness_deg_pct)/2
lab['PlaceboIdx']=(lab.z_plant_height_cm+lab.z_panicles_10k_mu)/2
for y,nm in [('QualIdx','Quality index'),('PlaceboIdx','Placebo index')]:
    sub=lab.dropna(subset=[y])
    m=smf.ols(f"{y} ~ INT + PUB + C(region)+C(breeding_system)",data=sub).fit(cov_type='cluster',cov_kwds={'groups':sub.variety})
    print(f"  pooled INT on {nm:14s}: {m.params['INT']:+.3f} (SE {m.bse['INT']:.3f}, p={m.pvalues['INT']:.4f}, n={int(m.nobs)})")
# restrict to 2019-2024 (modern regime only)
sub=lab[(lab.approval_year>=2019)].dropna(subset=['QualIdx'])
m=smf.ols("QualIdx ~ INT + PUB + C(yr)+C(region)+C(breeding_system)",data=sub).fit(cov_type='cluster',cov_kwds={'groups':sub.variety})
print(f"  2019-2024 only, QualIdx: INT={m.params['INT']:+.3f} (p={m.pvalues['INT']:.4f}, n={int(m.nobs)})")
sub=lab[(lab.approval_year>=2019)].dropna(subset=['yield_gain_pct'])
m=smf.ols("yield_gain_pct ~ INT + PUB + C(yr)+C(region)+C(breeding_system)",data=sub).fit(cov_type='cluster',cov_kwds={'groups':sub.variety})
print(f"  2019-2024 only, yield gain vs CK: INT={m.params['INT']:+.3f} (p={m.pvalues['INT']:.4f}, n={int(m.nobs)})")
