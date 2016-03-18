
Assignment Using ^13^C-detected Spectra
=======================================

At moderate spinning rates and fully protonated samples it is not possible to detect protons in a useful manner in the solid state since the linewidths are very large due to the strong dipolar coupling network between protons. Therefor until very recently assignments where done almost exclusively using ^15^N and ^13^C chemical shifts. This was the method used when I started the project.

## Types of Experiments

The three main types of spectra recorded were 2D trough-space ^13^C-^13^C and 2 and 3D NCACX and NCOCX spectra using the pulse sequence shown in figure {@fig:carbon_detected_pulse_sequences_and_magnetization_transfers}. Depending on the mixing time correlations between spins at different distance can be observed. To create spin-systems, mostly 2D ^13^C-^13^C and NCACX spectra with a short DARR mixing time of about 20 to 50 ms were used. When a longer mixing time is used, around 150 to 200 ms short range crosspeaks can be observed that help connecting spin systems sequentially. Also NCOCX spectra are used for this since they directly correlate a spin system i with its sequential i-1 neighbor through the backbone. The 13^C^-^13^C and through backbone ^15^N-resolved spectra are always used in combination since they both have their positive sites. The nice feature of the though-backbone experiments is that there is a sense of directionality. If two spin-systems are connected in these type of spectra one always knows which one is the first in the sequence, making mapping to a subsequence easier. Whereas when a connection between two spin systems is established in the purely through-space 2D ^13^C-^13^C experiments, it is not clear purely from the spectrum in what order they appear in the sequence. Of course even whether they are truly sequential should always be doubted. At the other side, in 2D ^13^C-^13^C corelations very specific crosspeaks between the less degenerate side chain resonances can be found. These type of cross-peaks are not present in the NCACX and NCOCX spectra because one of the ^13^C-dimensions encodes either the CA or the CO.

When performing a backbone walk using NCACX and NCOCX spectra, the ^15^N chemical shift is used as a pivot and therefor the usefulness of these spectra is highly dependent on the ^15^N chemical shift dispersion, which is not very large in general. There are other ^13^C-detected experiments possible that complement the NCACX and NCOCX, such as CANCO and CANcoCA, that prevemt the ^15^N chemical shift from being the sole pivot [@schuetz_protocols_2010]. However these experiments are lower in signal to noise, because of a added NC cross polarization step. Because of this, we were never able to get satisfying spectra using these type of experiments.


![Pulse sequences and magnetization transfers in carbon detected experiments. A) Pulse sequence of 2D CC correlation using DARR. Phases are Φ0 = 0, Φ1 = 13, Φ2 = {0}*8 {2}*8, Φ3 = 1133, Φ4 = 1122 3300, Φaq = 2013 0231 0231 2013. B) Pulse sequence of NCACX and NCOCX. The sequences are identical. Only the specific CP condition is different between both experiments. Phases are Φ0 = 0, Φ1 = 1111  1111 3333 3333, Φ2 = {0}*16 {2}*16, Φ3 = 0202, Φ4 = 0022, Φ5 = 3333 1111, Φ6 = 1122, Φaq = 0231 2013 2013 0231 2013 0231 0231 2013. Both sequences are part of Trent Franks' pulse sequence repository at github.com/TrentFranks/ssNMR_pp_TopSpin2 as fmp.hCC_DARR and fmp.hNCC_DARR respectively. C) Magnetization transfers of 2D CC correlations. In spectra with a short mixing time (50 ms) only cross-peaks will arise that correlate two nuclei in the same residue. Using longer mixing times (200 ms)allows magnetization transfer to neighboring residues. If the mixing time is even increased (400 ms)long range correlations can be observed. D) Magnetization transfers demonstrating how a sequential walk can be performed using NCACX and NCOCX spectra.](figures/carbon_detected_pulse_sequences_and_magnetization_transfers.svg){#fig:carbon_detected_pulse_sequences_and_magnetization_transfers}



## Isotope Labeling Schemes
Both 2- and 3-dimensional ^13^C-detected spectra of uniformly ^13^C-^15^N labeled OmpG are very crowded, and therefor very hard to assign. Therefor a set of sparsely labeled samples was produced. Two main techniques were used to produce these samples: forward labeling and reverse labeling. When forward labeling a sample, a set of labeled amino acids are added to a otherwise unlabeled feedstock. As the name suggests, reverse labeling is exactly the other way around: E. Coli is grown on a isotopically labeled feedstock and all amino acids that should not be labeled are added in unlabeled, to suppress the metabolism producing these amino acids from the feedstock. Also samples have been produced from a feedstock of 1,3- and 2-labeled glycerol giving a very specific labeled and unlabeled nuclei of the different amino acids. This last strategy can be combined with the reverse labeling strategy to produce samples that only have a subset of the residues labeled in this specific patterns, while leaving the rest of the residues completely unlabeled.
The combinations of amino acids that can be labeled together is restricted by the amino acid metabolism. Since it is not possible to suppress the metabolic routes to and from a amino acid completely just by feeding them unlabeled to the organism, some isotope leakage will always appear. This effect is minimized by choosing sets of amino acids that are relatively closely related in the metabolism or were the production/use of this amino acid is easily suppressed. This is especially apparent in the reverse labeling strategy, when amino acids that were supposed to be unlabeled are produced from the labeled feedstock anyway. The exact same effect in the forward labeling strategy would however just cause the amino acids that should be labeled to be labeled slightly less, which only affects the signal to noise ratio, but is not directly visible in the spectra.

To choose a set of amino acid selective labeling schemes a concession has to be made between two major conflicting interests. At the one hand the crowding in the resulting spectra should be reduced as much as possible. But at the other hand, as many as possible neighboring residues should be co-labeled in at least one of the labeling schemes. For example, as can be seen in figure {@fig:labelling_venn} alanine is co-labeled with every other amino acid (except for Lysine) in at least one of the labeling schemes. That means that there will almost always be one or more spectra were the cross peaks between a sequential stretch involving an alanine can be observed, thereby enabling the assignment of this stretch. At the other hand, for instance proline and tyrosine are not co-labeled in any of the residue specific labeling schemes, so therefor whenever there is a proline-tyrosine pair in the sequence, the more crowded non-residue specific labeled spectra have to be used to find the crosspeaks connecting them. As discussed earlier, it is preferable to be able to connect at least three spin systems to unambiguously assign them to a subsequence of the protein. By having a set of labeling schemes with a certain overlap as is indicated in the venn diagram of figure {@fig:labelling_venn} it is possible to jump between spectra to find the connectivities to produce such longer stretches of connected spin systems. In figure {@fig:labeling_schemes_on_ompg_sequence} the OmpG sequence were such stretches are hight-lighted. Whenever the color changes there is a 'dead end', where there is no residue specific labeling scheme to connect two neighboring residues. Any given residue in the sequence is on average part of a sequential stretch of 5.5 residues, which allows an unambiguous assignment in many cases.



![2D ^13^C-^13^C DARR spectrum with 25 ms mixing of uniformly labeled OmpG at 400 MHz.](figures/uniform_cc_25ms.svg){#fig:uniform_cc_25ms}



![Venn-diagram illustrating the overlap between the different labeling schemes that were produced of OmpG. Every amino acid in the OmpG sequence is at least labeled in one labeling scheme. Some of these labeling schemes are produced by forward labeling, others by reverse labeling.](figures/labelling_venn.png){#fig:labelling_venn}




![All amino acid selective labeling schemes used for the sequential assignment of OmpG on the sequence. Highlighted rectangles indicate in which labeling schemes the residue is labeled. Colored (green, orange and purple) clusters of rectangles indicate that a sequential walk is possible without using the more crowded spectra of non-residue specific labeling schemes. A sequential walk is possible when two sequential residues are co-labeled in at least one labeling scheme. Grey rectangles indicate that the residue is not co-labeled with any of its two neighboring residues. The average cluster length is 3.0 and on average a given residue is part of a cluster of length 5.5.](figures/labelling_schemes_on_ompg_sequence.png){#fig:labeling_schemes_on_ompg_sequence}





### Forward labeled schemes

Both the forward labeling schemes, where mostly only a few amino acids are labeled and the 1,3- and 2-glycerol labeling schemes have pro's and cons. The big pro of the forward labeled samples is that the amino acids that are labeled are uniformly labeled. Or in the case of GAF~2,3~Y~2,3~(S) at least the nuclei giving rise to peaks in the aliphatic part of the spectra are. It is extremely useful for grouping resonances into spinsystems. This is especially true for the amino acids in group I in figure {@glycerol_labeling}. Because there is only one isotopomer for both the samples based on 1,3- and 2-glycerol, the nuclei from both these worlds never 'meet' and is would not be possible to connect them into one spin system representing one residue in the sequence. Therefor it is necessary, in the case of large proteins, to have these residue specific but uniformly ^13^C labeled samples with as little as possible overlap of the intra-residual peaks of different amino acids. As will be discussed later, these spectra are really helpful when connecting data from ^1^H- and ^13^C-detected spectra as there is for most amino acids at least one spectrum where the Cα-Cβ crosspeaks are clearly separated.


#### RIGA(S)

#### GAF~2,3~Y~2,3~(S)
In this labeling scheme the phenylalanine and tyrosine where ^13^C-labeled only on the Cα and Cβ nuclei. This was done because their fast relaxing aromatic rings can act as a magnetization sinc. Serine was not added labeled to the feedstock, but as it is metabolically closely related to glycine, it was labeled as well. This labeling strategy has been described in Hiller et al. 2008 [@hiller_2313clabeling_2008].

#### GAVLS
Contains tryptophan as well.

#### GANDSH

#### GAF~2,3~Y~2,3~SHVL
The nice feature of this labeling scheme is that because the aromatic rings of phenylalanine and tyrosine are not labeled, the only signals in the aromatic part of the spectrum are from histidines.

#### GENDQPASR


### 1,3- and 2-Glycerol Labeling

Apart from decreasing the amount of signals in the spectra, these labeling schemes also produce narrower linewidths because the in most cases directly bound carbon nuclei are not both labeled in the same isotopomer. This reduces the ^13^C-^13^C homonuclear dipolar coupling, which in turn causes lines to be narrow.

![Amino acid metabolism. \label{glycerol_metabolism}](figures/glycerol_metabolism.svg)



![Labeling patterns in 20 amino acids when 1,3-glycerol (blue) or 2-glycerol are used as feedstock. \label{glycerol_labeling}](figures/glycerol_labeling.svg){#glycerol_labeling}



## A CCPNMR Plug-in for the visualization of crosspeak patterns

When using a lot of labeling schemes it can be very useful to visualize the cross-peak patterns that are expected, especially for the case of the glycerol based labeling schemes. Although it is not impossible to infer these patterns directly from the diagrams of the isotopomer schemes it is easier to directly look at the expected peak patterns. The supporting material of the paper of Higman et al. 2009 contains such figures for the 1,3- and 2-glycerol labeling schemes [@higman_assigning_2009]. Inspired on these type of diagrams I wrote a plug-in for CCPNMR Analysis to automatically generate the expected cross-peak pattern in 2D ^13^C-^13^C correlations for any labeling scheme, see figure {@fig:labeling_patterns_plugin}. Integrating these kind of diagrams within the Analysis software has some advantages:

1. Not only intra-residual, but also expected inter-residual crosspeak patterns can be shown for any combination of two residues. This would be hard on paper since it would involve a lot of figures.
2. The location of expected peaks can be based on assigned chemical shifts, if present, instead of average values from the bmrb. Hovering the mouse over the diagram will make the cross-hairs move in the spectra, so the actualy peaks can be found. It will also show which peak dimensions are based on assigned chemical shifts.
3. The assignment status of peaks in a spectrum is indicated by dark/light coloring.

Especially the last feature is really helpful as it gives a quick overview of which peaks in a pattern are assigned and which are not. It is hard to get this type of overview just by looking at the spectra or in peak tables. Also the expected peaks for the whole spectrum can be shown at once, which can be handy when considering which labeled samples to produce in the future.

CCPNMR Analysis has great support for configuring custom labeling schemes. All necessary information about the labeling scheme is directly taken from the project and therefor basically any scheme can be visualized in this way. All other information, like residue sequences and assigned chemical shifts are also pulled directly from the project.

The plug-in can be downloaded from <https://github.com/jorenretel/ccpnmr-cc-patterns> and is easy to install.



![CCPNMR plug-in that helps visualizing expected subpatterns in ^13^C-^13^C correlation spectra of labeled samples. The size of the circles represent the co-labeling of the two nuclei being correlated by a peak.If chemical shifts are assigned, corresponding peaks will be at the correct position. Otherwise reference chemical shifts from the refDB are used. Dark and light colors repectively show whether the peak is assigned or not.](figures/labeling_patterns_plugin.svg){#fig:labeling_patterns_plugin}

