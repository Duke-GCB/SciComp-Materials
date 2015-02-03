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

             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           1965606     bench DCMbench    ark19  R    3:11:44      1 dscr-symposium-01
   1891510_[23-25]    common runSim_2      tz5 PD       0:00      1 (Resources)
           1888875    common process_      tz5 PD       0:00      1 (Dependency)
           1888876    common createGe      tz5 PD       0:00      1 (Dependency)
           1888877    common seedGen_      tz5 PD       0:00      1 (Dependency)
    1888878_[1-25]    common runSim_2      tz5 PD       0:00      1 (Dependency)
           1888903    common process_      tz5 PD       0:00      1 (Dependency)
           1888904    common createGe      tz5 PD       0:00      1 (Dependency)
           1888905    common seedGen_      tz5 PD       0:00      1 (Dependency)
           1966236    common     T1_1    crr22 PD       0:00      1 (Priority)
           1966237    common     T1_2    crr22 PD       0:00      1 (Priority)
           1966238    common     T1_3    crr22 PD       0:00      1 (Priority)
           1966239    common     T1_4    crr22 PD       0:00      1 (Priority)
           1966240    common     T1_5    crr22 PD       0:00      1 (Priority)
           1549772    common e4z4d_cu    am424 PD       0:00      1 (JobHeldUser)
           1549773    common e4z4d_cu    am424 PD       0:00      1 (JobHeldUser)
           1549774    common e4z4d_cu    am424 PD       0:00      1 (JobHeldUser)
           1549775    common e4z4d_cu    am424 PD       0:00      1 (JobHeldUser)
           1549776    common e4z4d_cu    am424 PD       0:00      1 (JobHeldUser)
           1549781    common e4z4d_cu    am424 PD       0:00      1 (JobHeldUser)
        1015214_76    common runmatla    tangn  R 12-10:43:41      1 dscr-gcb-25
           1038688    common clump.sh    all45  R 22-19:39:59      1 dscr-core-09
           1038697    common clump.sh    all45  R 19-16:07:21      1 dscr-compeb-03
            175394    common run_mcmc     hy39  R 82-02:51:43      1 dscr-compeb-12
            175395    common run_mcmc     hy39  R 82-02:51:43      1 dscr-compeb-12
           1099600    common structur    all45  R 19-22:21:48      1 dscr-gcb-35
           1959113    common  s6_19Tr    hl158  R   12:03:21      1 dscr-compeb-04
           1955299    common  s5_21Tr    hl158  R   20:56:13      1 dscr-econ-23
           1959111    common  s6_11Tr    hl158  R    7:36:36      1 dscr-compeb-01
           1966258    common trimmoma     nd28  R    1:12:36      1 dscr-gcb-17
           1966257    common trimmoma     nd28  R    1:12:57      1 dscr-warren-06
           1966252    common trimmoma     nd28  R    1:26:54      1 dscr-neuro-08
           1074612    common sspy_sli    kec30  R 14-15:39:04      1 dscr-gcb-30
        1016302_82    common runmatla    tangn  R 22-12:59:07      1 dscr-gcb-13
        1016302_85    common runmatla    tangn  R 12-05:49:33      1 dscr-gcb-31
        1016302_95    common runmatla    tangn  R 12-07:57:38      1 dscr-gcb-57
        1966190_32    common JobArray  atsweet  R    1:12:30      1 dscr-nescent-24
        1966190_31    common JobArray  atsweet  R    1:13:01      1 dscr-nescent-24
        1966190_30    common JobArray  atsweet  R    1:15:05      1 dscr-nescent-27
        1966190_29    common JobArray  atsweet  R      59:12      1 dscr-compeb-02
       1965940_231    common cb1.fp.d     zm14  R    1:22:40      1 dscr-dailabs-07
         1170111_3    common doCovers    cjt16  S 13-13:09:11      1 dscr-harerlab-03
        1016302_89    common runmatla    tangn  S 1-15:20:12      1 dscr-dbchem-06
        1186059_84    common doCovers    cjt16  S 13-10:04:57      1 dscr-compeb-17
           1944283    common   qsub.q    jc456  S   19:14:08      1 dscr-compeb-01
        1888850_19    common runSim_2      tz5  S       0:30      1 dscr-pcharbon-04
           1966726  harerlab   python    acd16  R       9:49      1 dscr-harerlab-01
           1966727  harerlab   python    acd16  R       9:49      1 dscr-harerlab-01
           1966725  harerlab   python    acd16  R       9:50      1 dscr-harerlab-02
           1966722  harerlab   python    acd16  R       9:51      1 dscr-harerlab-02
           1966723  harerlab   python    acd16  R       9:51      1 dscr-harerlab-02
           1966724  harerlab   python    acd16  R       9:51      1 dscr-harerlab-02
           1966720  harerlab   python    acd16  R       9:54      1 dscr-harerlab-01
           1966721  harerlab   python    acd16  R       9:54      1 dscr-harerlab-02

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
