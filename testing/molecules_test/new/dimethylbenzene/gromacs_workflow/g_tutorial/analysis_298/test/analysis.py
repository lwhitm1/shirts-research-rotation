import alchemlyb.workflows
import os
from alchemlyb.workflows import ABFE

dir = "/projects/liwh2139/rotations/shirts/test/gromacs/new/dimethylbenzene/gromacs_workflow/prod_298"

outdirectory = '/projects/liwh2139/rotations/shirts/test/gromacs/new/dimethylbenzene/gromacs_workflow/analysis_298/tesy'


workflow = ABFE(units='kcal/mol', software='GROMACS', dir=dir,
                prefix='dhdl', suffix='xvg', T=298, outdirectory=outdirectory)
workflow.run(skiptime=100, uncorr='dhdl', threshold=50,
             estimators=('MBAR', 'BAR', 'TI'), overlap='O_MBAR.pdf',
             breakdown=True, forwrev=10)
summary = workflow.generate_result()
print(summary)
