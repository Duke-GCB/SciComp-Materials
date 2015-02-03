# longest_span_v2.py

# Input Data
bed_string = 'chr1 6 12'

# parse_bed(bed_string)

def parse_bed(bed_string):
    bed_list = bed_string.split()
    chrom = bed_list[0]
    chrom_start = int(bed_list[1])
    chrom_end = int(bed_list[2])

    if chrom_start > chrom_end or chrom_start < 0:
        print "Bad data!"
    else:
        chrom_span = chrom_end - chrom_start
        print 'Chrom: {}, Span {}'.format(chrom, chrom_span)

parse_bed(bed_string)

# Add these later
parse_bed('chr2 12 23')
parse_bed('chrX 98 45')