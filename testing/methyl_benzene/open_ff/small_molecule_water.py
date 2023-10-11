import numpy as np
from openff.toolkit import ForceField, Molecule, Topology
from openff.units import unit
from openff.interchange import Interchange
from openff.interchange.components._packmol import RHOMBIC_DODECAHEDRON, pack_box
from openff.interchange.components.mdconfig import MDConfig



#constructing topology
mol = Molecule.from_smiles("CC1=CC=C(C)C=C1")
mol.generate_conformers()

water = Molecule.from_smiles("[OH2]")
water.generate_conformers()

topology = pack_box(
        molecules =[mol, water],
        number_of_copies=[1, 1000],
        box_vectors=3.5 * RHOMBIC_DODECAHEDRON * unit.nanometer,
        )

#topology = Topology.from_molecules([mol])

sage = ForceField("openff-2.0.0.offxml")

#create interchange
interchange = Interchange.from_smirnoff(
        force_field =sage,
        topology=topology,
        )

#export to GROMACS files
interchange.to_top("topol_mb.top")
interchange.to_gro("methylbenzene.gro")

#mdconfig = MDConfig.from_interchange(interchange)
#mdconfig.write_mdp_file(mdp_file="auto_generated_system.mdp")

