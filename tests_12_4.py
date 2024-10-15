import logging
import unittest
import runner_2

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, '')
    def test_walk(self):
        try:
            test_people = runner_2.Runner('test_people', -5)
            for _ in range(10):
                test_people.walk()
            self.assertEqual(test_people.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner')


    @unittest.skipIf(is_frozen == True, '')
    def test_run(self):
        try:
            test_people = runner_2.Runner(54)
            for _ in range(10):
                test_people.run()
            self.assertEqual(test_people.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner')

    @unittest.skipIf(is_frozen == True, '')
    def test_challenge(self):
        test_people_1 = runner_2.Runner('test_people_1')
        test_people_2 = runner_2.Runner('test_people_2')
        for _ in range(10):
            test_people_1.run()
            test_people_2.walk()
        self.assertNotEqual(test_people_1.distance, test_people_2.distance)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    unittest.main()