import time


class Stopwatch(object):

    def __init__(self, callback_func=None, args=None, kwargs=None):
        self._f = callback_func
        self._args = args if args is not None else []
        self._kwargs = kwargs if kwargs is not None else {}
        self._start_time = None
        self._elapsed_time = None
        self._running = False

    def _callback(self):
        if self._f:
            self._f(*self._args, **self._kwargs)

    def stop(self):
        if self._running:
            self._elapsed_time = time.time() - self._start_time
            self._running = False
            self._callback()

    def start(self):
        if not self._running:
            self._start_time = time.time()
            self._running = True

    def reset(self):
        self._start_time = None
        self._elapsed_time = None
        self._running = False

    @property
    def elapsed(self):
        return self._elapsed_time

    @property
    def running(self):
        return self._running
