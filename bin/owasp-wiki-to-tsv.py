"""
"""
import os
import string

def table_start(title, offset):
    offset = wikisrc.find(title, offset)
    
    if (offset < 0):
        print 'Unable to find string "' + title + ' "'
        exit (1)
    
    offset = wikisrc.find('|-', offset)
    offset = wikisrc.find('|-', offset+1)
    return offset

def save_data(string, file):
    print ('Generating ' + file);
    with open (file, 'w') as f:
        # Split into rows (returns list)
        rows = string.split('|-')
        for row in rows:
            lines = row.split('|')
            # First line always blank
            lines.pop(0)
            for line in lines:
                f.write(line.strip() + '\t')
            f.write('\n')
        print 'Found ' + str(len(rows)) + ' records'
                

wikifile = 'src/owasp-wiki/full.wiki'

if not os.path.isfile(wikifile):
    print 'Unable to find wiki source file ' + wikifile
    exit (1)

with open(wikifile, 'r') as wiki_file:
    wikisrc = wiki_file.read()

"""
TODO
    Output start - =On-Line apps=
"""

# On-Line apps section
start = table_start('=On-Line apps=', 0)
with open ('src/owasp-wiki/start.wiki', 'w') as f:
    f.write (wikisrc[0:start])

end = wikisrc.find('|}', start)
save_data(wikisrc[start:end], 'src/online.tsv')

# Off-Line apps section
start = table_start('= Off-Line apps =', end)
with open ('src/owasp-wiki/post-online.wiki', 'w') as f:
    f.write (wikisrc[end:start])

end = wikisrc.find('|}', start)
save_data(wikisrc[start:end], 'src/offline.tsv')

# Old Off-Line apps section
start = table_start('quite old', end)
with open ('src/owasp-wiki/post-offline.wiki', 'w') as f:
    f.write (wikisrc[end:start])

end = wikisrc.find('|}', start)
save_data(wikisrc[start:end], 'src/offline-old.tsv')

# Virtual Machines or ISOs section
start = table_start('= Virtual Machines or ISOs =', end)
with open ('src/owasp-wiki/post-offline-old.wiki', 'w') as f:
    f.write (wikisrc[end:start])

end = wikisrc.find('|}', start)
save_data(wikisrc[start:end], 'src/vm-iso.tsv')

# Virtual Machines or ISOs section
start = table_start('quite old', end)
with open ('src/owasp-wiki/post-vm-iso.wiki', 'w') as f:
    f.write (wikisrc[end:start])

end = wikisrc.find('|}', start)
save_data(wikisrc[start:end], 'src/post-vm-iso-old.tsv')

# The rest of the file
with open ('src/owasp-wiki/end.wiki', 'w') as f:
    f.write (wikisrc[end:])
