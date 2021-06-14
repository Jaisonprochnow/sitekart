from flask import Flask, redirect
from flask_mail import Mail, Message

from kartdosamigos.ContactForm import ContactForm, csrf

app = Flask(__name__)

mail = Mail()

app.config['SECRET_KEY'] = '29cecf8afd6176f06bb3f55472d490d1'
csrf.init_app(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jaisonprochnow@gmail.com'
app.config['MAIL_PASSWORD'] = 'Gabi@12345'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)


def send_message(message):
    print(message.get('email'))

    msg = Message(message.get('subject'),
                  sender=message.get('email'),
                  recipients=['jaisonprochnow@gmail.com', 'egotcham@yahoo.com.br'],
                  )

    msg.body = ('''Mensagem enviada de: {}

Email: {}
                 
Mensagem: {}        
                
''').format(message.get('name'), message.get('email'), message.get('message'))
    mail.send(msg)


from kartdosamigos import routes
