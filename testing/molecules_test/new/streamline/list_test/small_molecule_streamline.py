"""This script takes in a file that has molecule name and their corresponding
smiles string on each line. If separated by comma, change delimmiter in main
for split to a comma. This script will create a topology and GROMACS file for
each small molecule in water and output them into their own separate directories."""

import os
import sys
import argparse
import numpy as np
from openff.toolkit import ForceField, Molecule, Topology
from openff.units import unit
from openff.interchange import Interchange
from openff.interchange.components._packmol import RHOMBIC_DODECAHEDRON, pack_box
from openff.interchange.components.mdconfig import MDConfig


def get_args():
    parser = argparse.ArgumentParser(description='''Utilize open force field utilities
                                                    to construct a topology and gromacs
                                                    file for a small molecule in water
                                                    given a file containing molecule
                                                    names and smiles strings.''',
                                    prog='small_molecule_streamlined.py')
    parser.add_argument('--input_file',
                        type=str,
                        help='''Path to input file containing molecule
                        names and SMILES strings.''',
                        required=True)
    parser.add_argument('--out_dir',
                        type=str,
                        help='''Path to place where individual molecule
                        directories will be created.''',
                        required=True)
    args = parser.parse_args()
    return args


def main():
    arg = get_args()

    #read file and get molecule names and smiles strings
    with open(arg.input_file, 'r') as f:
        for line in f:
            molecule_name, smiles = line.strip().split()
            molecule_dir = os.path.join(arg.out_dir, molecule_name)
            os.makedirs(molecule_dir, exist_ok=True)

            os.chdir(molecule_dir)

            #constructing topology
            mol = Molecule.from_smiles(smiles)
            mol.generate_conformers()

            water = Molecule.from_smiles("[OH2]")
            water.generate_conformers()

            topology = pack_box(
                    molecules =[mol, water],
                    number_of_copies=[1, 1000],
                    box_vectors=3.5 * RHOMBIC_DODECAHEDRON * unit.nanometer,
                    )

            sage = ForceField("openff-2.0.0.offxml")

            #create interchange
            interchange = Interchange.from_smirnoff(
                    force_field =sage,
                    topology=topology,
                    )

            #export to GROMACS files
            interchange.to_top(molecule_name + '_topol.top')
            interchange.to_gro(molecule_name + '.gro')

            os.chdir(arg.out_dir)


if __name__ == '__main__':
    main()

