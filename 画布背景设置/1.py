import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.font_manager import FontProperties
import matplotlib.image as img
import os

axalpha = 0.05

def add_math_background(fig):
    ax = fig.add_axes([0.3, 0.25, 0.5, 0.5])

    text = []
    text.append(
        (r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = "
         r"U^{3\beta}_{\delta_1 \rho_1} + \frac{1}{8 \pi 2}"
         r"\int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 "
         r"\left[\frac{ U^{2\beta}_{\delta_1 \rho_1} - "
         r"\alpha^\prime_2U^{1\beta}_{\rho_1 \sigma_2} "
         r"}{U^{0\beta}_{\rho_1 \sigma_2}}\right]$", (0.6, 0.3), 20))
    text.append((r"$\frac{d\rho}{d t} + \rho \vec{v}\cdot\nabla\vec{v} "
                 r"= -\nabla p + \mu\nabla^2 \vec{v} + \rho \vec{g}$",
                 (0.45, 0.7), 20))
    text.append((r"$\int_{-\infty}^\infty e^{-x^2}dx=\sqrt{\pi}$",
                 (0.25, 0.4), 25))
    text.append((r"$F_G = G\frac{m_1m_2}{r^2}$",
                 (0.75, 0.6), 30))
    for eq, (x, y), size in text:
        ax.text(x, y, eq, ha='center', va='center', color="#11557c",
                alpha=0.25, transform=ax.transAxes, fontsize=size)
    ax.set_axis_off()
    return ax


def add_matplotlib_text(ax,color):
    font=FontProperties(fname=r"/Library/Fonts/Songti.ttc", size=85)
    ax.text(0.55, 0.6, 'matplotlib', color=color,size=35,
            ha='right', va='bottom', alpha=1.0, transform=ax.transAxes)
    ax.text(0.55, 0.45, u'小讲堂', color=color,fontproperties=font,
            ha='center', va='center', alpha=1.0, transform=ax.transAxes)

def add_polar_bar(fig):
    ax = fig.add_axes([0.25, 0.4, 0.2, 0.2], projection='polar')

    ax.axesPatch.set_alpha(axalpha)
    ax.set_axisbelow(True)
    N = 7
    arc = 2. * np.pi
    theta = np.arange(0.0, arc, arc/N)
    radii = 10 * np.array([0.2, 0.6, 0.8, 0.7, 0.4, 0.5, 0.8])
    width = np.pi / 4 * np.array([0.4, 0.4, 0.6, 0.8, 0.2, 0.5, 0.3])
    bars = ax.bar(theta, radii, width=width, bottom=0.0)
    for r, bar in zip(radii, bars):
        bar.set_facecolor(cm.jet(r/10.))
        bar.set_alpha(0.6)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(False)

    for line in ax.get_ygridlines() + ax.get_xgridlines():
        line.set_lw(0.8)
        line.set_alpha(0.9)
        line.set_ls('-')
        line.set_color('0.5')

    ax.set_yticks(np.arange(1, 9, 2))
    ax.set_rmax(9)

def pltfig(fig,color='#11557c'):
    main_axes = add_math_background(fig)
    add_polar_bar(fig)
    add_matplotlib_text(main_axes,color)
    
if __name__ == '__main__':
    fig1 = plt.figure(figsize=(16, 8),facecolor='snow')
    pltfig(fig1)
    fig2 = plt.figure(figsize=(16, 8))
    fig2.set_facecolor('blueviolet')
    pltfig(fig2)
    fig3 = plt.figure(figsize=(16, 8))
    a = [np.linspace(0, 1, 1600)]*1600
    fig3.figimage(a,cmap='autumn')
    pltfig(fig3,'w')
    fig4 = plt.figure(figsize=(16, 8))
    fn=os.path.dirname(os.path.realpath(__file__))+'/picture.png'
    bgimg = img.imread(fn)
    fig4.figimage(bgimg)
    pltfig(fig4,'w')
    plt.show()
