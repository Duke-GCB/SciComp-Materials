#!/bin/bash
#
#SBATCH --job-name=dscr_mem
#SBATCH --output=dscr_mem_%j.out
#SBATCH --time=10:00
#SBATCH --mem=100

srun echo "Starting memory allocation"
srun sleep 5
srun ~/bin/memalloc 512 15
srun echo "Program completed"
