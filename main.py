# Discord Bot - Financial Portfolio Game

# *** = implemented
# Queries/Commands
# $Next***                             //Adds X amount of _turns/years to the gameplay.
# $Start***                            //Resets and starts the game for _player.
# $Initialize***                       //Initialize the bot/game on the server.
# $Balance***                          //Checks the current _balance/cash the _player has.
# $Age***                              //Checks the _age for the current _player.
# $Assets***                           //Shows the ratio and breakdown of the players' assets.
# $Projection                       //Projects the possible future state of the players' assets.
# $Portfolio [#]***                    //Invest _balance into asset allocation.

# CSV, parsing Returns for projection.
# 7 different CSV's, 1 for each Asset Type.
#

# Gameplay
# Var/Constant for when the person dies.
# Variable for bank _balance; accumulation per turn.
# Constant for inflation.
# PrevDictionary (Balance, + 9 AssetTypes, Age)
# CurrDictionary (Balance, + 9 AssetTypes, Age)
#Gameplay
    #Constant for when the person dies.
    #Variable for bank _balance; accumulation per turn.
    #Constant for inflation.
    #PrevDictionary (Balance, + 9 AssetTypes, Age)
    #CurrDictionary (Balance, + 9 AssetTypes, Age)

import random

class Simulation:
    """Each _player has their own game object created when calling '$start'
    """

    ADMIN_LIST = {'Burbot#5573', 'ColdBrewOnNitroStat#4666', 'Lucas J#3567', '24karatsunshine#7559'} #List stored as Set, Set is pretty much better/efficient list if order does not matter.

    PORTFOLIO_PRESET = [
        (1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00)   ## Portfolio 0 - Default: All cash; no investments.
        (0.00, 0.05, 0.25, 0.25, 0.20, 0.10, 0.10, 0.05),  ## Portfolio 1 - A little bit of everything
        (0.00, 0.00, 0.22, 0.11, 0.34, 0.33, 0.00, 0.00),  ## Portfolio 2 - The Boglehead
        (0.00, 0.00, 0.00, 0.00, 0.25, 0.25, 0.25, 0.25),  ## Portfolio 3 - The Dave Ramsey
        (0.00, 0.00, 0.87, 0.13, 0.00, 0.00, 0.00, 0.00),  ## Portfolio 4 - Old School Pension Plan
        (0.00, 0.00, 0.00, 0.00, 1.00, 0.00, 0.00, 0.00),  ## Portfolio 5 - You only live once
        (0.00, 1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00)]  ## Portfolio 6 - The Shoebox
    """The portfolio preset variable contains different sets of asset distribution. Values in the set should add up to 1.00 or 100%."""

    def __init__(self, player_name):
        self._reset(player_name)

    def _reset(self, name, age=18):  # __init__ is a object method that python automatically runs, when the
        # instance/object is initialized/created
        self._world_seed = self._get_seed() # Initializes the _player with a randomly selected projection of how each asset varies per year
        """The _world_seed private data member stores all the asset type models in the current game."""
        self.AGGR_list = self._world_seed[0]  # Call the model for each asset type (stored in a list).
        self.INTT_list = self._world_seed[1]
        self.LTCORP_list = self._world_seed[2]
        self.MONEYY_list = self._world_seed[3]
        self.INTGOV_list = self._world_seed[4]
        self.US_list = self._world_seed[5]
        self.SMALL_list = self._world_seed[6]
        """Parsing the _world_seed private data member into the respective asset model variables. Each asset variable list contains incrementing values that determine the asset success for different years """

        # The following are all the private data members related to the player specifically.
        self._player = name # Name of the player
        self._balance = 100000  # Replace this with whatever the starting _balance is.
        self._age = age  # By default, this will be 18 unless the parameter is overwritten
        self._turns = 0 # Keeps track of the turns elapsed, first turn is 0. This also serves as the index to calculate different asset models.

        self._player_assets = [self._balance, 0, 0, 0, 0, 0, 0, 0]
        self._current_allocations = Simulation.PORTFOLIO_PRESET[0]

        self._asset_distributions = None """This is to initialize the temporary variable used during the next() function."""
        self._allocation_repr = f"CASH: 100%, MONEY: 0%, ITGVT:" \
                                f" 0%, LTCORP_list: 0%," \
                                f" Equity US_list: 0%, INT:" \
                                f" 0%, SMALL_list: 0%, " \
                                f"AGGR_list: 0%, FIXED:" \
                                f" 0%, BALANCED: 0%"

        """There are 7 asset types, by default the starting allocations are set to portfolio 0."""

        # values, more efficient), 9 different decimal values, for example:
        # [0.05, 0.10, 0.10, 0.7, 0.8, 0.25, 0.10, 0.05, 0.15, 0.05]  => 5% ASSET A, 10% in ASSET B, etc...

        self._is_admin = self._is_admin_check()  # Boolean; states whether or not the _player have admin privileges,
        # uses function to check if the _player's name is in the class list of admins.

    def get_player(self):  # __Repr__ is a method that tells python, what displays when you print or call
        # the object directly.
        return self._player

    def get_player(self):  # __Repr__ is a method that tells python, what displays when you print or call
        # the object directly.
        return self._age

    def _is_admin_check(self):
        return self._player in Simulation.ADMIN_LIST  # Returns True if the _player

    def get_portfolio(self, preset_choice):  # Bot command $Portfolio [#] would run this
        self._current_allocations = Simulation.PORTFOLIO_PRESET[index]
        print("Portfolio Successfully Changed.")
        self._allocation_repr = f"CASH: {self_current_allocations[0]}%, MONEY: {self._current_allocations[1] * 100}%, ITGVT:" \
                           f" {self._current_allocations[2] * 100}%, LTCORP_list: {self._current_allocations[3] * 100}%," \
                           f" Equity US_list: {self._current_allocations[4] * 100}%, INT:" \
                           f" {self._current_allocations[5] * 100}%, SMALL_list: {self._current_allocations[6] * 100}%, " \
                           f"AGGR_list: {self._current_allocations[6] * 100}%, FIXED:" \
                           f" {self._current_allocations[7] * 100}%, BALANCED: {self._current_allocations[8] * 100}%"
        return self._allocation_repr

    def get_balance(self):
        return self._balance

    def help(self): #This function is used for the $help command to find out the bot commands.
        pass

    def _get_seed(self):

        """ A function that picks randomly selected world parameters for asset classes through time."""

        # Need to speed this process up if possible.

        random_int = random.randint(0, 10000)

        asset_list = ["AGGR_list", "INT", "INTGOV_list", "LTCORP_list", "MONEY", "SMALL_list", "US_list"]
        asset_models = []
        for asset in asset_list:
            asset = asset
            fh = open(f"{asset}.csv")
            models_lst = []
            for line in fh:
                nospace = line.rstrip()
                split = nospace.split(",")
                models_lst.append(split)
            asset_models.append(models_lst)

        AGGR = asset_models[0]
        INT = asset_models[1]
        INTGOV = asset_models[2]
        LTCORP = asset_models[3]
        MONEY = asset_models[4]
        SMALL = asset_models[5]
        US = asset_models[6]

        player_models = [AGGR[random_int], INT[random_int], INTGOV[random_int], LTCORP[random_int], MONEY[random_int],
                         SMALL[random_int], US[random_int]]

        return player_models

    def next(self):
        # Increment _age, increment the turn
        if self._age >= 60:
            print({"Game over! You died at the age of 60."})
            self._reset()
        # Change the value in each asset list to the next value
        """Take the player balance, distribute it accordingly to the how much they want to put into each asset type. Take each asset type and multiply it by the modifier of each model (which is determined by current minus previous)."""
        self._asset_distributions = [self._balance * asset for asset in self._current_allocations]
        self._asset_multipliers = [1, (self.AGGR_list[self._turns+1] - self.AGGR_list[self._turns]),
                                   self.INTT_list[self._turns+1] -self.INTT_list[self._turns],
                                   self.LTCORP_list[self._turns + 1] - self.LTCORP_list[self._turns],
                                   self.MONEYY_list[self._turns + 1] - self.MONEYY_list[self._turns],
                                   self.INTGOV_list[self._turns + 1] - self.INTGOV_list[self._turns],
                                   self.US_list[self._turns + 1] - self.US_list[self._turns],
                                   self.SMALL_list[self._turns + 1] - self.SMALL_list[self._turns]
        ]
        self._asset_distributions = [a * b for a, b in zip(self._asset_distributions, self._asset_multipliers)] #Takes the player's dsitributions and multiply by the respective asset multipliers as generated by the models.
        self._balance = sum(self._asset_distributions) # Recalculates the player monetary balance by summing up all of the player's assets.

        self._turns += 1
        self._age += 1


        # Functions properly, just a bit ugly (F strings? A loop?). Need to incorporate math next.

# Examples / Tests

Jerrod = Simulation(
    'Burbot#5573')  # We want the bot to execute this function ; creating the
# _player's object using discord name when they type !start
print(Jerrod)  # Returns -> 'Burbot#5573'
print(Jerrod._balance)  # Returns -> '100000'
print(Jerrod.AGGR_list)
print(Jerrod.AGGR_index)
print(Jerrod._player_assets)
Jerrod.next()
print(Jerrod.AGGR_index)
Jerrod.next()
print(Jerrod.AGGR_index)
Jerrod.next()
Jerrod.next()
Jerrod.next()
print(Jerrod.AGGR_index)
print(Jerrod._player_assets)