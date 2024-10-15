import unittest
import tests_12_3

trnTs = unittest.TestSuite()
trnTs.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
trnTs.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(trnTs)
