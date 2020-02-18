import click


class BMI:
    def __init__(self, feet, inches, weight):
        self.feet = feet
        self.inches = inches
        self.weight = weight

    @property
    def calculate(self):
        self.feet = float(self.feet)
        self.inches = float(self.inches)
        self.weight = float(self.weight)
        height = (float(self.feet) * 12) + float(self.inches)
        total = (float(self.weight) / float(height) / float(height)) * 703
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

        # Returned for the test program to use
        return '%.1f' % total
