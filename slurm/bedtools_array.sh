#!/bin/bash
#
#SBATCH --output=bedtools_%A_%a.out
#SBATCH --error=bedtools_%A_%a.err # Standard error
#SBATCH --job-name=bedtools_array
#SBATCH --time=10:00
#SBATCH --mem=1000
#SBATCH --array=0-4

FILES=($(ls -1 cshl_rna_seq/*bed*))
bed_file=${FILES[$SLURM_ARRAY_TASK_ID]}
sorted_bed_file=$(basename $bed_file).sort.bed
srun sleep 30
srun sort -k1,1 -k2,2n $bed_file > $sorted_bed_file
srun /opt/apps/sdg/nextgen/tools/BEDTools-Version-2.16.2/bin/bedtools merge -i $sorted_bed_file
