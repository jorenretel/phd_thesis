
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


sns.set_style("white")
sns.set_context("paper")
sns.set(style="ticks", font="serif")

def make_histograms():

    #HHN_peaklist2_shiftmatch_0.07_0.1_0.4 before symmetry filter
    #HHN_before = {1: 3, 2: 6, 3: 2, 4: 6, 5: 2, 6: 6, 7: 6, 8: 8, 9: 9, 10: 74}

    HHN_before = [3, 6, 2, 6, 2, 6, 6, 8, 9, 74]
    #NNH_peaklist2_shiftmatch_0.07_0.4_0.4 before symmetry filter
    #NNH_before = {1: 4, 2: 10, 3: 6, 4: 6, 5: 8, 6: 12, 7: 9, 8: 9, 9: 6, 10: 57}

    NNH_before = [4, 10, 6, 6, 8, 12, 9, 9, 6, 57]
    #HHN_peaklist2_shiftmatch_0.07_0.1_0.4 after
    #HHN_after = {1: 41, 2: 20, 3: 4, 4: 8, 5: 1, 6: 3, 7: 3, 8: 3, 9: 5, 10: 34}

    HHN_after = [41, 20, 4, 8, 1, 3, 3, 3, 5, 34]
    #NNH_peaklist2_shiftmatch_0.07_0.4_0.4 after
    #NNH_after = {1: 42, 2: 26, 3: 2, 4: 5, 5: 5, 6: 4, 7: 7, 8: 3, 9: 1, 10: 32}

    NNH_after = [42, 26,  2, 5, 5, 4, 7, 3, 1, 32]

    total_before = list(np.array(NNH_before) + np.array(HHN_before))
    total_after = list(np.array(NNH_after) + np.array(HHN_after))

    together = HHN_before + NNH_before + total_before + HHN_after + NNH_after + total_after

    times = ['before']*30 + ['after']*30
    spectra = ['HHN']*10 + ['NNH']*10 + ['total']*10 + ['HHN']*10 + ['NNH']*10 + ['total']*10
    ambiguities = range(1,11)*6

    data = zip(ambiguities, together, times, spectra)


    df = pd.DataFrame(data, columns=['ambiguities', 'frequency', 'time', 'spectrum'])
    print df

    df_HHN = df[df['spectrum']=='HHN']
    df_total = df[df['spectrum']=='total']

    print df_HHN

    ax = sns.barplot(x='ambiguities', y='frequency', hue='time', data=df_total, palette=('#a6cee3','#fb9a99'))
    ax = sns.barplot(x='ambiguities', y='frequency', hue='time', data=df_HHN, palette=('#1f78b4','#e31a1c'))
    sns.despine()
    ax.set_ylabel("frequency")
    ax.set_xlabel("number of restraint items")
    plt.show()



if __name__ == '__main__':
    make_histograms()