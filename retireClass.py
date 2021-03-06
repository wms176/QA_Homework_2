import click


class Retire:
    def __init__(self, age, salary, saved, goal):
        self.age = age
        self.salary = salary
        self.saved = saved
        self.goal = goal

    @property
    def calculate(self):
        self.salary = float(self.salary)
        self.saved = float(self.saved)
        self.saved = float(self.saved) * float(self.salary)
        self.saved = float(self.saved) * 1.35
        self.goal = float(self.goal)
        total = float(self.goal) / float(self.saved)
        self.age = int(self.age) + round(total)
        if self.age >= 100:
            click.echo("\n\nThat is not a possible goal.")
        else:
            click.echo("\n\n=====================")
            click.echo('Years until goal is met: %.2f ' % total)
            click.echo('\nAge: %d' % self.age)
            click.echo("=====================\n\n")

            # Returned for the test program to use
            return self.age
