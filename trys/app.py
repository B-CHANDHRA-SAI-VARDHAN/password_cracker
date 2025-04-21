from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Serve the HTML page

@app.route("/guess", methods=["POST"])
def guess_password():
    password = request.form["password"]  # Retrieve the numeric password from the form
    guessed_password = ""
    attempts = []  # To store the guessing process for display later

    # Sequential guessing logic
    for number in range(1, 100000):  # Range from 1 to 99999
        guessed_password = str(number).zfill(len(password))  # Pad numbers to match the password's length
        attempts.append(guessed_password)  # Add each guess to the list

        if guessed_password == password:  # Check if the guess is correct
            # Simulate guessing step by step in the response
            return render_template("result.html", guessed_password=guessed_password, attempts=attempts)

    # If the password couldn't be guessed within the range
    return "<h2>Password not guessed within the range.</h2>"

if __name__ == "__main__":
    app.run(debug=True)