from flask import Flask, request

import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        text = request.form["text"]

        # HCF and LCM
        hcf = math.gcd(num1, num2)
        lcm = (num1 * num2) // hcf

        # Reverse string
        rev = text[::-1]

        # Factorials
        fact = ""
        for i in range(4, 9):
            fact += f"{i}! = {math.factorial(i)}<br>"

        result = f"""
        HCF = {hcf} <br>
        LCM = {lcm} <br><br>
        Reversed String = {rev} <br><br>
        Factorials:<br>{fact}
        """

    return f"""
    <h2>Simple Cloud Project</h2>

    <form method="post">
        Enter Number 1: <input name="num1"><br><br>
        Enter Number 2: <input name="num2"><br><br>
        Enter String: <input name="text"><br><br>
        <button type="submit">Submit</button>
    </form>

    <br>{result}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
