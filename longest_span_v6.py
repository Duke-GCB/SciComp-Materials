# longest_span_v6.py

import fileinput

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

def is_longest_span(bed_dict, longest_spans):
  if bed_dict is None:
    return False
  chrom = bed_dict['chrom']
  span = bed_dict['span']
  if chrom not in longest_spans:
    return True
  elif span > longest_spans[chrom]['span']:
    return True
  else:
    return False
    
def set_longest_span(bed_dict, longest_spans):
  chrom = bed_dict['chrom']
  longest_spans[chrom] = bed_dict

# Main functionality
longest_spans = dict()
for line in fileinput.input():
    bed_dict = parse_bed(line)
    if is_longest_span(bed_dict, longest_spans):
      set_longest_span(bed_dict, longest_spans)

# Now print!
for chrom in longest_spans:
  print_bed(longest_spans[chrom])
