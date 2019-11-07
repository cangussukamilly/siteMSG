from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MensagemForm(FlaskForm):
    mensahem = StringField ("Mensagem", validators=[DataRequired])
    botao = SubmitField('Enviar MSG')