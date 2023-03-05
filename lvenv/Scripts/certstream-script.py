#!C:\Users\Acer\web_project\lvenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'certstream==1.12','console_scripts','certstream'
__requires__ = 'certstream==1.12'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('certstream==1.12', 'console_scripts', 'certstream')()
    )
