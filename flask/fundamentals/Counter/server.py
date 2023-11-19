from flask import Flask, render_template , session , request

app = Flask(__name__)
num=1
app.secret_key = 'jnazhedbeubdf'

@app.route('/', methods=['GET','POST'])
def count():
    if 'num' not in session:
        session['num'] = 1
    else:
        if request.method == 'POST':
            if 'reset' in request.form:
                session['num'] = 1
            else:
                session['num'] += 1
    return render_template("index.html", num=session['num'])


if __name__ == "__main__":
    app.run(debug=True)
