import unittest
import runner


class TournamentTest(unittest.TestCase):
    
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

    

    def test_start_1(self):
        tnm = runner.Tournament(self.dist, self.usein, self.nik)
        TournamentTest.all_results[1] = tnm.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())], 'Ник')

    def test_start_2(self):
        tnm = runner.Tournament(self.dist, self.andrey, self.nik)
        TournamentTest.all_results[2] = tnm.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())], 'Ник')

    def test_start_3(self):
        tnm = runner.Tournament(self.dist, self.andrey, self.usein, self.nik)
        TournamentTest.all_results[3] = tnm.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())], 'Ник')        


if __name__ == "__main__":
    unittest.main()