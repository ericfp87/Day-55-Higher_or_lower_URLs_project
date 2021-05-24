from flask import Flask
import random

random_num = random.randint(0, 9)

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Escolha um número entre 0 a 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:escolha>")
def numero_escolha(escolha):
    if escolha > random_num:
        return "<h1 style='color: red'> 'Muito alto! Tente Novamente!!'</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

    elif escolha < random_num:
        return "<h1 style='color: yellow'> 'Muito Baixo! Tente novamente!!'</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    else:
        return "<h1 style='color: green'> 'Você me achou!!'</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
