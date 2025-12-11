import sys
import time
from rich.progress import track
from faker import Faker
from colorama import init, Fore, Back, Style

fake = Faker()

input(Back.BLACK + Style.BRIGHT + Fore.RED + "Welcome to The Fake ID Generator!!!\nPress ENTER to continue\n")

# Ask user what they want
gender = input("Do you want a male or female name? (m/f)\n").lower()
a = input("Do you want an address? y/n\n").lower()
p = input("Do you want a phone number? y/n\n").lower()
s = input("Do you want a social security number? y/n\n").lower()
d = input("Do you want a date of birth? y/n\n").lower()
jc = input("Do you want a job? y/n\n").lower()

if d == "y":
    minimum_age = int(input("What do you want your minimum age to be?\n"))
    maximum_age = int(input("What do you want your maximum age to be?\n"))

print(Style.RESET_ALL + "")

for step in track(range(50), description="[green]Processing..."):
    time.sleep(0.05)

print(Back.BLACK + Style.BRIGHT + Fore.RED + "\n--- Generated Fake ID ---\n")



# Name based on gender
if gender == "m":
    print(fake.name_male())
elif gender == "f":
    print(fake.name_female())
else:
    print(fake.name())
# Optional fields
if a == "y":
    print(fake.address())

if jc == "y":
    print(fake.job())
    print(fake.company())
if p == "y":
    print(fake.numerify('(###) ### ####'))

if d == "y":
    print(str(fake.date_of_birth(minimum_age=minimum_age, maximum_age=maximum_age)))

if s == "y":
    print(fake.ssn())

input("\nThank you for using The Fake ID Generator!!!\n\nPress ENTER to exit...")