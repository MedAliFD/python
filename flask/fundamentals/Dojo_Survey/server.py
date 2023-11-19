from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'jnazhedbeubdf'


@app.route('/', methods=['GET', 'POST'])
def feedback_form():
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        comment = request.form['comment']
        # Store form data in the session
        session['form_data'] = {
            'name': name,
            'country': country,
            'comment': comment
        }
        # Redirect to the result page
        return redirect('/result')
    return render_template("index.html")


@app.route('/result')
def result():
    form_data = session.get('form_data', {})
    # Clear the form data from the session to avoid displaying it again on refresh
    session.pop('form_data', None)

    return render_template("result.html", form_data=form_data)


if __name__ == "__main__":
    app.run(debug=True)
