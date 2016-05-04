\mainmatter
\part{Introduction}
\fancyhead[RE]{CHAPTER \thechapter}

Structural Biology of Membrane Proteins
=======================================

This thesis revolves around the sequential assignment and structure determination of outer membrane protein G (OmpG) by solid-state NMR.

Structural biology is essentially about reverse-engineering on a bio-molecular level. The central dogma in the field is that the structures of bio-molecules such as DNA, RNA and proteins can tell something about their function and how they fulfill this function. Of course this is interesting from a purely scientific point of view. However, understanding the biological mechanisms that are connected to diseases can help developing therapies.

The first structure of a protein,... was solved in 19.. by x-ray crystallography.


## Biological Membranes

Some form of compartmentalization is essential for the existence of life. In a semi-closed off system energy and organic matter can reach sufficiently high concentrations to support the rise of complex structures. Therefor every origin of live theory in one way or another involves spatial compartments [@deamer_first_1997]. These original compartments are often believed to be of non-biological nature such as mineral surfaces [@cairns-smith_genetic_1982][@koonin_origin_2005]. At some point during the early evolution of life first biological cells were formed that possessed a lipid membrane so that live could break free from the pre-existing compartments. Whether this happened before or after the last universal common ancestor and what the composition of this membrane exactly was is under some debate [@jekely_did_2006][@mulkidjanian_coevolution_2009]. The fact is that all modern cells have membranes though.

Membranes form the barrier between the inside and the outside of cells. In eukaryotes membranes are also present within the cell dividing it in different compartments such as the nucleus, mitochondria, golgi apparatus and in the case of plants the chloroplasts. Membranes do not only function purely as separators but play an active role determining the cell's shape, locomotion, interaction with other organisms or neighboring cells and the extracellular matrix in the case of multicellular organisms. Proton gradients over the membranes of mitochondria and chloroplasts drive the synthesis of ATP and ion gradients over the membranes of our neurons allow them to fire.

The lipids in membranes are arranged to form a bilayer. The hydrophobic tails are pointing towards the center of the bilayer while the the hydrophilic head groups point towards the aqueous solution. Because of the various different roles lipid composition in biological membranes is very diverse and differs widely between organisms and cell types [@dowhan_molecular_1997].

In general the main lipid component of membranes are phospholipids. In addition eukaryotic membranes also contain sterols influenceing rigidity and permeability [@haines_sterols_2001]. Furthermore membranes of plant cells contain large amounts of glycolipids. Knowledge about the exact chemical composition of different lipids in cells is mostly obtained by a combination of a combination of mass spectroscopy and liquid chromatography and generated its own omics field logically called lipidonomics [@dennis_lipidomics_2009][@ivanova_lipidomics_2009]. In eukaryotes thousands of different lipids can be present based on the combination of different head groups and chain lengths [@sud_lmsd_2007][@vanmeer_membrane_2008]. An interesting divide in the type of phospholipids that make up the membrane is between bacteria and eukaryotes versus archaea [@kates_phytanyl_1977][@pereto_ancestral_2004]. The most important distinction here is that in archaea the opposite glycerol stereoisomer is used to synthesize the phospholipid backbone in comparison to the other two branches of life.

The combination of lipids does not only vary between different membranes but also between the two leaflets that compose the lipid bilayer. This is also the case in the outer membrane of E. coli. The outer leaflet is composed of lipopolysaccharides (LPS), and the inner leaflet of the more usual phospholipids of which the majority is phosphatidylethanolamine (PE) (75%) and phosphatidylglycerol (PG) (20%) [@nikaido_molecular_2003][@gidden_lipid_2009][@garrett_quantification_2012][@sohlenkamp_bacterial_2016].

The fact that there is such a variety of lipids and organisms spend expensive resources to create this variety indicates its relevance. The mix of lipids making up the membrane directly influences properties such as its flexibility, curvature, permeability and interaction with membrane proteins [@kimura_roles_2016].



## Membrane Proteins

Besides lipids the membrane consists for a large part of membrane proteins. In mouse liver the fraction of protein by weight is about 45% and in E. coli this is 75% [@lehninger_lehninger_2008]. Some membrane proteins are mostly outside of membrane only being anchored to the membrane with a covalently bound lipid tag or hydrophobic α-helix. These proteins are known as peripheral or monotopic membrane proteins. Others span the entier bilayer and have parts of the proteins stick out on both sides of the membrane. These proteins are called integral membrane proteins. In turn there are two large classes of integral membrane proteins: proteins largely consistent of multiple membrane spanning α-helices and β-barrels.

In most organisms 20-30% of genes code for membrane proteins [@krogh_predicting_2001]. Membrane proteins play a role in numerous important biological events. Receptors transmit information from the outside of the cell to the inside. Transporters enable the flux of molecules and ions. Membrane proteins catalyze reaction such as the before mentioned synthesis of ATP. Almost the entier photosynthesis machinery consists of membrane proteins. The flagellar motor that lets some bacteria swim is membrane embedded. Of course membrane proteins are also active in processes during which the shape of the membrane has to be transformed such as endocytosis and cell division. Furthermore over 60% of all approved drugs target a membrane protein [@overington_how_2006][@yildirim_drugtarget_2007].

For these reasons it is important to gather a detailed understanding of how these membrane proteins work. However, the number of unique proteins in the database of membrane proteins of known 3D structure is at the moment (4.5.2016) 612 from which 22 are porins, like OmpG [@membrane-protein-db]. The reason for this underrepresentation is actually quite simple. The two major work horses for the structure elucidation at atomic length scales, x-ray crystallography and solution NMR spectroscopy, work very well with soluble protein but less so with large insoluble membrane proteins [@lacapere_determining_2007]. Although recent advances in both techniques have enabled the structure determination of most the membrane proteins in the protein data band (PDB), see table {@tbl:pdb_count_table}, the growth in the number of deposited membrane protein structures still lags behind. The most used technique to grow crystals for x-ray crystallography is the hanging drop method. This method relies on proteins being free in solution. To accomplish for membrane proteins detergents have to be added. As the volume of the drop shrinks and the concentration of both protein and detergent rises often a phase separation takes place negatively influencing the formation of crystals [@lacapere_determining_2007]. An alternative method to produce crystals is to employ a lipid cubic phase which is a complex but ordered matrix of lipid bilayers [@caffrey_comprehensive_2015]. For solution NMR studies membrane proteins are often introduced in micelles or nanodisks [@sanders_reconstitution_1995][@gluck_integral_2009]. Recently cryo-electron microscopy has made impressive progress and can be applied to membrane proteins [@zorzi_singleparticle_2015].


|                       | α-helical | β-barrel | monotopic |
|-----------------------|-----------|----------|-----------|
| total unique          | 463       | 133      | 46        |
| x-ray crystallography | 398       | 124      | 46        |
| electron microscopy   | 34        | 5        | 1         |
| solution NMR          | 55        | 16       | 1         |
| solid-state NMR       | 9         | 1        | -         |

Table: membrane proteins protein data bank (PDB) for four structure determination methods. To prevent over-representation of the amount of protein entries for each method have been filtered for 95% sequence similarity. Note that the numbers of structures determined by individual methods does not add up to the total number of unique structures because the structure of several proteins has been determined by more than one method. Also the total number of structures is slightly higher than the number reported in the database of membrane proteins of known 3D structure.{#tbl:pdb_count_table}



The topology of membrane proteins can often be predicted based on the residue sequence. For instance, 20 or more hydrofobic residues is a row is quite likely to form a transmembrane helix. Also other types of residues give a hint to the topology of a membrane protein. For instance tryptophan residues are often found at the interface between the transmembrane and the non-transmembrane part of the protein since they have a large flat aromatic ring system....



![Distribution of sequence lengths of all proteins in the uniProt database tagged as membrane protein. The amount of proteins with sequence lengths similar to OmpG, 281 residues, is very large, making OmpG a relevant model system.](figures/membrane_protein_sequence_lenth_distribution.svg){#fig:membrane_protein_sequence_lenth_distribution}


## Protein-lipid interactions






### Outer membrane proteins (Omps)

#### OmpG


## Solid-State NMR

Nuclear magnetic resonance, or NMR, spectroscopy is a very standard method for the analysis of chemical substances. The general idea behind the technique is, like in any other form of spectroscopy, to measure a difference in energy between different states. In the case of NMR spectroscopy the different states are generated by bringing the sample in a large magnetic field. All atomic nuclei have a quantum mechanical property called 'spin'. In a magnetic field the spin of some atomic nuclei, for example the nucleus of the normal hydrogen 1H isotope, will be either pointed along the magnetic field or against it. The energy of the spins that are aligned with the magnetic field is slightly lower than that of those that are pointed against it. This is the energy difference that is exploited by NMR spectroscopy and leads to a signal in a NMR spectrum. The energy difference is directly related to the strength of the magnetic field. However the magnetic field that is perceived by a given spin is not only only determined by the external field of the magnet. Also the direct chemical environment around the spin influences the local magnetic field. Therefor every nucleus in a molecule that has a slightly different chemical environment gives rise to a peak on a different position in the spectrum. By careful analysis of these spectra, often combined with mass spectrometry, it has been possible for decades to determine the composition and structure of small organic molecules.
The use of NMR spectrometry in structural biology, which this thesis is about, is a little bit different. We generally already know the chemical composition of the molecule of interest. In case of a protein we know its amino acid sequence. In case of RNA or DNA we know the nucleotide sequence. Of course we also know the chemical composition of the amino acids and nucleotides respectively. The only missing information is the shape it adopts in three dimensional space and how this shape changes over time.

The energy difference used in NMR is only very small compared to the thermal energy at biologically relevant temperatures. Therefor NMR is an inherently insensitive method. A measurable signal can only be generated by the measuring millions of molecules at the same time. As will be explained later, in one way or another all difficulties with this method lead back to this fact.



## Magic Angle Spinning

In both liquid and solid samples, every molecule in the sample has a different spacial orientation in respect to direction of the static field of the magnet.


## Cross-polarization

## Relaxation

## Sequential Assignment of solid state NMR spectra

In most NMR studies very little can be done before the chemical shifts of the nuclei that are interesting in the context of the biological question are known. Sometimes those are only a few. However if the goal is to calculate the structure and study the overall dynamics of the protein a fairly complete mapping between resonance frequencies and nuclei in the molecule has to be present. This mapping process is referred to as sequential assignment and often is the most time consuming part of a NMR study. The general idea behind sequential assignment methodologies is always the same: the graph that arises from a set of correlation spectra is mapped on the molecular topology. In most (but not all) methodologies to find this mapping, the process is divided into two steps. In the first step parts of the total signal pattern are identified that correspond to individual residues. In a second step connectivities are found between these signal patterns and a larger signal pattern that belongs to a set of sequentially connected residues is created. Because the nuclei in different amino acids give rise to a different combination of chemical shifts, the sets of signals can be classified down to a few or sometimes even one type of amino acid. When this is done, the larger pattern can be mapped to a subsequence in the protein that matches these possible residue type assignments.

From now on I will call the collection of resonance frequencies that belong to one residue a spin system. The term **spin system** is often used in NMR in a somewhat less confined sense, meaning a set of resonances that are in some way influenced by one another. However, since this thesis will deal with sequential assignment for a large extent, it is good to have quick way to describe this object. Also the CCPNMR Analysis software, that is used to analyze NMR spectra, uses the term as I just defined it.

In order to get a unique match between the potential residue types of a sequential stretch of spin systems and a subsequence in the protein, the stretches should in general be long enough. I.e. the longer a connected stretch is, the higher the chance there is only one possible location along the protein sequence were this stretch fits. Of course it highly depends on the length of the protein sequence how long it takes before this is the case. In figure {@fig:amount_of_unique_subsequences} the fraction of unique subsequences of lenght 1, 2 and 3 are plotted vs. the lenght of the protein. As can be seen, even for very large proteins, connected stretches of 3 spin systems can in theory be uniquely matched to a subsequence of the protein in the majority of cases. This is of course under the assumption that each spin system can be uniquely typed to one amino acid type, which is not the case in practice since some amino acids give rise to very similar signal sets. Therefor in practice often somewhat longer stretches need to be generated before a unique match to a subsequence in the protein can be found.



![Percentage of subsequences that is only present in the sequence once. Purple, orange and green correspond to subsequences of length 1,2 and 3 respectively. This plot is made using 1000 membrane protein sequences from the uniProt database. Every point represents one protein. As expected, the amount of single amino acids that only appear in the sequence once very quickly drops off with increasing sequence length. At the other side, even for the largest proteins still more than half of all triplets (subsequences of length 3) is completely unique in the sequence. Of course, the fact that the subsequence is unique does not necessarily mean that the subsequence can be distinguished from all other subsequences based on the chemical shifts of these residues. That also heavily depends on how many ^13^C chemical shifts of the spin systems are known, which is directly dependent on the type of spectra recorded.](figures/amount_of_unique_subsequences.svg){#fig:amount_of_unique_subsequences}


For the assignment of larger proteins both steps in the assignment process become more diffeicult. The real bottleneck in here is chemical shift degeneracy. The larger the amount of NMR active nuclei in a protein, the smaller the average spacing between the resonance frequences will be. This causes two problems that are very closely related, but should be considered both distinctly:

1. Spectral crowding, the overlap of signals in spectra.
2. Degeneracy of assignment of peaks.

The first problem is very simple, spectra get very hard to interpret if signals are piled on top of each other. The second problem maybe needs a little more explanation. In order to connect spin systems to form a sequential stretch, cross peaks between them in correlation spectra are needed. However, if a crosspeak can be explained by multiple different resonance frequencies from multiple spin systems on each dimension, it gets a lot harder to build these stretches. It is not so much that this type of peak is necessarily really overlapping with another peak, it is the apparent overlap of peaks.

Of course in the end both these problems barrel down to linewidth. If linewidths were infinitely narrow, none of these problems would exist. There would be no signal overlap and every cross-peak could be explained by the correlation of spins of exactly the same number as its dimensions. If this were the case, there would be a very clear one to one mapping between the signal set and the molecular topology.

To combat the problem of spectral crowding and assignment ambiguity of crosspeaks, in general three approaches can be taken:

1. Reduce the amount of signals in the signal set by isotopically labelling only a subset of the nuclei in the protein.
2. Spread the signal set over more dimensions.
3. Decrease linewidths.

Over the last few years, solid state NMR has made an enormous amount of progress and also the methods we used in this project changed during this process. The NMR methods used have a large influences on the way sequential assignments are made. A first chapter will explain the efforts we did to assign OmpG using ^13^C-detected NMR, because that is how this was generally done at the time this project started off. Afterwards the progress that was made in this project using ^1^H-detected experiments will be shown. Although it might seem that the use of the latter method is more important, the results from the ^13^C-detected experiments are not just included for chronological completeness. As will be clear, a lot of information obtained from the ^13^C-detected spectra is still very valuable and there is until now not a method in ^1^H-detected solid state NMR that can fully obtain all information provided by the ^13^C-detected experiments. Spectra from both methods have been used in conjunction and in a complementary fashion. Therefor in a third chapter the combination of both types of spectra will be discussed.

## Recent Progress


![Electron micrograph of the OmpG 2D crystals. In this specific case it is OmpG and E. Coli lipids in a 2:1 mass ratio in MES buffer at pH 6.3. The lipid-OmpG mix seems to make tubular shapes.](figures/OmpG_MES_pH63_70procentH_30procentD_30042014_B.png)








