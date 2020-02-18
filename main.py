import click
from bmiClass import BMI
from retireClass import Retire


@click.command()
@click.option('--func', prompt='Press enter the number for your desired option:\n1 to use the BMI Calculator \n2 to use the Retirement Calculator \n3 to exit\n',
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
        click.echo("\n\n======================================================\n")
        click.echo("***ERROR: Please enter either a 1, 2, or 3. Try again.")
        click.echo("\n======================================================\n\n")
        main()


@click.command()
@click.option('--feet', prompt='\n\nEnter your height: \nfeet',
              help='Your height, rounded down to the nearest whole number. Ex: if you are 5\'10\" then you would put 5')
@click.option('--inches', prompt='inches',
              help='Your height\'s remainder in inches. Ex: if you are 5\'10\" then you would put 10')
@click.option('--weight', prompt='Enter your weight in pounds',
              help='Your weight in pounds')
def bmi(feet, inches, weight):
    """A simple program that will calculate the user's BMI and tell them their weight category"""
    tmp = BMI(feet, inches, weight,)
    tmp.calculate
    main()


@click.command()
@click.option('--age', prompt='\n\nEnter your age ',
              help='Your age in years')
@click.option('--salary', prompt='Enter your yearly salary ',
              help='Your salary')
@click.option('--saved', prompt='Enter the percentage saved as a decimal. ',
              help='Percentage saved as a decimal. Ex: 35% would be 0.35')
@click.option('--goal', prompt='Enter your retirement goal in dollars ',
              help='Your retirement goal')
def retire(age, salary, saved, goal):
    """A simple function to determine the age that the user will reach their retirement goal"""
    tmp = Retire(age, salary, saved, goal)
    tmp.calculate
    main()


if __name__ == '__main__':
    main()
