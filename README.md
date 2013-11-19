OWASP-VWAD
==========

The OWASP Vulnerable Web Applications Directory Project (VWAD, https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project) is a comprehensive and well maintained registry of all known vulnerable web applications currently available.

The raw data for the project is held in the src/*.tsv files.

The full OWASP wiki source code is available at https://www.owasp.org/index.php?title=OWASP_Vulnerable_Web_Applications_Directory_Project&action=edit.

The individual five wiki source code pages are available at:
- [x] https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project/Pages/Online 
- [x] https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project/Pages/Offline
- [x] https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project/Pages/OfflineOld
- [x] https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project/Pages/VMs
- [x] https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project/Pages/VMsOld

To recreate the TSV files from the OWASP wiki pages:
* Copy the five wiki source code pages into the 'src/owasp-wiki/' directory, using the following filenames: Online.wiki, Offline.wiki, OfflineOld.wiki, VMs.wiki, and VMsOld.wiki.
* Run the 'python bin/owasp-wiki-to-tsv.py' script

To regenerate the OWASP wiki pages after updating the TSV files:
* Run the ' python bin/tsv-to-owasp-wiki.py' script
* Update the five OWASP wiki pages with the contents of the new files available at 'dist/': Online.wiki, Offline.wiki, OfflineOld.wiki, VMs.wiki, and VMsOld.wiki.

