# !/usr/bin/python3
import sys
import glob
from pathlib import Path
from datetime import datetime

import numpy
import pandas
import matplotlib.pyplot as plt

from tqdm import tqdm

from IPython import get_ipython
from IPython.display import display, HTML, Math, Markdown


plt.rcParams['svg.fonttype'] = 'none'

pandas.set_option('display.max_columns', 100)
pandas.set_option('display.max_colwidth', 100)
pandas.set_option('display.width', 200)


custom_css = """
<style>
table.dataTable td {
    white-space: normal !important;
    word-wrap: break-word;
    max-width: 450px;
}
</style>
"""

display(HTML(custom_css))


ipython = get_ipython()
if ipython is not None:
    ipython.run_line_magic('load_ext', 'autoreload')
    ipython.run_line_magic('autoreload', '2')


display('cwd:', Path.cwd())
display('python:', sys.executable)
display('started:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def show_package(package):
    module = __import__(package)
    display('{}: {}'.format(package, module.__file__))

display("🚀 Loaded default IPython startup script")
