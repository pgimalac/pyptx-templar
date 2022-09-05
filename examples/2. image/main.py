"""
Example using images and all possible modifiers.

Use both a vertical and an horizontal image, to show the difference.
"""

from pptx import Presentation
from pyptx_templar.placeholder import pres_replace
from pyptx_templar.presmanager import export

pres = Presentation("./pres-in.pptx")
pres_replace(pres, img='./imgh.png')
export(pres, './pres-out-h.pptx')

pres = Presentation("./pres-in.pptx")
pres_replace(pres, img='./imgv.png')
export(pres, './pres-out-v.pptx')
