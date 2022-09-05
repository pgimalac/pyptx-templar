"""
Example using arrays, of fixed and variable sizes.

Some context variables are added when replacing (cf documentation),
here we use:
- _sl: the current slide
- _table: the current table (only if we are evaluating inside a table)
- _r and _c: the row and column number of the current cell (only if we are
evaluating inside a table)

We also use the fact that commands are replaced in the order of the elements
in the slide, which can be seen (and changed) by selecting any element of the
slide, opening the "Layout" tab and clicking on the "Selection Pane" button.

Beware that if the table was before the text field in this list, then the
commands in the table would have been interpreted and only then the (already
filled) row would have been copied.

We also renamed the table to be able to identify it more easily (using
the provided "find_shape" function).
"""

from pptx import Presentation
from pyptx_templar.placeholder import pres_replace
from pyptx_templar.presmanager import export, find_shape, table_dup_row

pres = Presentation("./pres-in.pptx")
pres_replace(pres, table_dup_row=table_dup_row, find_shape=find_shape)
export(pres, './pres-out.pptx')
