#!/usr/bin/env python3

import contextlib
import io
import re
import unittest

from src.multiplication import main


class Multiplication(unittest.TestCase):

    def test_lines(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            main()
        result = buf.getvalue().strip()
        lines = result.split('\n')
        self.assertEqual(
            len(lines), 11,
            msg="The output must contain 11 lines (multipliers 0 through "
                "10). Got %d line(s)." % len(lines))

    def test_content(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            main()
        result = buf.getvalue().strip()
        lines = result.split('\n')
        for i, line in enumerate(lines):
            self.assertTrue(
                line.startswith("4 multiplied by %i is" % i),
                msg="Line %d should start with '4 multiplied by %d is'. "
                    "Got %r." % (i, i, line))
            m = re.search("4 multiplied by %i is (.*)" % i, line)
            x = m.group(1)
            self.assertEqual(
                x, str(4 * i),
                msg="4*%i is not %s" % (i, x))


if __name__ == '__main__':
    unittest.main()
