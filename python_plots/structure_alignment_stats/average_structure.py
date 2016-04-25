# -*- coding: UTF-8 -*-

'''Script to generate an average structure out of
   an ensemble. The ensemble should be aligned
   already.

   usage: python average_structure.py my_structure.pdb

   output: my_structure_average.pdb

'''

import Bio.PDB
import os
import sys
import numpy as np


def create_average_structure(ensemble_pdf_file):

    pdb_parser = Bio.PDB.PDBParser(QUIET = True)

    ensemble = pdb_parser.get_structure('ensemble', ensemble_pdb_file)

    # Take the whole ensemble and gather coordinates
    # for each model.
    ensemble_coords = []

    for model in ensemble:
        model_coords = []
        for chain in model:
            for res in chain:
                for atom in res:
                    model_coords.append(atom.coord)
        ensemble_coords.append(model_coords)

    # Calculate the averaged coordinates
    ensemble_coords = np.array(ensemble_coords)
    average_coords = sum(ensemble_coords)/len(list(ensemble))

    # Use the first model in the ensemble
    # as a template and reset all coordinates
    # to average values.
    i = 0
    model = list(ensemble)[0]
    for chain in model:
        for res in chain:
            for atom in res:
                atom.set_coord(average_coords[i])
                i += 1

    # Save the average model
    io = Bio.PDB.PDBIO()
    io.set_structure(model)
    io.save(ensemble_pdb_file[:-4] + '_average.pdb', write_end=False)


if __name__ == '__main__':
    arguments = sys.argv[1:]
    ensemble_pdb_file = arguments[0]
    create_average_structure(ensemble_pdb_file)

