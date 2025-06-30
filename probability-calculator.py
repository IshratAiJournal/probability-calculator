import copy
import random


class Hat:
    def __init__(self, **balls):
        """
        Accepts keyword arguments like Hat(red=3, blue=2)
        and stores a list of ball colors in self.contents.
        """
        self.contents = []
        for color, qty in balls.items():      # fixed items()
            self.contents.extend([color] * qty)

    def draw(self, num_balls):
        """
        Randomly remove num_balls from the hat without replacement.
        If num_balls >= contents length, return all remaining balls
        and leave the hat empty.
        """
        if num_balls >= len(self.contents):
            all_balls = self.contents.copy()
            self.contents.clear()
            return all_balls

        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Estimate probability of drawing at least expected_balls.
    """
    success_count = 0

    for _ in range(num_experiments):
        trial_hat = copy.deepcopy(hat)
        drawn = trial_hat.draw(num_balls_drawn)

        # count drawn colors
        drawn_count = {}
        for color in drawn:
            drawn_count[color] = drawn_count.get(color, 0) + 1

        # check expectation
        meets_expectation = True
        for color, qty in expected_balls.items():
            if drawn_count.get(color, 0) < qty:
                meets_expectation = False
                break

        if meets_expectation:
            success_count += 1

    probability = success_count / num_experiments
    return probability
