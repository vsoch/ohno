#!/usr/bin/python

# Copyright (C) 2022 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import ohno.main.client as client
import ohno.utils as utils
import os

root = os.path.dirname(utils.get_installdir())


def test_monitor():
    """
    Test ohno monitor
    """
    monitor = client.Monitor()
    script = os.path.join(root, "examples", "monitor", "failure.py")
    res = monitor.run(["python", script])
    content = res.parse()
    assert "error: We cannot do that thing." in content
    assert len(res.errors) == 1
    assert not res.warnings
    dumped = res.to_dict()
    for key in [
        "pwd",
        "user",
        "timestamp",
        "version",
        "host",
        "output",
        "error",
        "returncode",
        "pid",
        "cmd",
        "status",
        "command",
        "errors",
        "warnings",
    ]:
        assert key in dumped


def test_parse():
    """
    Test ohno parse
    """
    monitor = client.Monitor()
    script = os.path.join(root, "examples", "parse", "spack-error.txt")
    res = monitor.load(script)
    content = res.parse()
    assert "[all-recursive] Error" in content
    assert len(res.errors) == 34
    assert not res.warnings
    dumped = res.to_dict()
    for key in [
        "timestamp",
        "error",
        "command",
        "errors",
        "warnings",
    ]:
        assert key in dumped
