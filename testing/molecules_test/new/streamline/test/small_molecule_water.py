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
                                                    given a SMILES string.''',
                                    prog='small_molecule_water.py')
    parser.add_argument('--smiles',
                        type=str,
                        help='''SMILES string for the small molecule you
                                would like to simulate.''',
                        required=True)
    parser.add_argument('--top_name',
                        type=str,
                        help='''Name of the topology file outputted.''',
                        required=True)
    parser.add_argument('--gro_name',
                        type=str,
                        help='''Name of the GROMACS file outputted.''',
                        required=True)
    args = parser.parse_args()
    return args


def main():
    arg = get_args()

    #constructing topology
    mol = Molecule.from_smiles(arg.smiles)
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
    interchange.to_top(arg.top_name + '.top')
    interchange.to_gro(arg.gro_name + '.gro')


if __name__ == '__main__':
    main()

