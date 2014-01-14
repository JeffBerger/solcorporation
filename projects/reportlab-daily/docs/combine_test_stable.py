from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.charts.barcharts import VerticalBarChart
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
styleH = styles['Heading2']
styleT = styles['Heading1']
doc = Canvas('combine_test.pdf')


def box(flt, center=False):
    box_style = [('BOX', (0, 0), (-1, -1), 0.5, colors.lightblue)]
    if center:
        box_style += [('ALIGN', (0, 0), (-1, -1), 'CENTER')]

    return Table([[flt]], style=box_style)


def query(field):
    biddata = bid.find({}, {"_id": 0})
    for doc in biddata:
        return doc[field]

story = []
#add some flowables
story.append(box(Paragraph("Champions", styleT)))
story.append(Paragraph("Philosophizing", styleH))
story.append(Paragraph("""
    This is a paragraph in <i>Normal</i> style.  We do understand exactly why
    the system hates me.  I really really hate the autocorrect.  I really do
    not mind the tab-complete function, but the rest of this is shit.""",
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


story.append(Spacer(0, 0.5 * inch))
g = Drawing(3, 4)
f = Frame(inch, inch, 6.5 * inch, 9 * inch, showBoundary=0)
#St.append(g.add(star(c, title="Title", aka="comments", xcenter=2 * inch,
 #                    ycenter=3 * inch, nvertices=5)))
chart = VerticalBarChart()
# Set the starting point to be (0, 0).  Changing this value changes
# the position that the chart is rendered at within it's 'Drawing'
# space, which we create below.
chart.x = 0
chart.y = 0
# This determines the width, in centimeters (you could use 'inch'
# as well) of the chart on the paper, as well as the height.
chart_width = 5 * inch
chart_height = 4 * inch
chart.height = chart_height
chart.width = chart_width
# The vertical ticks will be labeled from 0 with a value every
# 15 units, spaced so that the maximum value is 60.
chart.valueAxis.valueMin = 0
chart.valueAxis.valueMax = 60
chart.valueAxis.valueStep = 15
# Put the labels at the bottom with an interval of 8 units,
# -2 units below the axis, rotated 30 degrees from horizontal
chart.categoryAxis.labels.dx = 8
chart.categoryAxis.labels.dy = -2
chart.categoryAxis.labels.angle = 30
# The text box's NE corner (top right) is located at the above
# coordinate
chart.categoryAxis.labels.boxAnchor = 'ne'

# Our various horizontal axis labels
catNames = ['Jan-06', 'Feb-06', 'Mar-06', 'Apr-06', 'May-06',
            'Jun-06', 'Jul-06', 'Aug-06']
chart.categoryAxis.categoryNames = catNames

# Some random data to populate the chart with.
chart.data = [(8, 5, 20, 22, 37, 28, 30, 47)]

# Since the 'Chart' class itself isn't a 'Flowable', we need to
# create a 'Drawing' flowable to contain it.  We want the basic
# area to be the same size as the chart itself, so we will
# initialize it with the chart's size.
g = Drawing(chart_width, chart_height)
g.add(chart)

# Add the Chart containing Drawing to our elements list
story.append(box(g))
g.add(star(doc, title="Right", aka="comments", xcenter=7 * inch,
           ycenter=7 * inch, nvertices=5))
g.add(star(doc, title="Left", aka="comments", xcenter=3 * inch,
           ycenter=7 * inch, nvertices=6))
story.append(Spacer(1, 1 * inch))
story.append(box(Paragraph("""
    Well, its now hard to argue that this is working pretty well.  Possibly
    make some nice output charts, and import an image.""", styleH)))
# This is the star added on top of the flowable system, still want it in frame
f.addFromList(story, doc)
doc.save()
