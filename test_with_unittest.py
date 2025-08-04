from unittest import TestCase

"""unittest is a build-in module for 
tests, following Arrenge-Act-Assert 
model. Significant amount of code needed. 
To run unittests from the 
command line:
    $ python -m unittest discover
"""

class TryTesting(TestCase):
    def test_always_pases(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

