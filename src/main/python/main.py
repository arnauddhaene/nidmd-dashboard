"""
main.py
=======

main
"""
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
import logging

from dashboard import Dashboard
from utils import *


if not Path(TARGET_DIR).exists():
    Path(TARGET_DIR).mkdir()
if not Path(CACHE_DIR).exists():
    Path(CACHE_DIR).mkdir()

clear_target()
clear_cache()

if not CACHE_DIR.joinpath('log.log').exists():
    CACHE_DIR.joinpath('log.log').open(mode='w')

logging.getLogger('werkzeug').setLevel(logging.ERROR)
logging.basicConfig(filename=CACHE_DIR.joinpath('log.log').as_posix(), filemode='a', level=logging.INFO,
                    format='%(asctime)s,%(msecs)d | %(levelname)s — %(message)s', datefmt='%H:%M:%S')

# overwrite automated QApplication from ApplicationContext to include flags
# ApplicationContext.app = QApplication(sys.argv)

appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

main_window = QMainWindow()

db = Dashboard()
db.show()

exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
sys.exit(exit_code)
