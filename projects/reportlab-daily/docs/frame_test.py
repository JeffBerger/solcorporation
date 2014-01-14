from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, Frame, Flowable)
from reportlab.rl_config import defaultPageSize
from reportlab.lib import colors
import pymongo
from reportlab.graphics.shapes import Drawing

client = pymongo.MongoClient("localhost", 27017)
db = client['charge']
bid = db.bid
styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']


def query(field):
    biddata = bid.find({}, {"_id": 0})
    for doc in biddata:
        return doc[field]


story = []
#add some flowables
story.append(Paragraph("This is a Heading", styleH))
story.append(Paragraph("This is a paragraph in <i>Normal</i> style.",
                       styleN))
data = [[query("cid"), query("total_price"), query("gross_margin"), '03',
         '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
t = Table(data)
t.setStyle(TableStyle([('BACKGROUND', (1, 1), (-2, -2), colors.green),
                       ('TEXTCOLOR', (0, 0), (1, -1), colors.red)]))
story.append(t)


class MCLine(Flowable):
    """Line flowable --- draws a line in a flowable"""

    def __init__(self, width):
        Flowable.__init__(self)
        self.width = width

    def __repr__(self):
        return "Line(w=%s)" % self.width

    def draw(self):
        self.canv.line(0, 0, self.width, 0)
# still want to get a drawing or abstract figure in as a flowable
St = []


def star(canvas, title="Title Here", aka="Comment here.",
         xcenter=None, ycenter=None, nvertices=5):
    from math import pi
    from reportlab.lib.units import inch
    radius = inch / 3.0
    #if xcenter is None: xcenter = 2.75 * inch
    #if ycenter is None: ycenter = 1.5 * inch
    canvas.drawCentredString(xcenter, ycenter + 1.3 * radius, title)
    canvas.drawCentredString(xcenter, ycenter - 1.4 * radius, aka)
    p = canvas.beginPath()
    p.moveTo(xcenter, ycenter + radius)
    from math import cos, sin
    angle = (2 * pi) * 2 / 5.0
    startangle = pi / 2.0
    for vertex in range(nvertices - 1):
        nextangle = angle * (vertex + 1) + startangle
        x = xcenter + radius * cos(nextangle)
        y = ycenter + radius * sin(nextangle)
        p.lineTo(x, y)
    if nvertices == 5:
        p.close()
    canvas.drawPath(p)
g = Drawing(3, 4)
c = Canvas('mydoc.pdf')
f = Frame(inch, inch, 2 * inch, 9 * inch, showBoundary=1)
f2 = Frame(4 * inch, inch, 2 * inch, 9 * inch, showBoundary=1)
#St.append(g.add(star(c, title="Title", aka="comments", xcenter=2 * inch,
 #                    ycenter=3 * inch, nvertices=5)))
g.add(star(c, title="Title", aka="comments", xcenter=4 * inch,
           ycenter=3 * inch, nvertices=5))
# This is the star added on top of the flowable system, still want it in frame
f.addFromList(story, c)
f2.addFromList(St, c)
c.save()
"""This is the frame test for the ReportLab structure.  It is currently
   and I like the current setup.  It runs using a two frame system, imports
   data from a json, and draws a star on the canvas at the end."""
