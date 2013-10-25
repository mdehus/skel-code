import sys
import argparse
import logging

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    description = ''' This tool takes one, or multiple Echo360 lecture(s), and
                      builds self-contained copies, stored in zip files. '''

    p = argparse.ArgumentParser(description=description)
    p.add_argument("lectures", nargs="+",
                   help="Path to Echo360 lecture or lectures to upload.")
    p.add_argument("-o", "--outputdir", default=None,
                   help='''Directory to save the resulting zip file(s). 
                           Files will be named automatically by their 
                           lecture GUID.  Default is /tmp''')
    p.add_argument("-verbose", "-v", action='count',
                   help='''-v prints informational messages, 
                            -vv prints debug messages.''')

    args = p.parse_args(argv)
    fmt = "%(message)s"

    if args.verbose == 1:
        logging.basicConfig(level=logging.INFO, format=fmt)
    elif args.verbose == 2:
        logging.basicConfig(level=logging.DEBUG, format=fmt)
    else:
        logging.basicConfig(level=logging.WARNING, format=fmt)

    return 0

if __name__ == "__main__":
    sys.exit(main())
