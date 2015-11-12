"""GDSCTools

::

    from gdsctools import ANOVA, ic50_test, ANOVAReport
    gdsc = ANOVA(ic50_test)
    results = gdsc.anova_all()

    report = ANOVAReport(gdsc, results)
    report.create_html_pages()


Please See documentation on gdsctools.readthedocs.org

"""
import pkg_resources
try:
    version = pkg_resources.require("gdsctools")[0].version
    __version__ = version
except:
    # update this manually is possible when the version in the
    # setup changes
    version = "0.3"

try:
    license = open('../LICENSE', 'r').read()
except:
    license = '3-clause ("Simplified" or "New") BSD'


from gdsctools.report import HTMLTable, Report
from gdsctools.readers import IC50, GenomicFeatures, DrugDecoder
from gdsctools.anova import ANOVA, ANOVAReport 
from gdsctools.settings import ANOVASettings
from gdsctools.volcano import VolcanoANOVA
from gdsctools.datasets import *

from easydev import browser
def gdsctools_help():
    browser.browse('http://gdsctools.readthedocs.org')
