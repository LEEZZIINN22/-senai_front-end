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

@bp.route("/dashboard") # cria uma rota para navegador 
def dashboard(): # função que gerencia rota deve ser única
    """ Painel de Vendas"""
    #  if 'user' not in session:  # garnate autenticação
    #       return redirect(url_for("auth.login"))

    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    vendas: list = [
        {"mês": "Janeiro" , "total" :139519.19},
        {"mês": "fevereiro" , "total" :99519.19},
        {"mês": "março" , "total" :149519.19},
        {"mês": "abril" , "total" :179519.19},
        {"mês": "maio" , "total" :199519.19},
        {"mês": "junho" , "total" :259519.19},
        {"mês": "julho" , "total" :509519.19},
        {"mês": "agosto" , "total" :209519.19},
        {"mês": "setembro" , "total" :129519.19},
        {"mês": "outubro" , "total" :119519.19},
        {"mês": "novembro" , "total" :109519.19},
        {"mês": "dezembrO" , "total" :479519.19},


     
    ] # fim lista de vendas
    return render_template("dashboard/index.html", title = "Painel de Vendas", vendas = vendas, locale = locale ) 
# Renderiza um template

