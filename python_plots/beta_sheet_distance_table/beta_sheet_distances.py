

from Bio.PDB import PDBParser
from numpy import std, average

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

OmpA_beta_sheet_pairs = [(8, 42), (10, 40), (12, 38), (14, 36), (16, 34),
                         (52, 80), (54, 78), (75, 103), (77, 101), (79, 99),
                         (81, 97), (83, 95), (85, 93)]

parser = PDBParser()

#structure = parser.get_structure('OmpA', '/homes/retel/qj/pdb1qjp.ent')
structure = parser.get_structure('OmpA', 'pdb2ge4.ent')



#nuclei = ['CA', 'CB', 'C', 'HA', 'H']
nuclei = ['H']

def calculate_distances():
    #nuclei = ['CA', 'CB', 'C']
    #nuclei = ['CA', 'CB', 'C', 'N', 'H', 'HA', 'HB']
    #nuclei = ['H', 'HA', 'HB']
    intra = {}
    sequential = {}
    longrange1 = {}
    longrange2 = {}
    for chain in structure.get_chains():
        residues = list(chain.get_residues())
        for one, two in OmpA_beta_sheet_pairs:
            resA = residues[one]
            resB = residues[one+1]
            resC = residues[two-1]
            resD = residues[two]

            for nucleus1 in nuclei:
                for nucleus2 in nuclei:

                    if nucleus1 in resA and nucleus2 in resA:
                        intra[(nucleus1, nucleus2)] = intra.get((nucleus1, nucleus2), [])
                        intra[(nucleus1, nucleus2)].append(resA[nucleus1] - resA[nucleus2])

                    if nucleus1 in resA and nucleus2 in resB:
                        sequential[(nucleus1, nucleus2)] = sequential.get((nucleus1, nucleus2), [])
                        sequential[(nucleus1, nucleus2)].append(resA[nucleus1] - resB[nucleus2])

                    if nucleus1 in resA and nucleus2 in resD:
                        longrange1[(nucleus1, nucleus2)] = longrange1.get((nucleus1, nucleus2), [])
                        longrange1[(nucleus1, nucleus2)].append(resA[nucleus1] - resD[nucleus2])

                    if nucleus1 in resB and nucleus2 in resC:
                        longrange2[(nucleus1, nucleus2)] = longrange2.get((nucleus1, nucleus2), [])
                        longrange2[(nucleus1, nucleus2)].append(resB[nucleus1] - resC[nucleus2])


    replace_by_stats(intra)
    replace_by_stats(sequential)
    replace_by_stats(longrange1)
    replace_by_stats(longrange2)

    return intra, sequential, longrange1, longrange2


def nucleus_in_residue(residue, nucleus):

    for name in residue.child_dict.keys():
        if nucleus in name:
            return residue[name]


def replace_by_stats(dictionary):

    for nuclei, distance in dictionary.items():
        dictionary[nuclei] = (average(distance), std(distance))


def create_correlation_plot(distances):

    xaxis_labels = nuclei
    yaxis_labels = nuclei * 4

    data = []

    for combination in distances:
        for nucleus2 in xaxis_labels:
            row = []
            data.append(row)
            for nucleus1 in xaxis_labels:
                if (nucleus1, nucleus2) in combination:
                    row.append(combination[nucleus1, nucleus2][0])
                else:
                    row.append(None)


    data = pd.DataFrame(data=data, index=yaxis_labels, columns=xaxis_labels)
    sns.heatmap(data, cmap="YlGn_r", annot=True)
    plt.show()


create_correlation_plot(calculate_distances())
