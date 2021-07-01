# Discord Bot - Financial Portfolio Game

# Queries/Commands
# $Next                             //Adds X amount of turns/years to the gameplay.
# $Start                            //Resets and starts the game for player.
# $Initialize                       //Initialize the bot/game on the server.
# $Balance                          //Checks the current balance/cash the player has.
# $Networth
# $Age                              //Checks the age for the current player.
# $Assets                           //Shows the ratio and breakdown of the players' assets.
# $Projection                       //Projects the possible future state of the players' assets.
# $Portfolio [#]                       //Invest balance into asset allocation.

# CSV, parsing Returns for projection.
# 9 different CSV's, 1 for each Asset Type.
#

# Gameplay
# Constant for when the person dies.
# Variable for bank balance; accumulation per turn.
# Constant for inflation.
# PrevDictionary (Balance, + 9 AssetTypes, Age)
# CurrDictionary (Balance, + 9 AssetTypes, Age)
#Gameplay
    #Constant for when the person dies.
    #Variable for bank balance; accumulation per turn.
    #Constant for inflation.
    #PrevDictionary (Balance, + 9 AssetTypes, Age)
    #CurrDictionary (Balance, + 9 AssetTypes, Age)


class Player:  # Each player has their own gameInstance object created when calling $start

    ADMIN_LIST = {'Burbot#5573', 'ColdBrewOnNitroStat#4666', 'Lucas J#3567', '24karatsunshine#7559'} #List stored as Set, Set is pretty much better/efficient list if order does not matter.
    PORTFOLIO_PRESET = [
        (0.05, 0.25, 0.25, 0.20, 0.10, 0.10, 0.05, 0.00, 0.00)  ## Portfolio 1 - A little bit of everything
        (0.00, 0.00, 0.00, 0.34, 0.33, 0.00, 0.00, 0.33, 0.00)  ## Portfolio 2 - The Boglehead
        (0.00, 0.00, 0.00, 0.25, 0.25, 0.25, 0.25, 0.00, 0.00)  ## Portfolio 3 - The Dave Ramsey
        (0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00)  ## Portfolio 4 - Old School Pension Plan
        (0.00, 0.00, 0.00, 1.00, 0.00, 0.00, 0.00, 0.00, 0.00)  ## Portfolio 5 - You only live once
        (1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00)  ## Portfolio 6 - The Shoebox
    ]

    def __init__(self, name, age=18):  # __init__ is a object method that python automatically runs, when the
        # instance/object is initialized/created
        self.user = name
        self.balance = 100000  # Replace this with whatever the starting balance is.
        self.age = age  # By default, this will be 18 unless the parameter is overwritten
        self.allocations = None  # Text representation of percentage invested in each allocation type

        self._current_assets = dict()      #Storing all of the player's data as key:pair dictionary format. Setting to empty one to begin with.
        self._previous_assets = dict()     #Storing all of the player's data as key:pair dictionary format. Setting to empty one to begin with.
        self._current_allocations = tuple()     #9 asset types stored as tuple (a list that you cant edit individual values, more efficient), 9 different decimal values, for example: [0.05, 0.10, 0.10, 0.7, 0.8, 0.25, 0.10, 0.05, 0.15, 0.05]  => 5% ASSET A, 10% in ASSET B, etc...

        # values, more efficient), 9 different decimal values, for example:
        # [0.05, 0.10, 0.10, 0.7, 0.8, 0.25, 0.10, 0.05, 0.15, 0.05]  => 5% ASSET A, 10% in ASSET B, etc...

        self._is_admin = self._is_admin_check()  # Boolean; states whether or not the player have admin privileges,
        # uses function to check if the player's name is in the class list of admins.

    def __repr__(self) -> str:  # __Repr__ is a method that tells python, what displays when you print or call
        # the object directly.
        return self.user

    def _is_admin_check(self):
        return self.user in Player.ADMIN_LIST  # Returns True if the player

    def _game_over(self):  # This function will run to cleanup and reset game. As well as update leaderboard data.
        pass

    def portfolio(self, preset_number):  # Bot command $Portfolio [#] would run this
        index = preset_number - 1  # Python uses Based 0 index, but we want to let users start from Index of 1.
        # So accounting internally.
        self._current_allocations = Player.PORTFOLIO_PRESET[index]
        print("Portfolio Successfully Changed.")
        self.allocations = f"MONEY: {self._current_allocations[0] * 100}%, ITGVT:" \
                           f" {self._current_allocations[1] * 100}%, LTCORP: {self._current_allocations[2] * 100}%," \
                           f" Equity US: {self._current_allocations[3] * 100}%, INT:" \
                           f" {self._current_allocations[4] * 100}%, SMALL: {self._current_allocations[5] * 100}%, " \
                           f"AGGR: {self._current_allocations[6] * 100}%, FIXED:" \
                           f" {self._current_allocations[7] * 100}%, BALANCED: {self._current_allocations[8] * 100}%"

    def help(self): #This function is used for the $help command to find out the bot commands.
        pass

    def next(self):
        self.age += 1
        if self.age >= 60:
            self._game_over()


# Examples / Tests

Jerrod = Player(
    'Burbot#5573')  # We want the bot to execute this function ; creating the
# player's object using discord name when they type !start
print(Jerrod)  # Returns -> 'Burbot#5573'
print(Jerrod.balance)  # Returns -> '100000'
