from flask import Flask, render_template, url_for, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def about():
    return render_template("index.html")

@app.route("/passwords", methods=["POST", "GET"])
def passwords():
    return render_template("passwords.html")

@app.route("/secure", methods=["POST", "GET"])
def secure():
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
            return render_template("securepasswords.html", password=newPassword)
        else:
            newPassword = newPassword + "!"
            return render_template("securepasswords.html", password=newPassword)
    else:
        return render_template("securepasswords.html", password=newPassword)

@app.route("/check", methods=["POST", "GET"])
def check():
    enteredPassword = ""
    message = ""

    def hasSpecialChars(word):
        specialChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '_']
        result = any(element in word for element in specialChars)
        return result

    def hasNums(word):
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        result = any(element in word for element in nums)
        return result

    if request.method == "POST":
        enteredPassword = request.form["currentPassword"]
        if enteredPassword.lower() == enteredPassword and hasSpecialChars(enteredPassword) == False and len(enteredPassword) < 12 and hasNums(enteredPassword) == False:
            message = "WEAK"
        if enteredPassword.lower() != enteredPassword or hasSpecialChars(enteredPassword) == True or len(enteredPassword) >= 12 or hasNums(enteredPassword) == True:
            message = "MEDIUM STRENGTH"
        if enteredPassword.lower() != enteredPassword and hasSpecialChars(enteredPassword) == True and len(enteredPassword) >= 12 and hasNums(enteredPassword) == True:
            message = "STRONG"
        return render_template("checkpasswords.html", message=message)
    else:
        return render_template("checkpasswords.html")

if __name__ == "__main__":
    app.run(debug=True)