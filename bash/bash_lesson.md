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
     
If we wanted to ask the same question for all of the files, we can use a **wildcard** to expand:

	$ ls -lh wg*
	$ wc -l wg*
	
The wildcard works at any position in the filename:

    $ wc -l *.bed*
        
These are big files! What if wanted a small subsection of the file (for example, to do a test analysis):

	$ head -n 100 wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements

The bed files are formatted with multiple columns. We can filter out specific columns using the `cut` command. Let's look at the man page for `cut`:

    $ man cut

There are three options that we need to provide: the fields to cut, the character (delimiter) that separates columns and the input file. The default delimiter is TAB, which is what we have, so we can ignore that option. 

    $ cut -f 1-3  wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements

## Extracting subsets of a file

To save this output to a file, we can **redirect** the output into a file rather than to the screen:

	$ cut -f 1-3 wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements > small.bed

***Excercise*** : Create a small sample file named "sample_file.bed", including the first 200 lines and all columns except 4th column. *Hint*: This will take two separate steps and involve creating a temporary file. 

We've introduced **wildcards** to operate on files that match a patters and **redirection** to save output to a file instead of the screen. The final concept in this section is combining commands using **pipes**.

The power of the shell comes from the vast number of commands that do a small thing really well and the fact that we can combine these small programs into pipelines that do complex things. 

Let's check the number of chromosomes in the file. The first column contains the chromosomes:

	$ cut -f1 wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements

The `uniq` command will print out unique elements in the input. We could save column 1 to a file and then run uniq, but it is shorter to simply *pipe* the output from the first command as input into the second command:

	$ cut -f1 wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements | uniq

The `uniq` command looks for runs of identical elements. Let's `sort` the list first before running `uniq`. Bash has a command for that, and we can chain together multiple commands using `|`. 

	$ cut -f1 wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements | sort | uniq 


## Finding things in files and directories 

Use `grep` to find information about specific chromosomes in the file. We can output the contents of the file to the screen, and then search that output for lines that match chromosome X.

	$ cat wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements | grep chrX

***Exercise***: Do the same for chromosome 1. What happens?

We can use more complex patterns with `grep` (and other tools) by using *regular expressions*. For example, to find both chromosome X and Y:

	$ cat wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements | grep chr[XY]

If we want to be sure that we are ignoring lines that might  
use find to locate all of the .csv files in your home directory
 
use find + grep to find all of the python files that use the BeautifulSoup library

## Loops

Perhaps we want to extract only the information for the X chromosome from every file. We therefore want to repeat the same command multiple times with different input. 

	$ for i in 1 2 3 B B 4
	> do
	> echo $i
	> done

We have created a *variable* i and a list [1,2,3,4]. For each element in the list, we assign i=element_in_list and then do something with that variable (in this case, simply print it to the screen using `echo`). Note that we use `$` to refer to a variable once we have defined it.

Use the up arrow to see how bash represents a loop on one line. 

	$ for c in X Y
	> do
	> echo $c
	> done

We can modify the body of the loop (what's between `do` and `done`) to run a different command, or multiple commands, on each file. 

	$ for c in X Y
	> do
	> echo $c
	> echo chromosome$c.bed
	> head n -1 wgEncodeCshlShortRnaSeqA549CellContigs.bedRnaElements
	> done

***Exercise***: Modify the loop to use the `grep` example from above to print the data from the X and Y chromosomes to two new files. 

## Putting actions in scripts

Copy that last command to the clipboard. Then, create and open a new text file. The `nano` editor is a simple text editor that allows you to edit files from the bash shell, without opening up a graphical editor.

	$ nano get_X_data.sh

Run the script using:

	$ bash get_X_data.sh

If we wanted to do the same thing for another input file, we would need to edit the script and change the filename. What if we had hundreds or thousands of input files? We can pass the filename into the script as an *argument*:

	$ bash get_X_data.sh my_input_file.bed

There are various ways to access the command line arguments. We are going to show you the simplest way, but one that doesn't do any error checking or allow for fancy features. In a script:

   ```
   echo $0  # prints the name of the script
   echo $1  # prints the first argument
   echo $2  # prints the second argument
   ```
   
The following script will take the filename from the command line:

```
inputfile=$1
for c in X Y
do 
        echo chrosome$c
        echo intputfile: $inputfile
        echo outputfile: $inputfile.chr$c
done
```

***Exercise***: Modify this script to print the data for the specified chromsome from the input file to the output file