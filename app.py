from flask import Flask, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    active = request.args.get("tab", "hcf")
    result = ""

    if request.method == "POST":

        if active == "hcf":
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])

            hcf = math.gcd(num1, num2)
            lcm = (num1 * num2) // hcf

            result = f"HCF = {hcf} <br> LCM = {lcm}"

        elif active == "reverse":
            text = request.form["text"]
            result = f"Reversed String = {text[::-1]}"

        elif active == "fact":
            fact = ""
            for i in range(4, 9):
                fact += f"{i}! = {math.factorial(i)}<br>"
            result = fact

    return f"""
    <html>
    <head>
        <title>Cloud Project</title>
        <style>
            body {{
                font-family: Arial;
                background: linear-gradient(to right, #667eea, #764ba2);
                color: white;
                text-align: center;
                padding: 20px;
            }}

            h1 {{
                margin-bottom: 20px;
            }}

            .nav {{
                margin-bottom: 30px;
            }}

            .nav a {{
                text-decoration: none;
                color: white;
                padding: 10px 20px;
                margin: 5px;
                border-radius: 20px;
                background: rgba(255,255,255,0.2);
            }}

            .active {{
                background: white !important;
                color: black !important;
                font-weight: bold;
            }}

            .nav a:hover {{
                background: rgba(255,255,255,0.5);
                color: black;
            }}

            .card {{
                background: white;
                color: black;
                padding: 20px;
                border-radius: 15px;
                width: 300px;
                margin: auto;
                box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            }}

            input, button {{
                padding: 10px;
                margin: 10px;
                width: 80%;
                border-radius: 10px;
                border: none;
            }}

            button {{
                background: #667eea;
                color: white;
                cursor: pointer;
            }}

            button:hover {{
                background: #764ba2;
            }}

            .result {{
                margin-top: 20px;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>

    <h1>✨ Cloud Based Mini Project</h1>

    <div class="nav">
        <a href="/?tab=hcf" class="{ 'active' if active=='hcf' else '' }">HCF & LCM</a>
        <a href="/?tab=reverse" class="{ 'active' if active=='reverse' else '' }">Reverse String</a>
        <a href="/?tab=fact" class="{ 'active' if active=='fact' else '' }">Factorial</a>
    </div>

    <div class="card">
    """

    + (
        f"""
        <form method="post" action="/?tab=hcf">
            <input name="num1" placeholder="Enter Number 1"><br>
            <input name="num2" placeholder="Enter Number 2"><br>
            <button type="submit">Calculate</button>
        </form>
        """
        if active == "hcf"
        else ""
    )

    + (
        f"""
        <form method="post" action="/?tab=reverse">
            <input name="text" placeholder="Enter String"><br>
            <button type="submit">Reverse</button>
        </form>
        """
        if active == "reverse"
        else ""
    )

    + (
        f"""
        <form method="post" action="/?tab=fact">
            <button type="submit">Show Factorials (4-8)</button>
        </form>
        """
        if active == "fact"
        else ""
    )

    + f"""
        <div class="result">{result}</div>
    </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
