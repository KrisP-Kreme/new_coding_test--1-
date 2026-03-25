# My Submission

## Submission Outline and How to run

My submission consists of four different files. Two of the files are class files, player.py and space.py. The third file is program.py where the main program lives. The final file is tests.py, where I've written my test cases. 

To run the simulation, run
``` python program.py ``` and follow the console instructions.

To run the test file, run
``` python tests.py ```
The test file is written using assertions. Any assertion failure will raise an error. Only console logs for the game running the different functions will be shown during a successful run of the tests. 

## Design Decisions

I started this project by implementing object-oriented programming (OOP) principles . I first defined classes for the different types of objects in the game, players and spaces. This allows each object to have its own attributes and allows for extensibility of the program, as I will talk about later. 

In the main program file, I initially had all my code in one overall simulation loop, just to have the basic logic figured out and written. After ensuring that the main logic was working, I decided to split up all the key behaviours, such as handling property interactions and end game conditions, into separate functions for better readabililty. This also allowed me to keep the main part of the program clean and uncomplicated.

While writing the program, I identifed that a lot of the logic I had written used global variables defined at the start of the program. This meant that my code broke encapsulation and was much harder to test. I fixed this by rewriting the functions I created to use passed parameter within their logic, rather than the global variables. This then allowed me to test the code much more easily as I could pass data from the tests straight into the functions. 

## Extensibility

Extensibility was something I considered during and after this project. When I created the space class and logic surrounding landing on a space, I made sure to allow for any future changes the code might have, such as the implementation of different types of spaces (as for now, there are only spaces of the "property" type). For example, in the run_simulation function of my code, I could have simply handled landing on a space without checking what kind of space was landed on. However, I implemented a checker that checks whether the board space was of type "property" before handling, which allows the code to be extended to allow other types of spaces to be handled, should they be added. The space class itself has a "type" attribute, allowing for new space types to be added. 

I also thought about how this game could be turned from a pre-determined spectator game into a turn-based, interactive, multiplayer game played on one device. The deterministic rolls could be replaced by each player taking turns "rolling the dice" (a random number generated between 1 and 6) and then moving that many spaces. Any properties they land on could be bought by the player and landing on an owned property would require rent to be paid. Chance and community chest cards could also be implemented by having a list of the cards prepopulated and "shuffled" before the game starts. Since most of the game is automatic, all turns would be output into the console. Players would simply need to hit a key to roll the dice. The only other manual decision that could be implemented would be the option for players to buy houses and hotels for their properties. This could be simply implemented by asking users each turn if they would like to build any houses or hotels. If no, continue normally with their turn. If yes, ask which property they would like to build the houses/hotels on and then store it in the program as such so that rent is increased when players land on said property.

## Conclusion

This was a really fun and interesting project. Despite appearing simple, there were a few times where I sat back and wondered "how should I approach this". I really liked the kind of thinking it provoked and the problem-solving aspect. I believe that the program I've written satisfies the rules of the game, is clear and readable and is extendable. 


# Project Outline

## Woven coding test

Your task is to write an application to play the game of Woven Monopoly.

In Woven Monopoly, when the dice rolls are set ahead of time, the game is deterministic.

### Game rules
* There are four players who take turns in the following order:
  * Peter
  * Billy
  * Charlotte
  * Sweedal
* Each player starts with $16
* Everybody starts on GO
* You get $1 when you pass GO (this excludes your starting move)
* If you land on a property, you must buy it
* If you land on an owned property, you must pay rent to the owner
* If the same owner owns all property of the same colour, the rent is doubled
* Once someone is bankrupt, whoever has the most money remaining is the winner
* There are no chance cards, jail or stations
* The board wraps around (i.e. you get to the last space, the next space is the first space)


### Your task
* Load in the board from board.json
* Implement game logic as per the rules
* Load in the given dice rolls files and simulate the game
  * Who would win each game?
  * How much money does everybody end up with?
  * What spaces does everybody finish on?


The specifics and implementation of this code is completely up to you!

### What we are looking for:
* We are a Ruby house, however feel free to pick the language you feel you are strongest in.
* Code that is well thought out and tested
* Clean and readable code
* Extensibility should be considered
* A git commit-history would be preferred, with small changes committed often so we can see your approach

Please include a readme with any additional information you would like to include, including instructions on how to test and execute your code.  You may wish to use it to explain any design decisions.

Despite this being a small command line app, please approach this as you would a production problem using whatever approach to coding and testing you feel appropriate.
