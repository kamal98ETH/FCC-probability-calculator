import copy
import random

# Consider using the modules imported above.


class Hat:
    contents = list()
    save = list()

    def __init__(self, **balls):
        for (color, num) in balls.items():
            color = (color + " ") * num
            self.contents = self.contents + color.split()

    def draw(self, draw_num):
        drawn = list()
        # saving a copy of the list contents
        self.save = copy.deepcopy(self.contents)
        # drawing from the contents list using a random number and putting the ball in drawn list
        for i in range(draw_num):
            if len(self.contents) == 0:
                # Checking if the contents list is empty and filling it up with the save copy we made
                self.contents = copy.deepcopy(self.save)
                n = random.randint(0, len(self.contents) - 1)
                drawn.append(self.contents.pop(n))
            else:
                n = random.randint(0, len(self.contents) - 1)
                drawn.append(self.contents.pop(n))

        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    found = 0
    # List of expected balls
    wantedList = list()
    for (k, v) in expected_balls.items():
        b = (k + " ") * v
        wantedList = wantedList + b.split()

    # repeating the experiment:
    for i in range(num_experiments):
        check = copy.deepcopy(wantedList)
        # Draw balls from the hat
        draw = hat.draw(num_balls_drawn)
        hat.contents = hat.save

        # Checking if we got the wanted balls
        for item in draw:
            rep = reversed(range(len(check)))
            for i in rep:
                if item == check[i]:
                    check.remove(check[i])
                    break
        if check != []:
            continue
        else:
            found = found + 1

    prob = found / num_experiments
    return prob
