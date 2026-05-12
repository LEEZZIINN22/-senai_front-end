"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

bp = Blueprint(__name__, "HomeController")

@bp.route("/") # cria uma rota
def index(): # função que gerencia rota
    """ Página inicial"""
    if '_user_id' not in session:
        return redirect(url_for("auth.login"))
   
    return render_template("dashboard/index.html") # Renderiza um template

@bp.route("/dashboard") # cria uma rota para navegador http://127.0.0.1:5000/dashboard
def dashboard(): # função que gerencia rota deve ser única
    """ Painel de Vendas"""
    #  if 'user' not in session:  # garnate autenticação
    #       return redirect(url_for("auth.login"))
    import locale
    # Define a localidade para português do Brasil
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    vendas: list = [
        {"mes":"Janeiro", "total": 128742.36},
        {"mes":"Fevereiro", "total": 18452.91},
        {"mes":"Março", "total": 13210.74},
        {"mes":"Abril", "total": 9754.28},
        {"mes":"Maio", "total": 14123.67},
        {"mes":"Junho", "total": 8631.42},
        {"mes":"Julho", "total": 10458.93},
        {"mes":"Agosto", "total": 12387.15},
        {"mes":"Setembro", "total": 13776.48},
        {"mes":"Outubro", "total": 14992.31},
        {"mes":"Novembro", "total": 11754.66},
        {"mes":"Dezembro", "total": 16840.27}
    ] # fim da lista de vendas
    
    return render_template("dashboard/index.html", title = "Painel de Vendas", vendas = vendas, locale = locale) # Renderiza um template
