
Structure Calculation
=====================

The restraints used in the structure calculation of OmpG can exist of two types: torsion angle restraints that are based on chemical shifts of the residues and distances restraints based on crosspeaks in through-space correlation spectra. This second group of restraints can in turn be subdivided into a group of distance restraints obtained from ^1^H-detected experiments and another group that is based on ^13^-detected experiments.


## Torsion Angle Restraints

Torsion angles where predicted using the program TALOS+ [@shen_talos_2009][@cornilescu_protein_1999].

![Prediction of the secondary structure of OmpG by TALOS+ and PRED-TMBB. TALOS+ uses the secondary chemical shifts to predict the secondary structure of each residue. PRED-TMBB is a algorithm that solely relies on the sequence and predicts which parts of the sequence are intra-cellular, extra-cellular and transmembrane given the molecule is a transmembrane beta-barrel.](figures/secondary_structure_and_topology_prediction.svg)



![Average distances between carbon nuclei (top), and the amide protons in the backbone (bottom) in anti-parallel betasheets. The residues i and j are two residues that are facing one another in the oposing strands of the betasheet and are linked with two hydrogen bonds.](figures/distances_in_antiparallel_betasheet.svg)



![Strips in the hNhhNH and NNH corresponding to the cross-strand inaction between the backbone amide groups of Tyrosine 76 and Leucine 88.](figures/through_space_proton_detected_strips_Tyr76_Leu88.svg)



