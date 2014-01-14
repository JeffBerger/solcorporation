from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
#  myCanvas = Canvas('helloworld.pdf', pagesize=letter)


def hello(c):
    from reportlab.lib.units import inch
    # move the origin up and to the left
    c.translate(3 * inch, 5 * inch)
    # define a large font
    c.setFont("Helvetica", 22)
    # choose some colors
    c.setStrokeColorRGB(1, 0, 0)
    c.setFillColorRGB(0, .1, 0)
    # draw some lines
    c.line(0, 0, 0, 1.7 * inch)
    c.line(0, 0, 1 * inch, 0)
    # draw a rectangle
    c.rect(0.2 * inch, 0.2 * inch, 1 * inch, 1.5 * inch, fill=1)
    # make text go straight up
    c.rotate(90)
    # change color
    c.setFillColorRGB(1, 0, 0)
    # say hello (note after rotate the y coord needs to be negative!)
    c.drawString(0.3 * inch, -inch, "Hello World")
c = canvas.Canvas("hello.pdf", pagesize=letter)
width, height = letter  # keep for later
hello(c)
c.showPage()
c.save()
# return cursormoves2
