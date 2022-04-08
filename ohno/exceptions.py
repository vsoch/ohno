__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"


class MissingEnvironmentVariable(RuntimeError):
    """Thrown if a required environment variable is not provided."""

    def __init__(self, varname, *args, **kwargs):
        super(MissingEnvironmentVariable, self).__init__(*args, **kwargs)
        self.varname = varname

    def __str__(self):
        return "Missing environment variable '{}' is required".format(self.varname)


class DirectoryNotFoundError(FileNotFoundError):
    """Thrown if a directory is not found"""

    def __init__(self, dirname, reason, *args, **kwargs):
        super(DirectoryNotFoundError, self).__init__(*args, **kwargs)
        self.dirname = dirname
        self.reason = reason

    def __str__(self):
        return "{} {}.".format(self.dirname, self.reason)


class MissingImportError(ImportError):
    """Thrown if a library is missing."""

    def __init__(self, name, reason, *args, **kwargs):
        super(MissingImportError, self).__init__(*args, **kwargs)
        self.name = name
        self.reason = reason

    def __str__(self):
        return "{} {}.".format(self.name, self.reason)


class NotSupportedError(NotImplementedError):
    """Thrown if functionality isn't supported, and not implemented."""

    def __init__(self, reason, *args, **kwargs):
        super(NotSupportedError, self).__init__(*args, **kwargs)
        self.reason = reason

    def __str__(self):
        return self.reason


class UnrecognizedTargetError(ValueError):
    """Thrown if an unrecognized target is given for an action"""

    def __init__(self, name, reason="", *args, **kwargs):
        super(UnrecognizedTargetError, self).__init__(*args, **kwargs)
        self.name = name
        self.reason = reason

    def __str__(self):
        return "Unrecognized target {} {}.".format(self.name, self.reason)


class OutputParsingError(ValueError):
    """Thrown if an output cannot be correctly parsed"""

    def __init__(self, reason="", *args, **kwargs):
        super(OutputParsingError, self).__init__(*args, **kwargs)
        self.reason = reason

    def __str__(self):
        return self.reason
