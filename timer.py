#!/usr/bin/env python
"""
A timer as a context manager.

Wraps around a time generator. A custom generator can be passed
to the constructor. The default timer is timeit.default_timer.

This measures wall clock time, not CPU time!
On Unix systems, it corresponds to time.time.
On Windows systems, it corresponds to time.clock.

Example:
>>> with Timer() as timer:
...     for i in xrange(10000000):
...         pass
...
>>> print(timer.start)
1341568310.06
>>> print(timer.end)
1341568310.14
>>> print(timer.elapsed_ms)
73.6618041992
>>> print(timer.elapsed_secs)
0.0736618041992

Written by Balthazar Rouberol - <brouberol@imap.cc>
"""

from timeit import default_timer


class Timer(object):
    """ A timer as a context manager. """

    def __init__(self, timer=default_timer):
        self.timer = default_timer
        # measures wall clock time, not CPU time!
        # On Unix systems, it corresponds to time.time
        # On Windows systems, it corresponds to time.clock

    def __call__(self):
        """Return the current time"""
        return self.timer()

    def __enter__(self):
        self.start = self.timer() # measure start time
        self.end = None
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = self.timer() # measure end time
        self.elapsed_s = self.end - self.start # elapsed time, in seconds
        self.elapsed_ms = self.elapsed_s * 1000  # elapsed time, in milliseconds

    def elapsed(self):
        """Return elapsed time in seconds"""
        if self.end is None:
            return self.timer() - self.start
        else:
            return self.end - self.start

    def elapsed_ms(self):
        """Return elapsed time in milliseconds"""
        if self.end is None:
            return (self.timer() - self.start) * 1000
        else:
            return (self.end - self.start) * 1000
