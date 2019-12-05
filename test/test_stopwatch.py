import unittest
import time
from thym.thym.stopwatch import Stopwatch

class TestStopwatch(unittest.TestCase):

    def stopped(self, name):
        print("Stopwatch: " + name)

    def test_init(self):
        t = Stopwatch()
        self.assertIsNotNone(t)

    def test_running_start(self):
        t = Stopwatch()
        t.start()
        self.assertEqual(t.running, True)

    def test_running_stop(self):
        t = Stopwatch()
        t.start()
        t.stop()
        self.assertEqual(t.running, False)

    def test_stop(self):
        t = Stopwatch()
        t.start()
        time.sleep(2)
        t.stop()
        self.assertAlmostEqual(2, t.elapsed, places=2)

    def test_callback(self):
        t = Stopwatch(self.stopped, args=["test_callback"])
        t.start()
        time.sleep(2)
        t.stop()
        self.assertIsNotNone(t._f)

if __name__ == '__main__':
    unittest.main()
