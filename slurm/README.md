This lesson introduces the concepts of data staging and job execution on cluster using SLURM.
# Concepts covered

* Copying data between remote servers
* Using ssh to connect to remote computers
* Command line tools for downloading files
* Explaining the difference between head and compute nodes
* Viewing the job queue and narrowing the focus to only jobs the user has submitted
* Creating and submitting jobs to the cluster
* Viewing the status of running jobs
* Cancelling jobs
* Job arrays

# Lessons

## Copy files over ssh

* Log into the DSCR (dscr-slogin-02.oit.duke.edu)
* Log into the vm in another terminal window
* Cd to the directory where the bed files are located
* Perform a recursive scp initiated from the dscr
* Remove the files and directory
* Perform a recursive scp initiated from the vm
* Remove the .txt files
* Show an rsync example
* rsync -a cshl_rna_seq dtb17@dscr-slogin-02.oit.duke.edu:
* show verbose and dry-run as well
* use curl and wget to download a file from

## Overview
Introduction to using SLURM (Simple Linux Utility for Resource Management)

### SLURM overview

#### Head node

* The computer where you submit jobs and query the state of the cluster
* Never run any applications on the head node of the cluster
* Memory and cpu core limited (dscr-slogin-01 and dscr-slogin-02 have 8GB memory and 2 cpu cores)
* Talk about difference between the DSCR and HARDAC

```bash
netid@dscr-slogin-01  ~ $ nproc
netid@dscr-slogin-01  ~ $ free -m
netid@dscr-slogin-01  ~ $ squeue |less
netid@dscr-slogin-01  ~ $ squeue -u userid
```
##### JOB STATE CODES
```bash
Jobs  typically  pass  through  several  states  in the course of their
execution.   The  typical  states  are  PENDING,  RUNNING,   SUSPENDED,
COMPLETING, and COMPLETED.  An explanation of each state follows.

       CA  CANCELLED       Job  was explicitly cancelled by the user or system
                           administrator.  The job may or may  not  have  been
                           initiated.

       CD  COMPLETED       Job has terminated all processes on all nodes.

       CF  CONFIGURING     Job  has  been allocated resources, but are waiting
                           for them to become ready for use (e.g. booting).

       CG  COMPLETING      Job is in the process of completing. Some processes
                           on some nodes may still be active.

       F   FAILED          Job  terminated  with  non-zero  exit code or other
                           failure condition.

       NF  NODE_FAIL       Job terminated  due  to  failure  of  one  or  more
                           allocated nodes.

       PD  PENDING         Job is awaiting resource allocation.

       R   RUNNING         Job currently has an allocation.

       S   SUSPENDED       Job  has  an  allocation,  but  execution  has been
                           suspended.

       TO  TIMEOUT         Job terminated upon reaching its time limit.
```

##### Compute nodes

* The computers where the actual processing occurs
* Will have substantially more memory than the head nodes (one of the gcb nodes has 32GB memory and 16 cpu cores)

```bash
netid@dscr-slogin-01  ~ $ srun --pty bash -i
netid@dscr-econ-20 ~ $ nproc
netid@dscr-econ-20 ~ $ free -m
netid@dscr-econ-20 ~ $ exit
netid@dscr-slogin-01 ~ $ srun --mem=256 --pty bash -i
```
```bash
sinfo
```

##### Node states

```bash
   ALLOCATED
    The node has been allocated to one or more jobs. 
   COMPLETING
    All jobs associated with this node are in the process of COMPLETING. This node state will be removed when all of the job's processes have terminated and the SLURM epilog program (if any) has terminated. See the Epilog parameter description in the slurm.conf man page for more information. 
   DOWN
    The node is unavailable for use. SLURM can automatically place nodes in this state if some failure occurs. System administrators may also explicitly place nodes in this state. If a node resumes normal operation, SLURM can automatically return it to service. See the ReturnToService and SlurmdTimeout parameter descriptions in the slurm.conf(5) man page for more information. 
   DRAINED
    The node is unavailable for use per system administrator request. See the update node command in the scontrol(1) man page or the slurm.conf(5) man page for more information. 
   DRAINING
    The node is currently executing a job, but will not be allocated to additional jobs. The node state will be changed to state DRAINED when the last job on it completes. Nodes enter this state per system administrator request. See the update node command in the scontrol(1) man page or the slurm.conf(5) man page for more information. 
   FAIL
    The node is expected to fail soon and is unavailable for use per system administrator request. See the update node command in the scontrol(1) man page or the slurm.conf(5) man page for more information. 
   FAILING
    The node is currently executing a job, but is expected to fail soon and is unavailable for use per system administrator request. See the update node command in the scontrol(1) man page or the slurm.conf(5) man page for more information. 
   IDLE
    The node is not allocated to any jobs and is available for use. 
   MAINT
    The node is currently in a reservation with a flag value of "maintainence". 
   UNKNOWN
    The SLURM controller has just started and the node's state has not yet been determined. 
```

##### Locating software on the cluster

* Explain the different between /usr/bin and executables in /usr/local/bin and /opt

```bash

/opt/apps/bedtools2-2.19.1/bin/bedtools
```
* Using find on /opt
* Explain how to redirect stderr
##### Running an interactive job
* Run bedtools merge
* Show the following page
* http://quinlanlab.org/tutorials/cshl2014/bedtools.html
* Run examples from the merge section
```bash
sort -k1,1 -k2,2n ~/cshl_rna_seq/wgEncodeCshlShortRnaSeqA549CellCiptapContigs.bedRnaElements > ~/cshl_rna_seq/CellCiptapContigs.sort.bed
/opt/apps/bedtools2-2.19.1/bin/bedtools merge -i ~/cshl_rna_seq/CellCiptapContigs.sort.bed 
```
* Check memory usage using sacct
##### Partitions

* Classes of compute nodes
* Denote ownership
* It's all up to the HPC admins
* How to show partition information
* Explain premtion for low priority jobs
* Submit job to a partion you don't have access to

##### Running a batch job
```bash
#!/bin/bash
#
#SBATCH --output=bedtools.out
#SBATCH --error=bedtools.err
#SBATCH --job-name=bedtools
#SBATCH --time=10:00
#SBATCH --mem=200

bed_file=wgEncodeCshlShortRnaSeqA549CellCiptapContigs.bedRnaElements
sorted_bed_file=$(basename $bed_file).sort.bed
srun sleep 30
srun sort -k1,1 -k2,2n ~/cshl_rna_seq/$bed_file > ~/cshl_rna_seq/$sort
ed_bed_file
srun /opt/apps/sdg/nextgen/tools/BEDTools-Version-2.16.2/bin/bedtools 
merge -i ~/cshl_rna_seq/$sorted_bed_file
```
* Check memory use
```bash
sacct -o maxrss -j jobid
```
* Lines with and without srun
* Talk about exit codes
* 0 is normal and anything else is not
* Kill signals
* SIGKILL is 9 and SIGTERM is 15
##### Running a job array
```bash
#!/bin/bash
#
#SBATCH --output=output/bedtools_%A_%a.out
#SBATCH --error=output/bedtools_%A_%a.err # Standard error
#SBATCH --job-name=bedtools_array
#SBATCH --time=10:00
#SBATCH --mem=200
#SBATCH --array=0-4

inputs=(wgEncodeCshlShortRnaSeqA549CellCiptapContigs.bedRnaElements wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements wgEncodeCshlShortRnaSeqA549CytosolCiptapContigs.bedRnaElements wgEncodeCshlShortRnaSeqA549CytosolContigs.bedRnaElements wgEncodeCshlShortRnaSeqA549NucleusContigs.bedRnaElements)

bed_file=${inputs[$TASK_ID]}
sorted_bed_file=$(basename $bed_file).sort.bed
srun sleep 30
srun sort -k1,1 -k2,2n ~/cshl_rna_seq/$bed_file > ~/cshl_rna_seq/$sorted_bed_file
srun /opt/apps/sdg/nextgen/tools/BEDTools-Version-2.16.2/bin/bedtools merge -i ~/cshl_rna_seq/$sorted_bed_file
```
##### Job failures
* Emails on job failure
```bash
#SBATCH --mail-user=darren.boss@duke.edu
#SBATCH --mail-type=FAIL
```
* Mail-type can be set to BEGIN, END, FAIL, REQUEUE, and ALL
* Run memory job
##### Permissions on files
* bitmask
* setgid

##### Multi-threaded applications
* Use the --cpus-per-task option in coordination with the option in the application that requests the number of threads to use

##### How to get help
* make sure to always give your netid, jobid and any error messages
* for DSCR help contact hpc-admins@duke.edu
* for HARDAC support contact gcb-help@duke.edu
* Classes at rc.duke.edu