import seaborn as sns
import matplotlib.pyplot as plt


sns.set_style("white")
sns.set_context("paper")
sns.set(style="ticks", font="serif")


def make_figure():

    f, ax = plt.subplots(1, 1, figsize=(5, 3), sharey=True)

    file_name = 'malandro_deleting_peaks.txt'

    colors = ['#1f78b4', '#e31a1c']

    fractions, correct, false_positive = parse_stats_file(file_name)

    ax.scatter(fractions, correct, color=colors[0])
    ax.plot(fractions, correct, color=colors[0], label='correct assignment')

    ax.scatter(fractions, false_positive, color=colors[1])
    ax.plot(fractions, false_positive, color=colors[1], label='false positive')

    ax.set_xlim([0, 1.0])
    ax.set_ylim([0, 1.0])
    ax.set_xlabel('fraction of deleted peaks')
    ax.set_ylabel('fraction of residues')
    ax.legend()
    plt.tight_layout()
    sns.despine()
    plt.savefig('malandro_deleing_peaks.svg')


def parse_stats_file(file_name):

    correct = []
    false_positive = []
    fractions = []

    with open(file_name, 'r') as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            if words:
                fractions.append(float(words[0]))
                correct.append(float(words[3]))
                false_positive.append(float(words[4]))
    return fractions, correct, false_positive


if __name__ == '__main__':
    make_figure()