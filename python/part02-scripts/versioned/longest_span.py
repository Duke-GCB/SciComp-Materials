# longest_span_v3.py

# Input Data
bed_string = 'chr1 6 12'

# parse_bed(bed_string)

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
    
print_bed(parse_bed(bed_string))

print_bed(parse_bed('chr2 12 23'))
print_bed(parse_bed('chrX 98 45'))
print bed_string