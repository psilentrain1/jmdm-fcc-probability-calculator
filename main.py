import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for x, y in kwargs.items():
            i = 0
            while i < y:
                self.contents.append(x)
                i += 1

    def draw(self, n):
        current_draw = []
        """ if n > len(self.contents):
            return current_draw """

        n = min(n, len(self.contents))

        i = 0
        while i < n:
            select = random.randint(0, (len(self.contents) - 1))
            choice = self.contents.pop(select)
            current_draw.append(choice)
            i += 1

        return current_draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = num_experiments
    M = 0
    exp = 0
    while exp < N:
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        current_draw = {}
        for color in draw:
            current_draw[color] = current_draw.get(color, 0) + 1
        if all(
            k in current_draw and current_draw[k] >= expected_balls[k]
            for k in expected_balls
        ):
            M += 1
        exp += 1

    return M / N


hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000,
)
print(probability)
