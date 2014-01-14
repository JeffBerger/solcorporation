    framePage(c, "Font Control")

    c.drawString(inch, 10*inch, 'Listing available fonts...')

    y = 9.5*inch
    for fontname in c.getAvailableFonts():
        c.setFont(fontname,24)
        c.drawString(inch, y, 'This should be %s' % fontname)
        y = y - 28
    makesubsection(c, "fonts and colors", 4*inch)

    c.setFont('Times-Roman', 12)
    t = c.beginText(inch, 4*inch)
    t.textLines("""Now we'll look at the color functions and how they interact
    with the text.  In theory, a word is just a shape; so setFillColorRGB()
    determines most of what you see.  If you specify other text rendering
    modes, an outline color could be defined by setStrokeColorRGB() too""")
    c.drawText(t)

    t = c.beginText(inch, 2.75 * inch)
    t.setFont('Times-Bold',36)
    t.setFillColor(colors.green)  #green
    t.textLine('Green fill, no stroke')

    #t.setStrokeColorRGB(1,0,0)  #ou can do this in a text object, or the canvas.
    t.setStrokeColor(colors.red)  #ou can do this in a text object, or the canvas.
    t.setTextRenderMode(2)   # fill and stroke
    t.textLine('Green fill, red stroke - yuk!')

    t.setTextRenderMode(0)   # back to default - fill only
    t.setFillColorRGB(0,0,0)   #back to default
    t.setStrokeColorRGB(0,0,0) #ditto
    c.drawText(t)
    c.showPage()