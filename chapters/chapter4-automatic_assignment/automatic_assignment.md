
(Semi-) Automatic Assignment of Solid-State NMR spectra
=======================================================

Over the years a lot of different sequential assignment algorithms have been written. This is completely understandable since this is a completely deterministic problem, the kind computers are actually very good at solving. However, a lot of these scripts suffer from limitations that made them unsuitable to use in my project. None of the methods was able to correctly deal with 2- and 1,3-glycerol labeled samples, for instance. A more general problem is that most algorithms are implemented as stand-alone applications. This often invokes a complicated work-flow in which one has to export several peak and resonance lists from the program that is used to do the analysis of the NMR spectra and convert them to the format expected by the routine. Afterwards the results should be imported back into the analysis program so the result can be analyzed. This is not necessarily bad if it has to be done only be done once. However, for complex assignment projects, with a work-flow in which new data and assignments are added incrementally, this becomes cumbersome. Ironically, often these programs do not get used either for the less complicated assignment tasks since the expected payoff is lower for the user when the assignment can also be done by hand in a reasonable amount of time. Installing the program, converting a hand full of text files and having to check the results afterwards in a not so straight-forward way might be enough to scare off users that would potentially have gotten perfect results using an automatic assignment algorithm.

Also the type of data these stand-alone applications output is somewhat problematic. Often this is one possible sequential assignment that is the true one according to the program. In other words, there is little space for human interference. It would be great however to be able to compare the alternative assignments that the algorithm had to consider and cherry-pick the results for those assignments you actually believe are correct. Many of these problems can be easily overcome when the (semi-) automatic assignment algorithm is integrated within the analysis program. CCPN Analysis databases a lot of information that is relevant to an automatic assignment routine, that would often be lost in a export-import routine. The program has a great Application Programming Interface (API) that gives access to all information stored in the project by the user.

It was not the initial goal to write an assignment algorithm, but to create a tool that would help compare alternative assignment possibilities in a fast way. Because of the extensive use of different labeling schemes used in the assignment of OmpG the peaks that sequentially connect spin systems are often spread over a large amount of spectra. Therefor I needed a tool that would show me which peaks are expected in all differently labeled experiments for two sequential residues A and B. Furthermore the tool should then use the resonance information from all combinations of spin systems A' and B' with a residue type assignment that matches the types of residues A and B to cross check whether there are indeed peaks in the peak lists at the expected positions. The general idea is that the more peaks present, the higher the likelihood that these two spin systems are indeed sequentially connected. The only method I could use before, was to plot rulers on the spectra at the resonance frequencies of the nuclei within a pair of spin systems A' and B'. Then the intersections of those rulers could be used to check whether there were the expected crosspeaks in different spectra. Of course this was too slow to systematically try out all combinations of spin systems over the whole sequence. Also, when this does not immediately result in a sequential assignment it is hard to remember or write down which combinations of spin systems fit together sequentially and to which extend. Therefor information can easily be lost and work has to be redone.

Of course, an application that compares different assignment possibilities for two sequential residues can easily be abstracted to the whole sequence. Then a optimization procedure can be used to find out the optimal mapping between spin systems and residues. In figure {@fig:malandro_flow_diagram} an overview is given of the different steps in the algorithm, which are discussed in more detail in the following paragraphs.



#### 1. Input of data

 In the first step the input to the algorithm is gathered. In principle most information can be automatically loaded from the CCPN project:

* molecular topology
* labeling schemes
* experiment types describing the magnetization transfer pathway
* picked peaks
* spin systems
* shift lists
* assignment tolerances
* previously made sequential, tentative, and non-sequential amino acid type assignments

Not all information that is databased in project does not have to be used necessarily. The user can choose which information is used and which is not. Excluding certain information can be practical when one wants to check a ready made assignment for instance. Spin systems in CCPN Analysis can basically have one of to following five levels of assignment: 1) The most definite form of assignment is of course when a spin system is sequentially assigned to a specific residue in the sequence. 2) One level of assignment lower, a spin system can be assigned 'tentatively' to multiple residues but it is not known which of those residues is the correct one. 3) Then there are spin systems that are residue typed, but no information about sequential assignment is present. 4) Also multiple residue types can be set for a residue. This option is not standardly accessible in the GUI of CCPN Analysis, but is present in the API and called ResidueTypeProbs. This is handy because often a residue type can be narrowed down to two very closely related residue types like asparagine and aspartic acid. 5) All the way at the bottom there are spin systems where not any form of sequential assignment nor residue type information is available.

In the part of the GUI shown in figure {@fig:malandro_gui}B it can be configured which of these different levels of assignment are used. If residue type information is not available or  not used, the residue typing algorithm already included in CCPN will be used to classify the spin systems to residue types. Because in most cases the classification is not definite, the user can set a threshold value above which all residue types will considered a possible.

There is one more type of assignments that can either be used or not by the algorithm, namely the assignment of peak dimensions to specific nuclei (resonances in CCPN). If this information is used, the only possible assignment of a peak dimension that is considered is the present assignment.

Furthermore the molecular chain that is used (the molecule) has to be selected and optionally only parts of the chain have to be considered for assignment. This last option can be used if it is clear that parts of the molecule can not be seen because of dynamics or for instance incomplete back-exchange of protons.

#### 2 Evaluate possible mapping between spin systems and residues

On the basis of the different levels of assignment describe above and which of that information should be used, for each spin system a set of possible residue assignments is created. Based on these sets, it can already be determined for each spin system with which other spin systems it could ever exchange sequential assignments in the Monte Carlo procedure later on. This information is used during the Monte Carlo procedure to pick which two spin systems to exchange. Also, at this stage 'joker' spin systems are introduced to make sure that always a spin system can be assigned to every residue. This is important since the Monte Carlo procedure was designed to select two spin systems and exchanging their residue assignments rather than the other way around, it is important that all residues always have a spin system assigned to them, because once that would not be case no spin system will ever be assigned to it.









![Flow diagram of the (semi-) automatic assignment algorithm.](figures/malandro_flow_diagram.svg){#fig:malandro_flow_diagram}



![The expected peaks can be matched to picked peaks in the spectra. Therefor the chemical shifts of all combinations of spin systems A', B' that can be assigned to sequential residues A and B can be used to predict the location of the peaks (A). How well the real fits the predicted peak location is scored by a flat bottom scoring function (B).](figures/malandro_peak_matching.svg){#fig:malandro_peak_matching}




![Graphical User Interface of the (semi-)automatic assignment algorithm. A: a subset of spectra can be selected to be used by the routine. B: a number of settings can be configured controlling which information in the CCPN project is used by the algorithm. Also parameters controlling the annealing process are set here. The graph at the bottom shows the progress of the annealing procedure. C: The results are shown in 5 tables, representing 5 consecutive residues in the sequence. In each table all spin systems that can be assigned to that particular residue are listed. When selecting two spin systems for two sequential residues, all peaks that connect these spin systems are listed in the table at the bottom. Assignments can be inspected here and individually transferred to the project. D: Assignments can also be transferred in bulk to the project. In order to do so, the user should indicate which assignments exactly as multiple annealings were performed. One of the possibilities is to only assign those spin systems that are assigned in a threshold fraction of all annealing runs.](figures/malandro_gui.png){#fig:malandro_gui}


