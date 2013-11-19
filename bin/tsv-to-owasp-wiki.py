"""
"""
import os
import string

def load_data(file):
    print ('Loading ' + file);
    lines = tuple(open(file, 'r'))
    #with open (file, 'r') as f:
    # Split into rows (returns list)
    #rows = f.read().split('\n')
    rrows = []
    for line in lines:
        rrow = []
        fields = line.split('\t')
        if (len(fields) > 1):
            for field in fields:
                rrow.append(field.strip())
            rrows.append(rrow)
        elif (not len(fields) == 1):
            print 'Unexpected line? ' + line
    print 'Found ' + str(len(rrows)) + ' records'
    return rrows

def convert(in_file, out_file):
    data = load_data(in_file)
    with open (out_file, 'w') as f:
        f.write("|-\n")
        for row in data:
            row.pop()    # Ignore last blank field
            for field in row:
                f.write("| " + field + "\n")
            f.write("|-\n")


convert('src/online.tsv', 'dist/Online.wiki')
convert('src/offline.tsv', 'dist/Offline.wiki')
convert('src/offline-old.tsv', 'dist/OfflineOld.wiki')
convert('src/vm-iso.tsv', 'dist/VMs.wiki')
convert('src/vm-iso-old.tsv', 'dist/VMsOld.wiki')
