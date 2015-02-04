import fileinput
import re

def parse_record(record_string):
    '''
    Return formatted data record as (Y, M, D, site, value) or None
    '''

    match = re.search('^(\w+)\s+(20\d\d)-(\d\d)-(\d\d)\s+(\d+\.?\d*)$', record_string)
    
    if match:
        return [
            match.group(2),  # year
            match.group(3),  # month
            match.group(4),  # day
            match.group(1),  # site
            match.group(5)   # value
        ]
    
    return None

for line in fileinput.input():
    if fileinput.isfirstline():
        continue

    fields = parse_record(line)

    if fields:
        print ",".join(fields)
    else:
        print "Line {} did not match!".format(fileinput.lineno())
