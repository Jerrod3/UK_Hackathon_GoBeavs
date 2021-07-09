# List of event texts that can randomly be assigned depending on portfolio overall return.
# Events here are purely aesthetic/eye candy and will not affect the algorithm/calculation.
# See examples at very bottom.

VERY_GOOD_EVENTS = [
    "Harvard economists are surprised by the positive economic growth following the latest Lady Gaga album that inspired millions of consumers around the world to 'give back' during this pandemic."
    "Pfizer announces they've invited a vaccine that will prevent all viruses from spreading"
    "90% of 1st world companies have opted for a 4 day work week, tripling economic production"
]

GOOD_EVENTS = [
    "Immense quantity of gold dating back to 1800's was recently discovered in D.C."
    "Amazon Prime day overcomes Black Friday to become the biggest shopping day of the year."
    "All world billionaires have pledged to donate 50% of their income to their respective countries' citizens"
]

BAD_EVENTS = [
    "(Un)expected global warming led to recent tsunami damage to thousands of homes in the East Coast."
    "Oil prices rise sharply; families opt to stay home this shopping season."
    "Fed Chairman announces interest rates will double unexpectedly."
    "New trade policies raises consumer uncertainty to all time highs."
    "Meme stonks have skyrocketed, destroying 80% of pension funds"
]

VERY_BAD_EVENTS = [
    "Millions of Americans disappointed as a handful of U.S. Senators have been found guilty of accepting unwarranted bribes in the forms of bitcoins."
    "Housing market crashes. Unemployment at all time highs."
    "Software glitches cause markets to tumble; investers flee markets at record rates."
    "Canada has invaded the United States for its maple syrup reserves, WW3 has begun"
]

#If the yearly profitted over 3 percent in return, randomly pull an event text from the VERY_GOOD_EVENTS list.
#If the yearly profit is between 0-3 percent in return,  randomly pull an event text from the GOOD_EVENTS list.
#If the yearly loss is between 0-3 percent in return, randomly pull an event text from the BAD_EVENTS list.
#If the yearly loss is greater than 3 percent in return, randomlyp ull an event text from the VERY_BAD_EVENTS list.