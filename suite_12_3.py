import unittest
from task_12_1 import RunnerTest
from task_12_2 import TournamentTest

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)