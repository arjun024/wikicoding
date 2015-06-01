#! /usr/bin/env python

import os
import sys
from pygments.formatters import HtmlFormatter

path = os.path.join(os.path.dirname(__file__), "../static/wiki/wc_pygments/pygments.css")
f = open(path, 'w')
f.write(HtmlFormatter(style='colorful').get_style_defs('.wikicoding-code'))
f.close()
