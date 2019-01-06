from flask import render_template, url_for, redirect, request, jsonify
from app import app
from app.controllers.auxiliar import Cotacao
from app.models.Form import FiltroCot


@app.route('/Home', methods=('GET', 'POST'))
@app.route('/', methods=('GET', 'POST'))
def home():
        
        return render_template('index_v1.html')

@app.route('/cotacao', methods=('GET' , 'POST'))
def cotacao():
        form = FiltroCot()

        data = form.data
        if request.method == 'POST':
                        print(data)

        return render_template('cotacao_v2.html', form= form)

@app.route('/cotVisuPrin')
def cotVisuPrin():
        coll = Cotacao()
        results = coll.cotVisuPrin()

        return jsonify(data=results)

