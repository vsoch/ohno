__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from ohno.logparser import parse_output
from jinja2 import Template


class Result:
    """A base result handles parsing a command run."""

    def __init__(self, **kwargs):
        self._result = kwargs
        self.errors = []
        self.warnings = []

    def __getattr__(self, key):
        return self._result.get(key)

    def to_dict(self):
        res = self._result
        res.update(
            {"command": self.command, "errors": self.errors, "warnings": self.warnings}
        )
        return res

    @property
    def command(self):
        cmd = self.cmd
        if cmd:
            return " ".join(cmd)
        return ""


md_template = """### To Reproduce

```bash
$ {{ res.command }}
```            

### Environment

{% if res.version %}- Version: {{ res.version }}  {% endif %}
- Host:
  {% for k, v in res.host.items() %}- {{k}}: {{v}}
  {% endfor %}
### Errors

```bash
{% for error in errors %}{{ error.text }}
{% endfor %}
```"""


class MarkdownResult(Result):
    def parse(self):
        if self.returncode != 0:
            entries = parse_output(self.error)
            self.errors = entries["errors"]
            self.warnings = entries["warnings"]
            template = Template(md_template)
            return template.render(res=self, errors=entries["errors"])
        else:
            return "No errors."
