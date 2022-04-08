__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from ohno.main.executor import ShellExecutor, BaseExecutor
import ohno.main.result as result
import ohno.utils as utils
from ohno.logger import logger
import os


class Monitor:
    """Monitor a running process, collecting the output and parsing for errors.

    We also parse those errors and return to the user in a useful format for
    submitting a bug report.
    """

    def __init__(self):
        self.errors = []
        self.warnings = []
        self.tasks = {}

    def load(self, logfile):
        """
        Parse a logfile and return the result.
        """
        if not logfile or not os.path.exists(logfile):
            logger.exit(f"{logfile} does not exist!")

        executor = BaseExecutor()
        executor.data["error"] = utils.read_file(logfile)
        return result.MarkdownResult(**executor.export())

    def run(self, command, message=None):
        """
        Given a command, run it and capture (and parse) errors.
        """
        executor = ShellExecutor(command)
        executor.execute(message=message)
        res = executor.export()

        # Save the task for later
        self.tasks[executor.command] = executor

        if res["returncode"] == 0:
            logger.info(f"{executor.summary()}")
        else:
            logger.error(f"{executor.summary()}")
        return result.MarkdownResult(**executor.export())
