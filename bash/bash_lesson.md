This lesson instroduces intermediate bash skills to learners who have some familiarity with the shell. 

# Concepts to cover

* contents of files: head, tail, cut
* using wildcards and simple regex for pattern matching
* redirecting ouput
* pipes
* finding things: in files (grep) and across filesystem (find)
* writing and running a simple bash script
* moving data between computers: scp and rsync
* file permissions
* good practices for organizing files and directories

# Assumptions
We assume that learners:


1. understand the difference between a command-line interface and a graphical user interface
1. can open a bash shell on their computer
1. understand paths and the structure of the filesystem
1. can move and copy files between directories

# Lessons
## Setup
1. Download the [repository for the bash and HPC lessons](https://github.com/Duke-GCB/GCB-Academy-2015-02-05/archive/master.zip). 
3. Move that file into a directory where you want the files for this course. 
4. Unzip the file:

For some reason I need to put text here in order for Markdown to turn the next line into code

     $ unzip GCB-Academy-2015-02-05-master.zip


## Examining the contents of files

Navigate into the /GCB-Academy-2015-02-05/bash/cshl_rna_seq directory. There are some .bed files here. When we have a directory of files, we probably want to explore then a little. 









