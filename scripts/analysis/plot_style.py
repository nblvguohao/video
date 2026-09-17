"""
plot_style.py

Shared matplotlib style for every figure in the paper, so the figure set reads
as one designed system rather than each script's own matplotlib defaults.
Applies a consistent palette (semantic colours preserved from earlier figures:
blue = third-party-assayed, red = applicant-self-reported, plus a fixed
categorical order for trait/channel series), a light panel background, thin
recessive gridlines, and no top/right spines.

Import and call `apply()` once at the top of a figure script.
"""
import matplotlib as mpl

# ---------------------------------------------------------------------------
# Semantic colours, held constant across every figure in the paper.
# ---------------------------------------------------------------------------
COLOR_3RD = "#2166ac"     # third-party assayed (blue)
COLOR_SELF = "#b2182b"    # applicant self-reported (red)
COLOR_UNIFIED = "#4c72b0"  # Unified channel
COLOR_GREEN = "#2ca858"    # Green channel
COLOR_CONSORTIUM = "#d9720a"  # Consortium channel
COLOR_FLAG = "#d95f02"    # flagged / attention
COLOR_NEUTRAL = "#6b6b76"  # neutral / reference

# Fixed categorical order for the 6 traits in the breakpoint scan / event study,
# chosen to be distinguishable under common colour-vision deficiencies (avoids
# red-green as an adjacent pair; keeps blue/red mapped to their established
# measuring-party meaning where the trait belongs to that class).
TRAIT_PALETTE = {
    "yield_2yr_kg_mu":   "#b2182b",  # self-reported
    "head_rice_pct":     "#2166ac",  # third-party
    "chalkiness_deg_pct": "#4393c3",  # third-party (lighter blue)
    "quality_top2_var":  "#053061",  # third-party (dark navy)
    "yield_gain_pct":    "#d9720a",  # self-reported (orange, distinct from red)
    "duration_d":        "#6b6b76",  # agronomic / context only
}

PANEL_BG = "#fbfbfd"
GRID_COLOR = "#d8d8e0"

def apply(dark_grid=False):
    mpl.rcParams.update({
        "figure.facecolor": "white",
        "axes.facecolor": PANEL_BG,
        "axes.edgecolor": "#9a9aa5",
        "axes.linewidth": 0.9,
        "axes.grid": True,
        "grid.color": GRID_COLOR,
        "grid.linewidth": 0.8,
        "grid.alpha": 0.9,
        "axes.axisbelow": True,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "DejaVu Sans", "Helvetica"],
        "font.size": 10.5,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.labelsize": 10.5,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
        "legend.fontsize": 9.5,
        "legend.frameon": False,
        "figure.titlesize": 13,
        "figure.titleweight": "bold",
        "xtick.color": "#3a3a45",
        "ytick.color": "#3a3a45",
        "text.color": "#1a1a22",
        "axes.labelcolor": "#1a1a22",
        "axes.titlecolor": "#1a1a22",
    })


def era_band(ax, x0, x1, color, alpha=0.06, label=None, y_frac=1.0):
    """Light background shading for an institutional era, drawn behind data."""
    ax.axvspan(x0, x1, color=color, alpha=alpha, zorder=0, lw=0)


def style_legend(ax, **kwargs):
    leg = ax.legend(**kwargs)
    if leg:
        leg.get_frame().set_linewidth(0)
    return leg
