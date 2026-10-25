from flask import Flask
from random import randint

app = Flask(__name__)


def count_it(sequence):
    numbers = {}

    for digit in sequence:
        digit = int(digit)
        numbers[digit] = numbers.get(digit, 0) + 1

    top3 = dict(
        sorted(numbers.items(), key=lambda x: x[1], reverse=True)[:3]
    )

    return top3


@app.route('/')
def main():
    string = ''.join(
        str(randint(0, 9))
        for _ in range(randint(10, 21))
    )

    result = count_it(string)

    return f"""
    <h1>Sequence of Numbers</h1>
    <p>{string}</p>

    <h2>Three Most Common Numbers</h2>
    <p>{result}</p>
    """


if __name__ == '__main__':
    app.run(debug=True)