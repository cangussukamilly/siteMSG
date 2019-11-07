from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from formulario import MensagemForm

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///minhasmensagens.db"
app.config['SECRET_KEY'] = 'ÇHIHOOYOFYDYG26MN2L'

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.Text, nullable=False)

    def __repre__(self):
        return self.mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/NovaMensagem', methods=['POST','GET'])
def NovaMensagem():

    form = MensagemForm()
    print(form.mensagem.data)

    return render_template('Mensagens.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)