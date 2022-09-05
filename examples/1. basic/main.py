"""
Basic example using variables, library, functions.
"""

import datetime

from pptx import Presentation
from pyptx_templar.placeholder import pres_replace
from pyptx_templar.presmanager import export

TITLE = "Something"
NAME = "John Smith"

pres = Presentation("./pres-in.pptx")
pres_replace(pres, title=TITLE, name=NAME, datetime=datetime)
export(pres, './pres-out.pptx')
