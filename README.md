OWASP-VWAD
==========

The OWASP Vulnerable Web Applications Directory Project (VWAD) is a comprehensive and well maintained registry of all known vulnerable web applications currently available.

The raw data for the project is held in the src/*.tsv files

The OWASP wiki source code is https://www.owasp.org/index.php?title=OWASP_Vulnerable_Web_Applications_Directory_Project&action=edit

To recreate these from the OWASP wiki page:
* Copy the wiki source code into the src/owasp-wiki/full.wiki file 
* Run the bin/owasp-wiki-to-tsv script

Note that this will update the other *.wiki 'snippet' pages in the src/owasp-wiki folder

To regenerate the OWASP wiki page:
* Run the bin/tsv-to-owasp-wiki.py script
* Update the OWASP wiki page with the contents of dist/owasp.wiki


