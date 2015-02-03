import fileinput
import re

def parse_record(record_string):
    '''
    Return formatted data record as (Y, M, D, site, value) or None
    '''
    
    month_conversions = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }

    # each pattern is a tuple, with the regex as the first value, 
    # then the matches in the order we would like:
    # year, month, day, site, value
    patterns = [
        ( 
            '(.*)\t(20\d\d)-(\d\d)-(\d\d)\t(\d+\.?\d*)',
            2, 3, 4, 1, 5
        ),
        (
            '^([\w|\s]+)/(\w+)\s*(\d+),?\s*(20\d\d)/(\d+\.?\d*)$',
            4, 2, 3, 1, 5
        )
    ]
    
    for pattern, y, m, d, s, v in patterns:
        match = re.search(pattern, record_string)
        if match:
            if match.group(m)[0:3] in month_conversions.keys():
                month = month_conversions[match.group(m)[0:3]]
            else:
                month = match.group(m)
            
            return [
                match.group(y), 
                month, 
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
