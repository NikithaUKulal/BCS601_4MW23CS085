from flask import Flask, render_template, request
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
            action = request.form.get("action")

            if action == "hcf":
                result = f"Output: HCF = {math.gcd(num1, num2)}"
            elif action == "lcm":
                hcf = math.gcd(num1, num2)
                lcm = (num1 * num2) // hcf
                result = f"Output: LCM = {lcm}"

        elif active == "reverse":
            text = request.form["text"]
            result = f"Output: {text[::-1]}"

        elif active == "fact":
            num = int(request.form["num"])
            result = f"Output: {num}! = {math.factorial(num)}"

    return render_template("index.html", active=active, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
