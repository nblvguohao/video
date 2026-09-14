import pandas as pd, numpy as np, re
raw=pd.read_csv('evidence/data/national_rice_varieties_raw.csv',encoding='utf-8-sig',dtype=str).fillna('')
raw['row_index']=raw['row_index'].astype(int)
p=pd.read_csv('evidence/data/national_rice_parsed.csv',encoding='utf-8-sig')
p['yr']=pd.to_numeric(p['approval_year'],errors='coerce')
p['_c']=p.notna().sum(axis=1); p['_n']=p.variety.astype(str).str.len()
p=(p.sort_values(['_c','_n'],ascending=[False,True]).drop_duplicates(subset=['approval_no'],keep='first'))
m=p.merge(raw[['row_index','产量表现','特征特性','品种来源','申请者','选育单位','育种者']],on='row_index',how='left')
yp=m['产量表现'].fillna('').astype(str).str.replace(r'\s+','',regex=True)
cf=m['特征特性'].fillna('').astype(str).str.replace(r'\s+','',regex=True)
txt=yp+cf
m['ch_green']=txt.str.contains('绿色通道|自主试验')
m['ch_union']=txt.str.contains('联合体')
m['channel']=np.where(m['ch_green'],'Green',np.where(m['ch_union'],'Consortium','Unified'))
m['new_channel']=(m['channel']!='Unified').astype(int)
# trial group: text between 参加 and 区域试验/试验, strip channel words & year
def tg(t):
    g=re.search(r'参加(.{0,40}?)(?:区域试验|区试|试验)',t)
    if not g: return ''
    s=g.group(1)
    s=re.sub(r'^\d{4}年?','',s)
    s=re.sub(r'绿色通道|联合体|自主|水稻|国家|品种|组$','',s)
    s=re.sub(r'组$','',s)
    return s
m['trial_group']=yp.map(tg)
# applicant type
ENT=r'公司|种业|集团|有限|股份'
PUB=r'农业科学院|农科院|大学|学院|研究所|科学院|农业厅|技术推广|研究中心|农科所|农试站|种子站|农业局'
def org_type(s):
    s=str(s)
    if s.strip() in ('','nan'): return 'Unknown'
    e,q=bool(re.search(ENT,s)),bool(re.search(PUB,s))
    if e and q: return 'Joint'
    if e: return 'Enterprise'
    if q: return 'Public'
    return 'Unknown'
app=(m['申请者'].fillna('')+'|'+m['选育单位'].fillna('')+'|'+m['育种者'].fillna('')).str.strip('|')
m['app_full']=app
m['applicant_type']=app.map(org_type)
def bsys(r):
    if r.two_line and not r.three_line: return 'Two-line'
    if r.three_line and not r.two_line: return 'Three-line'
    if r.is_hybrid: return 'Hybrid-unclear'
    return 'Inbred'
m['bsys']=m.apply(bsys,axis=1)
m['hyb']=np.where(m['bsys']=='Inbred','Inbred','Hybrid')
ped=m['品种来源'].fillna('').astype(str).str.replace(r'\s+','',regex=True)
m['pedigree']=ped
name=m['variety'].astype(str).str.replace(r'\s+','',regex=True)
m['winall']=(name.str.startswith('荃')|ped.str.contains('荃')|ped.str.contains(r'YR\d')|m['is_winall'].astype(bool))
m['quality_top2']=np.where(m.quality_grade.notna(),(m.quality_grade<=2).astype(float),np.nan)
m['neck_blast_ok']=np.where(m.neck_blast_loss_max_grade.notna(),(m.neck_blast_loss_max_grade<=5).astype(float),np.nan)
m['ck_n']=m['ck'].fillna('').astype(str).str.replace(r'\s+','',regex=True)
m.to_pickle('evidence/data/analysis_rice_channel.pkl')
print(m.shape)
n=m[(m.level=='国审')&(m.yr.between(2005,2022))]
print(pd.crosstab(n['yr'],n['channel']))
print("\ntop trial groups (national 2005-2022):")
print(n['trial_group'].value_counts().head(15))
