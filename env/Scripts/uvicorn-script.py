#!c:\users\guillempuig\desktop\hackupc\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'uvicorn==0.9.0','console_scripts','uvicorn'
__requires__ = 'uvicorn==0.9.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('uvicorn==0.9.0', 'console_scripts', 'uvicorn')()
    )
