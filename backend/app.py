from flask import Flask, render_template, request


app = Flask(__name__, template_folder=r"..\templates")


@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        print("the button is pressed")
    return render_template("home.html")

    


if __name__ == "__main__":
    app.run()