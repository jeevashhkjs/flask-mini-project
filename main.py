from flask import Flask, render_template, request

application = Flask("__name__")

@application.route("/", methods=["GET", "POST"])
def home():
    return render_template('register.html')

@application.route("/create",methods=["GET","POST"])
def getvalues():
    if request.method == "POST":
        nam=request.form.get("name")
        mal=request.form.get("email")
        return render_template('getvalue.html',name=nam,email=mal)

application.run(debug=True,port=8080)