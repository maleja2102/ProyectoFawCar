from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class formIngreso(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='Obligatorio')], render_kw={'placeholder':'Usuario', 'class':'form-control form-control-lg'})
    contrasena = PasswordField('Contraseña', validators=[DataRequired(message='Mínimo 5 caracteres')], render_kw={'placeholder':'Contraseña', 'class':'form-control form-control-lg'})
    iniciar = SubmitField('Ingresar', render_kw={'class':'btn btn-dark btn-lg btn-block', 'onmouseover':'guardarEst()'})