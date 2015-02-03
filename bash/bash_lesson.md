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

Navigate into the `/GCB-Academy-2015-02-05/bash/cshl_rna_seq` directory. There are some .bed files here. When we have a directory of files, we probably want to explore then a little. Picking one of the files:

    $ cat wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements

Well, that all went by pretty fast. How would we browse through the file starting from the top?

    $ less wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements
    
or just look at the top?

    $ head wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements
    
How big is this file? We can use the `-l` (long format) and `-h` (human readable) flags for `ls`:
 
    $ ls -lh wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements
    
How many lines? The `wc` command gives us words, characters, and lines in a file. The `-l` flag gives us only lines: 

     $ wc -l wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements
     
If we wanted to ask the same question for all of the files, we can use the wildcard to expand:

	$ ls -lh wg*
	$ wc -l wg*
	
The wildcard works at any position in the filename:

    $ wc -l *.bed*
    
What if wanted a small subsection of the file (for example, to do a test analysis):

    $ head -n 100 wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements
    
To save this to a file, we can redirect the output into a file rather than to the screen:

    $ head -n 100 wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements > small.bed
    
The bed files are formatted with multiple columns. In addition to filtering rows, we can also filter columns. The `cut` command can extract only specific columns. Let's look at the man page for `cut`:

    $ man cut

There are three options that we need to provide: the fields to cut, the character (delimiter) that separates columns and the input file. The default delimiter is TAB, which is what we have, so we can ignore that option. 

   $ cut -f 1-3  wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements

**Excercise** : Create a small sample file named "sample_file.bed"of just the first 200 lines, including everything except the 4th column.

## Finding things in files and directories 

use grep to find information about specific chromosomes in the file

use find to locate all of the .csv files in your home directory
 
use find + grep to find all of the python files that use the BeautifulSoup library

## Loops
use a loop to create a separate file for each chromosome in the input file, using bash and redirection







