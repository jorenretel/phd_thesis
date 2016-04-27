# -*- coding: UTF-8 -*-

import Bio.PDB
import os
import sys
import numpy as np

# BETA SHEET and turn residues in OmpG
BETA_SHEET = range(8, 17)
BETA_SHEET.extend(range(34, 42))
BETA_SHEET.extend(range(44, 52))
BETA_SHEET.extend(range(70, 79))   # 1 res shorter as solution structure
BETA_SHEET.extend(range(85, 96))
BETA_SHEET.extend(range(110, 123))
BETA_SHEET.extend(range(127, 140))
BETA_SHEET.extend(range(151, 162))
BETA_SHEET.extend(range(167, 176))  # 1 res shorter
BETA_SHEET.extend(range(194, 203))  # lacking 3 residues at the start
BETA_SHEET.extend(range(205, 212))
BETA_SHEET.extend(range(238, 245))
BETA_SHEET.extend(range(249, 256))
BETA_SHEET.extend(range(274, 281))

TURN = range(42, 44)
TURN.extend(range(79, 85))
TURN.extend(range(123, 127))
TURN.extend(range(162, 167))
TURN.extend(range(203, 205))
TURN.extend(range(245, 249))





def allign(ensemble_pdb_file, ref_pdb_file, residues=None, index_diff=0):

    #print ensemble_pdb_file, ' compared to ', ref_pdb_file

    # Select what residues numbers you wish to align
    # and put them in a list

    rmsds = []

    residues_to_be_aligned = residues
    #print residues_to_be_aligned

    residues_to_be_aligned_ref = [res + index_diff for res in residues_to_be_aligned]

    # ARIA 'Ordered Resdidues'
    # residues_to_be_aligned.extend(range(32, 52))
    # residues_to_be_aligned.extend(range(68, 79))
    # residues_to_be_aligned.extend(range(88, 96))
    # residues_to_be_aligned.extend([97])
    # residues_to_be_aligned.extend(range(107,120))
    # residues_to_be_aligned.extend([124])
    # residues_to_be_aligned.extend(range(127,131))
    # residues_to_be_aligned.extend(range(132,136))
    # residues_to_be_aligned.extend(range(137,146))
    # residues_to_be_aligned.extend([148])
    # residues_to_be_aligned.extend(range(151,164))
    # residues_to_be_aligned.extend(range(165,175))
    # residues_to_be_aligned.extend(range(194,212))
    # residues_to_be_aligned.extend(range(238,244))
    # residues_to_be_aligned.extend(range(249,254))
    # residues_to_be_aligned.extend(range(273,281))


    # Start the parser
    pdb_parser = Bio.PDB.PDBParser(QUIET = True)

    # Get the structures
    ref_structure = pdb_parser.get_structure("reference", ref_pdb_file)
    ref_model = ref_structure[0]

    # Make a list of the atoms (in the structures) you wish to align.
    # In this case we use CA atoms whose index is in the specified range
    ref_atoms = []

    ensemble = pdb_parser.get_structure('ensemble', ensemble_pdb_file)
    #average = pdb_parser.get_structure('average', 'fitted_ompg_dmso_average.pdb')
    #ref_model = average[0]

    for ref_chain in ref_model:
        for ref_res in ref_chain:
          if ref_res.get_id()[1] in residues_to_be_aligned_ref:

              ref_atoms.extend([ref_res[a] for a in ('N', 'CA', 'C', 'O')])
        break


    io = Bio.PDB.PDBIO()
    io.set_structure(ref_model)

    i = 1
    #for pdb_file in pdb_files[1:]:
    for sample_model in ensemble:

        sample_atoms = []

        # Do the same for the sample structure
        for sample_chain in sample_model:
            for sample_res in sample_chain:
                #print sample_res.get_id()
                if sample_res.get_id()[1] in residues_to_be_aligned:
                    sample_atoms.extend([sample_res[a] for a in ('N', 'CA', 'C', 'O')])

        # Now we initiate the superimposer:
        super_imposer = Bio.PDB.Superimposer()
        super_imposer.set_atoms(ref_atoms, sample_atoms)
        super_imposer.apply(sample_model.get_atoms())

        sample_model.id = i
        i +=1
        io.structure.add(sample_model)
        rmsds.append(super_imposer.rms)


    new_file_name = 'alligned_{}_{}.pdb'.format(ensemble_pdb_file[:-4], ref_pdb_file[:-4])

    io.save(new_file_name, write_end=False)

    #print 'mean: ', np.mean(rmsds)
    #print 'standard deviation: ', np.std(rmsds)

    print '{} vs. {} {} (±{})'.format(ensemble_pdb_file, ref_pdb_file, round(np.mean(rmsds),2), round(np.std(rmsds),2))



def get_energy(pdb_file):

    with open(pdb_file, 'r') as f:
        for line in f.readlines():
            if line.startswith('REMARK energies:'):
                return float(line.split()[2][:-1])



if __name__ == '__main__':

    #files = [name for name in os.listdir(os.getcwd()) if os.path.isfile(name) and name.endswith('.pdb') and not name == 'aligned.pdb']

    #files = ['ompg_{}.pdb'.format(x) for x in range(1,21)]
    #arguments = sys.argv[1:]
    #pdb_file = arguments[0]

    print 'beta sheet'
    allign('fitted_ompg_dmso.pdb', 'fitted_ompg_dmso_average.pdb', BETA_SHEET)
    print 'sheet + turn'
    allign('fitted_ompg_dmso.pdb', 'fitted_ompg_dmso_average.pdb', BETA_SHEET+TURN)
    allign('fitted_ompg_dmso.pdb', '2iww.pdb', BETA_SHEET, index_diff=-1)
    allign('fitted_ompg_dmso.pdb', '2iwv.pdb', BETA_SHEET, index_diff=-1)
    allign('fitted_ompg_dmso.pdb', '2f1c.pdb', BETA_SHEET, index_diff=-1)
    #allign('2jqy.pdb', '2iwv.pdb', index_diff=0)
    allign('fitted_ompg_dmso.pdb', '2jqy_average.pdb', BETA_SHEET, index_diff=-1)
    allign('fitted_ompg_dmso_average.pdb', '2jqy_average.pdb', BETA_SHEET, index_diff=-1)
