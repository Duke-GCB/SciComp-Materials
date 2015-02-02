# longest_span_v1.py

# Input Data
bed_string = 'chr1 6 12'

# Parsing
bed_list = bed_string.split()
chrom = bed_list[0]
chrom_start = int(bed_list[1])
chrom_end = int(bed_list[2])

# Checking
if chrom_start > chrom_end or chrom_start < 0:
    print 'Bad data!'
else:
    # Calculating
    chrom_span = chrom_end - chrom_start
    print 'Chrom: {}, Span {}'.format(chrom, chrom_span)

