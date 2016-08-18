# -*- coding: utf-8 -*-
import numpy as np
import os
# import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as patches

SVDSLOGO = plt.imread(os.path.join(os.path.dirname(__file__), 'logo-plot.png'))
WIDE=(12, 8)
WIDER=(15, 8)

import seaborn as sns

sns.set_context('poster', font_scale=1.3)

almost_black = '#262626'
dark_gray = '#555555'
light_gray = '#E5E5E5'
# testing
sns_light_gray = '.8'
sns_dark_gray = '.15'

# so they are essentially off but change the color anyway
svds_style = {
 'xtick.color': dark_gray,
 'ytick.color': dark_gray,
 'axes.edgecolor': dark_gray,
 'axes.labelcolor': dark_gray,
 'text.color': dark_gray,
 'grid.color': light_gray,
 'lines.markeredgewidth': 0.15,
 'lines.markeredgecolor': almost_black,
 }

# set the matplotlib rcparams to use sns darkgrid with svds custom style
sns.set_style('darkgrid', svds_style)

# official svds colors
hex_to_name = {
 '#D34100': 'leafblower red',
 '#707071': 'medium gray',
 '#ECEFF0': 'oyster gray',
 '#2C3E4F': 'tardis blue',
 '#F15E24': 'dark orange',
 '#FF9700': 'orange',
 '#0055A7': 'blue',
 '#091D32': 'midnight tardis',
 '#26C5ED': 'sully blue',
 '#00CC66': 'leaf green',
 }
svds_color_dict = {v: k for k, v in hex_to_name.items()}

svds_color_names = svds_color_dict.keys()

def plot_named_colors(color_dict=svds_color_dict):
    num_colors_by_two = int((len(color_dict))/2.0 + 0.5)

    x0, y0 = (0.0, 0.0)
    dy = 1.0/num_colors_by_two
    pad = 0.05
    w, h = (0.5 - pad, 0.5*dy)

    fig, ax = plt.subplots(figsize=(8, 1*num_colors_by_two))
    for i, (name, color) in enumerate(color_dict.items()):
        x = x0 + (i // num_colors_by_two) * 0.5
        y = y0 + 2*(i % num_colors_by_two) * h
        ax.add_patch(patches.Rectangle((x, y), w, h, color=color))
        ax.annotate(' '.join([color.upper(), name]),
                    xy=(x, y), xytext=(x, y - 0.25*dy), family='monospace')
    plt.axis('off')

# my original estimates for svds color pallette
# ['#26B8E8', '#FD840A', '#19C653', '#C62D04', '#074097', '#F25A1B', '#0A1626']

svds_colors = [svds_color_dict[c] for c in [
               'blue',
               'orange',
               'leaf green',
               'leafblower red',
               'sully blue',
               'dark orange',
               'midnight tardis',
               ]]
svds_palette = sns.color_palette(svds_colors)

# set the default color cycler
sns.set_palette(svds_palette)

# these are estimates of the colors in the svds diamond logo
oranges = ['#F07034', '#F28130', '#EE8E2F', '#EFA737']
blues = ['#0E60AC', '#006DB3', '#0486C8', '#19A2DC']


def hex2rgb(colors):
    """
    Converts a list of color hex strings to rgb tuples of
    integers between [0, 255]

    For example:

    >>> hex2rgb(['#123ABC', '#000000', '#FFFFFF'])
    [(18, 58, 188), (0, 0, 0), (255, 255, 255)]

    """
    # convert list of string color hexes to rgb. why did I do this myself?
    n = 2
    rgb_colors = zip(
        *[
          [int(c[i:i+n], 16) for c in colors]
          for i in range(1, 7, n)
        ])
    return rgb_colors


def norm_rgb(colors):
    """
    Scales a list of tuples of integers between [0, 255] to [0, 1]

    >>> norm_rgb([(0, 51, 255)])
    [(0.0, 0.2, 1.0)]

    """
    return [tuple([c/float(255) for c in rgb]) for rgb in colors]


def diverging_cmap(colors):

    rgb_colors = norm_rgb(hex2rgb(colors))

    cdict = {}
    dxmax = 0.25

    xhalf = np.linspace(0, dxmax, len(rgb_colors)//2)
    # insert white to list of colors in the middle
    rgb_colors.insert(len(rgb_colors)//2, (1, 1, 1))
    xs = xhalf.tolist() + [.5] + (1 - dxmax + xhalf).tolist()

    for k, v in [('red', 0), ('green', 1), ('blue', 2)]:
        ctuples = [(x, c, c) for x, c in zip(xs, [c[v] for c in rgb_colors])]
        cdict[k] = tuple(ctuples)
    return cdict

blue_white_orange = (colors.LinearSegmentedColormap(
    'svds_diverging', diverging_cmap(blues+oranges[::-1])))
plt.register_cmap(cmap=blue_white_orange)


def color_cmap(colors, reverse=False):
    rgb_colors = norm_rgb(hex2rgb(colors))
    cdict = {}
    # linear color map
    xs = [0, 0.15, 0.30, 0.45, 1]
    # add white to list of colors
    rgb_colors += [(1, 1, 1)]
    if reverse:
        rgb_colors = rgb_colors[::-1]
    for k, v in [('red', 0), ('green', 1), ('blue', 2)]:
        ctuples = [(x, c, c) for x, c in zip(xs, [c[v] for c in rgb_colors])]
        cdict[k] = tuple(ctuples)
    return cdict

cmap_oranges = (colors.LinearSegmentedColormap(
    'svds_oranges', color_cmap(oranges)))
cmap_oranges_r = (colors.LinearSegmentedColormap(
    'svds_oranges_r', color_cmap(oranges, reverse=True)))

plt.register_cmap(cmap=cmap_oranges)
plt.register_cmap(cmap=cmap_oranges_r)

cmap_blues = (colors.LinearSegmentedColormap(
    'svds_blues', color_cmap(blues)))
cmap_blues_r = (colors.LinearSegmentedColormap(
    'svds_blues_r', color_cmap(blues, reverse=True)))

plt.register_cmap(cmap=cmap_blues)
plt.register_cmap(cmap=cmap_blues_r)
