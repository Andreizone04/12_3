import unittest
from runner import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runners = [Runner('Усэйн', 10), Runner('Андрей', 9), Runner('Ник', 3)]

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            for x in result:
                print(f' {x} {result[x]} ', end=' ')
            print()

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_runners_1(self):
        route = Tournament(90, *[self.runners[0], self.runners[2]])
        result = route.start()
        self.all_results.append(result)
        self.assertTrue(result[2] == self.runners[2])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_runners_2(self):
        route = Tournament(90, *[self.runners[1], self.runners[2]])
        result = route.start()
        self.all_results.append(result)
        self.assertTrue(result[2] == self.runners[2])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_runners_3(self):
        route = Tournament(90, *self.runners)
        result = route.start()
        self.all_results.append(result)
        self.assertTrue(result[3] == self.runners[2])


if __name__ == "__main__":
    unittest.main()
