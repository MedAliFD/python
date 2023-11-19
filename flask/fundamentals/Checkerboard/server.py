from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def index4():
    return render_template("index4.html")


@app.route('/<int:x>/<int:y>')
def index_xy(x,y):
    return render_template("index_xy.html", x=int(x), y=int(y) )



if __name__ == "__main__":
    app.run(debug=True)
