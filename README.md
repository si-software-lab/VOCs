*README file*



## VOC Data Validator Taxonomy Report

---
- Report Date: Wednesday, May 14, 2025
- Report Title: Volatile Organic Compounds (VOC) Taxonomy
- Target Audience: DEQ Air Pollution Grant (105) - Tech Analysis & Inventories
- Author Name: David Balkcom, MPH
- Author Affiliation: Principal Data Engineer, Quality Measurement Group

###
May 14, 2025

> ## State of Utah
> ### Department of Environmental Quality (DEQ)
> DEQ Air Pollution Grant (105) - Tech Analysis & Inventories
>
<img width="640" alt="img_official_utah_flag" src="images/img_official_utah_flag.jpg" />

# Volatile Organic Compounds (VOC) Taxonomy Overview


##  III. Appendix
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

#
#
#
#
*end of README file*

