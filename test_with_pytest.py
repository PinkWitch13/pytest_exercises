"""Pytest use 'assert' keyword 
to specify what output is expected 
- just by prefixing it, 
and functions name prefixed by 
'test' word. Economical in coding.
tests should evaluate to True:
To run:
    $ pytest
"""

def test_always_passes():
    assert True

def test_always_fails():
    assert False

    