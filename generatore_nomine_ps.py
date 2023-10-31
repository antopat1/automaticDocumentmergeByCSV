import os, sys
import json, re

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
import csv

# set the variables

basedir = './ps_calusco_23_24'
template_path = 'addetti_psb.html'
input_path = 'ps_23_24a.csv'

# generate the form given the input data
# format of the input data: dictionary substitution key - value

def generate_form(data, filename):
    
    # Create a report
    # Load the template file
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)

    # Define the data for substitution

    # Open the file in read mode

    # Render the template with the data
    rendered_html = template.render(data)

    # Generate PDF from the rendered HTML
    HTML(string=rendered_html).write_pdf(filename)
  
# genitivo
def genitivo(preposizione):
    if preposizione == 'al':
        return('del')
    elif preposizione == 'alla':
        return('della')
    else:
        return(preposizione)

def convert_to_number(str_data):
    pattern = r'\d*,\d'
    matches = re.findall(pattern, str_data)
    #print(matches[0])
    try:
        return(matches[0].replace(',','.'))
    except:
        return 0

# dictionary
with open(input_path, mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        doc_data = row
        print(doc_data['plesso'])
        doc_data['titolo'] = doc_data['titolo'].capitalize()
        out_file = basedir + '/'+ 'ps_' + doc_data['cognome'] + '_23_24.pdf'
        print('Processing:' + doc_data['cognome'] + '\n')
        generate_form(doc_data, out_file)



