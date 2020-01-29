import click


class BMI:
    def __init__(self, feet, inches, weight):
        self.feet = feet
        self.inches = inches
        self.weight = weight

    def calculate(self):
        self.feet = float(self.feet)
        self.inches = float(self.inches)
        self.weight = float(self.weight)
        self.weight = float(self.weight) * float(0.45)
        height = float(self.feet) * float(12.0)
        height = float(height) + float(self.inches)
        height = float(height) * float(0.025)
        height = float(height) * float(height)
        total = float(self.weight) / float(height)
        click.echo("\n\n=====================")
        click.echo('BMI: %.2f' % total)
        if total < 18.5:
            click.echo("\nYou are underweight.")
        if 18.5 <= total <= 24.9:
            click.echo("\nYou are normal weight.")
        if 25 <= total <= 29.9:
            click.echo("\nYou are overweight.")
        if total > 30:
            click.echo("\nYou are obese.")
        click.echo("=====================\n\n")
