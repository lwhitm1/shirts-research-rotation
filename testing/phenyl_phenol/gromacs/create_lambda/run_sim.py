#!/usr/bin/env python

import sys
import os
from pathlib import Path

def main(output_directory, number_of_lambdas, mdp_template_file):
    output_files = Path(output_directory)

    with open(mdp_template_file, 'r') as mdp_template:
        run_mdp = mdp_template.read()

    for lambda_number in range(number_of_lambdas):
        lambda_directory = output_files / f'lambda_{lambda_number:02}'
        lambda_directory.mkdir(parents=True, exist_ok=True)

        # Copy 'equil.gro' to 'conf.gro' in lambda_directory
        (lambda_directory / 'conf.gro').write_text((output_files / 'phenylphenol_equil.gro').read_text())

        # Copy 'topol.top' to lambda_directory
        (lambda_directory / 'topol.top').write_text((output_files / 'phenylphenol_topo.top').read_text())

        # Write the customized MDP file 'grompp.mdp' in lambda_directory
        with open(lambda_directory / 'grompp.mdp', 'w') as mdp_file:
            mdp_file.write(run_mdp.format(lambda_number))

        # Change the current working directory to lambda_directory
        os.chdir(lambda_directory)

        # Execute GROMACS commands (assuming you have GROMACS installed and set up in your environment)
        os.system('gmx grompp')
        os.system('gmx mdrun')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <output_directory> <number_of_lambdas> <mdp_template_file>")
        sys.exit(1)

    output_directory = sys.argv[1]
    number_of_lambdas = int(sys.argv[2])
    mdp_template_file = sys.argv[3]

    main(output_directory, number_of_lambdas, mdp_template_file)

