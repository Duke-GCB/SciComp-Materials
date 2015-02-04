import fileinput
import re

for line in fileinput.input():
    if fileinput.isfirstline():
        continue
    
    match = re.search('^(.*)\s+(20\d\d)-(\d\d)-(\d\d)\s+(\d+\.?\d*)$', line)
    
    if match:
        fields = [
            match.group(2),  # year
            match.group(3),  # month
            match.group(4),  # day
            match.group(1),  # site
            match.group(5)   # value
        ]
        
        print ",".join(fields)
    else:
        print "Line {} did not match!".format(fileinput.lineno())
