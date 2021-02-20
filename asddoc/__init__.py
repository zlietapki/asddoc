import os
import os.path
import sys
from pathlib import Path
from . import cfg


# name -> name/name.md || name.md
# folder/name -> folder/name/name.md || folder/name.md


def resolve_doc(doc):
    basedir = Path(os.path.expanduser(cfg.BASEDIR))

    full_doc = os.path.join(basedir, doc)
    real_full_doc = os.path.realpath(full_doc)

    if os.path.isdir(real_full_doc):
        doc_basename = os.path.basename(real_full_doc)  # tail can changed because of symlink
        res = os.path.join(real_full_doc, doc_basename + '.md')
        return res

    res = real_full_doc + '.md'
    return res


def main():
    arg = sys.argv[1]

    # self edit
    if arg == 'add':
        os.system(f'code {__file__}')
        return

    doc = resolve_doc(sys.argv[1])
    os.system(f'{cfg.VIEWER} {doc}')
    exit()


def show_help():
    print(f"Usage: {os.path.basename(__file__)} <command>")
    sys.exit()
