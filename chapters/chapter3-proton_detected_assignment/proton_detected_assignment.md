
Assignment Using ^1^H-detected Spectra
======================================

## Introduction


There are good reasons to detect proton. Since the gyromagnetic ratio of protons is 8 and 31 times higher as those of ^13^C and ^15^N respectively, the signal to noise in proton detection is higher. Also adding an observable nucleus adds dispersion in multi-dimensional spectra. That proton detection was badly needed was clear since applications of solid state on biological samples became into reach. There are two main strategies that can be employed to reduce the ^1^H linewidths:

1. Reduce the amount of ^1^H in the sample by perdeuterating the sample and subsequently reintroduce protons at the exchangeable sites, see figure {@fig:deuteration}.
2. Spin small diameter rotors (<2 mm) at higher MAS frequencies (>40 kHz).

Early proton-detected experiments were performed on dipeptides and small model proteins using the first method [@reif_1h1h_2001][@reif_1h_2003][@chevelkov_1h_2003][@paulson_sensitive_2003]. It was shown that by drastically reducing the amount of back-exchanged protons from 100% to 10% ^15^N-^1^H correlation spectra of the model protein SH3 could be acquired with ultra-high resolution [@chevelkov_ultrahigh_2006]. Also proton detect experiments that allowed the assignment and, in combination with protonated methyls, the structure calculation of SH3 could be performed under these low back-exchange levels (10 and 25% respectively) and moderate MAS rates [@linser_protondetected_2008][@linser_structure_2011]. The optimal amount of reprotonation at 24kHz MAS was found to be around 30% [@akbey_optimum_2009]. A first ^15^N-^1^H correlation of OmpG was measured at this back-exchange level [@linser_protondetected_2011].

Recently probes spinning small diameter rotors at ultra-fast MAS rates (40-60kHz) have become available. At these high spinning rates high resolution spectra can be recorded with full reprotonation of the exchangeable sites [@zhou_protondetected_2007][@lewandowski_enhanced_2011]. Although the sample volume in these rotors is smaller, loss of signal to noise is balanced by a few factors. First of all, the higher proton content of course increases the signal to noise. Second the improved filling factor of the coils for smaller rotors plays a role. Furthermore, at ultra-fast spinning conditions spectroscopic techniques have been developed that can not be employed at lower MAS frequencies. Low power hetero-nuclear decoupling can be used, which reduces sample heating [@ernst_lowpower_2001][@kotecha_efficient_2007][@laage_fast_2009]. Also ^1^H-^13^C cross-polarization conditions become available that selectively transfer magnetization to either the carbonyl or aliphatic carbons at these spinning rates [@laage_bandselective_2008].


![The samples using for proton detected at 60 kHz MAS were expressed ^2^D/^13^C/^15^N labeled, afterwards protons were reintroduced on exchangeable sites by performing the refolding in buffer containing the desired H~2~O/D~2~O ratio.](figures/deuteration.svg){#fig:deuteration}



Various groups have introduced proton detected experiments for sequential assignments at ultra-fast MAS and have successfully applied them to a number of different systems: micro-crystalline (SH3, GB1, Human Superoxide Dismutase, DsbA and β2m), α-synuclein fibrils, sedimented viral capsids, a secretion needle from salmonella and membrane proteins (the conductance domain from influenza A M2, and DsbB) [@zhou_solidstate_2007][@knight_fast_2011][@barbet-massin_rapid_2014][@zhou_solidstate_2012][@chevelkov_protondetected_2014]. Also structures have been calculated using ^1^H-^1^H distances acquired at fast MAS, among which GB1 and Human Superoxide Dismutase  [@zhou_solidstate_2007][@knight_fast_2011][@knight_structure_2012].
TODO: it does not seem like there is many more. DsbA restraints were in zhou 2012 paper, but no real structure yet.

For the assignment of OmpG two sets of three experiments were recorded illustrated in figure {@fig:assignment_experiments_proton_detected} at 60 kHz MAS. These are the pulse sequences presented in the papers of Barbet-Massin et al. in 2013 and 2014 [@barbet-massin_outandback_2013][@barbet-massin_rapid_2014]. The first set, consisting of the hCANH, hCOcaNH and hcaCBcaNH, correlates each ^1^H-^15^N pair in the backbone to respectively the Cα, CO and Cβ frequencies within the same residue. The second set correlates the ^1^H-^15^N pairs to the Cα, CO and Cβ frequencies of the preceding residue. By subsequently matching strips at ^1^H-^15^N positions were the ^13^C chemical shifts from the first set match the second set a sequential walk can be generated and matched to a part of the sequence.

The hcoCAcoNH, hCOcaNH, hcaCBcaNH and hcaCBcacoNH pulse sequences make use of scalar-coupling based transfer steps to transfer magnetization between the carbons. These transfer blocks are basically equivalent to INEPT except that the magnetization is transferred between two nuclei of the same type. To evolve the scalar coupling relatively long delays τ  of 1/(4J~CC~) are needed. This equals 4.5 ms for a Cα-CO and 7.1 ms for a Cβ-Cα transfer (with J~CαCO~=55Hz and J~CαCβ~=35Hz). For the transfer of magnetization between the CO and Cα in the hcoCAcoNH and the Cα and Cβ in the hcaCBcaNH and hcaCBcacoNH experiments out-and-back schemes are used [@barbet-massin_outandback_2013]. This means that instead of using a CP transfer directly from proton to the carbon measured in one of the indirect dimensions (which would be the case in hCAcoNH, hCBcaNH and hCBcacoNH experiments), the magnetization is transfered first to the neighboring carbon on the magnetization transfer pathway. Both in the out-and-back and 'normal' variant of the experiment contain 4 delays τ. The advantage of the out and back scheme is that the transverse magnetization during these delays is on the slower relaxing nucleus (Cα in case of a Cα-Cβ transfer and CO in case of a Cα-CO transfer) instead of on each nucleus for 2 out of 4 delays. Only just before acquisition of the carbon dimension the spin of the faster relaxing nucleus is tipped in the transverse plane. Because of the inhomogeneous nature of the sample ^13^C T2 times are very short in OmpG. The bulk T2 time for Cα was measured to be around 8 ms. The CO T2 was not measured but is likely to be a factor of 3-4 larger. Therefor this experimental scheme helped making these experiments sensitive enough.


![Proton detected pulse sequences for assignment. Phase cycle: (a and d) ph0 = 0, φ1 = 0 2, φ2 = 1, φ5 = 0, φ6 = 0 0 2 2, φ7 = 1, φ11 = 1 1 1 1 3 3 3 3, φ10 = 0, φ15 = 0, φ17 = 0, φ19 = 0, φ20 = 1, φrec = 1 3 3 1 3 1 1 3; (b and e) φ0 = 0, φ1 = 1 3, φ2 = 1 1 3 3, φ3 = 0, φ4 = 1, φ5 = 1, φ6 = 0, φ7 = {1}*4 {3}*4, φ8 = {0}*8 {2}*8, φ9 = 3, φ10= 1, φ11= 0, φ12= 0, φ20= 0, φrec= 0 2 2 0 2 0 0 2 2 0 0 2 0 2 2 0; (c) φ0 = 0, φ1  = 0 2, φ20 = 1, φ15 = 0, φ10 = 0, φ2 =  1, φ5 =  0, φ6 =  0 0 2 2, φ14 = {0}*4 {1}*4, φ16 = 0, φ17 = {0}*8 {1}*8, φ19 = 0, φ7 = 1, φ11 = 1 1 1 1, φ31 =  3 1 1 3 1 3 3 1 1 3 3 1 3 1 1 3; (f) φ0 = 0, φ1 = 1 3, φ2 = 1 1 3 3, φ3 = 0, φ4 = 1, φ5 = 1, φ6 = 0, φ8 = {0}*16 {2}*16, φ9 = 3, φ10= 1, φ11= 0, φ12= 0, φ20= 0, φ16 = 3, φ18=0, φ17= {0}*4 {1}*4, φ19 = 0, φ14= {0}*8 {1}*8, φ27 = 0, φrec= 0 2 2 0 2 0 0 2 2 0 0 2 0 2 2 0 2 0 0 2 0 2 2 0 0 2 2 0 2 0 0 2.](figures/assignment_experiments_proton_detected.svg){#fig:assignment_experiments_proton_detected}



This set of spectra is conceptually very similar to the basic set of spectra used for the assignment of solution NMR data although there are a few differences. Because in solution NMR the ^15^N-^13^C transfer is achieved by INEPT instead of CP and the N-Cα~i~ and N-Cα~i-1~ scalar couplings are similar in size, the HNCA experiment in solution NMR normally includes both the Cα~i~ and Cα~i-1~ peak. In the solid-state version of the experiment the hCANH only includes the Cα~i~ peak, which is advantageous since this reduces signal overlap. Also in solution NMR the Cα-Cβ scalar transfer is generally evolved only half-way to create an HNCA/CB experiment were the Cβ peaks are negative.

In comparison to ^13^C-detected experiments, the assignment strategy is enormously simplified. As discussed before, in the 3-dimensional ^13^C detected experiments NCACX and NCOCX, the pivot along which a strip representing one spin system is connected to its sequential neighbor is the backbone ^15^N chemical shift. In the set of ^1^H-detected experiments, this pivot is dispersed by the chemical shift of its directly bound proton. Therefor it is in most cases clear which 6 peaks belong to one ^1^H-^15^N combination. At this point, already before any strips have been matched, the possible amino acid types of two correlated residues can be deduced. In the ^13^C-detected 3D experiments at least two strips have to be matched to do the same. When considering a strip in the NCACX one can not tell just on the basis of the ^15^N chemical shift which NCOCX strip is connecting to its N-terminal neighbor. The two strips have to matched based on corresponding peaks in both strips. Only at the point this match has been done, the possible residue types of two sequential spin systems can be deduced. Because of the reduced overlap in the ^1^H-detected strips it is often possible multiple strips can be matched with a relative high degree of certainty before the stretch of connected spin systems has to be matched to a subsequence of the protein.

## Materials and methods

### Sample preparation

Samples were prepared in the same way as described before with a few exceptions [@hiller_solidstate_2005]. The M9 minimal medium was perdeuterated. For the samples used to record the hCANH and hcoCAcoNH shown here the refolding buffer contained a mixture of 70:30 H~2~O:D~2~O. Reconstitution in lipid bilayers of this last sample was performed in buffer containing H~2~O. After reconstitution the samples were pelleted and incubated in a MES buffer with pH 6.3. In the case of the hCANH and hcoCAcoNH samples this buffer contained a mixture of 70:30 H~2~O:D~2~O.

### NMR experiments


| experiment  | ^13^C aq (ms) | ^15^N aq (ms) | scans | duration |
|-------------|--------------:|--------------:|------:|---------:|
| hCANH       |  8.6          | 14.4          | 12    | 1d15h    |
| hcoCAcoNH   |  6.6          | 14.4          | 36    | 3d18h    |
| hcaCBcaNH   |  3.0          |  5.           | 64    | 2d20h    |
| hcaCBcacoNH |  3.0          |  5.4          | 128   | 5d23h    |
| hCONH       | 10.0          | 14.0          | 8     |   16h    |
| hCOcaNH     | 10.0          |  9.8          | 64    | 3d15h    |

Table: Aquisition parameters for the six ^1^H-detected experiments used for the assignment of OmpG.{#tbl:proton_detected_aquisition_times}



## Results and discussion


There is still a lot of overlap in the ^1^H-^15^N correlation compared to a similar spectrum in solution NMR (see figure {@fig:HN_solid_solution}). However, in the 3-dimensional spectra it is easier to distinguish individual ^1^H-^15^N pairs, simply because the peaks mostly do not overlap in the ^13^C dimension, thereby making it possible to see the exact peak maxima.

![Overlay of HN correlations in solid state NMR (red), and solution NMR (black). The solid state spectrum is recorded using the cross-polarization based pulse sequence as described ..... The solution spectrum is a modified copy of the second figure in the paper of Lukas K. Tamm and coworkers describing the solution structure of OmpG [@liang_structure_2007]. The solution spectrum was recorded using a TROSY-HSQC sequence. Besides the obvious difference in line-width between the two spectra, there are also peaks present in the solution spectrum that are absent in the solid state spectrum. These peaks correspond mostly to the flexible loops on the extra-cellular side of OmpG and some to the shorter turns on the intra-cellular side.](figures/HN_solid_solution.png){#fig:HN_solid_solution}



Using the hCANH, hcoCAcoNH, hCONH, hCOcaNH, hcaCBcaNH and hcaCBcacoNH spectra 151 strips could be matched corresponding to 55% of the sequence when prolines are excluded, see figure {@tbl:extend_of_assignment_table}. In addition some of the ^13^C chemical shifts of another 16 residues, among which 6 prolines, could be determined based on peaks in the hcoCAcoNH, hCONH and hcaCBcacoNH spectra. Interestingly only a few strips (TODO:number) where left unassigned and therefor the signal set for a large part of the sequence seems to be missing. Because the ^1^H-^15^N-correlation is a bit too crowded, the ^13^C-^15^N-projection of the hCANH, shown in figure {@fig:CAN_projection}, was used as a reference spectrum for orientation. Although of course some of the peaks in this projection are dispersed into multiple peaks in the ^1^H-dimension, it is clear that the vast majority of present peaks is assigned.



![Assignment shown on the CN projection of the hCANH spectrum.](figures/CAN_projection.svg){#fig:CAN_projection}




In figure {@fig:strip_plots_37_52_B} a representative stretch of strips is shown. Here it can be observed that towards the end of this stretch, which is also the end of the assignment for this part of the sequence, peak intensities become smaller. This is especially the case for the peaks in the Cβ-correlated spectra. The decline of peak intensity towards the end of assigned stretches seems to be a trend over the whole sequence. Of course the lack of cross peaks is a direct cause for the assignments to stop. In figure {@fig:strip_plots_37_52_B} signal intensities of the hCANH, hcoCAcaNH, hcaCBcaNH and hcaCBcacoNH spectra are shown for the assigned residues in the sequence. As can be seen there are very large differences in the peak intensities in the Cβ-correlated spectra, whereas they are more constant in the Cα correlated spectra. The residue numbers in the plot correspond to the residue of the carbon that is measured. It can be observed that there is a strong correlation between the signal intensities of the hcaCBcaNH and the hcaCBcacoNH. This hints that not so much the efficiency of the CP steps determines the signal intensity but the ^13^C-relaxation during the delays τ that allow the scalar coupling to evolve (which are much longer than the acquisition time). As explained in the introduction the transfers magnetization during these delays is on the Cα in the case of the hcaCBcaNH and hcaCBcacoNH (for the last experiment at least in all the delays for the Cα-Cβ transfer and half of the time during the Cα-CO transfer). In the hcoCAcoNH the transverse magnetization during these delays is on the CO. In this light it is also interesting to note that some hCOcaNH peaks are missing towards the end of the assigned stretch in figure {@fig:strip_plots_37_52_B}. Also during this experiment the transverse magnetization is on Cα for half of the scalar transfer step. The pattern here is not so clear though as the quality of this spectrum is slightly lower than expected. For instance also the hCOcaNH peak in the 46 isoleucine strip is missing while the hcaCBcaNH peak is large. For this reason the CO-correlated spectra have been excluded from the plot in figure {@fig:peak_intensities_on_sequence.svg}. It is likely that structural inhomogeneity and slow motions in the large extra-cellular loops OmpG is causing widely varying T2 relaxation times. This is discussed further in the next chapter when comparing the signal sets in the ^1^H- and ^13^C- datasets.

Now the peaks in the hCANH spectrum have a signal to noise around 10, which is far from excessive. Therefor it might be interesting to signal-average the hCANH experiment longer to see how many peaks are still below the noise level. Also experiments with dipolar transfer schemes should be tried [@zhou_solidstate_2012]. On model proteins such as SH3 scalar coupling based homo-nuclear transfer schemes proofed slightly more efficient as dipolar based ones. However on proteins such as OmpG with T2 times that are about three times shorter as in SH3 (8 vs. 25 ms for Cα) DREAM based transfers might lead to less signal loss.




![Strip plots showing the backbone walk from phenyl-alanine 37 to Glutamine 52. Residue 42 is a proline and therefor this strip is not present. The correlations to the carbon nuclei can be observed in the strip of tryptophan 44. Notice how the signal intensities, especially of the peaks in the longer experiments like the hcaCBcacoNH, drop off towards the end of this sequential stretch and eventually even completely disappear in the strip of Glutamic acid 52, which is the last assigned residue on this strand of the β-sheet.](figures/strip_plots_37_52_B.svg){#fig:strip_plots_37_52_B}




![Signal intensities in the hCANH, hcoCAcoNH, hcaCBcaNH and hcaCBcacoNH versus sequence. Every panel represents two strands in the β-sheet connected by a intra-cellular turn in the structure, except for the two panels on the top which represent the first and last strand in the sequence respectively. For all peaks residue indeces are bases on the location of the measured carbon. I.e. peak intensities in the hcoCAcoNH and hcaCBcacoNH correspond to strips at the ^15^N-^1^H position of index+1. Noise level (1) is defined as one standard deviation of noise intensity calculated by CCPN analysis by taking 10 subsets of 1000 random samples in a spectrum and choosing the smallest subset.](figures/peak_intensities_on_sequence.svg){#fig:peak_intensities_on_sequence.svg}




