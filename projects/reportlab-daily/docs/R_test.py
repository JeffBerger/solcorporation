# Sample platypus document
# From the FAQ at reportlab.org/oss/rl-toolkit/faq/#1.1

from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import colors
import pymongo
from reportlab.pdfgen import canvas

client = pymongo.MongoClient("localhost", 27017)
db = client['charge']
bid = db.bid
PAGE_HEIGHT = defaultPageSize[1]
PAGE_WIDTH = defaultPageSize[0]
styles = getSampleStyleSheet()
Title = "Customer Bid- SBS|Charge"
pageinfo = "Bid Powered by SBS|Charge"


def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold', 16)
    canvas.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 108, Title)
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
    canvas.restoreState()


def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()


def query(field):
    biddata = bid.find({}, {"_id": 0})
    for doc in biddata:
        return doc[field]


def line(canvas):
    l = canvas.beginPath()
    l.moveTo(10 * inch, 0)
    l.lineTo(0, 5 * inch)
    canvas.drawPath(l, stroke=1, fill=1)


def go(filename):
    doc = SimpleDocTemplate(filename)
    Story = [Spacer(1, 2 * inch)]
    style = styles["Heading1"]
    bogustext = ("This is my simple test of text")
    p = Paragraph(bogustext, style)
    Story.append(p)
    Story.append(Paragraph(
        """Testing the use of the python three quote text business.  I am
           completely unsure if this will function as I think that it should.
           What a stupid thing.  We'll see i suppose.
        """,
        styles["Normal"]))
    Story.append(Spacer(1, 2 * inch))
    beginText(inch, 2 * inch)
    setFont('Times-Roman', 25)
    textLines("""
    We are testing the idea of adding test lines in the middle of no where
    """)

    drawText()
    data = [[query("cid"), query("total_price"), query("gross_margin"), '03',
             '04'],
           ['10', '11', '12', '13', '14'],
           ['20', '21', '22', '23', '24'],
           ['30', '31', '32', '33', '34']]
    t = doc.Table(data)
    t.setStyle(TableStyle([('BACKGROUND', (1, 1), (-2, -2), colors.green),
                           ('TEXTCOLOR', (0, 0), (1, -1), colors.red)]))
    Story.append(t)
    # Next is to get the output to look reasonable
    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

if __name__ == "__main__":
    go("r_test.pdf")
