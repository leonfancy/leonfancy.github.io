"""
Add a link to every heading
"""

from panflute import *


def action(elem, doc):
    if isinstance(elem, Header):
        link = Link(Str(''), url="#" + elem.identifier, title=elem.identifier, classes=['headerLink'])
        elem.content.insert(0, link)
        return elem


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == '__main__':
    main()
