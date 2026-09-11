from flask import Flask, request, render_template_string, session

app = Flask(__name__)
app.secret_key = "local-xss-lab-secret"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Local XSS Lab</title>
</head>
<body>
    <h1>Local XSS Lab</h1>

    {% if session.get("user") %}
        <p>Logged in as: <b>{{ session["user"] }}</b></p>
        <p>Fake secret: <b>{{ session["secret"] }}</b></p>
    {% else %}
        <form method="POST" action="/login">
            <input name="username" value="victim">
            <button type="submit">Login</button>
        </form>
    {% endif %}

    <hr>

    <form method="GET" action="/">
        <input name="name" placeholder="Enter a name">
        <button type="submit">Submit</button>
    </form>

    {% if name %}
        <h2>Hello, {{ name }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    name = request.args.get("name", "")
    return render_template_string(HTML, name=name)

@app.route("/login", methods=["POST"])
def login():
    session["user"] = request.form.get("username", "victim")
    session["secret"] = "FAKE-SECRET-12345"
    return "Logged in. Go back to /"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
