import random

class Dice:
    def __init__(self, times_rolled: int, num_sides: int):
        self.times_rolled = times_rolled
        self.num_sides = num_sides

    def roll_dice(times_rolled: int, num_sides: int) -> int:
        i = 0
        sum = 0

        while i < times_rolled:
            sum += random.randint(1, num_sides)
            i += 1

        return sum