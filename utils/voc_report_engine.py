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


















