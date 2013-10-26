""" This is a useful description for the Python program that
    will be printed out to the user.
"""
import sys
import argparse
import logging

LOGGING_FORMAT = "%(message)s"

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    p = argparse.ArgumentParser(description=__doc__)
    """ The following are a set of common examples for arguments
        with the argparse module.
    
    p.add_argument("singl_iteme", help='')
    p.add_argument("multiple_items", nargs="+", help='')
    p.add_argument("-o", "--outputdir", default=None, help='')
    p.add_argument("-unixtime", "-u", action="store_true", help='')
    """
    p.add_argument("-verbose", "-v", action='count', help='')

    args = p.parse_args(argv)
    fmt = LOGGING_FORMAT

    if args.verbose == 1:
        logging.basicConfig(level=logging.INFO, format=fmt)
    elif args.verbose == 2:
        logging.basicConfig(level=logging.DEBUG, format=fmt)
    else:
        logging.basicConfig(level=logging.WARNING, format=fmt)

    logger = logging.getLogger()
    logger.warn('hello')

    return 0

if __name__ == "__main__":
    sys.exit(main())
