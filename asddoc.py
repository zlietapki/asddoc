#!/usr/bin/env python3
import sys
import os
import re


BASEDIR = '~/Dropbox'
VIEWER = 'code'


def show_help():
    print(f"Usage: {os.path.basename(__file__)} <command>")
    sys.exit()


def resolve_path(doc):
    basedir = os.path.expanduser(BASEDIR)

    if not re.search('/', doc):
        res = os.path.join(basedir, doc, doc + '.md')
        return res

    res = os.path.join(basedir, doc + '.md')
    return res


def main():
    doc_path = resolve_path(sys.argv[1])
    os.system(f'{VIEWER} {doc_path}')
    exit()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        show_help()

    main()
