#!/bin/bash
#
#SBATCH -p common                # Partition to submit to (comma separated)
#SBATCH -J dscr_template         # Job name
#SBATCH -n 1                     # Number of cores
#SBATCH -N 1                     # Ensure that all cores are on one machine
#SBATCH -t 0-0:10                # Runtime in D-HH:MM (or use minutes)
#SBATCH --mem 1000               # Memory in MB
#SBATCH -o dscr_template_%j.out # File for STDOUT (with jobid = %j) 
#SBATCH -e dscr_template_%j.err       # File for STDERR (with jobid = %j) 
#SBATCH --mail-type=ALL          # Type of email notification: BEGIN,END,FAIL,ALL
#SBATCH --mail-user=EMAIL@duke.edu  # Email where notifications will be sent
#Your actual work goes after this line

srun echo "Use this SLURM template as a starting point for running"
srun echo "your own jobs"
