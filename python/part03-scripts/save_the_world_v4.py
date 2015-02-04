import fileinput
import re

def parse_record(record_string):
    '''
    Return formatted data record as (Y, M, D, site, value) or None
    '''

    # Save patterns in a dictionary. For each pattern:
    #   - key is the regex string
    #   - value is the field order in a list. 
    # The value list field order is:
    #   - year, month, day, site, value
    patterns = {
        '^(.*)\s+(20\d\d)-(\d\d)-(\d\d)\s+(\d+\.?\d*)$': [2, 3, 4, 1, 5],
        '^([\w|\s]+)/(\w+)\s*(\d+),?\s*(20\d\d)/(\d+\.?\d*)$': [4, 2, 3, 1, 5]
    }
    
    for pattern, order_list in patterns.items():
        match = re.search(pattern, record_string)
        if match:
            return [
                match.group(order_list[0]),  # year
                match.group(order_list[1]),  # month
                match.group(order_list[2]),  # day
                match.group(order_list[3]),  # site
                match.group(order_list[4])   # value
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
