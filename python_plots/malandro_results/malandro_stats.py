import seaborn as sns
import matplotlib.pyplot as plt


def make_figure():

    f, axes = plt.subplots(5, 1, figsize=(12, 8), sharey=True)

    file_names = ['sh3_carbon.txt', 'sh3_proton.txt', 'yada.txt', 'ompg.txt', 'ompg_proton.txt']
    titles = ['SH3 carbon detected', 'SH3 proton detected',
              'yadA carbon detected', 'OmpG proton and carbon detected', 'OmpG proton detected']
    colors = ['#1f78b4', '#e31a1c', '#a6cee3', '#fb9a99']

    for file_name, ax, title in zip(file_names, axes, titles):
        stats = parse_stats_file(file_name)
        print title
        for stat, color in zip(stats, colors):
            first_picks = 0
            zero_free = []
            for point in stat:
                if point == 0:
                    zero_free.append(None)
                else:
                    zero_free.append(point)
                if point > 50.0:
                    first_picks += 1
            print first_picks        
            ax.scatter(range(1, len(stat)+1), zero_free, color=color)
        ax.set_title(title)
        ax.set_xlim([0, len(stat)+1])
        ax.xaxis.set_ticks(range(0, len(stat)+1, 10))
        ax.set_ylim([0, 105])
        ax.set_xlabel('residues')
        ax.set_ylabel(r'% agreeing / disagreeing')
    plt.tight_layout()
    plt.savefig('malandro_statistics.svg')


def parse_stats_file(file_name):

    correct = []
    incorrect = []
    correct_joker = []
    incorrect_joker = []

    with open(file_name, 'r') as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            if words:
                correct.append(int(words[0]))
                incorrect.append(abs(int(words[1])))
                correct_joker.append(int(words[2]))
                incorrect_joker.append(abs(int(words[3])))
    return correct, incorrect, correct_joker, incorrect_joker



if __name__ == '__main__':
    print make_figure()