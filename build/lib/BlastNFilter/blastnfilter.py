#!/usr/bin/env python

__author__ = 'robswift'

import sys
from BlastNFilter.Utilities import IOParser
from BlastNFilter.Utilities import Run


def main(argv=[__name__]):
    itf = IOParser.interface(argv[1:])
    options = IOParser.SplitInput(itf)
    Run.run(options)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
