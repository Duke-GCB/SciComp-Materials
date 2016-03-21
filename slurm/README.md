---
title: "HPC Introduction"
author: "Darren Boss"
date: "Tuesday, October 10, 2015"
---
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Concepts covered](#concepts-covered)
- [Cluster basics](#cluster-basics)
  - [What are some of reasons to access a remote computer system?](#what-are-some-of-reasons-to-access-a-remote-computer-system)
  - [What does a cluster look like?](#what-does-a-cluster-look-like)
- [Filesystems and Storage](#filesystems-and-storage)
- [Using & installing software](#using-&-installing-software)
  - [Choosing the proper resources for your job For both foreground and](#choosing-the-proper-resources-for-your-job-for-both-foreground-and)
    - [Time This is determined by test runs that you do on your code during an](#time-this-is-determined-by-test-runs-that-you-do-on-your-code-during-an)
    - [Memory: We recommend that you check the software docs for memory](#memory-we-recommend-that-you-check-the-software-docs-for-memory)
    - [# of Cores](#-of-cores)
    - [# of Nodes](#-of-nodes)
    - [Partitions (Queues)](#partitions-queues)
  - [Creating submission scripts](#creating-submission-scripts)
  - [Example batch script (SLURM)](#example-batch-script-slurm)
    - [JOB STATE CODES ```bash squeue Jobs  typically  pass  through  several](#job-state-codes-bash-squeue-jobs--typically--pass--through--several)
    - [Node states](#node-states)
  - [Managing jobs and getting job information](#managing-jobs-and-getting-job-information)
      - [Running a job array](#running-a-job-array)
      - [Job failures](#job-failures)
      - [How to get help and training](#how-to-get-help-and-training)
    - [Other resources](#other-resources)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts covered
* Why use a cluster?
* Copying data to a remote server
* Using ssh to connect to remote computers
* Interacting with the job scheduler
* Understand batch script options how how to submit jobs

Note: A large portion of this material was taken from a Data Carpentry workshop
taught at a Harvard FAS Research Computing Genomics workshop last year.
Course materials can be found at the Github repository at
[https://github.com/fasrc/2015-08-19-HU_FASRC](https://github.com/fasrc/2015-08-19-HU_FASRC)

## Cluster basics
Clusters, are often referred to as  high-performance computing (HPC) or
high-throughput computing systems. Resources also include other high-end compute
systems such as distributed databases, large-scale fileystems, and
software-defined networks.

### What are some of reasons to access a remote computer system?

* Your computer does not have enough resources to run the desired analysis.
  *E.g.* memory, processors, disk space, or network bandwidth.
* You want to produce results faster than your computer can.
* You want to use your computer for tasks other then running your analysis.
* You cannot install software in your computer. That is, the application does
  not have support for your operating system, conflicts with other existing
  applications, or software licensing does not allow for installation on
  personal laptops.

### What does a cluster look like?

“High Performance Computing most generally refers to the practice of aggregating
computing power in a way that delivers much higher performance than one could
get out of a typical desktop computer or workstation in order to solve large
problems in science, engineering, or business.”
--http://insidehpc.com/hpc-basic-training/what-is-hpc/

Clusters are simply a grouping of computers with the same components (RAM, disk,
processors/cores, and networking cards) as those in your desktop or laptop, but
with more umph! and are networked with high-speed interconnect that can be
accessed (indirectly) through software, the scheduler, that manages simultaneous
execution of jobs, or analyses, by multiple persons.

![Overview of a compute cluster](images/cluster-generic.png)

The user accesses the compute cluster through one or more login nodes, and
submits jobs to the scheduler, which will dispatch to and collect the completed
work from the compute nodes. Frequently, clusters have shared disks, or
filesystems, of various flavors where you can store your data, programs, and use
for in-job execution (working or scratch areas)

**Exercises**
* ssh into the DSCR, using the dscr-slogin-02.oit.duke.edu login node
* Use the scheduler command `sinfo` to inspect your local cluster. Confer with
  your neighbor. What is going on here?
* Try using the `sinfo --long` command. Any more insights?
* Make note of how much memory and cpu core are on the login node
  * Command to count of number of cpu cores is `nproc` and querying the amount
    of memory is `free -g`

## Filesystems and Storage

What is a filesystem?  Storage on most compute systems is not what and where you
think they are! Physical disks are bundled together into a virtual volume; this
virtual volume may represent one filesystem, or may be divided up, or
partitioned, into multiple filesystems. And your directories then reside within
one of these fileystems. Filesystems are accessed over the network through mount
points.

There are often multiple storage/filesystems options available for you to do
your work. The most common are:
* home: where you land when you first login
* shared (lab): a directory on the network
* "working" directories, like SCRATCH or TEMP

Home folders are great for keeping information specific to your account, your
workflows, and your environment. Typically, these are backed up and are limited
in space. Note that these are usually appropriate for small amounts of work --
up to 10 or so jobs -- as these are on filesystems with large #s of other
accounts on low-throughput/low bandwidth disk infrastructure.

Shared (lab) systems are typically the same, though may vary from site to site
and will vary in size, backup strategy, and usage. These are also usually
appropriate for small amounts of work -- up to 10 or so jobs -- as these are on
filesystems with large #s of other accounts on low-throughput/low bandwidth disk
infrastructure.

"Working directories, often called TEMP, SCRATCH, or WORK, are often
specialized, high-availability & high-speed systems designed especially for
large volumes of read and write operations found on HPC/HTC systems. Often times
this is not backed and files are deleted after an aged period of time "

* On the DCC
  * /dscrhome - where your home directory is located. 250GB group quota and two
    week backup.
  * /work - 100TB total volume size, not backed up and subject to file purges
    based based on the file age and/or utilization levels
  * /scratch - local to compute node and varies in size based on compute node
    hardware

* On HARDAC
  * All home directories and everything under /data is considered scratch
  * No automatic purge but there are 5GB quotas on individual home directories
    and 5TB for lab shares
  * The scratch space is .5PB and consists of 240 hard drives grouped in to 24
    raid groups
  * No primary data should be kept on the cluster file system, data needs to be
    staged in for analysis and copied off the system to systems that are backed
    up

**Exercises**
* Fork the materials repository to your own github account
  * Repository repo url is
    [https://github.com/Duke-GCB/SciComp-Materials.git](https://github.com/Duke-GCB/SciComp-Materials.git)
* Clone the repo to your local computer
* Change into the repository materials directory
* Cd into the directory containing the bed files
* Copy a single bedRnaElements file to your home directory on the DSCR
  * `scp CellCiptapContigs.bedRnaElements netid@dscr-slogin-02.oit.duke.edu:`
* In another shell, log into the DSCR
  * `ssh netid@dscr-slogin-01.oit.duke.edu`
* We copied the file to one server but it exists on the other server as well,
  how is this possible?
* What filesystem are you currently on? Can you figure that out?
* Use the `df .` command or `df -h .` for human readable output.
* Change to /work and /datacommons/netscratch directory and try the
  command again
* On your local system, cd to the directory one level up from where the bed
  files are located
* Perform a recursive scp of the cshl_rna_seq directory
  * scp -r cshl_rna_seq netid@dscr-slogin-01.oit.duke.edu
* Show an rsync example
* rsync -a cshl_rna_seq dtb17@dscr-slogin-01.oit.duke.edu:
* show verbose and dry-run as well
* use curl and wget to download a file from [https://raw.githubusercontent.com/Duke-GCB/SciComp-Materials/master/materials/cshl_r](https://raw.githubusercontent.com/Duke-GCB/SciComp-Materials/master/materials/cshl_r)
  * `wget https://raw.githubusercontent.com/Duke-GCB/SciComp-Materials/master/materials/cshl_rna_seq/CellCiptapContigs.bedRnaElements

  * `curl -O https://raw.githubusercontent.com/Duke-GCB/SciComp-Materials/master/materials/cshl_rna_seq/CellCiptapContigs.bedRnaElements

## Using & installing software 

On the DSCR you will find commonly used scientific applications installed under
/opt/apps. On other clusters tools like *Lmod* are commonly used to allow access
to applications.

```bash python --version
   module avail
   module load Anaconda
   python --version
   module purge
   python --version ```

*For Perl & Python module or R packages*, we encourage you to set up directories
in your home and/or lab folder for installing your own copies locally.

*If software you need is not installed*, we encourage you to do local installs
in your home or lab folder for bleeding-edge releases, software you are testing,
or software used only by your lab.

Depending on the nature of the software and the experience of the software
developers that created the software distribution it can be a very time
consuming procedure to deploy software on the cluster.

**Exercises**

* The Samtools version on the DSCR is lacking a feature that you want to use
* Download the Samtools source code to your home directory
* Don't download it to your laptop first, use the wget or curl command to
  download it directly to the cluster
* Extract the source tarball
  * `tar xvfj samtools-1.2.tar.bz2`
* Compiling source code and be a resource intensive process so lets all by good
  citizens and extract and compile the source code on a compute node of the
  cluster

## Working with the scheduler

As mentioned before, the scheduler is responsible for listening to your job
requests, then finding the proper compute node that meets your job's resource
requirements -- RAM, # cores, time, etc -- dispatches the job to that compute
node, collects info about the completed work, and stores information about your
job. If you've asked it to do so, it will even notify you about the status of
your job (e.g. begin, end, fail, etc).

### Running & submitting jobs

There are two ways to run jobs on a cluster. One, usually done at the start, is
to get an interactive/foreground session on a compute node. This looks and
behaves exactly as when you first log into a compute cluster, on a login node,
but the work is being done a compute node, a worker node on the cluster. This is
usually a best practice technique, and should be done for all work that will tie
up resources (e.g. CPU- or memory-intensive tasks).

To get an interactive session, you issue the `srun` command with the appropriate
parameters for requesting the resources you require. For example:

```bash srun --pty --mem 1000 /bin/bash ```

This command requests from the scheduler a foreground/interactive job with the
following resources:

```bash
--pty           # a parameter specific for the srun command for bash sessions
--mem 1000      # memory request, in MB
/bin/bash       # the program we want to run, which is the bash shell
```

Two additional, optional, parameters were left out; as such, SLURM will give us
the defaults:
```bash
-n 1            # how many cores (CPUs) we want (default = 1)
-N 1            # how many nodes we want the cores on (not needed, as we're
                # getting one core; required otherwise)
```

The other method of running jobs on the cluster is by running a job in batch,
using the `sbatch` command. On rare occasion, you can use this just like the
`srun` example, to run a simple command:

```bash
sbatch --mem=1000 --wrap="uname -a; free -g; nproc"
```

**Exercise**
* Submit a batch job to extract the samtools archive
  * The command to extract bz2 archives in the current directory is `tar xvfj
    filename`
* Start an interactive job and follow the instructions on the htslib website on
  how to compile and install samtools

The other way is to create a batch submission script file, which has these
parameters embedded inside, and submit your script to the scheduler:

```bash
sbatch my_batch_script.sh
```

In all cases, the scheduler will return to you a jobID, a unique ID for your job
that you can use to get info or control at that time, or refer to it
historically.

### Choosing the proper resources for your job For both foreground and
background submissions, you are requesting resources from the scheduler to run
your job. These are:
* time
* memory
* # of cores (CPUs)
* # of nodes
* (sort of) queue or group of machines to use

Choosing resources is like playing a game with the scheduler: You want to
request enough to get your job completed without failure, But request too much:
your job is ‘bigger’ and thus harder to schedule. Request too little: if your
job goes over that requested, it is killed. So you want to get it just right,
and pad a little for wiggle room.

Another way to think of 'reserving' a compute node for you job is like making a
reservation at a restaurant:
* if you bring more guests to your dinner, there won't be room at the
  restaurant, but the wait staff may try to fit them in. If so, things will be
  more crowded and the kitchen (and the whole restaurant) may slow down
  dramatically
* if you bring fewer guests and don't notify the staff in advance, the extra
  seats are wasted; no one else can take the empty places, and the restaurant
  may lose money.

“Never use a piece of bioinformatics software for the first time without looking
to see what command-line options are available and what default parameters are
being used” -- acgt.me · by Keith Bradnam

#### Time
This is determined by test runs that you do on your code during an
interactive session.  Or, if you submit a batch job, over-ask first, check the
amount of time actually needed, then reduce time on later runs.

**Please!** Due to scheduler overhead, bundle commands for minimum of 10 minutes
/ job

#### Memory
We recommend that you check the software docs for memory
requirements. But often times these are not stated, so we can take another
approach. On HARDAC and on the DSCR, each job is allowed 2 GB RAM/core by
default. Try the default via `srun` or `sbatch`. If your job was killed, look at
the log files or immediately with squeue. If it show a memory error, you went
over. Ask for more and try again.

Once the job has finished, ask the scheduler how much RAM was used by using the
`sacct` command to get post-run job info: ```bash sacct -j JOBID
--format=JobID,JobName,ReqMem,MaxRSS,Elapsed  # RAM requested/used!!  ``` The
`ReqMem` field is how much you asked for and `MaxRSS` is how much was actually
used. Now go back and adjust your RAM request in your sbatch command or
submission script.

#### # of Cores
This is determined by your software, how anxious you are to get
the work done, and how well your code scales. **NOTE! Throwing more cores at a
job does not make it run faster!** This is often a newbie mistake and will waste
compute, making your admin grumpy. Ensure your software can use multiple cores:
Inspect the parameters for your software and look for options such as 'threads',
'processes', 'cpus'; this will often indicate that it has been parallelized.
Then run test jobs to see how well it performs with multiple cores, inching
slowing from 1 to 2, 4, 8, etc, assessing the decrease in time for the job run
as you increase cores. Programs often do not scale well -- it's important to
understand this so you can choose the appropriate number.

#### # of Nodes
For most software in biology, this choice is simple: 1. There
are *very* few biology softare packages capable of running across multiple
nodes. If they are capable, they will mention the use of technology called 'MPI'
or 'openMPI'.

#### Partitions (Queues)
Partitions, or queue, are a grouping of computer to run a certain profile or
jobs. Historically, partitions on the DSCR were used to give priority access to
those schools, institutes and centers that paid into buying hardware for the
DSCR. This is slowly opening up and most PIs should be able to get time on the
DSCR now.

HARDAC used to have high and low memory partitions but this introduced a
unnessesary barrier in scheduling jobs so it was removed.

### Creating submission scripts
When creating submission scripts, use your favorite text editor and include the
following sections:

**Required**
* shebang, or shell invocation
* Any sofware or module loads (HARDAC only)
* actual commands to do work

**Recommended**
* Partition to submit to (comma separated)
* job name
* # of cores
* # of nodes
* amount of time
* amount of memory
* STDOUT file
* STDERR file

**Optional**
* what mail notifications you want, if any
* email notification address (or text msg email address if you want an SMS
  alert!)

All the scheduler directives need to be at the start of the file, then your
module/software loads, and then your actual job commands.

### Example batch script (SLURM)
The following is an example submission script for an example `bedtools` run,
which is a single-core program. See
[http://bedtools.readthedocs.org/en/latest/content/tools/merge.html](http://bedtools.readthedocs.org/en/latest/content/tools/merge.html)
and
[http://quinlanlab.org/tutorials/bedtools/bedtools.html#bedtools-merge](http://quinlanlab.org/tutorials/bedtools/bedtools.html#bedtools-merge)
for an explanation of the bedtools merge command:

```bash
#!/bin/bash
#
#SBATCH -p common              # Partition to submit to (comma separated)
#SBATCH -J gcb_bedtools        # Job name #SBATCH -n 1
# Number of cores #SBATCH -N 1 # Ensure that all cores are on one machine
#SBATCH -t 0-0:10              # Runtime in D-HH:MM (or use minutes)
#SBATCH --mem 1000             # Memory in MB
#SBATCH -o bedtools_%j.out     # File for STDOUT (with jobid = %j)
#SBATCH -e bedtools_%j.err     # File for STDERR (with jobid = %j)
#SBATCH --mail-type=ALL        # Type of email notification: BEGIN,END,FAIL,ALL
#SBATCH --mail-user=EMAIL@duke.edu  # Email where notifications will be sent
#Your actual work goes after this line
```
The bedtools executatble is located
at /opt/apps/sdg/nextgen/tools/BEDTools-Version-2.16.2/bin/bedtools on the DSCR.
**Exercises**
* Clone the materials git repository from your github account on the DSCR
* In an interactive session
  * Sort an import bed file using the suggestions for using sort in the above
    tutorial
  * Run bedtools merge on the sorted bedfile
* Combine the above slrum template with the command and submit the job as a
  batch job
  * There is a template in the slurm folder in the git repository you just
    checked out
  * Don't forget to enter your email address in the script

#### JOB STATE CODES
```bash
squeue Jobs  typically  pass  through  several
states  in the course of their execution.   The  typical  states  are  PENDING,
RUNNING,   SUSPENDED, COMPLETING, and COMPLETED.  An explanation of each state
follows.

       CA  CANCELLED       Job  was explicitly cancelled by the user or system
       administrator.  The job may or may  not  have  been initiated.

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

#### Node states

```bash
sinfo
ALLOCATED The node has been allocated to one or more jobs.
COMPLETING All jobs associated with this node are in the process of COMPLETING.
This node state will be removed when all of the job's processes have terminated
and the SLURM epilog program (if any) has terminated. See the Epilog parameter
description in the slurm.conf man page for more information.
DOWN The node is
unavailable for use. SLURM can automatically place nodes in this state if some
failure occurs. System administrators may also explicitly place nodes in this
state. If a node resumes normal operation, SLURM can automatically return it to
service. See the ReturnToService and SlurmdTimeout parameter descriptions in the
slurm.conf(5) man page for more information.
DRAINED The node is unavailable
for use per system administrator request. See the update node command in the
scontrol(1) man page or the slurm.conf(5) man page for more information.
DRAINING The node is currently executing a job, but will not be allocated to
additional jobs. The node state will be changed to state DRAINED when the last
job on it completes. Nodes enter this state per system administrator request.
See the update node command in the scontrol(1) man page or the slurm.conf(5) man
page for more information.
FAIL The node is expected to fail soon and is
unavailable for use per system administrator request. See the update node
command in the scontrol(1) man page or the slurm.conf(5) man page for more
information.
FAILING The node is currently executing a job, but is expected to
fail soon and is unavailable for use per system administrator request. See the
update node command in the scontrol(1) man page or the slurm.conf(5) man page
for more information.
IDLE The node is not allocated to any jobs and is
available for use.
MAINT The node is currently in a reservation with a flag
value of "maintainence".
UNKNOWN The SLURM controller has just started and the
node's state has not yet been determined.
```
### Managing jobs and getting job information

There are several commands that you can use to control and get info about your
jobs:

`scancel` will become your friend! At some point, you'll fire off one or more
jobs, and realize you've made a mistake. (What? You don't make them? Then you
can forget about this command) Here are a few examples of `scancel` in action:

```bash
scancel JOBID                                       # specific job
scancel -u dtb17                                    # ALL my jobs
scancel -u dtb17 -J many_blast_jobs                 # named jobs
scancel -u dtb17 -p gcb                             # ALL in partition
```

`squeue` will give you pending (to be done), running, and
recently completed job info. Some examples:

```bash
squeue -u dtb17                                     # jobs for dtb17
squeue -u dtb17 --states=R | wc –l                  # # of Running jobs
```

`sacct` will give you current and historical information, since time began or
you were an HPC-infant, whichever came first. More examples:

```bash
sacct -u dtb17                                      # jobs for dtb17
sacct -u dtb17 -p common --starttime=9/1/15         # same+common partition
sacct -j JOBID --format=JobID,JobName,ReqMem,MaxRSS,Elapsed # RAM requested & used!!
```

* Run `dscr_mem_kill.sbatch`
* Lines with and without srun
* Examine exit codes
* 0 is normal and anything else is not
* Kill signals
* SIGKILL is 9 and SIGTERM is 15

##### Running a job array
```bash
#!/bin/bash
#
#SBATCH --output=bedtools_%A_%a.out
#SBATCH --error=bedtools_%A_%a.err # Standard error
#SBATCH --job-name=bedtools_array
#SBATCH --time=10:00
#SBATCH --mem=1000
#SBATCH --array=0-4

inputs=(CellCiptapContigs.bedRnaElements CellContigs.bedRnaElements CytosolCiptapContigs.bedRnaElements CytosolContigs.bedRnaElements NucleusContigs.bedRnaElements)

bed_file=${inputs[$TASK_ID]} sorted_bed_file=$(basename $bed_file).sort.bed
srun sleep 30
srun sort -k1,1 -k2,2n cshl_rna_seq/$bed_file > cshl_rna_seq/$sorted_bed_file
srun /opt/apps/sdg/nextgen/tools/BEDTools-Version-2.16.2/bin/bedtools merge -i cshl_rna_seq/$sorted_bed_file
```

##### Job failures
* Emails on job failure
```bash
#SBATCH --mail-user=darren.boss@duke.edu
#SBATCH --mail-type=FAIL
```
* Mail-type can be set to BEGIN, END, FAIL, REQUEUE, and ALL
* Run memory job

##### How to get help and training
* If you don't have access to the DCC, check the point of contact list and
  request access if you are able
  [https://wiki.duke.edu/display/SCSC/DSCR+Point+of+Contact+list](https://wiki.duke.edu/display/SCSC/DSCR+Point+of+Contact+list)
* make sure to always give your netid, jobid and any error messages when
* for DCC help contact help@oit.duke.edu and make sure to indicate you are
  requesting assistance on the DCC
* HARDAC support email gcb-help@duke.edu
* Training at Duke
  [https://training.oit.duke.edu/enroll/index.php/public_research](https://training.oit.duke.edu/enroll/index.php/public_research)
* Innovation CO-LAB at Duke
  [https://training.oit.duke.edu/enroll/index.php/public_colab](https://training.oit.duke.edu/enroll/index.php/public_colab)
* Harvard Reseach Computing has some excellent documentation on effective use of
  SLURM at
  [https://rc.fas.harvard.edu/resources/documentation/](https://rc.fas.harvard.edu/resources/documentation/)

#### Other resources
* HPC offerings:
  * DCC: https://rc.duke.edu/the-duke-compute-cluster/
  * HARDAC: https://wiki.duke.edu/display/HAR/Welcome+to+HARDAC
  * XSEDE: https://www.xsede.org/high-performance-computing
* Cloud computing offerings:
  * VM Manage [https://vm-manage.oit.duke.edu/](https://vm-manage.oit.duke.edu/)
  * Amazon EC2: http://aws.amazon.com/ec2/
  * Microsoft Azure: https://azure.microsoft.com/en-us/
  * Google Cloud Platform: https://cloud.google.com/
  * CyVerse Atmosphere: http://www.cyverse.org/atmosphere
