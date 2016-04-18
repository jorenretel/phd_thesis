
Connecting Assignments in ^13^C- and ^1^H-detected Spectra
==========================================================

## Access to side-chain chemical shifts in perdeuterated proteins

For the sequential assignment of proteins the knowledge of side-chain chemical shifts other than the Cβ has a great advantage. Because these shifts vary more widely between different amino acids, residue typing is simplified which in turn helps mapping stretches of connected spin systems to a subsequence of the protein. Also for structure calculation of most proteins side-chain chemical shifts have to be known to generate the necessary distance restraints. In perdeuterated proteins two related problems arise that complicate the acquisition of the spectra necessary to group a complete set of side-chain resonances into spin systems. First of all the protons in close proximity to the carbon nuclei in the side-chain are removed making ^1^H-^13^C cross-polarization less efficient. Second, mixing schemes that are based on the re-introduction of ^1^H-^1^H dipolar couplings such as DARR and PDSD become ineffective, especially at very fast MAS.

The simplest solution to the first problem is to use direct ^13^C excitation. Obviously that leads to lower signal to noise compared to ^1^H-^13^C CP in a fully protonated protein due to the lower gyromagnetic ratio of ^13^C. Also the ^13^C T1 relaxation times are rather long and therefor a long recycle delay is necessary. However this can be reduced by adding a paramagnetic relaxation enhancer to the sample [@linser_sensitivity_2007][@linser_sidechain_2011]. An alternative solution could be to transfer magnetization from deuterium to carbon. Although deuterium actually has a slightly lower gyromagnetic ratio than ^13^C itself (4.11x10^7^ versus 6.73x10^7^ T^-1^s^-1^) its T1 time is very short allowing for very fast repetition of experiments. Initial deuterium excited experiments have been performed on SH3, ubiquitin and OmpG [@agarwal_highresolution_2009][@lalli_threedimensional_2011]. Aside from just using deuterium to transfer magnetization to carbons in these studies the deuterium double quantum frequency was measured in a indirect dimension, adding dispersion to the spectra. This technique is promising but not very mature yet.

As to which mixing scheme to use for the transfer of magnetization between carbons in the side-chain there are multiple options such DREAM, RFDR and TOBSY that do not rely on protons [@verel_adiabatic_2001][@hardy_fast_2001][@leppert_adiabatic_2004][@agarwal_residual_2008][@huang_homonuclear_2011]. The ideal experiment would be an experiment similar to the NH-TOCSY used in solution NMR where a complete set of side-chain ^13^C resonances is correlated to the ^15^N-^1^H pair in the backbone [@montelione_efficient_1992][@grzesiek_correlation_1993]. Indeed *Linser* performed a conceptually similar experiment on SH3 in the solid state using a combination of a long-range ^1^H-^13^C CP step and direct ^13^C excitation to transfer sufficient magnetization to the carbons and using TOBSY as the mixing sequence [@linser_sidechain_2011]. Here the ^13^C magnetization is transferred back to the backbone using another long-range ^1^H-^13^C CP instead of a ^15^N-^13^C CP, which positively influenced the signal to noise but comes at the cost of losing some specificity for intra-residual peaks. In a larger protein this will be more problematic because signal overlap and ambiguity are increased. It would be interesting to see how well a similar sequence based on deuterium excitation works.

Yet another very practical approach is use a sample that is  sparsely and randomly protonated at non-exchangeable sites giving access to both assignments and distance restraints [@asami_high_2010][@asami_assignment_2011][@asami_optimal_2012]. Another way to gain access to structural restraints is to introduce proton labeled methyls, which is often done in solution NMR of large proteins with long correlation times and has also been applied in the solid state [@tugarinov_isotope_2006][@agarwal_high_2006][@linser_structure_2011][@huber_protondetected_2011].


## Combining information from protonated and deuterated samples

For the assignment of OmpG a combination of ^13^C- and ^1^H-detected experiments has been used. Since a large set of fully protonated and residue specifically labeled samples and corresponding spectra already existed this was the most straight-forward approach. The three nuclei that are measured in both the ^1^H- and ^13^C-detected experiments, namely the N, Cα and Cβ, can be used to connect data from both these types of samples. The ^13^C chemical shifts found in a strip of the ^1^H detected spectra can be used to find the Cα-Cβ cross peak 2D ^13^C-^13^C correlation spectra. If there is enough dispersion in the ^13^C-^13^C spectrum this peak can be easily found and from there the rest of the ^13^C chemical shifts of the side-chain. Also the NCACX spectra are used for this purpose. Because of the superior quality of the 2D ^13^-^13^Ĉ correlations use of these spectra was preferred. An added advantage of using both protonated and deuterated samples is that both ^1^H-^1^H restraints from ^1^H-detected RFDR experiments and ^13^C-^13^C restraints from PDSD or DARR experiments can be used during the structure calculation.


### Isotope Shift

The replacement of protons by deuterons can alter the ^13^C chemical shifts by up to a full ppm. Therefor a correction for this deuterium isotope shift has to be performed. This deuterium shift has been described before and quantified by solution NMR spectroscopists [@hansen_isotope_1988][@venters_characterizing_1996][@maltsev_deuterium_2012]. The magnitude of the shift can be approximated by the following equation:

$$\Delta C(D) =  ^{1}\Delta C(D)d _{1} + ^{2}\Delta C(D)d _{2} + ^{3}\Delta C(D)d _{3}$$ {#eq:isotope_shift}

Here *d~1~*, *d~2~* and *d~3~* are the amount of deuterons one, two and three bonds away from the carbon nucleus of interest. For all amino acid types, except Glycine, more deuterons are surrounding the Cβ than the Cα and therefor the Cβ shifts are more affected. One of the residue types with the largest isotope shifts is leucine, as can be seen in figure {@fig:thr_and_leu_dotplots}. Both *Venters et al.* and *Maltsev et al.* determined the factors ^i^ΔC(D) experimentally, but got slightly different values [@venters_characterizing_1996][@maltsev_deuterium_2012]. As argued by *Maltsev et al.* this is just a estimate, as the real values also heavily depend on the local structure. Indeed the study of *Maltsev et al.* used α-synuclein, which is an intrinsically disordered protein where *Venters et al.* used human carbonic anhydrase I, which is mostly β-sheet with some small α-helices.

The values found by these studies can be used to be in the right ball park and will in most cases be good enough to connect the resonances in proton and carbon detected spectra.  A more exact calculation of the isotope shift does not seem possible for now and if possible in the future it will most probably involve at least secondary structure information like φ and χ angles, which are most likely not known at the stage of sequential assignment.


### Strategy for combining spin systems

Having residue specifically labeled samples will ease the process of matching Cα and Cβ chemical shifts in protonated and deuterated samples enormously since there is a lot less overlap of in the Cα-Cβ regions of these spectra. Because of the many labeling schemes that were produced, there is for nearly every residue type a spectrum in which the Cα-Cβ is well resolved, see table {@tbl:prefered_samples}. It has to be noted that starting from a strip in the ^1^H-detected data to find Cα-Cβ peak in the ^13^C-detected 2D spectra is a lot less error-prone and faster than the reverse procedure. The reason for this is that when starting from a peak in the ^13^C-detected 2D spectra all planes in the ^1^H-detected 3D spectra have to be checked for a fitting Cα-Cβ combination.

The most straight-forward approach to sequential assignment might seem to first finish the backbone and Cβ chemical shift assignment using the ^1^H detected strip matching approach described earlier, and afterwards find the ^13^C side-chain chemical shifts using ^13^C-detected spectra. However, whether it is easier to first sequentially assign a strip in the ^1^H-detected data to a residue and then find its ^13^C detected counterpart or the other way around completely depends on the situation. If the Cα-Cβ combination in the deuterated sample is corresponding to an uncrowded part of the uniformly labeled 2D ^13^C-^13^C correlation, it is of course favorable to find the corresponding spin system in the ^13^C-detected data first since the improved residue typing decreases the amount of options for the sequential assignment. Also, from that point on inter-residual cross peaks in the ^13^C-^13^C correlation can reinforce the certainty that two strips really fit together sequentially.


![Mapping Cα-Cβ combinations from the experiments on deuterated samples on 2D ^13^C-^13^C DARR spectra. For the leucine mapping the GAVLS(W) spectrum (20 ms DARR) is used; for the threonine the 1,3-TEMPQANDSG (50 ms DARR). Positions of Cα-Cβ chemical shifts in deuterated and protonated samples are depicted by stars and circles respectively. Blue colors indicate assigned residues, red colors indicate unassigned spin systems. Light color indicates that no strip in the hCANH, hcaCBcaNH or hCOcaNH could be found corresponding to this residue and therefor the ^1^H shift is unknown.](figures/thr_and_leu_dotplots.svg){#fig:thr_and_leu_dotplots}



![Mapping Cα-Cβ combinations for tryptophan and proline. These are the same two spectra as shown in figure 5.1. GAVLS(W) was used for tryptophan and 1,3-TEMPQANDSG for prolines. Colors also have the same meaning. Two of the tryptophan peaks are very close to the noise and therefor below the contour level drawn here.](figures/trp_and_pro_dotplots.svg){#fig:trp_and_pro_dotplots}



However, if the Cα-Cβ combination in a strip of the deuterated sample corresponds to a very crowded area of the uniformly labeled ^13^C-^13^C correlation, it can sometimes be easier to sequentially assign the spin system purely based on matching strips in the ^1^H-detected spectra first. The reason why the crowding in the uniformly labeled sample matters here is that for a degenerate Cα-Cβ combination it is not known yet to which residue-specifically labeled sample it belongs. Therefor the peaks from different residue-specifically virtually still overlap.
Of course finding the i+1 strip is also harder for very degenerate Cα-Cβ combinations, but at least the peak positions in the ^13^C-dimensions of the matching strips should fit almost perfectly because of the lack of isotope shift within spectra recorded using the same sample. Also, when the hcaCBcacoNH and hcoCAcoNH peaks in the strip correspond to a less degenerate Cα-Cβ combination the assignment can be easily extended in the N-terminal direction. After the sequential assignment of a particular spin system is done, it is a lot easier to find the corresponding ^13^C-detected spin system since now the residue type is known, which limits the choice between possible spin systems and it is clear which of the residue specific labeled ^13^C-^13^C correlations to use to find the matching Cα-Cβ peak. If it is still not clear which Cα-Cβ peak should be chosen, the exact resonance frequencies in the protonated samples can be found by looking at sequential cross-peaks instead of just at the Cα-Cβ peaks. When the strip has already been sequentially assigned, this becomes a lot more trivial since often the correct ^13^C chemical shifts of the neighboring spin system in the protonated sample are already known.
In practice, there is no sharp distinction between the two strategies, since they can basically be used at the same time. In solution NMR the situation is similar. Often the entire back-bone is assigned first before the TOCSY spectra are used to find the side-chain chemical shifts. However in many cases they are consulted already during the sequential assignment process to aid residue typing.



| amino acid                 | sample         | comment            |
|----------------------------|----------------|--------------------|
| alanine                    | RIGA(S)        |                    |
| asparagine / aspartic acid | 1,3 MKINDT     |                    |
| glutamine /glutamic acid   | 1,3-TEMPQANDSG |                    |
| phenylalanine / tyrosine   | GAFY           |                    |
| glycine                    | RIGA(S)        | Cα-CO peak is used |
| histidine                  | GANDSH         |                    |
| isoleucine                 | RIGA(S)        |                    |
| lysine                     | 1,3-MKINDT     |                    |
| leucine                    | GAVLS(W)       |                    |
| methionine                 | 2-TEMPQANDSG   | Cα-Cγ peak is used |
| proline                    | 1,3-TEMPQANDSG |                    |
| arginine                   | RIGA(S)        |                    |
| serine                     | RIGA(S)        |                    |
| threonine                  | 1,3-TEMPQANDSG |                    |
| valine                     | GAVLS(W)       |                    |
| tryptophan                 | GAVLS(W)       |                    |

Table: For every amino acid there is a labeled sample where the intra-residual peaks are best resolved. For some residue types, multiple spectra could be used as a reference spectrum in which case the one specifically used in this study is listed. For methionine there is no labeling scheme in which the Cα-Cβ is separated well from other peaks. Therefor the Cα-Cγ peak is used. The Cγ chemical shift can not be observed in ^1^H-detected spectra. Therefor only the Cα shift can be used directly, further support for the assignment is given by sequential cross peaks.{#tbl:prefered_samples}


## Final extend of the assignment

By combining data from the ^1^H- and ^13^C-detected spectra, a coherent assignment could be found for a bit less than 60% of the residues, see table {@tbl:extend_of_assignment_table}. As can be seen in this table, there are some assigned residues for which the ^1^H and ^15^N is not known. Often these residues are the first residue in an assigned stretch of strips and therefor the ^13^C chemical shifts are known from the hcaCBcacoNH and hcoCAcoNH in the first strip. Also there are a few residues that only have assignments in the ^1^H-detected data, in this case it was very hard to determine exactly where the correspoding shifts in the ^13^C-detected data were. This was the case for a few glutamic acid and glutamine residues and residues where only the Cα-peak was found in the ^1^H detected data and not the Cβ-peak, which makes it harder finding the correspoding spin system in the ^13^C-detected data. In Appendix A the full chemical shift is printed, where the Cα and Cβ shifts given for both the protonated and deuterated samples.




|                   | of assigned residues  | of all residues   |
|-----------------  |---------------------: |----------------:  |
| Carbon Detected   |                       |                   |
| Residues          |        165/170 (97%)  |   165/281 (59%)   |
| N backbone        |        124/170 (73%)  |   124/281 (44%)   |
| C aliphatic       |        443/485 (91%)  |   443/781 (57%)   |
| C aromatic        |         58/227 (26%)  |    58/341 (17%)   |
| CA                |        163/170 (96%)  |   163/281 (58%)   |
| CB                |        145/156 (93%)  |   145/254 (57%)   |
| CO                |        127/204 (62%)  |   127/360 (35%)   |
| Proton Detected   |                       |                   |
| Residues          |        167/170 (98%)  |   167/281 (59%)   |
| H backbone        |        151/164 (92%)  |   151/273 (55%)   |
| N backbone        |        151/170 (89%)  |   151/281 (54%)   |
| CA                |        167/170 (98%)  |   167/281 (59%)   |
| CB                |        131/156 (84%)  |   131/254 (52%)   |
| CO                |        133/204 (65%)  |   133/360 (37%)   |

Table: Extend of the assignment in the shift lists based on the carbon and proton detected spectra.{#tbl:extend_of_assignment_table}


![Assigned status of residues on the topology of OmpG. Colors correspond to the colors used in figure 5.1 and 5.2: blue labeled residues are assigned. Light blue indicates that the ^1^H chemical shift of this residue is not known. Often these residues are the first in a connected stretch and their ^13^C chemical shifts are known from the hcaCBcacoNH, hcoCAcoNH and hCONH peaks in the strip the next residue in the sequence. Residues in red highlight the unassigned residues corresponding to the unassigned spin systems in figure 5.1 and 5.2: three leucines, two threonines, six tryptophans and two prolines. There is only one unassigned proline spin system in figure 5.2, the chemical shifts corresponding to a remaining proline spin system could not be easily determined because of signal overlap.](figures/assignment_on_topology_thr_leu_pro_trp.svg){#fig:assignment_on_topology}





## A CCPNMR Analysis plug-in for comparing spin systems

During the assignment process described above one will very likely end up with two sets of spin systems, one from the ^1^H detected data and one from the ^13^C detected data. In CCPN Analysis ^1^H- and ^13^C-detected spectra should be connected to separate shift lists to prevent internally averaging the two shifts into one main shift. This would be very unhandy for all parts of the program that rely on shift matching in some way. To make the process of matching up and merging the two sets of spin systems I wrote a simple CCPN analysis plug-in, see figure {@fig:compare_spin_systems_gui}. Any two spin systems can be compared to one another. As a measure of how comparable the two spin systems are, the root mean square deviation between the corresponding shifts is calculated. If the shifts from protonated and deuterated samples are indeed divided into two different shift lists, a correction based on the values reported by *Maltsev et al.* can be performed. This tool could also be useful in other scenarios where spin systems have to be compared. It can be downloaded at <https://github.com/jorenretel/compare_spinsystems>.


![Graphical User Interface of the CCPN Analysis plug-in that helps comparing spin systems to each other. In the tables at the top, the two spin systems that should be compared are selected. The three tables at the bottom show the resonances unique to the first spin system, the resonances that are assigned to the same type of nuclei and the resonances unique to the second spin system respectively. In this case a spin system created based on the proton detected data (left side) is compared to one that was created using carbon detected data (right side). Discrepancy of values in delta chemical shift in the intersections table are due to the fact that for untyped spin systems an average isotope shifts correction is used where a amino acid specific one is used for the typed spin system on the right.](figures/compare_spin_systems_gui.png){#fig:compare_spin_systems_gui}







