from alchemtest.gmx import load_ABFE
from alchemlyb.workflows import ABFE
# Obtain the path of the data
import os
dir = '/projects/liwh2139/rotations/shirts/test/gromacs/methyl_benzene/gromacs/final/updated_create_lambda/sim'
outdirectory = '/projects/liwh2139/rotations/shirts/test/gromacs/methyl_benzene/gromacs/final/analysis/updated'
#print(dir)

workflow = ABFE(units='kJ/mol', software='GROMACS', dir=dir,
                prefix='dhdl', suffix='xvg', T=300, outdirectory=outdirectory)
workflow.run(skiptime=100, uncorr='dhdl', threshold=50,
             estimators=('MBAR', 'BAR', 'TI'), overlap='O_MBAR.pdf',
             breakdown=True, forwrev=10)
