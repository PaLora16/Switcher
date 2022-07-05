import emoji

from switcher_definition import switcher

"""
This example use decorators for emulation of switch expression
in Python 3.9 and lower
"""

# Decorator logic which cannot be achieved via lambda


def not_int(x: any) -> bool:
    return not isinstance(x, int)


def not_day_of_week(x: int) -> bool:
    return x not in range(1, 8)

# according to day, you get your emoji
@switcher
def how_you_feel(day_of_the_week: int = None) -> None:
    # Next you can add another logic following switcher
    pass


"""
Functions serves as code block following 
"case" expression in standard "switch" expression.
Registered function substitue comparison expression "case x:"
"""


@how_you_feel.register(not_int)
def not_allowed_arguments() -> None:
    print(emoji.emojize(":prohibited: You suck trying to cheat my AI-based algorithm!"))
    exit(1)


@how_you_feel.register(lambda x: x in {1, 2})
def day_1_2() -> None:
    print(emoji.emojize(":grimacing_face: It seems you are at work!"))


@how_you_feel.register(lambda x: x in {3, 4})
def day_3_4() -> None:
    print(emoji.emojize(":hot_face: Weekend is miles away !"))


@how_you_feel.register(lambda x: x in {5, 6})
def day_5_6() -> None:
    print(emoji.emojize(":beer_mug: Payday comes !"))


@how_you_feel.register(lambda x: x == 7)
def day_7() -> None:
    print(emoji.emojize(":face_vomiting: New week ahead !"))


@how_you_feel.register(not_day_of_week)
def default() -> None:
    print(emoji.emojize(":confounded_face: Could not count from 1 to 7 ?"))
