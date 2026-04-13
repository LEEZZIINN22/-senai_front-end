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
    if 'user' not in session:
        return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html") # Renderiza um template
<<<<<<< HEAD

@bp.route("/dashboard") # cria uma rota para navegador 
def dashboard(): # função que gerencia rota deve ser única
    """ Painel de Vendas"""
    #  if 'user' not in session:  # garnate autenticação
    #       return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html", title = "Painel de Vendas") # Renderiza um template
=======
    ks

@bp.route("/dashboard") # cria uma rota
def dashboard(): # função que gerencia rota
    """ Painel de vendas"""
    # if 'user' not in session:
        # return redirect(url_for("auth.login"))
    return render_template("dashboard/index.html", title="Painel de vendas") # Renderiza um template
>>>>>>> 860074fbeb6f42c79deda0f914060da2ce143584
