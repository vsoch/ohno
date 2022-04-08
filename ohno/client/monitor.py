__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import ohno.main.client as client
from ohno.logger import logger
import shlex


def main(args, extra):

    # Create a queue object, run the command to match to an executor
    monitor = client.Monitor()

    # Don't allow an empty command!
    if not args.cmd:
        logger.exit("Please provide a command to execute.")

    command = args.cmd

    # --help needs to be quoted, make sure if provided, gets parsed into command
    if any(["--help" in x for x in args.cmd]):
        command = []
        for item in args.cmd:
            command += shlex.split(item)

    # Extra might include unparsed arguments
    task = monitor.run(command=command + extra)
    md = task.parse()
    print(md)
