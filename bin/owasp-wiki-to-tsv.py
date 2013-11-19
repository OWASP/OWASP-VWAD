"""
"""
import os
import string

def table_start(data):
    offset = data.find('|-')
    offset = data.find('|-', offset+1)
    return offset

def convert(file_in, file_out):

    if not os.path.isfile(file_in):
        print 'Unable to find wiki source file ' + file_in
        exit (1)
    
    with open(file_in, 'r') as wiki_file:
        wikisrc = wiki_file.read()

    start = table_start(wikisrc)
    end = wikisrc.find('|}', start)
    
    data = wikisrc[start:end]
    
    print ('Generating ' + file_out);
    with open (file_out, 'w') as f:
        # Split into rows (returns list)
        rows = data.split('|-')
        for row in rows:
            lines = row.split('|')
            # First line always blank
            lines.pop(0)
            for line in lines:
                f.write(line.strip() + '\t')
            f.write('\n')
        print 'Found ' + str(len(rows)) + ' records'


convert('src/owasp-wiki/Online.wiki', 'src/online.tsv')
convert('src/owasp-wiki/Offline.wiki', 'src/offline.tsv')
convert('src/owasp-wiki/OfflineOld.wiki', 'src/offline-old.tsv')
convert('src/owasp-wiki/VMs.wiki', 'src/vm-iso.tsv')
convert('src/owasp-wiki/VMsOld.wiki', 'src/vm-iso-old.tsv')
