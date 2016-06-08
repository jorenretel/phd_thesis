

General Discussion and Outlook
==============================

The goal of these studies is to develop new methods for the structure determination of membrane proteins. OmpG reconstituted in native lipids serves as a good system for the development of new methods in solid-state NMR. Because of the size of the protein and the non-crystalline nature of the sample, OmpG provides the challenges that make it necessary to explore different strategies for sequential assignment and structure calculation.

Different labeling strategies were explored to be able to make assignments using ^13^C-detected experiments. This strategy gave access to a starting assignment. However, the use of ^1^H-detected experiments were absolutely necessary to make a complete assignment. The assignment strategy based on ^1^H-detected experiments is much more robust since the addition of an independent nucleus contributes enormously to the dispersion of the spectra. Furthermore, it is more clear how many residues contribute to the total signal set as there is exactly one peak per residue in these spectra. So far, the signal to noise and dispersion of OmpG spectra obtained by ^1^H-detection experiments are very limited, but there is still a lot of room for improvement.

The successful application of ^1^H-detection on a variety of systems, among which OmpG, already caused ^1^H-detection to become more common and will undoubtedly become the standard detection method in solid-state NMR within the next few years. Whereas 3 years ago only a few labs in the world owned a ultra fast spinning probe, the field is quickly adapting. Because more spectrometers are equipped with ultra fast spinning probes, experiment time on these devices will become slightly less scarce and therefore it will be feasible to explore more systematically which type of experiments work best for systems like OmpG. For example, it would be interesting to compare different ^13^C-^13^C transfer methods as it seems that a lot of signal is lost during the scalar based method used so far in this project. This transfer method was used, because other experiments on proteins in micro-crystalline samples indicated that it was slightly more efficient than dipolar based methods. As discussed, this might be different for OmpG because the T~2~ is shorter. Also ^1^H-detected experiments that give access to sidechain chemical shifts should be tested. Although it was possible to assign OmpG ^13^C sidechain chemical shifts with the aid of ^13^C-detected experiments, a completely different set of isotope labeled samples was used to do this. It would be favorable to only use one sample to obtain the spectra necessary for the sequential assignment and the assignment of sidechain chemical shifts. As discussed in chapter 4, a number of different ^1^H-detected approaches have been developed to access sidechain chemical shifts but it should be assessed which approach would be most effective on a membrane protein preparation like OmpG.

For the structure calculation it was very important that the restraint sets based on ^1^H-detected and ^13^C-detected experiments could enter the calculation at different stages. In addition, restraint combination was crucial to minimize the negative effect of ambiguous restraints that did not contain the correct assignment option. Because OmpG is a β-barrel, ^1^H-^1^H restraints between amide groups in the backbone are in principle sufficient to define the contacts between the individual β-strands. Therefore, the correct topology of the strands is already found in the first iteration of the ARIA protocol. This in turn restricts the possibilities for the assignment of the ^13^C-^13^C restraints that enter the calculation in a later stage. In proteins with other topologies, restraints between sidechains are necessary to find the correct relative orientation between different structural elements and therefore the structure calculation protocol described here, using only ^1^H-^1^H restraints between exchangeable protons in the first iterations, will not work. To be able to let the ^13^C-^13^C restraints enter the calculation in the very first iteration, the fraction of assigned ^13^C chemical shifts should be higher, so that it can be made sure that almost no ambiguous restraints are present that do not contain the correct assignment option. In alternative would be to measure ^1^H-^1^H restraints between labeled methyl groups. Yet another option would be to use even higher MAS rates, so that fully protonated protein samples can be used.

The use of fully protonated proteins and faster MAS frequencies (~100 kHz) might also be necessary for proteins that can not (in contrast to OmpG) be easily refolded. In these proteins, the exchange of deuterons by protons within secondary structure elements will not be efficient as all amide protons will be involved in a hydrogen bond.

Besides using OmpG as a system to further improve solid-state NMR methodology, it will be interesting to address some of the open questions surrounding the pH-dependent opening and closing mechanism of this porin. It could be investigated whether more signals are present in spectra of OmpG mutants for which the spontaneous gating is minimized, described in the general introduction.

During the assignment process, which was by far the most time consuming part of these studies, it was important to keep a good bookkeeping. For this reason, the comprehensive data model provided by CCPNMR was of great value. Furthermore, it is very important to be able to get a fast overview of the assignments that have been made and of those that are still missing. Because methodologies in solid-sate NMR are quickly evolving, the possibility to extend CCPNMR Analysis by writing macros is very useful. This can be used to provide computational tools that fit newly developed methodology. The plug-ins for CCPNMR Analysis written in the context of these studies proved to be very helpful during the assignment process.