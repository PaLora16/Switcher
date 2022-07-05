import argparse

import sys

from switcher_decorator import how_you_feel

# Create the parser
day_of_the_week_parser = argparse.ArgumentParser(
    description='Input day of the weeek')

# Add the arguments
day_of_the_week_parser.add_argument('day_of_the_week',
                                    metavar='day',
                                    type=int,
                                    help='Entering day of the week, you get your personalized horoscop. Just enter 1-Monday,2-Tuesday...7-Sunday')

# Execute the parse_args() method
args = day_of_the_week_parser.parse_args()

day_of_the_week = args.day_of_the_week

if not day_of_the_week:
    print('Please enter 1-7')
    sys.exit()

how_you_feel(day_of_the_week)
