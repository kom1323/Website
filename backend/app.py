from flask import Flask, render_template, request
from DataBase import DataBase

app = Flask(__name__, template_folder=r"..\templates")
db = DataBase(r".\backend\New-Zealand-period-life-tables-2017-2019-CSV.csv")


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods = ['GET', 'POST'])
def search():
    if request.method == 'GET':
        print("the button is pressed")
        print(request.form.getlist("search"))
        return render_template("home.html", data=db.get_first_row())


    


if __name__ == "__main__":
    app.run()