'''
Template : Reddit programming top10 and HN top10 Extension for Python-Markdown
=============================================================================

Copyright Arjun Sreedharan <arjun024@gmail.com>

License: GPLv3

'''


from __future__ import absolute_import
from __future__ import unicode_literals
from markdown import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree
import re


class RedditHNtoptenExtension(Extension):

    def __init__(self, *args, **kwargs):
        super(RedditHNtoptenExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        self.md = md
        # append to end of inline patterns
        RedditHNtopten_RE = r'\{\{(reddit-hn-top)\}\}'
        RedditHNtoptenPattern = RedditHNtopten(RedditHNtopten_RE, {})
        RedditHNtoptenPattern.md = md
        md.inlinePatterns.add('Reddithntopten', RedditHNtoptenPattern, "<wikicodinglink")


class RedditHNtopten(Pattern):
    def __init__(self, pattern, config):
        super(RedditHNtopten, self).__init__(pattern)
        self.config = config

    def handleMatch(self, m):
        if m.group(2).strip():
            """
                    <div class="col-md-12 reddit-top-hn-top" style="margin-bottom: 5%;">
                      <div class="row"> <!--@div1 -->
                          <div class="col-sm-6"> <!--@div21 -->
                              <div class="hn-top"> <!--@div31 -->
                                <h4 class="rh-master">{% trans "Top news from Hacker News" %}</h4> <!--@h41 -->
                                <br/>
                              </div>
                          </div>
                          <div class="col-sm-6"> <!--@div20 -->
                              <div class="reddit-top"> <!--@div30 -->
                                <h4 class="rh-master">{% trans "Top programming news from reddit" %}</h4> <!--@h40 -->
                                <br/>
                              </div>
                          </div>
                      </div>
                      <script>
                        window.wikicoding.reddit_hn_top_flag = 1;
                        reddit_hn_top_init();
                      </script>
                    </div>
            """
            div = etree.Element('div')
            div.set('class' , 'col-md-12 reddit-top-hn-top')
            div.set('style', 'margin-bottom: 5%;')
            div1 = etree.SubElement(div, 'div')
            div1.set('class' , 'row')
            div21 = etree.SubElement(div1, 'div')
            div20 = etree.SubElement(div1, 'div')
            div20.set('class' , 'col-sm-6')
            div21.set('class' , 'col-sm-6')
            div30 = etree.SubElement(div20, 'div')
            div31 = etree.SubElement(div21, 'div')
            div30.set('class' , 'reddit-top')
            div31.set('class' , 'hn-top')
            h40 = etree.SubElement(div30, 'h4')
            h40.set('class' , 'rh-master')
            h40.text ='Top programming news from reddit'
            br0 = etree.SubElement(div30, 'br')
            h41 = etree.SubElement(div31, 'h4')
            h41.set('class' , 'rh-master')
            h41.text = 'Top news from Hacker News'
            br1 = etree.SubElement(div31, 'br')
            scrpt = etree.SubElement(div, 'script')
            scrpt.text = """
                window.wikicoding = window.wikicoding || {};
                window.wikicoding.reddit_hn_top_flag = 1;
            """
        else:
            div = ''
        return div

def makeExtension(*args, **kwargs):
    return RedditHNtoptenExtension(*args, **kwargs)
