
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib import gridspec
from matplotlib import colors as mplcolors

sns.set_style("white")
sns.set_context("paper")
sns.set(style="ticks", font="serif")


def main():
    gs = gridspec.GridSpec(3, 1, height_ratios=[5, 10, 1])
    ax2 = plt.subplot(gs[0])
    ax1 = plt.subplot(gs[1], sharex=ax2)
    ax3 = plt.subplot(gs[2], sharex=ax2)

    color_map = get_colors()
    sequence = []
    secondary_structure = []
    helix_prediction = []
    sheet_prediction = []
    coil_prediction = []
    s2 = []

    domains = [['in', 1, 6],
               ['tm', 7, 15],
               ['out', 16, 28],
               ['tm', 29, 37],
               ['in', 38, 43],
               ['tm', 44, 50],
               ['out', 51, 65],
               ['tm', 66, 78],
               ['in', 79, 83],
               ['tm', 84, 92],
               ['out', 93, 112],
               ['tm', 113, 123],
               ['in', 124, 126],
               ['tm', 127, 135],
               ['out', 136, 151],
               ['tm', 152, 162],
               ['in', 163, 165],
               ['tm', 166, 178],
               ['out', 179, 191],
               ['tm', 192, 202],
               ['in', 203, 204],
               ['tm', 205, 215],
               ['out', 216, 234],
               ['tm', 235, 245],
               ['in', 246, 248],
               ['tm', 249, 259],
               ['out', 260, 270],
               ['tm', 271, 281]]

    predtmbb = [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2,
                2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2,
                2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2,
                2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0,
                2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2,
                2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2,
                2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    predtmbb = np.array([predtmbb])

    for domain in domains:
        if domain[0] == 'tm':
            ax2.axvspan(domain[1], domain[2]+1, alpha=0.2, color='grey')
            ax1.axvspan(domain[1], domain[2]+1, alpha=0.2, color='grey')

    predtmbb_colors = sns.color_palette("Dark2", 5)
    predtmbb_colors_map = mplcolors.ListedColormap([predtmbb_colors[2], predtmbb_colors[3], predtmbb_colors[0]])
    ax3.pcolor(predtmbb, cmap=predtmbb_colors_map, vmin=0, vmax=2)

    in_patch = mpatches.Patch(facecolor=predtmbb_colors[2], label='Intra-Cellular')
    out_patch = mpatches.Patch(facecolor=predtmbb_colors[3], label='Extra-Cellular')
    tm_patch = mpatches.Patch(facecolor=predtmbb_colors[0], label='Transmembrane')
    ax3.legend(handles=[ tm_patch, in_patch, out_patch], loc='lower left', bbox_to_anchor=(0.78, 0.5),fontsize='x-small', labelspacing=0.05)#prop={'size':6})

    with open('pred.tab', 'r') as pred:
        lines = pred.readlines()
        sequence = get_sequence(lines)
        s2 = [None]*len(sequence)
        helix_prediction = [0.0]*len(sequence)
        sheet_prediction = [0.0]*len(sequence)
        coil_prediction = [0.0]*len(sequence)
        for line in lines:
            words = line.split()
            if words and words[0].isdigit():
                s2[int(words[0])-1] = float(words[7])
    with open('predSS.tab', 'r') as pred_ss:
        secondary_structure = [0.0]*len(sequence)
        for line in pred_ss.readlines():
            words = line.split()
            if words and words[0].isdigit():
                highest = max([float(prob) for prob in words[-5:-2]])
                secondary_structure[int(words[0])-1] = highest
                helix_prediction[int(words[0])-1] = float(words[4])
                sheet_prediction[int(words[0])-1] = float(words[5])
                coil_prediction[int(words[0])-1] = float(words[6])

    ax1.bar(range(1,len(sequence)+1), sheet_prediction, width=1.0, color=color_map['E'], alpha=0.75, label='Beta Sheet')
    ax1.bar(range(1,len(sequence)+1), coil_prediction, width=1.0, color=color_map['L'], alpha=0.75, label='Coil')
    ax1.bar(range(1,len(sequence)+1), helix_prediction, width=1.0, color=color_map['H'], alpha=0.75, label='Helix')


    ax1.legend(loc='lower left', bbox_to_anchor=(0.78, 0.95),fontsize='x-small', labelspacing=0.05)
    xs = []
    ys = []
    x_series = [xs]
    y_series = [ys]

    last_x = 0
    for i, value in enumerate(s2):
        if value:
            if i == last_x + 1:
                xs.append(i+1)
                ys.append(value)
            else:
                xs = [i+1]
                ys = [value]
                x_series.append(xs)
                y_series.append(ys)
            last_x = i

    for xs, ys in zip(x_series, y_series):
        ax2.plot(xs, ys, marker='.', color=color_map['E'])
    ax2.axis([1, 282, 0.5, 1])
    ax2.xaxis.set_visible(False)
    ax1.xaxis.set_visible(False)
    ax3.yaxis.set_visible(False)

    ax2.set_title('TALOS+ Predicted RCI S2 Value', y=1.2)
    ax2.set_ylabel('S2 Value')
    ax1.set_title('TALOS+ Predicted Secondary Structure', y=1.1)
    ax1.set_ylabel('probability')
    ax3.set_title('PRED-TMBB Predicted Topology', y=2)
    ax3.set_xlabel('residue number')
    ax3.xaxis.set_ticks(range(0, 282, 20))

    sns.despine()

    plt.subplots_adjust(hspace=0.55)
    plt.savefig('secondary_structure_and_topology_prediction.svg', bbox_inches='tight')


def get_sequence(lines):

    found = False
    sequence = []

    for line in lines:
        words = line.split()

        if words and words[0] == 'DATA' and words[1] == 'SEQUENCE':
            sequence.extend(list(words[2]))
            found = True
        elif found:
            break
    return sequence

def get_colors():
    e, h, l = sns.color_palette("Dark2", 3)
    return {'E': e, 'H': h, 'L': l, 'X': None}


if __name__ == '__main__':
    main()