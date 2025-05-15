###  VOC Sample Report

---
    

###
May 14, 2025

> ## State of Utah
> ### Department of Environmental Quality (DEQ)
> DEQ Air Pollution Grant (105) - Tech Analysis & Inventories
>
<img width="780" alt="img_official_utah_flag" src="images/img_official_utah_flag.jpg" />

# Volatile Organic Compounds (VOC) Taxonomy Overview

###
### Table of Contents
 - [**I. Background**](#i-background)
 - [**II. List of Common Volatile Organic Compounds by Class**](#ii-list-of-common-volatile-organic-compounds-by-class)
   - [1. Hydrocarbons](#1-hydrocarbons)
   - [2. Chlorinated Solvents](#2-chlorinated-solvents)
   - [3. Alcohols & Ketones](#3-alcohols--ketones)
   - [4. Aldehydes](#4-aldehydes)
   - [5. Terpenes](#5-terpenes)
   - [6. Others (Relevant to EMS or Health IT Environments)](#6-others-relevant-to-ems-or-health-it-environments)
- [**III. Appendix**](#iii-appendix)
  - [i. References](#i-references)
  - [ii. Python Project Structure](#ii-python-project-structure)
  - [iii. Code Index](#iii-code-index)

###
_**please note:** a human-readable code index is included in this markdown document in the appendix below for information security purposes._ 

---



---

## II. List of Common Volatile Organic Compounds by Class

##
Here is a list of common **Volatile Organic Compounds (VOCs)**, grouped by category, along with typical sources and their relevance:

###
### **1. Hydrocarbons**

| Compound | IUPAC Name | Source | Health Outcomes | NIOSH REL | Value Set |
 | -------- | ---------- | ------ | --------------- | --------- | --------- |
| Benzene | Benzene | Vehicle exhaust, Tobacco smoke, Solvents | Carcinogenic, Bone marrow suppression, Leukemia | 0.1 ppm | NIOSH, EPA |
| Toluene | Methylbenzene | Paints, Adhesives, Nail polish | Neurotoxic, Fatigue, Headache | 100 ppm | NIOSH, EPA |
| Xylenes | Dimethylbenzene | Gasoline, Paints, Lab solvents | Irritation, CNS effects | 100 ppm | NIOSH, EPA |
| Ethylbenzene | Ethylbenzene | Gasoline, Varnishes | Hearing loss, Possible carcinogen | 100 ppm | NIOSH, EPA |

### **2. Chlorinated Solvents**

| Compound | IUPAC Name | Source | Health Outcomes | NIOSH REL | Value Set |
 | -------- | ---------- | ------ | --------------- | --------- | --------- |
| Trichloroethylene | Trichloroethene | Degreasers, Industrial solvents | Carcinogenic, Liver toxicity, CNS depression | 25 ppm | NIOSH, EPA |
| Tetrachloroethylene | Tetrachloroethene | Dry cleaning, Metal cleaning | CNS effects, Liver damage, Possible carcinogen | 25 ppm | NIOSH, EPA |
| Chloroform | Trichloromethane | Water disinfection byproduct | Carcinogen, Liver damage, CNS depression | 2 ppm | NIOSH, EPA |

### **3. Alcohols and Ketones**

| Compound | IUPAC Name | Source | Health Outcomes | NIOSH REL | Value Set |
 | -------- | ---------- | ------ | --------------- | --------- | --------- |
| Isopropyl alcohol | Propan-2-ol | Disinfectants, Hand sanitizers | CNS depression, Respiratory irritation | 400 ppm | NIOSH, EPA |
| Ethanol | Ethyl alcohol | Solvents, Hand sanitizers, Lab use | CNS effects, Irritation | 1000 ppm | NIOSH, EPA |
| Acetone | Propanone | Nail polish remover, Lab solvents | Eye irritation, CNS effects | 250 ppm | NIOSH, EPA |
| Methyl ethyl ketone | Butan-2-one | Paints, Glues | Eye, nose, throat irritation, Headaches | 200 ppm | NIOSH, EPA |

### **4. Aldehydes**

| Compound | IUPAC Name | Source | Health Outcomes | NIOSH REL | Value Set |
 | -------- | ---------- | ------ | --------------- | --------- | --------- |
| Formaldehyde | Methanal | Building materials, Disinfectants | Carcinogenic, Respiratory irritation, Allergic sensitizer | 0.016 ppm | NIOSH, EPA |
| Acetaldehyde | Ethanal | Combustion byproduct, Disinfectants | Respiratory irritant, Possible carcinogen | 25 ppm | NIOSH, EPA |

### **5. Terpenes**

| Compound | IUPAC Name | Source | Health Outcomes | NIOSH REL | Value Set |
 | -------- | ---------- | ------ | --------------- | --------- | --------- |
| Limonene | 1-Methyl-4-(1-methylethenyl)cyclohexene | Citrus scents, Cleaners | Airway irritation, Forms ozone indoors | Not established | NIOSH, EPA |
| Pinene | Pin-2(10)-ene | Pine-scented cleaners, Air fresheners | Respiratory irritation, Forms ozone indoors | Not established | NIOSH, EPA |

### **6. Others**

| Compound | IUPAC Name | Source | Health Outcomes | NIOSH REL | Value Set |
 | -------- | ---------- | ------ | --------------- | --------- | --------- |
| Styrene | Phenylethene | Plastics, Resins, Ambulance interiors | Respiratory irritant, Possible carcinogen, Hearing loss | 50 ppm | NIOSH, EPA |
| 1,3-Butadiene | Buta-1,3-diene | Combustion byproduct, Rubber | Carcinogenic, Cardiovascular effects | 1 ppm | NIOSH, EPA |
| Methylene chloride | Dichloromethane | Paint strippers, Lab solvents | CO poisoning, Carcinogen | 75 ppm | NIOSH, EPA |
#


---

---

##  III. Appendix

###
### i. References

1. U.S. Environmental Protection Agency. (n.d.). Technical overview of volatile organic compounds. U.S. Environmental Protection Agency. Retrieved May 14, 2025, from https://www.epa.gov/indoor-air-quality-iaq/technical-overview-volatile-organic-compounds
1. Agency for Toxic Substances and Disease Registry. (2024). Toxicological profile development guidance (PDF). U.S. Department of Health and Human Services. Retrieved May 11, 2025, from https://www.atsdr.cdc.gov/toxicological-profiles/media/pdfs/2024/10/tox-profile-development-guidance.pdf
1. Occupational Safety and Health Administration. (n.d.). Annotated Permissible Exposure Limits (PELs). U.S. Department of Labor. Retrieved May 12, 2025, from https://www.osha.gov/annotated-pels
1. National Emissions Inventory (NEI), County-Level, US, 2008, 2011, 2014, EPA OAR, OAPQS; Retrieved May 11, 2025, from https://catalog.data.gov/dataset/national-emissions-inventory-nei-county-level-us-2008-2011-2014-epa-oar-oapqs8
1. Barsan, Michael E. (2007). NIOSH Pocket Guide to Chemical Hazards [2007]. Retrieved May 12, 2025, from https://stacks.cdc.gov/view/cdc/21265
1. National Institute for Occupational Safety and Health. (1994). NIOSH pocket guide to chemical hazards. U.S. Department of Health and Human Services, Centers for Disease Control and Prevention. https://www.cdc.gov/niosh/npg/ 

###
### i. Python Project Structure
```text
VOCs
├── .venv/                    ← virtual environment / isolated python project repository
├── data/                     ← developer-generated definitions, scratches, consoles, stashed files
├── images/                   ← any graphics or images (e.g., Utah flag)
├── logs/                     ← logging file holder
├── resources/                ← pdf resource & references archive
│   ├── npg.pdf               ← reference: niosh pocket guide to chemical hazards
│   └── tpd.pdf               ← reference: toxological profile development guidance / HHS-ATSDR
├── utils/                    ← utilities holder 
│   ├── .git_init             ← automatically initializes a new git repository with new report instance (bash/zsh)
│   ├── .git_init.py          ← automatically initializes a new git repository with new report instance (python)
│   ├── logging_config.py     ← logging configuration as a json dictionary
│   ├── markdown_maker.py     ← converts voc data dictionary into reader-friendly markdown
│   ├── slugify.py            ← mini module that creates url-friendly slugs from headers
│   ├── table_maker.py        ← converts voc data dictionary into reader-friendly tables for cutting, pasting and markdown
│   ├── toc_generator.py      ← mini module that creates table of contents from url-friendly slugs
│   └── voc_report_engine.py  ← c-python 13.3 code that generates report voc_data_dictionary.json (main engine)
├── .gitignore                ← tells git which files/directories to ignore
├── LICENSE.md                ← software licensing information
├── README.md                 ← git repository standard reference 
├── requirements.txt          ← python package dependencies & libraries 
├── voc_data_dictionary.json  ← fallback json dictionary unifying voc attributed from niosh and epa
├── voc_EXAMPLE_REPORT.md     ← reader-friendly report in markdown format
├── voc_EXAMPLE_REPORT.pdf    ← reader-friendly report in .pdf format
```


###
### ii. Code Index

###
#### utils/.git_init
```zsh
#!/bin/bash

# Check if .git directory exists
if [ ! -d ".git" ]; then
    echo "Git not initialized. Running git init..."
    git init
else
    echo "Git already initialized."
fi

# copyright 2025 Quality Measurement Group: si-software-lab


```

###
#### utils/.git_init.py
```python
import pathlib
import subprocess

# Check if .git directory exists
git_dir = pathlib.Path(".git")

if not git_dir.exists():
    print("Git not initialized. Running git init...")
    subprocess.run(["git", "init"])
else:
    print("Git already initialized.")
```

###
#### utils/logging_config.py
```python
import pathlib
import inspect


# derive name of caller
def caller():
    stack = inspect.stack()
    stack_length = len(stack)
    frame = stack[stack_length - 1]
    caller = pathlib.Path(frame.filename).name.split('.')[0]
    return caller


# derive project root from anywhere on this repo's filesystem tree
def repo_base_name(starting_path=None):
    p = pathlib.Path(starting_path or __file__).resolve()
    return next(parent for parent in [p] +list(p.parents) if (parent / '.git').exists())


# file sys name walk
caller = caller()
project_root = repo_base_name()
logging_dir = project_root / "logs"
logging_dir.mkdir(parents=True, exist_ok=True) # ensure logging directory exists


# cover letter logging config
logging_config_cover_letter_engine_dict = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {
            "format": "-> %(filename)s - %(asctime)s - %(levelname)s </> %(message)s"
        },
        "detailed": {
            "format": "-> %(filename)s - %(asctime)s - %(name)s - %(levelname)s </>  %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "INFO",  # Log at INFO level
            "formatter": "detailed",
            "filename": str(logging_dir / f"{caller}.log"),
            "mode": "a"
        },
    },
    "root": {
        "level": "INFO",  # Set root logger to INFO level
        "handlers": ["console", "file"],
    },
}
```

###
#### utils/markdown_maker.py
```python
import json

# markdown maker

"""
converts any dictionary with nested dicts up to 6 levels to markdown
by david balkcom

-----------------------------------
| Depth | Markdown Output Example |
| ----- | ----------------------- |
| 2     | `## Key`                |
| 3     | `### Subkey`            |
| 4     | `#### Deeper key`       |
| 5     | `#####`                 |
| 6     | `######`                |
| 7+    | `- Bullet with indent`  |
-----------------------------------

"""


# modular fcn to compile json content into md
def dict_to_markdown(data_to_convert, level=2):
    markdown = ''
    for key, value in data_to_convert.items():
        heading_level = min(level, 6)
        markdown += f"{'#' * heading_level} {key}\n\n"

        if isinstance(value, dict):
            markdown += dict_to_markdown(value, level + 1)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    markdown += dict_to_markdown(item, level + 1)
                else:
                    markdown += f"{'  ' * (level - 1)}- {item}\n"
        else:
            markdown += f"{'  ' * (level - 1)}- {value}\n"

        markdown += '\n'
    return markdown


# fetch source content
with open('../voc_data_dictionary.json', 'r') as f1:
    data_to_convert = json.load(f1)


# call compiler fcn
markdown_content = dict_to_markdown(data_to_convert)


# write content to markdown file
with open('../data/voc_data_markdown.md', 'w') as f:
    f.write(markdown_content)

print('Markdown file created.')
```


###
#### utils/slugify.py
```python
import re


# transform given text string into a URL-friendly slug
def slugify(text):
    return re.sub(r'[^\w\- ]', '', text).lower().replace(' ', '-')

```


###
#### utils/toc_generator.py
```python
import re

def slugify(text):
    return re.sub(r'[^\w\- ]', '', text).lower().replace(' ', '-')

def generate_toc(markdown_text):
    toc_lines = []
    for line in markdown_text.splitlines():
        match = re.match(r'^(#{2,6}) (.+)', line)
        if match:
            level = len(match.group(1)) - 1  # Indent by level
            title = match.group(2).strip()
            slug = slugify(title)
            toc_lines.append(f"{'  ' * level}- [{title}](#{slug})")
    return '\n'.join(toc_lines)

# Example usage
with open('../README.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

toc = generate_toc(markdown_content)
print("# Table of Contents\n\n" + toc)

```


###
#### utils/voc_report_engine.py (main engine)
```python
import pyfiglet
import logging.config
from colorama import Fore
from utils import logging_config as lc
from utils.logging_config import project_root
import requests
from bs4 import BeautifulSoup
import json
import uuid
import csv
from fpdf import FPDF
from datetime import datetime
from prettyprinter import pprint




# dev console header
line_1 = ('\n\nWelcome to a VOC sample report'
          '\n')
line_2 = pyfiglet.figlet_format('Volatile \nOrganic \nCompounds ')
line_3 = (f'Today is {datetime.now().strftime('%A')}, {datetime.now().strftime('%B %d, %Y')}. Carpe Diem!\n\n'\
          '-------------------------------------------------------------------------------------\n'\
          '-------------------------------------------------------------------------------------\n')
line_4 = ('Software written by \n'\
          '    David Balkcom, MPH \n'\
          '    Principal Data Science Engineer \n'\
          '    Quality Measurement Group\n'\
          '    333 East Main Street No. 132, Lehi, UT 84043\n\n'
          '-------------------------------------------------------------------------------------\n'\
          '-------------------------------------------------------------------------------------\n')
# format mask: fallback macOS/linux/windows for current time in hour:minute/AM/PM format without leading zeros
if datetime.now().strftime('%I:%M %p') == '12:00 AM':  # To handle the midnight case (this looks hokey)

    time_format = datetime.now().strftime('%I:%M %p').lstrip('0')  # Remove leading zero

else:
    time_format = datetime.now().strftime('%l:%M %p').strip()  # Strip leading space from hour
print(Fore.CYAN + line_1)
print(Fore.CYAN + line_2)
print(Fore.CYAN + line_3)
print(Fore.CYAN + line_4)




# apply logging configuration & initialize logging
logging.config.dictConfig(lc.logging_config_cover_letter_engine_dict)
logging_file = __file__.split('/')[-1].split('.')[0]
logfile_path = lc.logging_dir / logging_file
logger = logging.getLogger(logging_file + '-logger')
logger.info(f'LOGGING INITIALIZED />\n'\
# f'  PROJECT DIRECTORY:   {lc.project_root}\n'\
f'  TIMESTAMP:           {datetime.now().strftime('%A')}, {datetime.now().strftime('%B %d, %Y')}, {time_format} Mountain Time\n'\
f'  REPORT AUTHOR:       DAVID BALKCOM, MPH\n'\
f'  DELIVER TO:          VOC Data Validation\n'\
f'                       State of Utah Department of Environmental Quality, \n'\
f'                       DEQ Air Pollution Grant (105) - Tech Analysis & Inventories \n\n'
f'-------------------------------------------------------------------------------------\n'\
f'-------------------------------------------------------------------------------------\n')




# data navigation constants
CSV_FALLBACK_PATH = 'voc_fallback_data.csv'
PDF_REPORT_PATH = 'voc_report.pdf'
NIOSH_URL = 'https://www.cdc.gov/niosh/npg/npgdtox.html'




# contingency planning step zero:
# check for live internet connection
def is_connected():
    try:
        requests.get('https://www.google.com', timeout=3)
        logger.info(f'\n    Step Zero: Test connection SUCCESSFUL to public internet...')
        return True
    except requests.ConnectionError:
        logger.info(f'\n    Step Zero: Test connection FAILED to public internet... \n loading most recent contingency data dictionary from disk...please wait...')
        return False




# contingency planning step 1:
# webscrape VOC data if online
def scrape_voc_data():
    voc_data_dict = {}
    try:
        response = requests.get(NIOSH_URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        if table:
            for row in table.find_all('tr')[1:]:
                cols = row.find_all('td')
                if len(cols) >= 4:
                    name = cols[0].get_text(strip=True)
                    iupac = cols[1].get_text(strip=True)
                    rel = cols[2].get_text(strip=True)
                    outcomes = cols[3].get_text(strip=True).split(', ')
                    voc_data_dict[name] = {
                        'iupac_name': iupac,
                        'source': ['Scraped from NIOSH database'],
                        'niosh_rel': rel,
                        'health_outcomes': outcomes,
                        'category': 'Unknown',
                        'value_set': 'NIOSH',
                        'utah_voc_reference_db_test_id': str(uuid.uuid4())
                    }
    except Exception as e_data_scrape:
        logger.error(f'AN ERROR OCCURRED: Scraping failed: {e_data_scrape}')
    return voc_data_dict




# contingency planning step 2:
# if step zero fails, then load fallback voc_data_dict offline
def load_fallback_csv(path):
    voc_data_dict = {}
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                voc_data_dict[row['compound']] = {
                    'iupac_name': row['iupac_name'],
                    'source': row['source'].split('|'),
                    'niosh_rel': row['niosh_rel'],
                    'health_outcomes': row['health_outcomes'].split('|'),
                    'category': row['category'],
                    'value_set': row['value_set'],
                    'utah_voc_reference_db_test_id': row['uuid']
                }
    except FileNotFoundError:
        logger.info('Fallback CSV file not found.')
    return voc_data_dict




# generate pdf report
def generate_pdf_report(voc_dict, path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.cell(200, 10, txt='VOC Reference Data Report', ln=True, align='C')
    pdf.ln(10)
    pdf.set_font('Arial', size=10)
    logging.info('pdf report format set')

    for compound, data in voc_dict.items():
        pdf.set_font('Arial', style='B', size=10)
        pdf.cell(0, 10, f'{compound}', ln=True)
        pdf.set_font('Arial', size=10)
        for key, value in data.items():
            if isinstance(value, list):
                value = ', '.join(value)
            pdf.multi_cell(0, 8, f'  {key}: {value}')
        pdf.ln(5)
    logging.info('pdf report document compiled')

    pdf.output(path)




# main routine
def main():
    if is_connected():
        voc_dict = scrape_voc_data()
        source_type = 'Scraped live from NIOSH'
    else:
        voc_dict = load_fallback_csv(CSV_FALLBACK_PATH)
        source_type = 'Loaded from fallback CSV'

    if not voc_dict:
        print('No VOC data available.')
        return

    print(f'{len(voc_dict)} VOC entries loaded from {source_type}.')
    generate_pdf_report(voc_dict, PDF_REPORT_PATH)
    print(f'PDF report generated at: {PDF_REPORT_PATH}')




# execute script
if __name__ in ('__main__'):
    main()




uvd = open('../voc_data_dictionary.json', "r")
unified_voc_dict = json.loads(uvd.read())
pprint(unified_voc_dict)




# repo filesystem walk for logging

print('...exiting runtime.')
quit()

```


###
#### voc_data_dictionary.json
```json
{
  "Benzene": {
    "iupac_name": "Benzene",
    "source": [
      "Vehicle exhaust",
      "Tobacco smoke",
      "Solvents"
    ],
    "niosh_rel": "0.1 ppm",
    "health_outcomes": [
      "Carcinogenic",
      "Bone marrow suppression",
      "Leukemia"
    ],
    "category": "Hydrocarbons",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "f0ce5c75-0344-471c-9add-3b1c2efc375c"
  },
  "Toluene": {
    "iupac_name": "Methylbenzene",
    "source": [
      "Paints",
      "Adhesives",
      "Nail polish"
    ],
    "niosh_rel": "100 ppm",
    "health_outcomes": [
      "Neurotoxic",
      "Fatigue",
      "Headache"
    ],
    "category": "Hydrocarbons",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "3ff044b6-c443-48c4-b647-41eaf1782d1b"
  },
  "Xylenes": {
    "iupac_name": "Dimethylbenzene",
    "source": [
      "Gasoline",
      "Paints",
      "Lab solvents"
    ],
    "niosh_rel": "100 ppm",
    "health_outcomes": [
      "Irritation",
      "CNS effects"
    ],
    "category": "Hydrocarbons",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "9c067b6b-656a-45cc-9a2a-b9608f028223"
  },
  "Ethylbenzene": {
    "iupac_name": "Ethylbenzene",
    "source": [
      "Gasoline",
      "Varnishes"
    ],
    "niosh_rel": "100 ppm",
    "health_outcomes": [
      "Hearing loss",
      "Possible carcinogen"
    ],
    "category": "Hydrocarbons",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "0ac93896-42b1-49d8-8a31-080d7739f3df"
  },
  "Trichloroethylene": {
    "iupac_name": "Trichloroethene",
    "source": [
      "Degreasers",
      "Industrial solvents"
    ],
    "niosh_rel": "25 ppm",
    "health_outcomes": [
      "Carcinogenic",
      "Liver toxicity",
      "CNS depression"
    ],
    "category": "Chlorinated Solvents",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "6942b2cc-0fed-49b5-8182-2306884ed95d"
  },
  "Tetrachloroethylene": {
    "iupac_name": "Tetrachloroethene",
    "source": [
      "Dry cleaning",
      "Metal cleaning"
    ],
    "niosh_rel": "25 ppm",
    "health_outcomes": [
      "CNS effects",
      "Liver damage",
      "Possible carcinogen"
    ],
    "category": "Chlorinated Solvents",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "d00d9c8a-f1d2-45d4-8971-27cd184805c6"
  },
  "Chloroform": {
    "iupac_name": "Trichloromethane",
    "source": [
      "Water disinfection byproduct"
    ],
    "niosh_rel": "2 ppm",
    "health_outcomes": [
      "Carcinogen",
      "Liver damage",
      "CNS depression"
    ],
    "category": "Chlorinated Solvents",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "ae9179fc-5c21-4335-89c6-529dcc357ca6"
  },
  "Isopropyl alcohol": {
    "iupac_name": "Propan-2-ol",
    "source": [
      "Disinfectants",
      "Hand sanitizers"
    ],
    "niosh_rel": "400 ppm",
    "health_outcomes": [
      "CNS depression",
      "Respiratory irritation"
    ],
    "category": "Alcohols and Ketones",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "1ec56467-ff1d-4d99-9955-3a1e17f34fcd"
  },
  "Ethanol": {
    "iupac_name": "Ethyl alcohol",
    "source": [
      "Solvents",
      "Hand sanitizers",
      "Lab use"
    ],
    "niosh_rel": "1000 ppm",
    "health_outcomes": [
      "CNS effects",
      "Irritation"
    ],
    "category": "Alcohols and Ketones",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "5e32f688-4d6a-4309-af44-aeefaf327e44"
  },
  "Acetone": {
    "iupac_name": "Propanone",
    "source": [
      "Nail polish remover",
      "Lab solvents"
    ],
    "niosh_rel": "250 ppm",
    "health_outcomes": [
      "Eye irritation",
      "CNS effects"
    ],
    "category": "Alcohols and Ketones",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "fe2cd045-cbf6-4cdc-b056-0db22412f52e"
  },
  "Methyl ethyl ketone": {
    "iupac_name": "Butan-2-one",
    "source": [
      "Paints",
      "Glues"
    ],
    "niosh_rel": "200 ppm",
    "health_outcomes": [
      "Eye, nose, throat irritation",
      "Headaches"
    ],
    "category": "Alcohols and Ketones",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "db586b21-c152-4bd3-a94a-1966bae88740"
  },
  "Formaldehyde": {
    "iupac_name": "Methanal",
    "source": [
      "Building materials",
      "Disinfectants"
    ],
    "niosh_rel": "0.016 ppm",
    "health_outcomes": [
      "Carcinogenic",
      "Respiratory irritation",
      "Allergic sensitizer"
    ],
    "category": "Aldehydes",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "c31682b6-ace4-4594-afa6-edee26c83cf0"
  },
  "Acetaldehyde": {
    "iupac_name": "Ethanal",
    "source": [
      "Combustion byproduct",
      "Disinfectants"
    ],
    "niosh_rel": "25 ppm",
    "health_outcomes": [
      "Respiratory irritant",
      "Possible carcinogen"
    ],
    "category": "Aldehydes",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "4e2ca2fa-2f2b-4791-a549-cb8d90f4e3ff"
  },
  "Limonene": {
    "iupac_name": "1-Methyl-4-(1-methylethenyl)cyclohexene",
    "source": [
      "Citrus scents",
      "Cleaners"
    ],
    "niosh_rel": "Not established",
    "health_outcomes": [
      "Airway irritation",
      "Forms ozone indoors"
    ],
    "category": "Terpenes",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "c3c9934b-76ab-452b-8288-195b01829dbf"
  },
  "Pinene": {
    "iupac_name": "Pin-2(10)-ene",
    "source": [
      "Pine-scented cleaners",
      "Air fresheners"
    ],
    "niosh_rel": "Not established",
    "health_outcomes": [
      "Respiratory irritation",
      "Forms ozone indoors"
    ],
    "category": "Terpenes",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "a2cd5083-4057-481e-b58a-759e48ab8a5c"
  },
  "Styrene": {
    "iupac_name": "Phenylethene",
    "source": [
      "Plastics",
      "Resins",
      "Ambulance interiors"
    ],
    "niosh_rel": "50 ppm",
    "health_outcomes": [
      "Respiratory irritant",
      "Possible carcinogen",
      "Hearing loss"
    ],
    "category": "Others",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "a8fb83a1-dfd6-4beb-b9f6-5a0dbecbf961"
  },
  "1,3-Butadiene": {
    "iupac_name": "Buta-1,3-diene",
    "source": [
      "Combustion byproduct",
      "Rubber"
    ],
    "niosh_rel": "1 ppm",
    "health_outcomes": [
      "Carcinogenic",
      "Cardiovascular effects"
    ],
    "category": "Others",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "0aaa9a26-ca93-4bd1-a017-c751fe93f7cc"
  },
  "Methylene chloride": {
    "iupac_name": "Dichloromethane",
    "source": [
      "Paint strippers",
      "Lab solvents"
    ],
    "niosh_rel": "75 ppm",
    "health_outcomes": [
      "CO poisoning",
      "Carcinogen"
    ],
    "category": "Others",
    "value_set": "NIOSH, EPA",
    "utah_voc_reference_db_test_id": "4e6cdc6e-4e58-4252-8575-a7c94a159542"
  }
}
```


#
#
#
_end report_
