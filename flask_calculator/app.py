from flask import Flask, render_template, request
import random
import re

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("app.html", result="", error="")

@app.route("/calculate", methods=['POST'])
def calculate():
    expression = request.form['expression']

    error_messages = {
        "zero_division": [
            "Dividing by zero? Really? Try harder!",
            "Infinite loops and chaos. Division by zero isn't cool.",
            "Did you just divide by zero? Math gods are crying!"
        ],
        "invalid_characters": [
            "Are you trying to invent a new math symbol?",
            "Only numbers and operators allowed. Nice try!",
            "This calculator doesn't speak alien math."
        ],
        "syntax_error": [
            "Incomplete math? Finish what you started!",
            "Syntax matters! Even for calculators.",
            "Math is an art. Try painting within the lines."
        ],
        "general_error": [
            "You broke the calculator. Congratulations!",
            "Not sure what you did, but it wasn't math.",
            "Try again. This time with less chaos."
        ]
    }

    result = ""
    error = ""

    try:
        if not re.match(r'^[0-9+\-*/.() ]+$', expression):
            raise ValueError("invalid_characters")
        
        result = eval(expression)

        if result == float('inf') or result == float('-inf'):
            raise ZeroDivisionError

    except ZeroDivisionError:
        error = random.choice(error_messages["zero_division"])
    except ValueError as e:
        if str(e) == "invalid_characters":
            error = random.choice(error_messages["invalid_characters"])
        else:
            error = random.choice(error_messages["general_error"])
    except SyntaxError:
        error = random.choice(error_messages["syntax_error"])
    except Exception:
        error = random.choice(error_messages["general_error"])

    return render_template('app.html', result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
