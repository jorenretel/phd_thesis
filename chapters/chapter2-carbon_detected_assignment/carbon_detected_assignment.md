
Assignment Using ^13^C-detected Spectra
=======================================

At moderate spinning rates and fully protonated samples it is not possible to detect protons in a useful manner in the solid state since the linewidths are very large due to the strong dipolar coupling network between protons. Therefor until very recently assignments where done almost exclusively using ^15^N and ^13^C chemical shifts. This was the method used when I started.

### Types of Experiments

The three main types of spectra recorded were 2D trough-space ^13^C-^13^C and 2 and 3D NCACX and NCOCX spectra using the pulse sequence shown in figure {@fig:carbon_detected_pulse_sequences_and_magnetization_transfers}. Depending on the mixing time correlations between spins at different distance can be observed. To create spin-systems, mostly 2D ^13^C-^13^C and NCACX spectra with a short DARR mixing time of about 20 to 50 ms were used. When a longer mixing time is used, around 150 to 200 ms short range crosspeaks can be observed that help connecting spin systems sequentially. Also NCOCX spectra are used for this since they directly correlate a spin system i with its sequential i-1 neighbor through the backbone. The 13^C^-^13^C and through backbone ^15^N-resolved spectra are always used in combination since they both have their positive sites. The nice feature of the though-backbone experiments is that there is a sense of directionality. If two spin-systems are connected one always knows which one is the first in the sequence. Whereas when a connection between to spin systems is established in the purely through-space experiments, this is not a given fact. Of course even whether they are truly sequential should always be doubted. At the other side, very specific crosspeaks between the less degenerate side chain chemical shifts can be found.

There are other experiments possible that complement the NCACX and NCOCX and help making the backbone walk, such as CONCA and NcoCACX. However these experiments are lower in signal to noise, because of a added NC cross polarization step in the former and a homenuclear transfer step using for instance spc7 in the latter. Because of this, we were never able to get satisfying spectra of from these experiments.


![Pulse sequences and magnetization transfers in carbon detected experiments. A) Pulse sequence of 2D CC correlation using DARR. Phases are Φ0 = 0, Φ1 = 13, Φ2 = {0}*8 {2}*8, Φ3 = 1133, Φ4 = 1122 3300, Φaq = 2013 0231 0231 2013. B) Pulse sequence of NCACX and NCOCX. The sequences are identical. Only the specific CP condition is different between both experiments. Phases are Φ0 = 0, Φ1 = 1111  1111 3333 3333, Φ2 = {0}*16 {2}*16, Φ3 = 0202, Φ4 = 0022, Φ5 = 3333 1111, Φ6 = 1122, Φaq = 0231 2013 2013 0231 2013 0231 0231 2013. Both sequences are part of Trent Franks' pulse sequence repository at github.com/TrentFranks/ssNMR_pp_TopSpin2 as fmp.hCC_DARR and fmp.hNCC_DARR respectively. C) Magnetization transfers of 2D CC correlations. In spectra with a short mixing time (50 ms) only cross-peaks will arise that correlate two nuclei in the same residue. Using longer mixing times (200 ms)allows magnetization transfer to neighboring residues. If the mixing time is even increased (400 ms)long range correlations can be observed. D) Magnetization transfers demonstrating how a sequential walk can be performed using NCACX and NCOCX spectra.](figures/carbon_detected_pulse_sequences_and_magnetization_transfers.svg){#fig:carbon_detected_pulse_sequences_and_magnetization_transfers}



### Isotope Labeling Schemes
Both 2- and 3-dimensional ^13^C-detected spectra of uniformly ^13^C-^15^N labeled OmpG are very crowded, and therefor impossible to assign. Therefor a set of sparsely labeled samples was produced. Two main techniques were used to produce these samples: forward labeling and reverse labeling. When forward labeling a sample, a set of labeled amino acids are added to a otherwise unlabeled feedstock. As the name suggests, reverse labeling is exactly the other way around: E. Coli is grown on a isotopically labeled feedstock and all amino acids that should not be labeled are added in unlabeled, to suppress the metabolism producing these amino acids from the feedstock. Also samples have been produced from a feedstock of 1,3- and 2-labeled glycerol giving a very specific labeled and unlabeled nuclei of the different amino acids. This last strategy can be combined with the reverse labeling strategy to produce samples that only have a subset of the residues labeled in this specific patterns, while leaving the rest of the residues completely unlabeled.
The combinations of amino acids that can be labeled together is restricted by the amino acid metabolism. Since it is not possible to suppress the metabolic routes to and from a amino acid completely just by feeding them unlabeled to the organism, some isotope leakage will always appear. This effect is minimized by choosing sets of amino acids that are relatively close in the metabolism or were the production/use of this amino acid is easily suppressed. This is especially apparent in the reverse labeling strategy, as when amino acids are produced from the feedstock anyway that were supposed to be unlabeled this will appear in the spectra. The exact same effect in the forward labeling strategy would however just cause the amino acids that should be labeled to be labeled slightly less, which only affects the signal to noise ratio, but is not directly visible in the spectra.

To choose a set of amino acid selective labeling schemes a concession has to be made between two major conflicting interests. At the one hand the crowding in the resulting spectra should be reduced as much as possible. But at the other hand, as many as possible neighboring residues should be co-labeled in at least one of the labeling schemes. For example, as can be seen in figure {@fig:labelling_venn} Alanine is co-labeled with every other amino acid in at least one of the labeling schemes, except for Lysine. That means that there will almost always be spectra were the cross peaks between a sequential stretch involving an Alanine can be observed, thereby enabling the assignment of this stretch. At the other hand, for instance Proline and Tyrosine are not co-labeled in any of the residue specific labeling schemes, so therefor whenever there is a Proline-Tyrosine pair in the sequence, the more crowded spectra have to be used to find the crosspeaks connecting them. As discussed earlier, it is preferable to be able to connect at least three spin systems to unambiguously assign them to a subsequence of the protein. By having a set of labeling schemes with a certain overlap as is indicated in the venn diagram of figure {@fig:labelling_venn} it is possible to jump between spectra to find the connectivities to produce such longer stretches of connected spin systems. In figure {@fig:labeling_schemes_on_ompg_sequence} the OmpG sequence were such stretches are hight-lighted. Whenever the color changes there is a 'dead end', where there is no residue specific labeling scheme to connect two neighboring residues. Any given residue in the sequence is on average part of a sequential stretch of 5.5 residues, which allows an unambiguous assignment in many cases.

TODO: figure of uniform labeled PDSD




![Venn-diagram illustrating the overlap between the different labeling schemes that were produced of OmpG. Every amino acid in the OmpG sequence is at least labeled in one labeling scheme. Some of these labeling schemes are produced by forward labeling, others by reverse labeling. \label{labelling_venn}](figures/labelling_venn.png){#fig:labelling_venn}




![All amino acid selective labeling schemes used for the sequential assignment of OmpG on the sequence. Highlighted rectangles indicate in which labeling schemes the residue is labeled. Colored (green, orange and purple) clusters of rectangles indicate that a sequential walk is possible without using the more crowded spectra of non-residue specific labeling schemes. A sequential walk is possible when two sequential residues are co-labeled in at least one labeling scheme. Grey rectangles indicate that the residue is not co-labeled with any of its two neighboring residues. The average cluster length is 3.0 and on average a given residue is part of a cluster of length 5.5.  \label{labeling_schemes_on_ompg_sequence}](figures/labelling_schemes_on_ompg_sequence.png){#fig:labeling_schemes_on_ompg_sequence}


#### RIGA
RIGA forward labeled

#### GAFY

#### GAVLS


#### 1,3- and 2-Glycerol Labeling

Apart from decreasing the amount of signals in the spectra, these labeling schemes also produce narrower linewidths because the in most cases directly bound carbon nuclei are not both labeled in the same scheme. This reduces the carbon homonuclear dippolar coupling, which in turn causes lines to be narrow.

![Amino acid metabolism. \label{glycerol_metabolism}](figures/glycerol_metabolism.svg)



![Labeling patterns in 20 amino acids when 1,3-glycerol (blue) or 2-glycerol are used as feedstock. \label{glycerol_labeling}](figures/glycerol_labeling.svg)




![CCPNMR plug-in that helps visualizing expected subpatterns in ^13^C-^13^C correlation spectra of labeled samples. If chemical shifts are assigned, corresponding peaks will be at the correct position. Otherwise reference chemical shifts from the refDB are used. Dark and light colors repectively show whether the peak is assigned or not.](figures/labeling_patterns_plugin.svg){#fig:labeling_patterns_plugin}

