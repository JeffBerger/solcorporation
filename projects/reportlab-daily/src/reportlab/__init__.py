#Copyright ReportLab Europe Ltd. 2000-2012
#see license.txt for license details
#history http://www.reportlab.co.uk/cgi-bin/viewcvs.cgi/public/reportlab/trunk/reportlab/__init__.py
__version__=''' $Id$ '''
__doc__="""The Reportlab PDF generation library."""
Version="2.7.20140105201709"

import sys

if sys.version_info[0:2] < (2, 7):
    warning = """The trunk of reportlab currently requires Python 2.7 or higher.

    This is being done to let us move forwards with 2.7/3.x compatibility
    with the minimum of baggage.
    
    ReportLab 2.7 was the last packaged version to suppo0rt Python 2.5 and 2.6.

    Python 2.3 users may still use ReportLab 2.4 or any other bugfixes
    derived from it, and Python 2.4 users may use ReportLab 2.5.  
    Python 2.2 and below need to use released versions beginning with 
    1.x (e.g. 1.21), or snapshots or checkouts from our 'version1' branch.
    
    Our current plan is to remove Python 2.5 compatibility on our next release,
    allowing us to use the 2to3 tool and work on Python 3.0 compatibility.
    If you have a choice, Python 2.7.x is best long term version to use.
    """
    raise ImportError("reportlab needs Python 2.5 or higher", warning)

def getStory(context):
    "This is a helper for our old autogenerated documentation system"
    if context.target == 'UserGuide':
        # parse some local file
        import os
        myDir = os.path.split(__file__)[0]
        import yaml
        return yaml.parseFile(myDir + os.sep + 'mydocs.yaml')
    else:
        # this signals that it should revert to default processing
        return None


def getMonitor():
    import reportlab.monitor
    mon = reportlab.monitor.ReportLabToolkitMonitor()
    return mon
