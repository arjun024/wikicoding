# wikicoding

*Every code has a silver lining*

wikicoding is the engine that powers [Wikicoding](http://wikicoding.org), the wikipedia of code.

Anyone can use it to run an instance of wikicoding of their own.

It serves as a wiki engine that manages a wiki of code articles.

This is a nonprofit, free and open source project.

wikicoding is written in Python. It uses the [Django](https://github.com/django/django) web framework and
borrows a good part of its codebase from the [django-wiki](https://github.com/django-wiki/django-wiki) project.


### Requirements

* Python (runs on Python 2.7.5)
* Django (runs on Django 1.6.11)
* Python Markdown
* Pygments
* django-south
* sorl-thumbnail
* django-sekizai
* django-mptt
* MySQL
* uWSGI
* nginx


### The stack

[Wikicoding](http://wikicoding.org) is an implementation of this project.
It depends on [nginx](http://nginx.org) to server static files, and [uWSGI](https://github.com/unbit/uwsgi) to run the
python application.
[MySQL](https://www.mysql.com) serves as the database.
Code hightlight is done using [Pygments](http://pygments.org).


### Installation

Please refer to installation manuals of django applications.

Certain rendundant / sensitive content has been redacted from the source code and are marked as `<<redacted>>`.

You may find them using the following and then replace them:

    $ grep -rn "<<redacted>>" .


### Support for languages

Please see [Languages](https://github.com/arjun024/wikicoding/blob/master/Languages) for the list of supported
langauges in which code articles can be created.

To request addition of a new language, please [submit an issue]
(https://github.com/arjun024/wikicoding/issues/new?title=add%20language&body=I%20want%20the%20following%20language(s)%20to%20be%20added%3A).
For the language to be part of the, the language needs to have a working lexer 
(preferably a [pygments lexer](//pygments.org/docs/lexers/)) so as to enable syntax highlighting.


### Contributions

All contributions are welcome.
You can have a look at the [TODO](https://github.com/arjun024/wikicoding/blob/master/TODO) file for a backlog of items open.
You may include new and relevant items.


Our logo:  Happy hamster.

Our motto: Every code has a silver lining.
