__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import ohno.main.client as client


def main(args, extra):
    monitor = client.Monitor()
    res = monitor.load(args.logfile)
    md = res.parse()
    print(md)
