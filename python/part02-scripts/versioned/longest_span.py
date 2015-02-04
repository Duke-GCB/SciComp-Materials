# longest_span_v4.py

import sys

def parse_bed(bed_string):
    bed_list = bed_string.split()
    chrom = bed_list[0]
    chrom_start = int(bed_list[1])
    chrom_end = int(bed_list[2])

    if chrom_start > chrom_end or chrom_start < 0:
        return None
    else:
        chrom_span = chrom_end - chrom_start
        return {'chrom': chrom, 'span': chrom_span}

def print_bed(bed_dict):
    if bed_dict is not None:
        print 'Chrom: {}, Span {}'.format(bed_dict['chrom'], bed_dict['span'])
    else:
        print "Bad data!"

for line in sys.stdin:
    print_bed(parse_bed(line))