#!C:\Users\Acer\web_project\lvenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pydevd==2.9.5','console_scripts','pydevd'
__requires__ = 'pydevd==2.9.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pydevd==2.9.5', 'console_scripts', 'pydevd')()
    )
