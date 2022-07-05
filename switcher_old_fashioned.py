import emoji

# according to day, you get your emoji


def how_you_feel(day_of_the_week: int = None) -> None:

    if not isinstance(day_of_the_week, int):
        print(
            emoji.emojize(
                ":prohibited: You suck trying to cheat my AI-based algorithm!"
            )
        )
        exit(1)

    if day_of_the_week in {1, 2}:
        day_1_2()
    elif day_of_the_week in {3, 4}:
        day_3_4()
    elif day_of_the_week in {5, 6}:
        day_5_6()
    elif day_of_the_week == 7:
        day_7()
    else:
        default()


def day_1_2() -> None:
    print(emoji.emojize(":grimacing_face: It seems you are at work!"))


def day_3_4() -> None:
    print(emoji.emojize(":hot_face: Weekend is miles away !"))


def day_5_6() -> None:
    print(emoji.emojize(":beer_mug: Payday comes !"))


def day_7() -> None:
    print(emoji.emojize(":face_vomiting: New weeks ahead !"))


def default() -> None:
    print(emoji.emojize(":confounded_face: Could not count to 7 ?"))
