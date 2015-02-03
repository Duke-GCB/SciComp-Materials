# Job and data staging for HPC

## Overview
Introduction to using SLURM (Simple Linux Utility for Resource Management)

### SLURM overview

#### Head node

* The computer where you submit jobs and query the state of the cluster
* Never run any applications on the head node of the cluster
* Memory and cpu core limited (dscr-slogin-01 and dscr-slogin-02 have 8GB memory and 2 cpu cores)

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

##### Partitions

```bash
/opt/apps/bedtools2-2.19.1/bin/bedtools
```
