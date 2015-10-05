
import pandas
import glob

def read_bed(filename):
    data = pandas.read_table(filename, header=None)
    data.columns = ['chrom','chromStart','chromEnd','name','score','strand','level','signif','score2']
    return data

def detect_problems(filename):
    data = read_bed(filename)
    if data['score2'].min() < 1 and data['score'].min() > 0:
        print 'Suspicious data!'
    elif data.loc[data['chrom'] == 'chrM']['score'].mean() > 200:
        print 'High scores on chrM!'
    else:
        print 'Seems OK!'
        
filenames = glob.glob('/Users/dcl9/gcbCourse/materials/cshl_rna_seq/*.bed*')
for f in filenames:
    print f
    detect_problems(f)