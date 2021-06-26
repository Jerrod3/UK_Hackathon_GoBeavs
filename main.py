#Discord Bot - Financial Portfolio Game

#Queries/Commands
    # $Next                             //Adds X amount of turns/years to the gameplay.
    # $Start                            //Resets and starts the game for player.
    # $Initialize                       //Initialize the bot/game on the server.
    # $Balance                          //Checks the current balance/cash the player has.
    # $Networth 
    # $Age                              //Checks the age for the current player.
    # $Assets                           //Shows the ratio and breakdown of the players' assets.
    # $Projection                       //Projects the possible future state of the players' assets.
    # $Preset [#]                       //Invest balance into asset allocation.

#CSV, parsing Returns for projection.
    # 9 different CSV's, 1 for each Asset Type.
    # 

#Gameplay
    #Constant for when the person dies.
    #Variable for bank balance; acculation per turn.
    #Constant for inflation.
    #PrevDictionary (Balance, + 9 AssetTypes, Age) 
    #CurrDictionary (Balance, + 9 AssetTypes, Age)

class player:                    #Each player has their own gameInstance object created when calling $start
    def __init__(self, name, age=18):        #__init__ is a object method that python automatically runs, when the instance/object is initialized/created
        self.user = name
        self.balanace = 100000            #Replace this with whatever the starting balance is.
        self.age = age    #By default, this will be 18 unelss the parameter is overwritten

        self._current_assets = dict()      #Storing all of the player's data as key:pair dictionary format.
        self._previous_assets = dict()

    def __repr__(self) -> str:       #__Repr__ is a method that tells python, what displays when you print or call the object directly.
        return self.user

Jerrod = player('Burbot#5573')
print(Jerrod)            #Returns -> 'Burbot#5573'
print(Jerrod.balanace)   #Returns -> '100000'

