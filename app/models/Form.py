#from flask_mongoengine.wtf import model_form
#from app import db
from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, Form

class FiltroCot(FlaskForm):
    rdPesquisaPor = RadioField('Escolha a opção de Busca:', default='1', choices=[(1,' Por Fonte'),(2,' Por Mercado'),(3,' Por Classe de Ativos'), (4,' Por Ativo')])
    txtBusca = StringField(render_kw={"placeholder": "O que deseja consultar?"})

