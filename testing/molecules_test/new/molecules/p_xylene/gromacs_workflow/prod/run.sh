#!/bin/bash

#SBATCH --partition=amilan
#SBATCH --job-name=p_xylene
#SBATCH --output=p_xylene.%j.out
#SBATCH --time=04:00:00
#SBATCH --nodes=4
#SBATCH --mail-type=ALL
#SBATCH --mail-user=liwh2139@colorado.edu

module purge
module load gcc
module load openmpi/4.1.1
module load gromacs


python prod_run.py