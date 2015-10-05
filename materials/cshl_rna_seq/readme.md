# Contents


* `*.bedRnaElements` : some sample bed files downloaded from the ENODE project and the UCSD genome browser. These have been renamed from the original filenames (see **File renaming**, below)
* originalfiles: the files named as downloaded from UCSD
* files.txt : metadata about the files

# Source of files
Top-level download page:
http://genome.ucsc.edu/ENCODE/downloads.html

Specific page source:
http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeCshlShortRnaSeq/

Specific track for these experiments:
http://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg19&g=wgEncodeCshlShortRnaSeq

# File renaming

I've renamed the originally downloaded files so that the filenames are shorter. I renamed these using wildcard matching and [parameter expansion](http://wiki.bash-hackers.org/syntax/pe) within a loop:

    $ for f in *.bedRnaElements ; do mv "$f" "${f#wgEncodeCshlShortRnaSeqA549}" ; done
