# AutomaticDocumentmergeByCSV
Script to creates institutional documents for the job appointment from a CSV files

The script, based on the Weasyprint library for HTML/CSS manipulation, allows you to dynamically modify from the content of a CSV file a document content that an educational institution uses to assign appointments to teachers, returning in output the set of PDF files one by one each line has the csv file.
Since Weasyprint by default can only be run on Linux systems, to run the script from Windows it is first necessary to enable WSL and install the Ubuntu distribution of Linux using the PowerShell command:
wsl --install

## Library to install in virtualenv:
* Jinja2
* WeasyPrint
* libpango-1.0-0
