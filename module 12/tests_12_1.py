import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_people = runner.Runner('test_people')
        for _ in range(10):
            test_people.walk()
        self.assertEqual(test_people.distance, 50)

    def test_run(self):
        test_people = runner.Runner('test_people')
        for _ in range(10):
            test_people.run()
        self.assertEqual(test_people.distance, 100)

    def test_challenge(self):
        test_people_1 = runner.Runner('test_people_1')
        test_people_2 = runner.Runner('test_people_2')
        for _ in range(10):
            test_people_1.run()
            test_people_2.walk()
        self.assertNotEqual(test_people_1.distance, test_people_2.distance)


if __name__ == "__main__":
    unittest.main()