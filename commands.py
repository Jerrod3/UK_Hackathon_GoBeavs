def next(years):
    message = f"You've progressed {years} years."
    return message


def start():
    message = "You've started the game!"
    return message


def initialize():
    message = "You've initialized the game!"
    return message


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)