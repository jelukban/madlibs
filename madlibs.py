"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return """ <!doctype html> <html> This is the home page. </html>
    <a href="/hello"> Click me to go the Madlib game </a>

    """



@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""


    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """Greet user with compliment."""

    game_question = request.args.get("game-decision")

    if game_question == "yes":
        return render_template("games.html")
    elif game_question == "no":
        return render_template("goodbye.html")

@app.route("/madlib")
def show_madlib():

    input_name = request.args.get("name")
    input_color = request.args.get("color")
    input_noun = request.args.get("noun")
    input_adjective = request.args.get("adjective")
    input_animal = request.args.get("animal")
    print(input_animal)
    input_food = request.args.get("food")


    return render_template("madlib.html", color=input_color, noun=input_noun, person=input_name,
    adjective=input_adjective, animal=input_animal, food=input_food)






if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
