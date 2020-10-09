123#!/usr/bin/env python3
import sys
from asddoc import main, show_help

if __name__ == "__main__":
    if len(sys.argv) == 1:
        show_help()

    main()
