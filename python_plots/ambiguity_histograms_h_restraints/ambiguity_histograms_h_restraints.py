
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


sns.set_style("white")
sns.set_context("paper")
sns.set(style="ticks", font="serif")

def make_histograms():

    HHN_before = [3, 6, 2, 6, 2, 6, 6, 8, 9, 74]
    NNH_before = [4, 10, 6, 6, 8, 12, 9, 9, 6, 57]
    HHN_after = [41, 20, 4, 8, 1, 3, 3, 3, 5, 34]
    NNH_after = [42, 26,  2, 5, 5, 4, 7, 3, 1, 32]

    total_before = list(np.array(NNH_before) + np.array(HHN_before))
    total_after = list(np.array(NNH_after) + np.array(HHN_after))
    together = HHN_before + NNH_before + total_before + HHN_after + NNH_after + total_after

    times = ['before']*30 + ['after']*30
    spectra = ['HHN']*10 + ['NNH']*10 + ['total']*10 + ['HHN']*10 + ['NNH']*10 + ['total']*10
    ambiguities = range(1,11)*6

    data = zip(ambiguities, together, times, spectra)
    df = pd.DataFrame(data, columns=['ambiguities', 'frequency', 'time', 'spectrum'])

    df_HHN = df[df['spectrum']=='HHN']
    df_total = df[df['spectrum']=='total']

    ax = sns.barplot(x='ambiguities', y='frequency', hue='time', data=df_total, palette=('#a6cee3','#fb9a99'))
    ax = sns.barplot(x='ambiguities', y='frequency', hue='time', data=df_HHN, palette=('#1f78b4','#e31a1c'))
    sns.despine()
    ax.set_ylabel("number of restraints")
    ax.set_xlabel("number of items per restraint")
    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[9] = '>=10'
    ax.set_xticklabels(labels)

    legend = ax.legend(loc='upper left')
    texts = legend.get_texts()
    texts[0].set_text('hNhhNH unfiltered')
    texts[1].set_text('hNhhNH filtered')
    texts[2].set_text('hNHH unfiltered')
    texts[3].set_text('hNHH filtered')

    plt.show()



if __name__ == '__main__':
    make_histograms()