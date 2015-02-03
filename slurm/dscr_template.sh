#!/bin/bash
#
#SBATCH --job-name=dscr_template
#SBATCH --output=dscr_template.out
#SBATCH --time=10:00
#SBATCH --mem=1K

srun echo "Use this SLURM template as a starting point for running"
srun echo "your own jobs"
