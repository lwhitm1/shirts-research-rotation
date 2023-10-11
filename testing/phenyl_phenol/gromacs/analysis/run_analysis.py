from alchemtest.gmx import load_ABFE
from alchemlyb.workflows import ABFE
# Obtain the path of the data
import os
dir = '/projects/liwh2139/rotations/shirts/test/gromacs/phenyl_phenol/gromacs/create_lambda/simulation'
outdirectory = '/projects/liwh2139/rotations/shirts/test/gromacs/phenyl_phenol/gromacs/analysis'
#print(dir)

workflow = ABFE(units='kcal/mol', software='GROMACS', dir=dir,
                prefix='dhdl', suffix='xvg', T=298, outdirectory=outdirectory)
workflow.run(skiptime=100, uncorr='dhdl', threshold=50,
             estimators=('MBAR', 'BAR', 'TI'), overlap='O_MBAR.pdf',
             breakdown=True, forwrev=10)
