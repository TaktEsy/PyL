import unittest
from add import runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        obj = runner.Runner("name")
        for i in range(0,10):
            res = obj.walk()
        self.assertEqual(obj.distance, 50)
    def test_run(self):
        obj = runner.Runner("name")
        for i in range(0, 10):
            res = obj.run()
        self.assertEqual(obj.distance, 100)
    def test_challenge(self):
        obj = runner.Runner("name")
        obj2 = runner.Runner("name")
        for i in range(0, 10):
            res = obj.run()
            res2 = obj.walk()
        self.assertNotEqual(obj2.run(), obj.walk())


if __name__ == 'name':
    unittest.main()