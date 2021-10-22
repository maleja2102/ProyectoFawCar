from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class formRegistro(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(message='Obligatorio')], render_kw={'placeholder':'Usuario', 'class':'form-control'})
    password = PasswordField('Contraseña', validators=[DataRequired(message='Mínimo 5 caracteres')], render_kw={'placeholder':'Contraseña', 'class':'form-control'})
    confirm = PasswordField('Confirmar Contraseña', validators=[DataRequired(message='Mínimo 5 caracteres')], render_kw={'placeholder':'Confirmar Contraseña', 'class':'form-control'})
    email = EmailField('Correo', validators=[DataRequired(message='Obligatorio')], render_kw={'placeholder':'ejemplo@ejemplo.com', 'class':'form-control'})
    name = StringField('Nombres', validators=[DataRequired(message='Obligatorio')], render_kw={'placeholder':'Nombres', 'class':'form-control'})
    surname = StringField('Apellidos', validators=[DataRequired(message='Obligatorio')], render_kw={'placeholder':'Apellidos', 'class':'form-control'})
    personalId = StringField('Identificacion', validators=[DataRequired(message='Obligatorio')], render_kw={'placeholder':'Identificación', 'class':'form-control'})
    registrar = SubmitField('Registrarse', render_kw={'class':'btn btn-dark btn-lg btn-block', 'onmouseover':'guardarEst()'})
