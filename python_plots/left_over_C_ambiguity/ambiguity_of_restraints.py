'''
CCPN Macro script to produce a histogram of ambiguity
in constraint lists. Here only the 13C-13C spectra are
plotted.

'''


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


sns.set_style("white")
sns.set_context("paper")
sns.set(style="ticks", font="serif")

OUTPUT_FILE = '/home/joren/left_over_C_ambiguity.svg'

# This causes the text to be saved as
# text in the SVG file instead of paths
matplotlib.rcParams['svg.fonttype'] = 'none'


def create_ambiguity_histogram(argServer):

    project = argServer.getProject()
    nmrProject = project.findFirstNmrProject()
    store_serial = 64   # Serial pointing to the constaint list I want to use
    nmrConstraintStore = nmrProject.findFirstNmrConstraintStore(serial=store_serial)
    allConstraintLists = nmrConstraintStore.constraintLists

    f, ax = plt.subplots(1, 1)

    xs = range(1,11)
    ys_total = np.zeros(10)

    colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e']

    # Making sure the smallest barchart is shown on top.
    zorder = len(allConstraintLists)

    for constraintList in allConstraintLists:
    	# Plotting ambiguity of rejected peaks does not make much sense
        if 'REJECT' in constraintList.name:
            continue
        # Only make the plot for the 13C-13C spectra
        if get_isotope(constraintList) != '13C':
        	continue
        print constraintList.name

        experiment_name = constraintList.findFirstExperiment().name

        ys_one_set = np.zeros(10)

        for constraint in constraintList.constraints:
        	ambiguity = len(constraint.items)
        	# I want to stop the plot at 10. So 10 is actually >=10
        	# I do not have any ambiguity over 10. Just for safety.
        	if ambiguity > 10:
        		ambiguity = 10
        	ys_one_set[ambiguity-1] += 1

        print ys_one_set

        ys_total += ys_one_set
        color = colors.pop()

        ax = sns.barplot(x=xs, y=ys_total, color=color, zorder=zorder, label=experiment_name, ax=ax)
        zorder -=1

    sns.despine()
    ax.set_ylabel("number of restraints")
    ax.set_xlabel("number of items per restraint")
    legend = ax.legend(loc='upper right')

    plt.savefig(OUTPUT_FILE)


def get_isotope(constraintList):

    c = constraintList.findFirstConstraint()
    item = c.findFirstItem()
    resonance = item.findFirstResonance()
    return resonance.isotopeCode