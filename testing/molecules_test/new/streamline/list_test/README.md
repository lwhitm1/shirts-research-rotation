# Project overview:

	- Streamlining openff -> gromacs -> alchemlyb workflow

	- This README contains information about the first stage of the workflow: generating topology files and GROMACS .gro files for specified molecules
		
		- This script was adapted from the following tutorial: https://docs.openforcefield.org/en/latest/examples/openforcefield/openff-interchange/ligand_in_water/ligand_in_water.html

# What you need to run:

	- The Open Force Field toolkit needs to be installed in your environment.

		-For more information on installation: https://docs.openforcefield.org/en/latest/install.html

	- A file containing molecule names and SMILES string representations of the molecule

		- We have an example file test_small_molecules.txt that contains three molecules with their SMILES strings.

	- The python script small_molecules_streamlined.py

		- This script takes in your molecule file and creates topology files and GROMACS files using open force field utilities and outputs them to the specified output directory. Each molecule will have its own subdirectory within the specified output directory and will contain the generated files.

# To run:

	- Run: `python small_molecule_streamline.py --input_file <path to file containing molecule names and SMILES strings> --out_dir 9path to specified output directory.` 
