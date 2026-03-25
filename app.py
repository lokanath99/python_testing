from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <body>
            <h2>Login Page</h2>
            <form action="/login" method="post">
                <input type="text" id="username" name="username" placeholder="Username"/>
                <input type="password" id="password" name="password" placeholder="Password"/>
                <button type="submit" id="login-btn">Login</button>
            </form>
        </body>
    </html>
    """

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "1234":
        return "Login Successful"
    return "Login Failed"

if __name__ == "__main__":
    app.run(debug=True)