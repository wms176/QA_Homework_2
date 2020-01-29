import click


@click.command()
@click.option('--func', prompt='Press 1 to use the BMI Calculator, 2 to use the Retirement Calculator, or 3 to exit',
              help='The person to greet.')
def main(func):
    """Simple program that greets NAME for a total of COUNT times."""
    if int(func) == 1:
        bmi()
    elif int(func) == 2:
        retire()
    elif int(func) == 3:
        return
    else:
        click.echo("***ERROR: Please enter either a 1 or a 2. Try again.")
        main()


@click.command()
@click.option('--feet', prompt='Enter your height: \nfeet',
              help='The person to greet.')
@click.option('--inches', prompt='inches',
              help='The person to greet.')
@click.option('--weight', prompt='Enter your weight in pounds',
              help='The person to greet.')
def bmi(feet, inches, weight):
    """Enter a description here"""
    feet = float(feet)
    inches = float(inches)
    weight = float(weight)
    weight = float(weight) * float(0.45)
    height = float(feet) * float(12.0)
    height = float(height) + float(inches)
    height = float(height) * float(0.025)
    height = float(height) * float(height)
    total = float(weight) / float(height)
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

    main()


@click.command()
@click.option('--age', prompt='Enter your age ',
              help='The person to greet.')
@click.option('--salary', prompt='Enter your salary ',
              help='The person to greet.')
@click.option('--saved', prompt='Enter the percentage saved as a decimal ',
              help='The person to greet.')
@click.option('--goal', prompt='Enter your retirement goal in dollars ',
              help='The person to greet.')
def retire(age, salary, saved, goal):
    """Enter a description here"""
    salary = float(salary)
    saved = float(saved)
    saved = float(saved) * float(salary)
    saved = float(saved) * 1.35
    goal = float(goal)
    total = float(goal) / float(saved)
    age = int(age) + round(total)
    click.echo("\n\n=====================")
    click.echo('Years until goal is met: %.2f ' % total)
    click.echo('\nAge: %d' % age)
    click.echo("=====================\n\n")

    main()


if __name__ == '__main__':
    main()
