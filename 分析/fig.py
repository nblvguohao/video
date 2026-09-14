import json, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
d=json.load(open('data.json'))
plt.rcParams['font.family']=['Liberation Serif','WenQuanYi Zen Hei','DejaVu Sans']
plt.rcParams['font.size']=8; plt.rcParams['axes.unicode_minus']=False
plt.rcParams['mathtext.fontset']='stix'
fig,axes=plt.subplots(1,3,figsize=(17/2.54,6.2/2.54),dpi=600)
panels=[('N','施N量/(kg/hm²)','a'),('P','施P₂O₅量/(kg/hm²)','b'),('K','施K₂O量/(kg/hm²)','c')]
for ax,(f,xl,tag) in zip(axes,panels):
    s=d['single'][f]; x=np.array(s['x']); y=np.array(s['y']); b=s['coef']
    xx=np.linspace(0,x.max(),200)
    ax.plot(xx,b[0]+b[1]*xx+b[2]*xx**2,'--',color='0.35',lw=0.9,label='一元二次')
    if f=='N':
        l=d['N_lpp']; yy=np.where(xx<l['x0'],l['a']+l['b']*xx,l['plateau']); ax.plot(xx,yy,'-',color='k',lw=0.9,label='线性加平台')
    else:
        l=d[f+'_lin']; ax.plot(xx,l['a']+l['b']*xx,'-',color='k',lw=0.9,label='线性')
    ax.plot(x,y,'o',ms=3.5,mfc='k',mec='k',label='实测值')
    ax.set_xlabel(xl,fontsize=7.5); ax.set_ylabel('产量/(kg/hm²)',fontsize=7.5)
    ax.set_ylim(6000,10800); ax.set_xlim(-0.04*x.max(),1.06*x.max()); ax.set_xticks(x)
    ax.tick_params(labelsize=7,direction='in',length=2.5)
    ax.text(0.03,0.92,f'({tag})',transform=ax.transAxes,fontsize=8)
    ax.legend(fontsize=6.2,frameon=False,loc='lower right',handlelength=1.6)
    for sp in ax.spines.values(): sp.set_linewidth(0.6)
plt.tight_layout(pad=0.4,w_pad=0.8)
plt.savefig('fig1.png',dpi=600); plt.savefig('fig1.pdf')
print('ok')
