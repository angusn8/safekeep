from flask import Flask, render_template, url_for, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def about():
    return render_template("index.html")

@app.route("/passwords", methods=["POST", "GET"])
def passwords():
    newPassword = ""
    if request.method == "POST":
        oldPassword = request.form["currentPassword"]
        newPassword = oldPassword
        if "s" or "S" or "a" or "o" or "O" or "c" or "C" or "i" or "I" or "e" or "E" in newPassword:
            newPassword = newPassword.replace("s", "$")
            newPassword = newPassword.replace("S", "$")
            newPassword = newPassword.replace("a", "@")
            newPassword = newPassword.replace("o", "0")
            newPassword = newPassword.replace("O", "0")
            newPassword = newPassword.replace("c", "(")
            newPassword = newPassword.replace("C", "(")
            newPassword = newPassword.replace("i", "1")
            newPassword = newPassword.replace("I", "1")
            newPassword = newPassword.replace("e", "3")
            newPassword = newPassword.replace("E", "3")
        else:
            newPassword = "Pick a stronger password to start!"
        if "!" in newPassword:
            newPassword = newPassword
            return render_template("passwords.html", password=newPassword)
        else:
            newPassword = newPassword + "!"
            return render_template("passwords.html", password=newPassword)
    else:
        return render_template("passwords.html", password=newPassword)

"""
@app.after_request
def securePassword(response):
    if request.path == "/passwords" and request.method == "POST":
        oldPassword = request.form["currentPassword"]
        newPassword = oldPassword
        newPassword.replace("s", "$")
        newPassword.replace("S", "$")
        newPassword.replace("a", "@")
        newPassword.replace("o", "0")
        newPassword.replace("O", "0")
        newPassword.replace("c", "(")
        newPassword.replace("C", "(")
        newPassword.replace("i", "1")
        newPassword.replace("I", "1")
        if "!" in newPassword:
            newPassword = newPassword
            return render_template("passwords.html")
        else:
            newPassword = newPassword + "!"
            return render_template("passwords.html")
    return response
"""
if __name__ == "__main__":
    app.run(debug=True)