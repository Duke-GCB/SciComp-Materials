# longest_span_v4.py

import fileinput

def parse_chrom(bed_string):
    bed_list = bed_string.split()
    chrom = bed_list[0]
    chrom_start = int(bed_list[1])
    chrom_end = int(bed_list[2])

    if chrom_start > chrom_end or chrom_start < 0:
        print "Bad data!"
    else:
        chrom_span = chrom_end - chrom_start
        print "Chrom: %s, Span %d" % (chrom, chrom_span)

for line in fileinput.input():
    parse_chrom(line)
