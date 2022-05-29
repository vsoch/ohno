__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import shlex
import shutil

from .base import ExecutorBase


class ShellExecutor(ExecutorBase):
    """
    Run a shell command and capture output.
    """

    name = "shell"

    def __init__(self, command=None):
        super().__init__()
        self.reset(command)

    def summary(self):
        if self.data.get("returncode") is not None:
            return "[%s][%s][ret: %s]" % (
                self.name,
                self.command,
                self.data.get("returncode"),
            )
        return "[%s][%s]" % (self.name, self.command)

    def reset(self, command=None):
        """
        refresh output and error streams
        """
        self.data = {
            "output": [],
            "error": [],
            "returncode": None,
            "pid": None,
            "cmd": [],
            "status": None,
        }
        if command:
            self.set_command(command)

    @property
    def command(self):
        return " ".join(self.data.get("cmd", []))

    def set_command(self, cmd):
        """
        Parse a newly provided command.

        parse is called when a new command is provided to ensure we have
        a list. We don't check that the executable is on the path,
        as the initialization might not occur in the runtime environment.
        """
        if not isinstance(cmd, list):
            cmd = shlex.split(cmd)
        self.data["cmd"] = cmd

    def execute(self, cmd=None, message=None):
        """
        Execute a system command and return output and error.

        Execute
        should take a cmd (a string or list) and execute it according to
        the executor. Attributes should be set on the class that are
        added to self.export. Since the functions here are likely needed
        by most executors, we create a self._execute() class that is called
        instead, and can be used by the other executors.
        """
        self.message = message
        return self._execute(cmd)

    def _execute(self, cmd=None):
        """
        Execute a command to the shell.

        The actual class to do the execution - can be used if ShellExecutor
        is used as a super and the class using it defines a custom execute
        """
        # Reset the output and error records
        self.reset(cmd or self.data.get("cmd"))
        cmd = self.data.get("cmd")

        # The executable must be found, return code 1 if not
        executable = shutil.which(cmd[0])
        if not executable:
            self.data["error"] = ["%s not found." % cmd[0]]
            self.data["returncode"] = 1
            return self.data["output"], self.data["error"]

        # remove the original executable
        args = cmd[1:]
        self.data["status"] = "running"

        # Use updated command with executable and remainder (list)
        cmd = [executable] + args

        # Capturing provides temporary output and error files
        capture = self.capture(cmd)
        self.data["pid"] = capture.pid
        self.data["returncode"] = capture.returncode
        self.data["output"] = capture.output
        self.data["error"] = capture.error
        self.data["status"] = "complete"
        return self.data["output"], self.data["error"]

    def get_output(self):
        """
        Returns the output from shell command
        """
        return self.data.get("output")

    def get_error(self):
        """
        Returns the error from shell command
        """
        return self.data.get("error")
