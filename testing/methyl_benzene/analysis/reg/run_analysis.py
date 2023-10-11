from alchemtest.gmx import load_ABFE
from alchemlyb.workflows import ABFE
import os

dir = '/projects/liwh2139/rotations/shirts/test/gromacs/methyl_benzene/gromacs/final/create_lambdas/sim'
outdirectory = '/projects/liwh2139/rotations/shirts/test/gromacs/methyl_benzene/gromacs/final/analysis/reg'


workflow = ABFE(units='kJ/mol', software='GROMACS', dir=dir,
                prefix='dhdl', suffix='xvg', T=300, outdirectory=outdirectory)
workflow.run(skiptime=100, uncorr='dhdl', threshold=50,
             estimators=('MBAR', 'BAR', 'TI'), overlap='O_MBAR.pdf',
             breakdown=True, forwrev=10)
