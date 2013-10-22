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

def write_table(data, f):
    f.write("|-\n")
    for row in data:
        row.pop()    # Ignore last blank field
        for field in row:
            f.write("| " + field + "\n")
        f.write("|-\n")

wikifile = 'dist/owasp.wiki'

with open (wikifile, 'w') as f:
    with open('src/owasp-wiki/start.wiki', 'r') as in_file:
        f.write(in_file.read())

    write_table(load_data('src/online.tsv'), f)
    with open('src/owasp-wiki/post-online.wiki', 'r') as in_file:
        f.write(in_file.read())

    write_table(load_data('src/offline.tsv'), f)
    with open('src/owasp-wiki/post-offline.wiki', 'r') as in_file:
        f.write(in_file.read())

    write_table(load_data('src/offline-old.tsv'), f)
    with open('src/owasp-wiki/post-offline-old.wiki', 'r') as in_file:
        f.write(in_file.read())

    write_table(load_data('src/vm-iso.tsv'), f)
    with open('src/owasp-wiki/post-vm-iso.wiki', 'r') as in_file:
        f.write(in_file.read())

    write_table(load_data('src/vm-iso-old.tsv'), f)
    with open('src/owasp-wiki/end.wiki', 'r') as in_file:
        f.write(in_file.read())

