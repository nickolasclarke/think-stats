from paver.easy import *
import paver.doctools
from paver.setuputils import setup

setup(
    name="ThinkStats",
    packages=['thinkstats'],
    version="1.0",
    url="https://github.com/xmlblog/think-stats",
    author="Christian Romney",
    author_email="cromney@pointslope.com"
)

@task
@needs(['html', "distutils.command.sdist"])
def sdist():
    """Generate docs and source distribution."""
    pass

