from flask import Flask, render_template, request, redirect, url_for
from app.models import Usuario
from flask_login import current_user, login_user, logout_user
from datetime import datetime
from app import app, db


# Exemplo de dados
usuarios_saldo = {
    'Ideal Guapo': 1500.00,
    'Combustíveis Guapo': 2380.75,
    'Ivaiporã': 322.00,
    'Rede Guapo': 982.30
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        cpf = request.form['cpf']
        pwd = request.form['password']

        user = Usuario.query.filter_by(cpf=cpf).first()
       
        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))        

        login_user(user)
        return redirect(url_for('index'))

    return render_template('auth/login.html')

@app.route('/controleusuario', methods=['GET', 'POST'])
def controleusuario():
    if current_user.is_authenticated:
        
        return render_template('auth/controleusuario.html')
    else:
     return redirect(url_for('login'))
    
@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if current_user.is_authenticated:
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            cpf = request.form['cpf']
            pwd = request.form['password']
            dt_inclusao = datetime.now()

            user = Usuario(nome, email, cpf, pwd, dt_inclusao)
            db.session.add(user)
            db.session.commit()
        return render_template('auth/registrar.html')
    else:
     return redirect(url_for('login'))
    

@app.route('/')
def index():
    # validar login
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
     return redirect(url_for('login'))


@app.route('/consultar', methods=['POST'])
def consultar():
    nome = request.form['nome'].strip().lower()
    saldo = usuarios_saldo.get(nome)
   
    if current_user.is_authenticated:
       return render_template('resultado.html', nome=nome.capitalize(), saldo=saldo)
    else:
     return redirect(url_for('login'))


@app.route('/contatos')
def contatos():
    # validar login
    if current_user.is_authenticated:
       return render_template('contatos.html')
    else:
     return redirect(url_for('login'))
    

@app.route('/consultapix')
def consultapix():
    # validar login
    if current_user.is_authenticated:
       return render_template('consultapix.html')
    else:
     return redirect(url_for('login'))
    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
