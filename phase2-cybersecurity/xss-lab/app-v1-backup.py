from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Local XSS Lab</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }
        input {
            width: 70%;
            padding: 10px;
        }
        button {
            padding: 10px 20px;
        }
        .comment {
            margin-top: 25px;
            padding: 15px;
            border: 1px solid #ccc;
        }
        code {
            background: #f4f4f4;
            padding: 3px 6px;
        }
    </style>
</head>
<body>

<h1>Local XSS Lab</h1>

<p>This application intentionally contains a reflected XSS vulnerability.</p>

<form method="GET" action="/">
    <input name="name" placeholder="Enter your name">
    <button type="submit">Submit</button>
</form>

{% if name %}
<div class="comment">
    <h2>Hello, {{ name }}</h2>
</div>
{% endif %}

<hr>

<p>Normal example:</p>
<code>http://127.0.0.1:5000/?name=Haseeb</code>

<p>The application intentionally uses <code>|safe</code>, meaning the submitted
value is inserted into the HTML without escaping.</p>

</body>
</html>
"""

@app.route("/")
def home():
    name = request.args.get("name", "")
    return render_template_string(HTML, name=name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
