'''
WikicodingIndent Extension for Python-Markdown
=============================================

Converts ':' at the beginning of a line to indentation.

Original code Copyright Arjun Sreedharan <arjun024@gmail.com>

License: [GPLv3]

'''


from __future__ import absolute_import
from __future__ import unicode_literals
from markdown import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree
import re


class WikiIndentExtension(Extension):
    def __init__(self, *args, **kwargs):
        super(WikiIndentExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        self.md = md
        # look for : at the beginning of line
        WIKILINDENT_RE = r'^(:+)'
        WikiIndentPattern = WikiIndent(WIKILINDENT_RE, self.getConfigs())
        WikiIndentPattern.md = md
        md.inlinePatterns.add('wikicodingindent', WikiIndentPattern, "<not_strong")


class WikiIndent(Pattern):
    def __init__(self, pattern, config):
        super(WikiIndent, self).__init__(pattern)

    def handleMatch(self, m):
        if m.group(2) is None:
            return ''
        count = m.group(2).count(':')
        padding = 2 * count
        span = etree.Element('span')
        span.set('style', 'padding-right:%sem' % str(padding))
        return span

def makeExtension(*args, **kwargs):
    return WikiIndentExtension(*args, **kwargs)
