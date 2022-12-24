class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):

    def test_worker_is_initialized_correctly(self):
        # Arrange
        worker = Worker("Test", 100, 13)
        # Act ^^^
        # Assert
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(13, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_increase(self):
        # arrange
        worker = Worker("Test", 100, 13)
        self.assertEqual(13, worker.energy)

        # Act
        worker.rest()

        # Assert
        self.assertEqual(14, worker.energy)

    def test_negative_energy_work_raises(self):
        worker = Worker("Test", 100, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_negative_enertgy_raises(self):
        worker = Worker("Test", 100, -100)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_salary_increase(self):
        worker = Worker("Test", 100, 13)

        self.assertEqual(0, worker.money)

        worker.work()

        # self.assertEqual(0 + worker.salary, worker.money)
        self.assertEqual(100, worker.money)

        worker.work()

        self.assertEqual(200, worker.money)

    def test_energy_is_decrased_after_work(self):
        worker = Worker("Test", 100, 13)

        self.assertEqual(13, worker.energy)

        worker.work()

        self.assertEqual(12, worker.energy)

    def test_info_method(self):
        worker = Worker("Test", 100, 13)

        self.assertEqual("Test has saved 0 money.", f'{worker.name} has saved {worker.money} money.')

if __name__ == "__main__":
    main()

