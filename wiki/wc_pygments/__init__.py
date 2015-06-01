from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter

def codeformat(code, language):
    # well, asm is supported - but I can't stand gas, make sure we get nasm
    # nasm rocks
    lexers_not_of_same_name = {
    'arm': 'nasm',
    'scpt': 'applescript',
    'cs': 'csharp',
    'fs': 'fsharp',
    'lgt': 'logtalk',
    'mod': 'modula2',
    'm': 'objective-c',
    'n': 'nemerle',
    'j': 'objective-j',
    'mli': 'ocaml',
    'ps': 'postscript',
    'ps1': 'powershell',
    'reb': 'rebol',
    'rs': 'rust',
    'sce': 'scilab',
    'sno' : 'snobol',
    'vb': 'vbnet'
    }

    if language in lexers_not_of_same_name:
        language = lexers_not_of_same_name[language]

    lexer = get_lexer_by_name(language, stripall=False, stripnl=False, ensurenl=True)
    formatter = HtmlFormatter(linenos=True, style='colorful', cssclass="wikicoding-code")
    return highlight(code, lexer, formatter)
