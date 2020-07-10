import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for colour, number in kwargs.items():
            self.contents += [colour for i in range(number)]

    def get_num_balls(self):
        return len(self.contents)

    def draw(self, number):
        if number >= self.get_num_balls():
            drawn = [*self.contents]
            self.contents = []
        else:
            drawn = []
            for _ in range(number):
                ind = random.randrange(self.get_num_balls())
                drawn.append(self.contents.pop(ind))

        return drawn


def is_contained(expected_balls, drawn_balls):
    for colour, number in expected_balls.items():
        if number > drawn_balls.get(colour, 0):
            return False

    return True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0

    for _ in range(num_experiments):
        current_hat = copy.deepcopy(hat)
        drawn = current_hat.draw(num_balls_drawn)
        drawn_balls = {colour: drawn.count(colour) for colour in set(drawn)}

        if is_contained(expected_balls, drawn_balls):
            successes += 1

    return successes / num_experiments
