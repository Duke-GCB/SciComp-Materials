import fileinput
import re

def parse_record(record_string):
    '''
    Return formatted data record as (Y, M, D, site, value) or None
    '''

    # each pattern is a tuple, with the regex as the first value, 
    # then the matches in the order we would like:
    # year, month, day, site, value
    patterns = [
        ( 
            '^(.*)\t(20\d\d)-(\d\d)-(\d\d)\t(\d+\.?\d*)$',
            2, 3, 4, 1, 5
        )
    ]
    
    for pattern, y, m, d, s, v in patterns:
        match = re.search(pattern, record_string)
        if match:
            return [
                match.group(y), 
                match.group(m), 
                match.group(d), 
                match.group(s), 
                match.group(v)
            ]
    
    return None

for line in fileinput.input():
    if fileinput.isfirstline():
        continue
    fields = parse_record(line)
    print fields
