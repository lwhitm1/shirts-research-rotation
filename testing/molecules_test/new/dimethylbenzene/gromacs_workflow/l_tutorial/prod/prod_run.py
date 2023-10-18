import os
import shutil

# Define the number of lambdas
number_of_lambdas = 7

# Define the output directory where lambda subdirectories will be created
output_files = '/projects/liwh2139/rotations/shirts/test/gromacs/new/dimethylbenzene/gromacs_workflow/l_tutorial/prod'

# Define the path to the template MDP file
template_mdp_file = os.path.join(output_files, 'run.mdp')

# Read the content of the template MDP file
with open(template_mdp_file, 'r') as template_file:
    template_mdp = template_file.read()

for lambda_number in range(number_of_lambdas):
    lambda_directory = os.path.join(output_files, 'lambda_{:0>2}'.format(lambda_number))

    # Create the lambda subdirectory
    os.mkdir(lambda_directory)

    # Define paths to necessary files
    gro_file = os.path.join(output_files, 'npt.gro')
    top_file = os.path.join(output_files, 'topol.top')
    cpt_file = os.path.join(output_files, 'npt.cpt')

    # Copy GRO file and topology file to the lambda subdirectory
    shutil.copy(gro_file, os.path.join(lambda_directory, 'conf.gro'))
    shutil.copy(top_file, lambda_directory)
    shutil.copy(cpt_file, lambda_directory)

    # Customize the MDP content for the current lambda
    mdp_content = template_mdp.replace('{}', str(lambda_number))

    # Write the customized MDP file for the current lambda
    mdp_filename = os.path.join(lambda_directory, 'grompp.mdp')
    with open(mdp_filename, 'w') as mdp_filehandle:
        mdp_filehandle.write(mdp_content)

    # Change the working directory to the lambda subdirectory
    os.chdir(lambda_directory)

    #Execute GROMACS commands using os.system
    os.system('gmx grompp -f grompp.mdp -c conf.gro -p topol.top -t npt.cpt -o md.tpr')
    os.system('gmx mdrun -deffnm md')

    # Return to the original working directory (optional)
    os.chdir(output_files)
