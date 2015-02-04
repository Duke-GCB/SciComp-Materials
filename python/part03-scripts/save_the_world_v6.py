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
        '^(\w+)\s+(20\d\d)-(\d\d)-(\d\d)\s+(\d+\.?\d*)$': [2, 3, 4, 1, 5],
        '^(\w+)/(\w+)\s*(\d+),?\s*(20\d\d)/(\d+\.?\d*)$': [4, 2, 3, 1, 5]
    }
    
    month_conversions = {
        "Jan": '01',
        "Feb": '02',
        "Mar": '03',
        "Apr": '04',
        "May": '05',
        "Jun": '06',
        "Jul": '07',
        "Aug": '08',
        "Sep": '09',
        "Oct": '10',
        "Nov": '11',
        "Dec": '12'
    }
    
    for pattern, order_list in patterns.items():
        match = re.search(pattern, record_string)
        if match:
            if match.group(order_list[1])[0:3] in month_conversions.keys():
                month = month_conversions[match.group(order_list[1])[0:3]]
            else:
                month = match.group(order_list[1])
            
            return [
                match.group(order_list[0]),  # year
                month,                       # month
                match.group(order_list[2]),  # day
                match.group(order_list[3]),  # site
                match.group(order_list[4])   # value
            ]
    
    return None

output = open('output.csv', 'w')

for line in fileinput.input():
    if fileinput.isfirstline():
        continue
    
    fields = parse_record(line)
    
    if fields:
        formatted_line = ','.join(fields)
        output.write(formatted_line + '\n')
