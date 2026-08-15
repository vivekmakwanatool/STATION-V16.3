from flask import Flask, render_template, request, session, redirect
import hashlib
import base64
import random

app = Flask(__name__)
app.secret_key = "secret123"


@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        if request.form["user"] == "admin" and request.form["pass"] == "1234":
            session["login"] = True
            return redirect("/")
        msg = "ACCESS DENIED ❌"
    return render_template("login.html", msg=msg)


@app.route("/", methods=["GET", "POST"])
def index():
    if not session.get("login"):
        return redirect("/login")

    result = ""
    mode = "crypto"

    if request.method == "POST":
        data = request.form.get("data", "")
        salt = request.form.get("salt", "")
        algo = request.form.get("algo", "sha256")
        mode = request.form.get("mode", "crypto")

        if mode == "crypto":
            result = hashlib.new(algo, (data + salt).encode()).hexdigest()
        elif mode == "base":
            result = base64.b64encode(data.encode()).decode()
        elif mode == "enhancer":
            result = data + str(random.randint(100, 999)) + "@#"
        elif mode == "identify":
            result = "MD5" if len(data) == 32 else "UNKNOWN"
        elif mode == "strength":
            result = "STRONG" if len(data) > 8 else "WEAK"

        if "history" not in session:
            session["history"] = []

        history = session["history"]
        history.append(result)
        session["history"] = history[-5:]

    return render_template("index.html", result=result, history=session.get("history", []))


@app.route("/hack")
def hack():
    return render_template("hack.html")


if __name__ == "__main__":
    app.run(debug=True)
