"""Choose Your Own Adventure!"""

from random import randint

points: int = 0
dook_points: int = 0
player: str = ""
playing: bool = True


def main() -> None:
    """Entrypoint/directory of experience."""
    greet()
    global player
    player = player
    decide()
    global points
    global playing
    while playing is False:
        print(f"Great job! You have {points} points so far!")
        decision = int(input("Would you like to take on the same challenge again, try another battle, or go back to the locker room for some more training? Enter '1' for 'Freethrows.' Enter '2' for 'Versus.' Enter '3' to leave: "))
        while (decision == 1 or decision == 2 or decision == 3) is False: 
            decision = int(input("There is not much time left to decide, so stop playing around! Enter '1' for 'Freethrows.' Enter '2' for 'Versus.' Enter '3' to leave: "))
        if decision == 1:
            playing = True
            freethrows()
        if decision == 2:
            playing = True
            versus(points)
        if decision == 3:
            print(f"Hubert Davis: \'Thanks for being honest, {player}. Now get back to the locker room.\'")
            print(f"{player}, thank you for playing! You have accumulated a total of {points} points during your fame! Great job!")
            playing = True


def greet() -> None:
    """Stores the player's name and greets the player."""
    global player
    print("Narrator: \"It's a big day. Today, the UNC Tarheels and the Dook Blue Devils fight on the court for the titles of 'Best Freethrow Basetball Team of the Millennium' and 'Best Versus Basketball Team of the Millennium'! You are the best player on the Tarheels and it is your resposibility to move the Tarheels to the Final Four.\"")
    player = input("I know you are on UNC's starting lineup, but I'm not good with names. What is your name again?: ")
    print(f"Narrator: \"Look, {player}, you cannot mess this up. Every Tarheel is counting on you. The game will be divided into two parts: freethrows and versus. It's game time, you got this!\"")


def freethrows() -> None:
    """One of the two possible interactive paths. Guides player through 'Freethrow' path."""
    global points
    global dook_points
    global playing
    print("Narrator: \"Here's how this works: you will guess a number between 1 and 10 (inclusive). A player from Dook will do the same. There is also a randomly-selected secret number. Once you and Dook select a number, each number is compared to the secret number. The number of points you or Dook accumulate depend on how far the selected number is from the secret number. Closer guesses results in lower point increases and a lower overall score, thus the team who has the LOWEST CUMULATIVE SCORE at the end of ten rounds wins!\"")

    attempts: int = 1

    while attempts <= 10:
        carolina = int(input(f"Referee: \"{player}, enter a number between 1 and 10 (inclusive)\": "))
        while carolina < 1 or carolina > 10:
            carolina = int(input("Referee: \"That's a foul! Enter another number between 1 and 10 (inclusive)\": "))
        print(f"=== Round {attempts} ===")
        secret = randint(1, 10)
        dook = randint(1, 10)
        print(f"Referee: \"Carolina has chosen {carolina} and Dook has chosen {dook}. The secret number was {secret}.\"")
        # I received instructor permission to use the abs() function
        if abs(secret - carolina) < abs(secret - dook):
            print("Referee: \"Carolina has won this round!\"")
        if abs(secret - dook) < abs(secret - carolina):
            print("Referee: \"Dook has won this round!\"")
        if abs(secret - dook) == abs(secret - carolina):
            print("Referee: \"There has been a tie!\"")
        dook_points += abs(secret - dook)
        points += abs(secret - carolina)
        print(f"Carolina has {points} points and Dook has {dook_points} points.")
        if points < dook_points:
            print("Carolina is in the lead!")
        if dook_points < points:
            print("Dook is in the lead!")
        if points == dook_points:
            print("There is currently a tie on the court!")
        attempts += 1
    print(f"Referee: \"Carolina finished with {points} total points and Dook has finished with {dook_points} total points.\"")
    if points < dook_points:
        print("Referee: \"That means Carolina has won the Freethrow battle. They are crowned 'Best Freethrow Basketball Team of the Millennium'!\"")
    if points > dook_points:
        print("Referee: \"That means Dook has won the Freethrow battle. They are crowned 'Best Freethrow Basketball Team of the Millennium'!\"")
    if points == dook_points:
        print("Referee: \"That means there has been a tie. Looks like no one goes home a winner!\"")
    playing = False


def versus(num: int) -> int:
    """One of two possible interactive paths. Guides player through 'Versus' path."""
    global points
    global dook_points
    global player
    global playing
    BASKETBALL: str = "\U0001F3C0"
    MISS: str = "\U0000274C"
    THREE_POINT: str = "\U00002B50"
    attempts: int = 1
    emojis: str = ""

    print(f"Narrator: \"Alright, {player}, it's time for the versus battle! In this battle, you will guess a number between 1 and 10 (inclusive). A player from Dook will do the same. There is also a randomly-selected secret number. The team who's chosen number is closest to the secret number is allowed to spin the Wheel of Basketball. After the team spins, three symbols will be randomly generated. Here are the point values associated with them: ")
    print("Red 'X' = 0 points")
    print("Basketball = 3 points")
    print("Star = 5 points")
    print("The team that has the MOST CUMULATIVE POINTS after 11 rounds wins the battle and takes home the title of 'Best Versus Basketball Team of the Millennium'!\"")
    print(f"Hubert Davis: \"{player}, do exactly how we practiced. We are couting on you, but no pressure. Get out there! Go Heels!\"")
    while attempts <= 11:
        carolina = int(input(f"Referee: \"{player}, enter a number between 1 and 10 (inclusive)\": "))
        if carolina < 1 or carolina > 10:
            carolina = int(input("Referee: \"That's a foul! Enter another number between 1 and 10 (inclusive)\": "))
        print(f"=== Round {attempts} ===")
        secret = randint(1, 10)
        dook = randint(1, 10)
        print(f"Referee: Carolina has chosen {carolina} and Dook has chosen {dook}. The secret number was {secret}.")
        if abs(secret - carolina) < abs(secret - dook):
            print("Referee: \"Carolina has won this round! They get to spin!\"")
            while len(emojis) < 3:
                x = randint(1, 3)
                if x == 1:
                    emojis += BASKETBALL
                    points += 3
                if x == 2:
                    emojis += MISS
                    points += 0
                if x == 3:
                    emojis += THREE_POINT
                    points += 5
            print(emojis)
            print(f"Referee: \"Carolina now has {points} points and Dook has {dook_points} points!\"")
            emojis = ""
        if abs(secret - dook) < abs(secret - carolina):
            print("Referee: \"Dook has won this round! They get to spin!\"")
            while len(emojis) < 3:
                x = randint(1, 3)
                if x == 1:
                    emojis += BASKETBALL
                    dook_points += 3
                if x == 2:
                    emojis += MISS
                    dook_points += 0
                if x == 3:
                    emojis += THREE_POINT
                    dook_points += 5
            print(emojis)
            print(f"Referee: \"Dook now has {dook_points} points and Carolina has {points} points!\"")
            emojis = ""
        if abs(secret - dook) == abs(secret - carolina):
            print("Referee: \"There has been a tie! No one gets to spin!\"")
        attempts += 1
    print(f"Game Over! Carolina has finished with {num} points and Dook has finished with {dook_points} points!")
    if points > dook_points:
        print("That means Carolina has won the Versus battle. They are crowned 'Best Versus Basketball Team of the Millennium'!")
    if points < dook_points:
        print("That means Dook has won the Versus battle. They are crowned 'Best Versus Basketball Team of the Millennium'!")
    if points == dook_points:
        print("That means there has been a tie.")
    playing = False
    points += num
    return num


def decide() -> None:
    """Gets player's first decision as to where to go next. This is where the player first goes once they enter the experience."""
    global player
    global points
    decision = int(input(f"Hubert Davis: {player}, we have the ball first. Do you want to shoot freethrows first or go straight to versus? If you aren't quite ready yet, just let me know. Enter 1 for 'Freethrows', enter 2 for 'Versus', or enter 3 to leave the court: "))
    while (decision == 1 or decision == 2 or decision == 3) is False:
        decision = int(input(f"Hubert Davis: \'That isn't what I asked you, {player}. What will it be: freethrows, versus, or back to the locker room?\' Enter 1 for 'Freethrows', enter 2 for 'Versus', or enter 3 to leave the court: "))
    else:
        if decision == 1:
            freethrows()
        if decision == 2:
            versus(points)
        if decision == 3:
            print(f"Hubert Davis: \'Thanks for being honest, {player}. Now get back to the locker room.\'")
            print(f"{player}, thank you for playing! You have accumulated a total of {points} points! Great job!")


if __name__ == "__main__":
    main()

    
