import unittest

class TestSetup(unittest.TestCase):

    def test_can_run_test_cases(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()