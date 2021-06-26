# List of event texts that can randomly be assigned depending on portfolio overall return.
# Events here are purely aesthetic/eye candy and will not affect the algorithm/calculation.
# See examples at very bottom.

VERY_GOOD_EVENTS = [
    "Harvard economists are surprised by the positive economic growth following the latest Lady Gaga album that inspired millions of consumers around the world to 'give back' during this pandemic."

]

GOOD_EVENTS = [
    "Immense quantity of gold dating back to 1800's was recently discovered in D.C."

]

BAD_EVENTS = [
    "(Un)expected global warming led to recent tsunami damage to thousands of homes in the East Coast."
]

VERY_BAD_EVENTS = [
    "Millions of Americans disappointed as a handful of U.S. Senators have been found guilty of accepting unwarranted bribes in the forms of bitcoins."

]

#If the yearly profitted over 3 percent in return, randomly pull an event text from the VERY_GOOD_EVENTS list.
#If the yearly profit is between 0-3 percent in return,  randomly pull an event text from the GOOD_EVENTS list.
#If the yearly loss is between 0-3 percent in return, randomly pull an event text from the BAD_EVENTS list.
#If the yearly loss is greater than 3 percent in return, randomlyp ull an event text from the VERY_BAD_EVENTS list.