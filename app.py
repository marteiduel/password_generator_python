from flask import Flask, render_template, request
import random

app = Flask(__name__)

LOWER_LETTERS = 'qwertyuiopasdfghjklzxcvbnmñ'
UPPER_LETTERS = 'QWERTYUIOPASDFGHJKLZXCVBNM'
SYMBOLS = '`~!@#$%^&*()-_=+[{]};:"\|.,/<>?]'
NUMBERS = '0123456789'


@app.route('/')
def home():
    characters = 16
    password = generate_random_password(characters)
    return render_template('index.html', password=password)


@app.route('/generate', methods=['POST'])
def generate_password():
    characters = int(request.form.get('num_of_characters', 16))
    password = generate_random_password(characters)
    return render_template('index.html', password=password)


def generate_random_password(characters):
    password = ''
    for _ in range(characters // 4):
        password += random.choice(NUMBERS)
        password += random.choice(LOWER_LETTERS)
        password += random.choice(UPPER_LETTERS)
        password += random.choice(SYMBOLS)
    return password


if __name__ == '__main__':
    app.run()
