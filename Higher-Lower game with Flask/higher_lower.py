from flask import Flask
import random

app = Flask(__name__)
no = random.randint(1, 11)

@app.route("/")
def game_start():
    return "<center><h1>Welcome to higher lower game</h1><h3>Enter value in URL</h3></center>"



@app.route("/<int:number>")
def guesser(number):


    if no > number:
        return '<center><h2>Too low guess. Try higher</h2><img src = "https://media.giphy.com/media/AisOYaOZdrS1i/giphy.gif" width ="350" height="250"/></center>'
    elif number > no:
        return '<center><h2>Too high guess. Try lower</h2><img src = "https://media.giphy.com/media/720g7C1jz13wI/giphy.gif" width ="350" height="250"/></center>'
    else:
        return '<center><h2>Right guess !!!</h2><img src = "https://media.giphy.com/media/PXvCWUnmqVdks/giphy.gif"/></center>'


if __name__ == "__main__":
    app.run(debug=True)
