from flask import render_template, request
from kartdosamigos import app
from kartdosamigos.ContactForm import ContactForm
from kartdosamigos import send_message, redirect



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato', methods=['POST', 'GET'])
def contato():
    form = ContactForm()
    if form.validate_on_submit():
        print('-------------------------')
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['subject'])
        print(request.form['message'])
        print('-------------------------')
        send_message(request.form)
        return redirect('/')

    return render_template('contato.html', form=form)

@app.route('/sobre_nos')
def sobre_nos():
    return render_template('sobre_nos.html')

@app.route('/resultado')
def resultado():
    return render_template('resultado.html')

@app.route('/videos2021')
def videos2021():
    return render_template('videos2021.html')

@app.route('/videos2020')
def videos2020():
    return render_template('videos2020.html')


@app.route('/regulamento')
def regulamento():
    return render_template('regulamento.html')

@app.route('/regulamento2')
def regulamento2():
    return render_template('regulamento2.html')

@app.route('/css')
def css():
    return render_template('/css/home.css')

@app.route('/patrocinadores')
def patrocinadores():
    return render_template('patrocinadores.html')

@app.route('/videos2019')
def videos2019():
    return render_template('videos2019.html')

@app.route('/videos2018')
def videos2018():
    return render_template('videos2018.html')

@app.route('/videos2017')
def videos2017():
    return render_template('videos2017.html')

@app.route('/entrevistas')
def entrevistas():
    return render_template('entrevistas.html')

@app.route('/agenda')
def agenda():
    return render_template('agenda.html')

