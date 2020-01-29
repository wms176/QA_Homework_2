import click


class Retire:
    def __init__(self, age, salary, saved, goal):
        self.age = age
        self.salary = salary
        self.saved = saved
        self.goal = goal

    def calculate(self):
        self.salary = float(self.salary)
        self.saved = float(self.saved)
        self.saved = float(self.saved) * float(self.salary)
        self.saved = float(self.saved) * 1.35
        self.goal = float(self.goal)
        total = float(self.goal) / float(self.saved)
        self.age = int(self.age) + round(total)
        click.echo("\n\n=====================")
        click.echo('Years until goal is met: %.2f ' % total)
        click.echo('\nAge: %d' % self.age)
        click.echo("=====================\n\n")