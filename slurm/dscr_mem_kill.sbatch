#!/bin/bash
#
#SBATCH --job-name=dscr_mem
#SBATCH --output=dscr_mem.out
#SBATCH --time=10:00
#SBATCH --mem=100

srun echo "Starting memory allocation"
srun sleep 5
srun ./memalloc 512 15
srun echo "Program completed"
