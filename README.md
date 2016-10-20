# OWASP-VWAD [![OWASP Incubator](https://img.shields.io/badge/owasp-incubator-blue.svg)](https://www.owasp.org/index.php/OWASP_Project_Inventory#tab=Incubator_Projects)

The OWASP Vulnerable Web Applications Directory Project (VWAD, https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project) is a comprehensive and well maintained registry of all known vulnerable web applications currently available.

The raw data for the project is held in the `src/*.tsv` files.

The full OWASP wiki source code is available at https://www.owasp.org/index.php?title=OWASP_Vulnerable_Web_Applications_Directory_Project&action=edit.

The individual five wiki source code pages are available at:
- https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project/Pages/Online 
- https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project/Pages/Offline
- https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project/Pages/OfflineOld
- https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project/Pages/VMs
- https://www.owasp.org/index.php/OWASP_Vulnerable_Web_Applications_Directory_Project/Pages/VMsOld

## Recreate the `tsv` files from the OWASP wiki pages
* Copy the five wiki source code pages into the `src/owasp-wiki/` directory, using the following filenames: `Online.wiki`, `Offline.wiki`, `OfflineOld.wiki`, `VMs.wiki`, and `VMsOld.wiki`.
* Run the `python bin/owasp-wiki-to-tsv.py` script

## Regenerate the OWASP wiki pages after updating the `tsv` files
* Run the `python bin/tsv-to-owasp-wiki.py` script
* Update the five OWASP wiki pages with the contents of the new files available at `dist/`: `Online.wiki`, `Offline.wiki`, `OfflineOld.wiki`, `VMs.wiki`, and `VMsOld.wiki`.

## Example to add a new entry via the `tsv` files (e.g. to the offline category)
* Add the new entry for the new vulnerable application to the corresponding `.tsv` file (e.g. `offline.tsv`) under `./src`
* Use `git` to submit a pull request (or commit the changes) from the modified `.tsv` file to this GitHub project

### Optional
* Run the `python bin/tsv-to-owasp-wiki.py` script from the main project directory
* This will generate all the `.wiki` files from the `.tsv` files under `./dist`
* Copy the contents of the corresponding `.wiki` file (e.g. `Offline.wiki`) to the official Wiki page of the OWASP VWAD project
  * _IMPORTANT: Do not forget that the `.wiki` file does __not__ include the header and the trailer used by the Wiki page to create the table. Simply, copy and paste the contents inside the current table._
* _(Optional)_ You can delete the contents of the `./dist` directory after copying them to the Wiki
