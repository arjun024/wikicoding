from __future__ import absolute_import, unicode_literals

from wiki.conf import settings
from wiki.core.markdown.mdx.previewlinks import PreviewLinksExtension
from wiki.core.markdown.wikicoding import wikicodinglinks
from wiki.core.markdown.wikicoding import wikicodingindent
from wiki.core.markdown.wikicoding import template_reddit_hn
from wiki.core.plugins import registry as plugin_registry
import markdown


class ArticleMarkdown(markdown.Markdown):
    def __init__(self, article, preview=False, *args, **kwargs):
        kwargs = settings.MARKDOWN_KWARGS
        kwargs['extensions'] = self.get_markdown_extensions()
        markdown.Markdown.__init__(self, *args, **kwargs)
        self.article = article
        self.preview = preview

    def core_extensions(self):
        """List of core extensions found in the mdx folder"""
        return [PreviewLinksExtension()]

    def get_markdown_extensions(self):
        kwargs = settings.MARKDOWN_KWARGS
        extensions = kwargs.get('extensions', [])
        extensions += self.core_extensions()
        extensions += plugin_registry.get_markdown_extensions()
        # add our wikicodinglink plugin
        extensions += [wikicodinglinks.WikiLinkExtension()]
        # add our wikicodingindent plugin
        extensions += [wikicodingindent.WikiIndentExtension()]
        # add our reddit-hn-top template
        extensions += [template_reddit_hn.RedditHNtoptenExtension()]
        return extensions


def article_markdown(text, article, *args, **kwargs):
    md = ArticleMarkdown(article, *args, **kwargs)
    return md.convert(text)
