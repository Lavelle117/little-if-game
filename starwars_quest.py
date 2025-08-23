             
print("""
                                         
                                    
                                   (    (  ( ()( /---\   (()( (
     _______                            )  ) )(@ !O O! )@@  ( ) ) )
    <   ____)                      ) (  ( )( ()@ \ o / (@@@@@ ( ()( )
 /--|  |(  o|                     (  )  ) ((@@(@@ !o! @@@@(@@@@@)() (
|   >   \___|                      ) ( @)@@)@ /---\-/---\ )@@@@@()( )
|  /---------+                    (@@@@)@@@( // /-----\ \\ @@@)@@@@@(  .
| |    \ =========______/|@@@@@@@@@@@@@(@@@ // @ /---\ @ \\ @(@@@(@@@ .  .
|  \   \\=========------\|@@@@@@@@@@@@@@@@@ O @@@ /-\ @@@ O @@(@@)@@ @   .
|   \   \----+--\-)))           @@@@@@@@@@ !! @@@@ % @@@@ !! @@)@@@ .. .
|   |\______|_)))/             .    @@@@@@ !! @@ /---\ @@ !! @@(@@@ @ . .
 \__==========           *        .    @@ /MM  /\O   O/\  MM\ @@@@@@@. .
    |   |-\   \          (       .      @ !!!  !! \-/ !!  !!! @@@@@ .
    |   |  \   \          )   -cfbd-   .  @@@@ !!     !!  .(. @.  .. .
    |   |   \   \        (    /   .(  . \)). ( |O  )( O! @@@@ . )      .
    |   |   /   /         ) (      )).  ((  .) !! ((( !! @@ (. ((. .   .
    |   |  /   /   ()  ))   ))   .( ( ( ) ). ( !!  )( !! ) ((   ))  ..
    |   |_<   /   ( ) ( (  ) )   (( )  )).) ((/ |  (  | \(  )) ((. ).
____<_____\\__\__(___)_))_((_(____))__(_(___.oooO_____Oooo.(_(_)_)((_
""")

import random

def play_game():
    print("Welcome to this important quest.")
    print("Your mission is to find Baby Grogu.")
    print("You are on an undiscovered planet and you have had a vision "
          "that Grogu is here.\nIf you make poor choices, you will not find him.")
    print("\n")

    choice1 = input("You are passing a big tree. Which way do you go? Type \"right\" or \"left\": ").lower()
    if choice1 == "left":
        choice2 = input("Now you have come to a lake. Do you swim or wait? Type \"swim\" to swim over or "
                        "\"wait\" to wait for a boat: ").lower()
        if choice2 == "wait":
            choice3 = input("While you waited, Luke Skywalker appears. He asks you to choose one colour of "
                            "lightsaber. Type 'red' or 'green': ").lower()
            if choice3 == "red":
                print("Luke kills you! He thinks you are an evil Jedi!")
            elif choice3 == "green":
                print("Good choice! You are one step closer to finding Grogu. You will need this lightsaber to continue your journey.")
                choice4 = int(input("Moff Gideon appears! He has Grogu in a cage. You will need to fight him. "
                                    "Choose how many times you swing\n"
                                    "your saber at Moff. Type a number between 1-50: "))
                moff_number = random.randint(1, 50)
                if moff_number > choice4:
                    print("Sorry, GAME OVER. Moff won the battle. You swung too few times.")
                elif moff_number < choice4:
                    print("Yay! You injured Moff and saved Grogu!")
                else:
                    print("Game over... You did not follow instructions...")
            else:
                print("Game over... You did not follow instructions...")
        else:
            print("In the water was a Mythosaur. You have been dragged down by it. "
                  "You will not find Grogu today.")
    else:
        print("You chose the wrong path, my friend. GAME OVER.")


while True:
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! May the Force be with you.")
        break