
Structure Calculation
=====================

The restraints used in the structure calculation of OmpG can exist of two types: torsion angle restraints that are based on chemical shifts of the residues and distances restraints based on crosspeaks in through-space correlation spectra. This second group of restraints can in turn be subdivided into a group of distance restraints obtained from ^1^H-detected experiments and another group that is based on ^13^-detected experiments.


## Torsion Angle Restraints

Torsion angles where predicted using the program TALOS+ [@cornilescu_protein_1999][@shen_talos_2009]. In figure {@fig:secondary_structure_and_topology_prediction} the secondary structure that correponds to these torsion angles by TALOS+ is shown along the OmpG sequence. Of course a prediction based on chemical shifts is only possible for assigned residues. As expected the larged part of the assigned residues are predicted to be in a β-sheet conformation. These results can also be compared to a prediction of the topology done purely on the basis of the amino acid sequence by the program called PRED-TMBB [@bagos_predtmbb_2004]. This tool is specifically designed for β-barrel and predicts which part of the molecule is part of the transmembrane β-sheet, intra-cellular turn and extra-cellular loop. Because the algorithm is based on machine learning, we send the author of the program an email to verify that previously calculated OmpG structures were not part of the training data, which was not the case. It can be observed that the to prediction allign fairly well. Where PRED-TMBB predicts a turn, the chemical shifts are more coil-like. In these turns also a lower RCI-S2 value can be observed, indicating a less ordered part of the molecule. The missing assignments cluster largely in the extra-cellular loops.


![Prediction of the secondary structure of OmpG by TALOS+ and PRED-TMBB. TALOS+ uses the secondary chemical shifts to predict the secondary structure of each residue. PRED-TMBB is a algorithm that solely relies on the sequence and predicts which parts of the sequence are intra-cellular, extra-cellular and transmembrane given the molecule is a transmembrane β-barrel.](figures/secondary_structure_and_topology_prediction.svg){#fig:secondary_structure_and_topology_prediction}



## Restraints based on ^1^H-detected through-space correlation experiments

To get a good set of restraints, through space correlations where acquired on the perdeuterated samples, where the exchangable sites where 100% back-exchanged for protons. The same type of sample that was used to aqcuire part of the proton-detected experiments needed for sequential assignment discussed earlier. Two spectra where recorded: an hNHH and an hNhhNH, both using cross-polarization for transfers between proton and nitrogen and a 2 ms radio frequency driven recoupling (rfdr) sequence for the transfer between the protons.
Since most of the proton sites in the molecule are deuterated, most peaks present in these spectra are peaks correlating one amide group to another. In both spectra a strip contains, besides the diagonal peak, one big crosspeak, and often one or two smaller crosspeaks. In the hHNHH this peaks correlate the nitrogen and proton of one NH-group to a closeby proton and in the hNhhNH the nitrogen and proton of one NH group is correlated to a nitrogen of a close NH-group. Since the correlation pathway of the latter experiment is makes sure that both intacting protons are part of an NH-group this spectrum is a little bit cleaner. If both spectra are considered together there are four peaks indicating the proximity of two NH groups. An example of such a group of four peaks correlating two amide groups is shown in figure {@fig:through_space_proton_detected_strips_Tyr76_Leu88}. In the case of an anti-parallel β-sheet, the biggest off-diagonal peak is almost always between two amide groups facing each other located in neighboring strands in the sheet. These two amide groups are making hydrogen bonds with each other's carbonyl-oxygens and are on average only 3.1 Å seperated from one another, see figure {@fig:distances_in_antiparallel_betasheet}B. The smaller peaks are often correlations to the amide groups of the neighboring residues in the same strand or to the amide group of the residue after the directly hydrogen bonded residue. As can be seen in {@fig:distances_in_antiparallel_betasheet}, a very specific alternating pattern of cross-peaks is expected connecting two strands in the β-sheet, skipping the residues in between which in turn are pointing towards the neighboring strand on the other side. Of course these restraints are very powerfull in defining the general fold of a β-barrel like OmpG.

Because there are in principle four crosspeaks the correlate the same two amide groups, this redundancy can easily be used to decrease the ambiguity of automatically generated ambidistances distance restraints, already before the structure calculation. A ccpn macro script was used to determine for which options in of the ambiguous restraint all four peaks where present (giving rise to three other ambiguous restraints that have the correlation between these amide hydrogens as on of the options). For the restraints that had such options, all other options that had only 2 or less peaks indicating that assignment of the restraint (instead of four), where removed. When plotting


## Restraints based on ^13^C-detected through-space correlation experiments

Another set of distance restraints comes from a set of ^13^C-detected experiments that where also used for the assignment. All spectra that where used where 2 dimensional 13^C^-^13^C correlations with 400 ms DARR mixing. Several spectra with good dispersion and signal to noise where selected to create distance restraints.





![Average distances between carbon nuclei (top), and the amide protons in the backbone (bottom) in anti-parallel β-sheets. The residues i and j are two residues that are facing one another in the oposing strands of the β-sheet and are linked with two hydrogen bonds.](figures/distances_in_antiparallel_betasheet.svg){#fig:distances_in_antiparallel_betasheet}





![Strips in the hNhhNH and NNH corresponding to the cross-strand inaction between the backbone amide groups of Tyrosine 76 and Leucine 88.](figures/through_space_proton_detected_strips_Tyr76_Leu88.svg){#fig:through_space_proton_detected_strips_Tyr76_Leu88}



