This lesson introduces intermediate bash skills to learners who have some familiarity with the shell.

# Concepts covered

* exploring the contents of files using basic bash commands
* using wildcards and simple regex for pattern matching
* redirecting ouput
* using pipe to chain commands together
* finding using grep and simple regex
* writing and running a simple bash script
* connecting to a different computer using ssh
* moving data between computers: scp

# Assumptions
We assume that learners:

1. understand the difference between a command-line interface and a graphical user interface
1. can open a bash shell on their computer
1. understand paths and the structure of the filesystem
1. can move and copy files between directories

# Lessons
## Setup
1. Download the [data files for the lessons](http://tiny.cc/gcb-data).
2. Create a directory for the course: `mkdir GCB-Academy-2015`
3. Move that file into a directory where you want the files for this course.
4. Unzip the file: `unzip GCB-Academy-2015-02-05-master.zip`


## Examining the contents of files

Navigate into the `/GCB-Academy-2015-02-05/cshl_rna_seq` directory.  There are some .bed files here. When we have a directory of files, we probably want to explore then a little. Picking one of the files:

    $ cat CellContigs.bedRnaElements

Well, that all went by pretty fast. How would we browse through the file starting from the top?

    $ less CellContigs.bedRnaElements

Use `q` to quit less. We can also just look at the top of the file:

    $ head CellContigs.bedRnaElements

How big is this file? We can use the `-l` (long format) and `-h` (human readable) flags for `ls`:

    $ ls -lh CellContigs.bedRnaElements

How many lines? The `wc` command gives us words, characters, and lines in a file. The `-l` flag gives us only lines:

     $ wc -l CellContigs.bedRnaElements

If we wanted to ask the same question for all of the files, we can use a **wildcard** to expand:

	$ ls -lh wg*
	$ wc -l wg*

The wildcard works at any position in the filename:

    $ wc -l *.bed*

These are big files! What if wanted a small subsection of the file (for example, to do a test analysis):

	$ head -n 100 CellContigs.bedRnaElements

The bed files are formatted with multiple columns. We can filter out specific columns using the `cut` command. Let's look at the man page for `cut`:

    $ man cut

There are three options that we need to provide: the fields to cut, the character (delimiter) that separates columns and the input file. The default delimiter is TAB, which is what we have, so we can ignore that option.

    $ cut -f 1-3  CellContigs.bedRnaElements

## Extracting subsets of a file

To save this output to a file, we can **redirect** the output into a file rather than to the screen:

	$ cut -f 1-3 CellContigs.bedRnaElements > small.bed

***Exercise*** : Create a small sample file named "sample\_file.bed", including the first 200 lines and all columns except 4th column. *Hint*: This will take two separate steps and involve creating a temporary file. Also, the `history` command might be useful.

We've introduced **wildcards** to operate on files that match a patters and **redirection** to save output to a file instead of the screen. The final concept in this section is combining commands using **pipes**.

The power of the shell comes from the vast number of commands that do a single thing really well and our ability to combine bash programs into pipelines that do complex things.

Let's build up a pipeline that counts the number of chromosomes that have data in this file. The first column contains the chromosomes:

	$ cut -f1 CellContigs.bedRnaElements

The `uniq` command will print out unique elements in the input. The standard usage of `uniq`:

    $ uniq CellContigs.bedRnaElements

If we wanted the unique chromosomes, we could save column 1 to a file and then run uniq, but it is shorter to simply *pipe* the output from the first command as input into the second command:

	$ cut -f1 CellContigs.bedRnaElements | uniq


The `uniq` command looks for runs of identical elements. Let's `sort` the list first before running `uniq`. Bash has a command for that, and we can chain together multiple commands using `|`.

	$ cut -f1 CellContigs.bedRnaElements | sort | uniq

## Finding things in files and directories

What if we only wanted the lines that matched a specific chromosome? Use `grep` to search input for particular patterns. The syntax for grep is `grep pattern input`.

	$ grep chrX CellContigs.bedRnaElements

***Exercise***: Search for the chromosome 1 instead of chromosome X. What happens?

Why do we get chromsome 1, 10, 11, 12, etc? Use the `-w` flag to get full words.

We can use more complex patterns with `grep` (and other tools) by using *regular expressions*. For example, to find both chromosome X and Y:

	$ cat CellContigs.bedRnaElements | grep chr[XY]

### Extra stuff
If there is time, you can show more regex examples:

    $ grep [unannotated] CellContigs.bedRnaElements

    $ cat CellContigs.bedRnaElements | grep chr[0-9]

    $ cat CellContigs.bedRnaElements | grep chr[A-Z]


## Loops

Perhaps we want to extract only the information for the X and Y chromosome from every file. Or we want to run a different analysis on every file. We want to repeat the same command multiple times with different input.

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
	> head n -1 CellContigs.bedRnaElements
	> done

***Exercise***: Modify the lines between `do` and `done` to use the `grep` example from above to create two new files containing data from the X and the Y chromosomes.

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
echo The name of this script is: $0
inputfile=$1
for c in X Y
do
        echo chromosome$c
        echo intputfile: $inputfile
        echo outputfile: $inputfile.chr$c
done
```

***Exercise***: Modify this script to print the data for the specified chromsome from the input file to an output file

# Logging into a remote machine

Finally, we are going to cover how to log into a remote machine. Even if you don't use the bash shell for your day-to-day work on your computer, once you log into a server (such as the Duke HPC), the bash shell will be your only interface.

Open a new window. We are going to use the `ssh` (secure shell) command. This creates a secure connection to a remote server.

    $ ssh netid@dscr-slogin-03.oit.duke.edu

You will see a message about not being able to establish authenticity of the hose. You will always get this message the first time you log into a server. Type `yes` and then type your netID password.

Note that the prompt changed. Try `whoami` or `pwd` or `hostname` to show other differences (and test where you are before doing things!).

To log out and return to your laptop:

    $ exit
