import unittest
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, '')
    def test_walk(self):
        test_people = runner.Runner('test_people')
        for _ in range(10):
            test_people.walk()
        self.assertEqual(test_people.distance, 50)

    @unittest.skipIf(is_frozen == True, '')
    def test_run(self):
        test_people = runner.Runner('test_people')
        for _ in range(10):
            test_people.run()
        self.assertEqual(test_people.distance, 100)

    @unittest.skipIf(is_frozen == True, '')
    def test_challenge(self):
        test_people_1 = runner.Runner('test_people_1')
        test_people_2 = runner.Runner('test_people_2')
        for _ in range(10):
            test_people_1.run()
            test_people_2.walk()
        self.assertNotEqual(test_people_1.distance, test_people_2.distance)
        

class TournamentTest(unittest.TestCase):
    is_frozen = True
    
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    
    @classmethod
    def tearDownClass(cls):
        for test in cls.all_results.values():
            print(test)

    def setUp(self):
        self.dist = 90
        self.usein = runner.Runner('Усэйн', 10)
        self.andrey = runner.Runner('Андрей', 9)
        self.nik = runner.Runner('Ник', 3)

    
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_start_1(self):
        tnm = runner.Tournament(self.dist, self.usein, self.nik)
        TournamentTest.all_results[1] = tnm.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())], 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_start_2(self):
        tnm = runner.Tournament(self.dist, self.andrey, self.nik)
        TournamentTest.all_results[2] = tnm.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())], 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_start_3(self):
        tnm = runner.Tournament(self.dist, self.andrey, self.usein, self.nik)
        TournamentTest.all_results[3] = tnm.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())], 'Ник')        


if __name__ == "__main__":
    unittest.main()