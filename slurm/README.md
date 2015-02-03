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

* Classes of compute nodes
* Denote ownership
* It's all up to the HPC admins
* How to show partition information

```bash
sinfo
```

##### Node states
* alloc - node is 
```ALLOCATED
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
```bash

/opt/apps/bedtools2-2.19.1/bin/bedtools
```
