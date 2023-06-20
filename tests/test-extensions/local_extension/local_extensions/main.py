"""Provides custom extension, exposing a ``foobar`` filter."""

from jinja2.ext import Extension
from cookiecutter.utils import simple_filter, simple_test


class FoobarExtension(Extension):
    """Simple jinja2 extension for cookiecutter test purposes."""

    def __init__(self, environment):
        """Foobar Extension Constructor."""
        super().__init__(environment)
        environment.filters['foobar'] = lambda v: v * 2


@simple_filter
def simplefilterextension(v):
    """Provide a simple function-based filter extension."""
    return v.upper()


@simple_test
def palindrome(v):
    """Provide a simple function-based test extension."""
    v_reverse =  v[::-1]
    return v_reverse == v
