from project.hero import Hero
from unittest import TestCase, main


class heroTest(TestCase):

    def test_hero_init_username(self):
        hero = Hero("Alex Malinov", 69, 100, 42)

        self.assertEqual("Alex Malinov", hero.username)

    def test_hero_init_level(self):
        hero = Hero("Alex Malinov", 69, 100, 42)

        self.assertEqual(69, hero.level)

    def test_hero_init_health(self):
        hero = Hero("Alex Malinov", 69, 100, 42)

        self.assertEqual(100, hero.health)

    def test_hero_init_damage(self):
        hero = Hero("Alex Malinov", 69, 100, 42)

        self.assertEqual(42, hero.damage)

    def test_hero_battle_oneself(self):
        hero = Hero("Alex Malinov", 69, 100, 42)
        enemy = Hero("Alex Malinov", 69, 100, 42)

        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_battle_zero_health(self):
        hero = Hero("Alex Malinov", 69, 0, 42)
        enemy = Hero("Arch Nemesis", 69, 100, 42)

        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_hero_battle_negative_health(self):
        hero = Hero("Alex Malinov", 69, -100, 42)
        enemy = Hero("Arch Nemesis", 69, 100, 42)

        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_hero_battle_enemy_negative_health(self):
        hero = Hero("Alex Malinov", 69, 100, 42)
        enemy = Hero("Arch Nemesis", 40, -15, 30)

        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)

        self.assertEqual("You cannot fight Arch Nemesis. He needs to rest", str(ex.exception))

    def test_hero_battle_draw(self):
        hero = Hero("Alex Malinov", 69, 100, 42)
        enemy = Hero("Arch Nemesis", 40, 100, 30)

        self.assertEqual("Draw", hero.battle(enemy))

    def test_hero_battle_win_return(self):
        hero = Hero("Alex Malinov", 10, 100, 15)
        enemy = Hero("Arch Nemesis", 5, 100, 10)

        self.assertEqual("You win", hero.battle(enemy))

    def test_hero_battle_win_level(self):
        hero = Hero("Alex Malinov", 10, 100, 15)
        enemy = Hero("Arch Nemesis", 5, 100, 10)

        hero.battle(enemy)

        self.assertEqual(11, hero.level)

    def test_hero_battle_win_hp(self):
        hero = Hero("Alex Malinov", 10, 100, 15)
        enemy = Hero("Arch Nemesis", 5, 100, 10)

        hero.battle(enemy)

        self.assertEqual(55, hero.health)

    def test_hero_battle_win_damage(self):
        hero = Hero("Alex Malinov", 10, 100, 15)
        enemy = Hero("Arch Nemesis", 5, 100, 10)

        hero.battle(enemy)

        self.assertEqual(20, hero.damage)

    def test_hero_battle_lose_return(self):
        hero = Hero("Alex Malinov", 5, 100, 10)
        enemy = Hero("Arch Nemesis", 15, 100, 10)

        self.assertEqual("You lose", hero.battle(enemy))

    def test_hero_battle_lose_level(self):
        hero = Hero("Alex Malinov", 5, 100, 10)
        enemy = Hero("Arch Nemesis", 15, 100, 10)

        hero.battle(enemy)

        self.assertEqual(16, enemy.level)

    def test_hero_battle_lose_hp(self):
        hero = Hero("Alex Malinov", 5, 100, 10)
        enemy = Hero("Arch Nemesis", 15, 100, 10)

        hero.battle(enemy)

        self.assertEqual(55, enemy.health)

    def test_hero_battle_lose_damage(self):
        hero = Hero("Alex Malinov", 5, 100, 10)
        enemy = Hero("Arch Nemesis", 15, 100, 10)

        hero.battle(enemy)

        self.assertEqual(15, enemy.damage)

    def test_hero_string_repr(self):
        hero = Hero("Alex Malinov", 5, 100, 10)

        correct = f"Hero Alex Malinov: 5 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 10\n"

        self.assertEqual(correct, hero.__str__())


if __name__ == "__main__":
    main()

