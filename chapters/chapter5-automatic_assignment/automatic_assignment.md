
(Semi-) Automatic Assignment of Solid-State NMR spectra
=======================================================

## Introduction

As described before the assignment process can be divided in two steps. First, resonances belonging to the same residue are grouped into spin systems. In the ^13^C-detected set of experiments through-space ^13^C-^13^C correlation spectra with short mixing times and NCACX spectra are used for this purpose. In the ^1^H-detected assignment suite the hCANH, hCOcaNH and hcaCBcaNH fulfill this function. The second step of the assignment process involves the sequence-specific assignment of these spin systems, in which each system is assigned to a specific residue in the protein sequence. This is generally done by evaluating through-space ^13^C-^13^C correlation spectra with longer mixing times, NCOCX spectra, NCACX spectra with longer mixing times or the ^1^H-detected hcoCAcoNH, hCONH and hcaCBcacoNH spectra.

Whereas the first step in this process is often relatively straight-forward, the sequential assignment step is non-trivial and time consuming. Often information from a large set of different spectra has to be combined to come to a solution. In practice, a series of hypotheses are made about two spin systems being a sequential pair in the sequence. Subsequently the chemical shifts of the resonances within the spin system are used (either by looking them up in a resonance list or by setting visual rulers on intra-residual peaks) to search for peaks that support this hypothesis. When spectra with different labeling schemes are used, an extra step is introduced where one determines which peaks are expected in which spectra. This is a repetitive effort that distracts from and confuses the actual sequential assignment. Furthermore, when assigning spectra it is tempting to focus on specific peak patterns for spin systems relevant to the current sub-hypothesis one tries to prove. However, as one pattern leads to another, each new sequential connectivity adds new (and often multiple) hypotheses that have to be tested in parallel with originals; after several steps, the amount of possibilities explodes and one might find himself wandering away from the initial hypothesis that was to be tested. We designed a plug-in for CCPNMR Analysis specifically to help with assignments in solid-state NMR.

CCPN analysis already has a graphical tool that interactively helps with back-bone walks [@stevens_software_2011]. This tool works very well with the typical spectra in solution NMR. However, it is not designed with the combinations of experiments typically used in solid state NMR in mind (with the exception of the newer proton detected experiments, which yield spectra very similar to the solution NMR spectra used for backbone walks). Using this tool a strip from a 'query' spectrum is selected and subsequently the program suggests multiple strips from a 'match' spectrum that could belong to the neighboring residue. Subsequently, when some strips are placed in order, fitting sequence fragments are suggested along with their likelihood. Unfortunately, especially experiments where magnetization between atoms of two residues is transferred through-space, instead of through a specific path over the backbone, do not fit well in this approach. Also often peak patterns in spectra that have more than one dimension in which more than one atom site is measured, such as 2D carbon-carbon correlations, can not be easily visualized as strips. Furthermore it is not always possible to differentiate between 'query' and 'match' spectra. Therefore, a similar tool with less restrictions to experiment types would be very helpful in the sequential assignment process of solid state NMR spectra.

The plug-in calculates the expected peak pattern for each neighboring pair in the sequence based on the magnetization transfer pathway of the experiment and the labeling scheme of the sample. These patterns are checked against the corresponding peak lists using the chemical shifts from every possible combination of spin systems that can be assigned to this pair. Subsequently, this information is used to search for a globally optimal sequential assignment using a combined Monte Carlo / simulated-annealing procedure in a way similar to the algorithm described by Tycko and coworkers for uniformly labeled spectra [@tycko_monte_2010][@hu_general_2011]. The principle is based on a simple scoring mechanism: the more (experimental) peaks that connect two spin systems show up and the better these peaks fit to the chemical shifts of the resonances within those spin systems, the more likely the hypothesized connection is real. The algorithm can be used in combination with virtually any labeling scheme, magnetization transfer pathway, through-bond or through-space, and is not limited by the dimensionality of the correlation spectra.

Many different algorithms for automatic sequential assignment have been published before but are never used [@guerry_advances_2011]. Many programs require of the input specifically formatted tables. This prevents users from
even trying out a program if expectations are already low. A general problem is that most algorithms are implemented as stand-alone applications. This often invokes a complicated work-flow in which several peak and shift lists from the program that is used to do the analysis of the NMR spectra have to be exported and converted to specially formatted tables that are expected by the routine. Afterwards often the results have be imported back into the analysis program so they can be carefully judged. This is not necessarily bad if it has to be done only once. However, for complex assignment projects, with a work-flow in which new data and assignments are added incrementally, this becomes cumbersome. Also the type of data these stand-alone applications output is somewhat problematic. Although mostly an output is generated containing some confidence measure for the individual assignments, it is hard to import more than the consensus assignment back into the analysis program.
Ideally one would like to compare the information that supports different assignment alternatives, even the ones that were never chosen by the algorithm, and cherry-pick the assignments that are believed to be correct.

Integrating the algorithm within a program that is used for spectral analysis (in this case CCPN analysis) allows for a natural interaction with the data and takes away an energy barrier for the user.
All relevant information can be automatically fetched from the Analysis project. All other information specific to the optimization procedure is configured in the Graphical User Interface (GUI) of the plug-in. The output is also shown in this GUI, to allow for quick comparison of alternative assignments. Peaks can be directly navigated to in the spectra and assignments can be transferred to the project one by one or all at
once. Also, CCPN analysis has great support for labeled samples. This is especially essential when labeled samples are used that are composed of different isotopomers, like those based on 1,3- and 2-glycerol used here, or glucose labelling [@schubert_solidstate_2006]. In these cases the expected peak pattern can only be calculated by correctly summing over all isotopomers. Otherwise excellent tools that do not support this can not be used if the dataset includes these type of labelling schemes.

Two algorithms worth mentioning explicitly, solid-state FLYA and GAMES_ASSIGN, have been respectively customized and created especially for assignment of solid-state NMR spectra [@schmidt_new_2012][@schmidt_automated_2013][@nielsen_automated_2014]. These algorithms do not require the creation of spin systems as a starting point for the assignment. This can be advantageous since wrongly configured spin systems will inevitably lead to wrong assignments. However they both suffer from some of the general drawbacks described before, some of which could be solved by a better integration with a spectral analysis program like CCPN Analysis. GAMES_ASSIGN does not support ^1^H-detected spectra and neither of them seems to support complex labeling schemes in a straight-forward matter.


## Description of the algorithm

In figure {@fig:malandro_flow_diagram} an overview is given of the different steps in the algorithm, which are discussed in more detail in the following paragraphs.


#### 1 Input of data

 In the first step the input to the algorithm is gathered. In principle most information can be automatically loaded from the CCPN project:

* primary sequence
* labeling schemes
* experiment types describing the magnetization transfer pathways
* peak lists
* spin systems
* shift lists
* assignment tolerances
* previously made sequential, tentative, and non-sequential amino acid type assignments

Which data is accessed by the algorithm can be configured by the user. This can be useful when the algorithm is used to confirm manually made assignments in an unbiased way without changing the CCPN analysis project.

Spin systems in CCPN Analysis can basically have one of to following five levels of assignment: 1) The most definite form of assignment is of course when a spin system is sequentially assigned to a specific residue in the sequence. 2) One level of assignment lower, a spin system can be assigned 'tentatively' to multiple residues but it is not known which of those residues is the correct one. 3) Then there are spin systems that are residue typed, but no information about sequential assignment is present. 4) Also multiple residue types can be set for a residue. This option is not standardly accessible in the GUI of CCPN Analysis, but is present in the API and called ResidueTypeProbs. An additional plug-in is provided to set this property. This feature is useful because often a residue type can be narrowed down to two very closely related residue types like asparagine and aspartic acid. 5) The spin systems with the lowest level of assignment are those that for which not any form of sequential assignment nor residue type information is available.

All levels of assignment may be used by the algorithm, if wanted. If residue type information is not available or not used, the residue typing algorithm already included in CCPN will be used to classify the spin systems to residue types. Because in most cases the classification is not definite, the user can set a threshold score above which residue types will considered a possibility. There is one more type of assignments that can be, namely the assignment of peak dimensions to specific resonances. If this information is chosen to be used, the only possible assignment of a peak dimension that is considered is the present assignment.

Resonances within spin systems should be assigned to an atom type, Cα for example. If a resonance does not have an atom type assignment it is not possible to map it to a dimension of an expected peak and therefore it will be ignored. Spin systems without any resonances will be ignored as they are generally used in CCPN Analysis as placeholders for unassigned residues. A subset of spectra can be selected using the GUI. In the Analysis project, each spectrum should have peak lists, a labelling scheme and an experiment type describing the magnetization transfer steps and dimensions of the experiment.

The spectra should be peak picked. In many experiments, most notably in experiments with a though-space step like ^13^C-^13^C or NCACX spectra, signal sets that originate from intra-residual, sequentially and long-distance correlations between nuclei are mixed. Although the program simulates and finds intra-residual peaks, the optimization procedure naturally only relies on peaks that form sequential links between two spin systems. To prevent the algorithm from misinterpreting intra-residual peaks as sequential peaks, these peaks should either not be picked in the spectra that are to be used by the algorithm or all their dimensions should be properly assigned to resonances from the same spin system, tipping the program off that the peak should not be interpreted as a possible sequential peak. Because grouping resonances into spin systems is a prerequisite for the algorithm, it is in principle already known which peaks are intra-residual. Assigning intra-residual peaks to known spin systems can be performed using a short run of the algorithm and subsequently letting it assign all intra-residual peaks.

Furthermore the molecular chain (the primary sequence) has to be selected. Optionally, parts of the sequence that should not be considered for assignment can be entered. This last option can be used if it is clear that parts of the molecule can not be seen because of dynamics or for instance incomplete back-exchange of protons.


#### 2 Evaluate possible mapping between spin systems and residues

On the basis of the different levels of assignment describe above and which of that information should be used, for each spin system a set of possible residue assignments is created. Based on these sets, it can already be determined for each spin system with which other spin systems it could ever exchange sequential assignments in the Monte Carlo procedure later on. This information is used during the Monte Carlo procedure to pick which two spin systems to exchange. Also, at this stage 'joker' spin systems are introduced to make sure that always a spin system can be assigned to every residue. This is important since the Monte Carlo procedure was designed to select two spin systems and exchanging their residue assignments rather than the other way around. For this reason all residues should at any stage of the optimization procedure have a spin system assigned to them, because once that would not be case no spin system will ever be assigned to it.

#### 3 Predict peak pattern

The intra-residual and sequential peak patterns are predicted based on the molecular topology, the experiment graph and the isotope labeling scheme. Each spectrum in a CCPN project is connected to an experiment type. Normally, the user is prompted to set the experiment type for each new spectrum that is loaded into the CCPN project. When this was not done, it can be set afterwards and is essential for this algorithm to work. In the CCPN data model each experiment type is connected to an experiment graph. This graph describes which magnetization transfers happen during the experiment and how parts of the experiment map to dimensions in the spectrum. For each magnetization transfer information is present about which types of nuclei take part, whether the transfer is through-space or through-bond and whether a transfer from a nucleus to itself can happen. The specified atom types are not restricted to just isotopes but can be more specific, only aromatic carbons for instance. Together with the molecular topology, the graph can be walked recursively to generate a list of expected peaks for virtually any correlation experiment. This list is then filtered by the labeling scheme. For each peak the colabeling fraction over all nuclei on the magnetization transfer pathway is calculated. Only if the colabeling fraction exceeds a user defined variable the peak is retained. By default this minimal colabeling fraction is 0.1.


#### 4 Match predicted and experimental peaks

Now that a peak pattern is predicted for each spectrum, this can be matched with the peaks in the peak lists corrsponding to those spectra. The positions of the expected peaks can be determined using the chemical shifts assigned to resonances in the spin systems. Of course we don't know yet at this moment which spin systems is in which position on the sequence as that is the purpose of this algorithm. Therefor the possible mapping between residues and spin systems determined in step 2 is used. For every two sequentially neighboring residues A and B, all combinations of spin systems A' and B' are used to search the peak lists, see figure {@fig:malandro_peak_matching} A. The position of the expected sequential peaks will be different for each combination of A' and B'. To find out which peaks in the peaklists match to the expected pattern a chemical shift tolerance is used in each dimension of the spectrum. For each dimension of each spectrum a assignment tolerance can be set in CCPN Analysis, and those tolerances are used here as well.

The more of the expected sequential cross peaks are present in the peak lists, the likelier it is that a specific combination A'-B' is indeed a sequential pair. It is also important how well the actual peak positions fit the expected positions. To do this, for each matched peak a simple function is used that assigns an energy between 0 and -1 depending on the difference between cross-peak position and expected peak position. That value is then multiplied with the square of the number of resonances involved with the expected peak to acknowledge that peaks in higher dimensional spectra carry more weight. This number is mostly equal to the number of dimensions, except for partially diagonal peaks. For instance the N~resonances~ for a diagonal peak in a NCOCX spectrum would be 2 instead of 3, which it should be since it contributes less prove for a sequential connection between two spin systems than an off-diagonal peak. Furthermore the energy is normalized by the symmetry of the spectrum the peak is in. A 2D ^13^C-^13^C correlation for instance has two sets of crosspeaks on each side of the diagonal, making the symmetry 2. All together the energy contribution of one peak can then be expressed as:

$$ E_{peak} = max(-1, \sum_{n=1}^{N_{d}} (\frac{\Delta\delta _{n}}{t_{n}}^2 - 1) \frac{1}{N_{d}(1-k^2)}) \frac{N_{resonances} ^2}{symmetry} $$

Where N~d~ is the number of dimensions, ∆δ~n~ is the difference between the shift of the peak and the shift from the shiftlist in the n-th dimension, t~n~ is the tolerance in the n-th dimension and k is the fraction of the tolerance window that has a flat bottom. This last value is set by default on 0.4.
The flat bottom was introduced to prevent over-interpreting small differences between the peak and the expected position. The energy then goes up gradually and becomes 0 for peaks that are all the way in the corner of the tolerance window, see figure {@fig:malandro_peak_matching} B.

As discussed before chemical shifts can differ between spectra depending on the sample and experimental conditions such as temperature and isotope shifts. If these kind of differences are present it is important that spectra are connected to different shift lists. The correct shift list is then used by this algorithm to perform this matching step.

Besides from sequential cross-peaks, also intra-residual cross-peaks are matched. They do not play a role during the optimization of the sequential assignment as they carry no sequential information. However, it is useful to collect these peaks as well, since they can be used for a quick assignment of peaks in new spectra to already known spin systems.


![The expected peaks can be matched to picked peaks in the spectra. Therefor the chemical shifts of all combinations of spin systems A', B' that can be assigned to sequential residues A and B can be used to predict the location of the peaks (A). How well the real fits the predicted peak location is scored by a flat bottom scoring function (B).](figures/malandro_peak_matching.svg){#fig:malandro_peak_matching}


#### 5 Temporarily remove a fraction of the cross peaks

The optimization procedure that follows is repeated multiple times to create an ensemble of possible sequential assignment, that can be later on compared to one another. If the assignment of a spin system to a residue in the sequence stays the same with different subsets of the peaks used, this might be a good indication that this assignment is correct. In each run a new randomly selected part of the data will be removed before the optimization starts. This is optional as the fraction can be set to 0. Also without removing cross-peaks the result of the optimization will likely be a little different every time depending on how well defined the energy minimum is.


#### 6 Generate a random starting assignment

A random assignment is generated that is consistent with the possible mapping between spin systems and residues determined in step 2. Every residue is assigned to one spin system. This can also be a 'joker' spin system. Not every spin system necessarily has a residue assignment, though. A spin system is never assigned to more than one residue.

#### 7 Optimization of the sequential assignment using a simulated annealing / Monte Carlo procedure

For each step in the Monte Carlo procedure two spin systems are selected to exchange residue assignments. In practice this is done by first randomly choosing one spin system, independent on whether it is assigned to a residue or not. Then from the more selective list of spin systems this spin system could ever exchange with, as determined in step 2, randomly one other spin system is chosen. Before the change is attempted, a check is performed to assure that the change would not produce an assignment that is inconsistent with the possible mapping between spin systems and residues. Now the change in energy can be calculated corresponding to the attempt. Therefor the energy of the individual links between the two spin systems and the current neighboring spin systems in the sequence has to be calculated. If both spin systems were assigned to residues this would be 4 links both in the old and the new situation. The energy of one link can be defined as:

$$ E_{link} = \sum_{n=1}^{N_{p}} \frac{E_{peak,n}}{degeneracy_{n}} N_{resonances, total}  $$

where N~p~ is the number of peaks. E~peak, n~ is the peak score of the n-th peak determined in step 4. The degeneracy is the amount of different assignments the peak has at the current point of the minimization. The peak energies are normalized by this value, because if a peak already has a lot of assignments it is not very relevant in proving this link between two spin systems is correct. N~resonances total~ is the total amount of unique resonances playing a role in the assignments of all peaks. The difference in energy is now simply:

$$  \Delta E = E_{links, new} - E_{links, old}  $$

The change will be accepted when the Monte Carlo criterium is fulfilled:

$$  e^\frac{-\Delta E}{kT} \geq random(0 \rightarrow 1)   $$

During the procedure the temperature is lowered in according to an annealing schedule, making it harder for assignment changes that increase the energy to be accepted in later stages of the optimization.

Steps 5, 6 and 7 are repeated a chosen number of times to generate an ensemble of solutions that can be compared in the graphical user interface.


![Flow diagram of the (semi-) automatic assignment algorithm.](figures/malandro_flow_diagram.svg){#fig:malandro_flow_diagram}


#### The graphical user interface

A relatively simple GUI was created to choose the data to be used, configure the algorithm and display the results. In the first tab, see figure {@fig:malandro_gui} A, spectra and corresponding peak lists and whether to use the connected labeling scheme are selected. In the second tab, the parameters discussed in step 1 can be set. Also the residue range can be set here, as it can be useful to exclude parts of the sequence from the optimization if it is known that these parts do not give rise to peaks in the spectra. Furthermore the cooling regime and the amount of steps per temperature point can be configured as well as the total amount of runs. When the algorithm is started, the energies after each temperature step is shown in a plot for all annealing runs.

After all annealing runs are completed the results will be shown, see {@fig:malandro_gui} B. The user can walk through the sequence and see a subsequence of five residues at a time. For each residue the spin system selected in a given run is shown. The five tables below summarize the overall outcome of all runs. For each residue all spin systems are shown that could be assigned to this residue consistent with the mapping performed in step 2. For each spin system the percentage of runs is shown in which it was selected as the assignment to the residue. When clicking on one of the 'links' buttons in between the buttons representing the residues, all peaks will be shown that were found to connect the two selected spin systems. These are the found peaks on which the algorithm based its decisions. When clicking on the residue button itself all found intra-residual peaks will be shown for the selected spin system.
Another row of residue buttons can be used to configure a self defined assignment, independent of the annealing procedure, and check the information supporting that assignment.
The advantage of having the assignment procedure integrated within CCPN Analysis is that it is possible to automatically navigate to a selected peak in the table. This makes checking by eye whether the peak pattern is indeed good prove for the assignment suggested by the algorithm easy and fast. It is also possible to automatically navigate to the expected peak positions of peaks that were not found. This is very important to form an opinion about the correctness of the assignment. In this way it is possible to check whether the peak is really absent, or it was just not picked.
If the user agrees with certain assignments, they can be transferred to the CCPN Analysis project. There are basically two types of assignment to be considered here. Assignment of spin systems to residues and assignment of resonances to peak dimensions. Both can be done independently. None of the suggested assignment are transferred to the project just by running the algorithm as this will change the CCPN Analysis project in an unwanted way. In this way assignments the user agrees on can be cherry-picked and transferred to the project individually. If the user wants to transfer the assignments to the project in bulk anyway, this is possible in the last tab, see figure {@fig:malandro_gui} D. Because every run of the annealing generates a different possible sequential assignment, the user has to choose one. It is also possible to only transfer assignment for those spin systems that were selected in a certain threshold percentage of all runs. This threshold has to be set higher than 50% as it is otherwise unclear which spin system to choose if there could be two spin systems exceeding the threshold otherwise.


![Graphical User Interface of the (semi-)automatic assignment algorithm. A: a subset of spectra can be selected to be used by the routine. B: a number of settings can be configured controlling which information in the CCPN project is used by the algorithm. Also parameters controlling the annealing process are set here. The graph at the bottom shows the progress of the annealing procedure. C: The results are shown in 5 tables, representing 5 consecutive residues in the sequence. In each table all spin systems that can be assigned to that particular residue are listed. When selecting two spin systems for two sequential residues, all peaks that connect these spin systems are listed in the table at the bottom. Assignments can be inspected here and individually transferred to the project. D: Assignments can also be transferred in bulk to the project. In order to do so, the user should indicate which assignments exactly as multiple annealing runs were performed. One of the possibilities is to only assign those spin systems that are assigned in a threshold fraction of all annealing runs.](figures/malandro_gui.png){#fig:malandro_gui}


## Implementation details

The plug-in for analysis was written in python, making extensive use of the Python API of CCPN analysis [@vranken_ccpn_2005]. Parts of the code that needed to be executed faster to make a lot of Monte Carlo attempts in a reasonable amount of time was written in Cython. Cython is used to generate Python extensions that are compiled to C, which in turn is compiled to byte code, making the execution a lot faster. [@behnel_cython_2011] The pseudo random number generator used is a Mersenne twister [@matsumoto_mersenne_1998]. At first the linear congruential generator from the c standard library was used. But this showed, as widely known, not to give random enough numbers and thereby skewed the results. The python mersenne twister was re-implemented in Cython by Josh Ayers [@_joshayers].


## Performance of the algorithm

To evaluate the algorithm, assignments made by Malandro where compared with the manual assignments that
were previously made for the α-Spectrin SH3 Domain and the Yersinia enterocolitica adhesin A (YadA) and OmpG. It was tested how well the algorithm was able to put existing spin systems in the right order on the sequence.
For SH3, two different tests were ran. First, with a sub-set of carbon detected spectra used for the
original assignment and structure determination [@pauli_backbone_2001] [@castellani_structure_2002]. And second, with a set of proton-detected spectra, recorded at 40 kHz MAS more recently [@nieuwkoop_sensitivity_2015]. For YadA a set of ^13^C-detected spectra of a uniformly labeled sample was avaible [@shahid_assignment_2012] [@shahid_membraneprotein_2012]. The original assignments where used to generate spin systems as this step is not part of the algorithm. Also intra-residual peaks were assigned. For OmpG, both ^1^H- and ^13^C-detected spectra were used in conjunction.


### SH3 ^13^C-detected spectra

To test the performance of the algorithm on spectra of specifically labeled samples, 5 spectra were of
SH3 were used: 2D ^13^C-^13^C DARR spectra with a mixing time of 300 ms and NCOCX spectra with a mixing time of 50 ms of both 2- and 1,3-glycerol labeled samples and a NCACX with a mixing time of 200 ms of the 2-glycerol
labeled sample. Spectra were peak picked automatically just above the noise, where the diagonal was excluded. In the 1,3 glycerol 2D ^13^C-^13^C correlation spectrum 168 out of 512 peaks were assigned as intra-residual. In the 2-glycerol 2D ^13^C-^13^C correlation spectrum these were 91 out of 449 peaks and in the NCACX 53 out of 271 peaks. In the two NCOCX spectra, there are no purely intra-residual peaks since the backbone nitrogen of residue i is correlated to the carbonyl of residue i-1. The tolerances of all 13C dimensions was set to 0.3 and 0.4 for all 15N dimensions. All spin-systems were typed automatically as part of the procedure, were the minimal type score was set to 1%. The system converged in 22 temperature steps with 100,000 Monte Carlo attempts per temperature point. For all but the first 5 residues, residues 47, 48 and 62 a unique spin system was assigned, see figure {@fig:malandro_statistics}A. All unassigned residues were also unassigned in the original assignment except for residue 62, of which only the backbone nitrogen was defined in the original assignment.

![Correctness of proposed sequential assignment of residues in three different proteins. The y-axis corresponds to the percentage of the ensemble of solutions in which a certain assignment was chosen. Assignments corresponding to previously made manual assignments are shown in blue. In red the most selected assignment is shown that did not correspond to the manual assignment. Light colors correspond to joker spin systems. A correctly placed joker is a joker placed on residue that was not assigned manually either.](figures/malandro_statistics.svg){#fig:malandro_statistics}


### SH3 ^1^H-detected spectra

From the ^1^H-detected spectra at 40 kHz MAS a HNCO and a HNcoCA were used as input to the algorithm, since these spectra contain sequential cross peaks. Spin systems were generated containing HN, N, CO, CA and CB resonances, by evaluating HNCA, HNcaCB and HNCO spectra. Automated peak picking yielded 52 peaks in the HNCO and 118 peaks in the HNcoCA. The higher than expected amount of peaks in the HNcoCA can be explained by the presence of the CA~i~ peak in a lot of strips where only a CA~i-1~ peak is expected. No repicking was performed to change this situation. Possible amino acid types were determined during the procedure as mentioned before, with a minimal type score of 1%. The algorithm already gives good results with 22 temperature steps and 100,000 attempts per step. However, when the amount of steps was increased to 1000,000 a bigger amount of the runs found the same final energy. This can partially be explained by the fact that the search-space is bigger due to less exclusive residue typing than is possible with ^13^C-detected data. Now spin systems only contain CA and CB carbon resonances that are relevant for residue typing, in contrast to the more fully configured spin-systems containing more side-chain carbon resonances in the previous example. For all residues the most frequent chosen assignment was the one that agrees with previously made manual assignments, except for proline 20, see figure {@fig:malandro_statistics}B. On this residue a joker spin system was placed in more than 90% of the runs, meaning that the algorithm could not assign it. No connecting peaks could be found to Arginine 21.


### YadA ^13^C-detected spectra

To test whether the algorithm was still of use for more challenging systems, YadA was used. Only two
spectra were used for this optimization: a 2D ^13^C-^13^C correlation spectrum, and a NCOCX, both
with a DARR mixing period of 200 ms and with uniform ^13^C, ^15^N labelling. As with
SH3, spin-systems were created using the published chemical shifts and the intra-residual peaks in the
2D carbon-carbon correlation were assigned to spin-systems by doing a short run of the algorithm. Two
alanine spin-systems (corresponding to residues 82 and 88) scored very low (less than 0.2%) for alanines in the residue-typing procedure as their Cβ shifts were slightly more downfield than expected. This was a clear case where human intervention was needed and these two spin systems were typed by hand. This directly
reveals one of the weakest spots in the procedure. If the correct residue-type is not in the set of
possibilities, a correct assignment of the spin system is not possible, which possibly leads to more
errors. For the rest of the spin systems, a set of possible residue-types was determined automatically
with a cut-off at 1% as described before. Tolerances were set to 0.3 and 0.4 for carbon and nitrogen
respectively. 100 independent runs with 22 temperature points and 1000,000 attempts per temperature point
were performed.
As can be observed in {@fig:malandro_statistics}C there are several differences between the manual assignment and the most frequently chosen assignment by the algorithm. There are basically 3 differences. In all cases the spin system corresponding to asparagine 55 in the original assignment is assigned to aspartic acid 22 and in most cases also visa versa. Assigning these residues manually was also very difficult. A collection of other sequential peaks from other connections are misinterpreted by the algorithm to be the connection between 21 and 55. Furthermore a large part of the signal set connecting Asparagine 55 to its neighbors is missing because the
residue is located in a loop between the beta-sheet and alpha-helix where a lot of line-broadening is
observed.
The second difference is that alanine 37 is assigned to glutamic acid 104 in almost all cases, leaving Ala 37 with a joker.This happens because not a lot of connections are found that support the original hypothesis. This is
solved when making the tolerances larger or when the spin system is hand-typed to Alanine. A third difference is that two out of the three serine-serine pairs (residues 65-66 and 92-93 respectively) are assigned differently. Some less severe issues includes placing jokers on 15 and 16, which basically indicates that the right solution could not be found, but also no erroneous solution is proposed.


### OmpG ^1^H- and ^13^C-detected spectra

For the assignment of OmpG seven spectra in total were selected. Five of those were ^13^C-^13^C correlation spectra with a DARR mixing period of 400 ms of the 1,3-glycerol, 2-glycerol, 1,3-TEMPQANDSG, 2-TEMPQANDSG and 2_SHLYGWAFV samples. These spectra are used for the structure calculation described later as well and the same peak lists were used as were used to generate distance restraints. The used ^1^H-detected spectra were the hcaCBcacoNH and hcoCAcoNH spectra as these contain good sequential data. The spin systems consisted of all the spin systems that were generated as described in previous chapters, including spin systems that could not be assigned to residues. This last category are mostly spin systems corresponding to intra-residual peak pattern that could be observed in the ^13^C-^13^C correlations but could not be sequentially assigned, such as the two threonine and three leucine spin systems correponding to the residues shown in red in {@fig:assignment_on_topology.svg}. Spin systems contain both chemical shift information on shifts in fully protonated and perdeuterated samples as described in the chapter about connecting assignments in ^13^C- and ^1^H-detected spectra.
Also here 100 independent runs with 22 temperature points and 1000,000 attempts per temperature point were performed.
The results on OmpG are a lot less clear than in the other two examples, see figure {@fig:malandro_statistics}D. Only 41 spin systems where unanimously and correctly assigned to a specific residue. These residues correspond to parts of the spectra with good signal to noise. Another 51 residues was assigned correctly in over 80% of the optimization runs, and another 25 in over 50% giving good hints for the possible assignment.


### Effect of missing peaks on the accuracy of proposed assignments

To simulate the effect of incomplete data, an increasing number of randomly selected peaks were
excluded from the carbon detected dataset of SH3. This dataset was chosen for this purpose because it
contains a lot of redundant information. The algorithm was tested on this reduced dataset and the
amount of correctly and incorrectly assigned spin-systems were determined. Because the quality of the
results is influenced by the subset of peaks that happens to be excluded, this procedure was repeated 10
times for each datapoint. The averages are shown in figure {@fig:malandro_deleting_peaks}. Each execution
of the algorithm consisted of 100 annealing runs in the same fashion as described before (22
temperature steps of 100.000 Monte Carlo attempts).


![Amount of correct assignments and false positives as a function of the amount of deleted peaks in ^13^C detected SH3. A (false) positive is defined here as any spin system being assigned to a residue in over 70% of the runs.](figures/malandro_deleting_peaks.svg){#fig:malandro_deleting_peaks}


## Download Information

Download and installation instructions for the assignment plug-in can be found at [https://github.com/jorenretel/Malandro](https://github.com/jorenretel/Malandro). The additional plug-in to set the residueTypeProp property of spin systems can be found at [https://github.com/jorenretel/ccpnmr-residueTypeProbs-editor](https://github.com/jorenretel/ccpnmr-residueTypeProbs-editor).

