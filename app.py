from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import logging
import mysql.connector
import config as cf
import db_queries as ag

app = Flask(__name__)

# Configuration de la clé secrète pour les sessions Flask
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', '774d8fe18f818cdb0f03a7d2471d55797c709a6aede6289dcc24481a7a92f40a')

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configuration du logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def index():
    nom_groupe_age = ag.get_groupe_age()

    nom_ind = None
    id_entite = None
    id_code_entite = None
    id_indicateur = None
    nom_entite = ""

    if request.method == 'POST':
        # Récupère le code indicateur et le code entité saisi par l'utilisateur
        id_indicateur = request.form.get('id_indicateur')
        id_code_entite = request.form.get('id_code_entite')

        if id_indicateur:
            # Utilisation de la fonction get_indicators avec la valeur saisie
            indicator = ag.get_indicators(id_indicateur)
            entite_geog = ag.get_geographical_entity_name(id_code_entite)

            if indicator:
                mon_id_indicateur, nom_ind = indicator
            else:
                nom_ind = "Indicateur non trouvé"
            if entite_geog:
                id_entite, nom_entite = entite_geog

    return render_template('index.html', nom_groupe_age=nom_groupe_age, nom_ind=nom_ind, id_entite=id_entite,
                           nom_entite=nom_entite, id_code_entite=id_code_entite, id_indicateur=id_indicateur)

@app.route('/submit', methods=['POST'])
def submit():
    # Récupère les données passées à la route submit
    mon_id_indicateur = request.form.get('id_indicateur2')
    id_code_entite = request.form.get('id_code_entite2')

    sous_prefecture_id = None
    region_id = None
    department_id = None

    if ag.get_region_name(id_code_entite):
        region_id = id_code_entite
    elif ag.get_department_name(id_code_entite):
        department_id = id_code_entite
    elif ag.get_sous_prefecture_name(id_code_entite):
        sous_prefecture_id = id_code_entite

    # Récupération de l'année
    annee = request.form.get('anne')

    # Traitement des données du formulaire
    data = request.form
    for key, value in data.items():
        if key.startswith('id_'):
            id_grpe_age = key.split('_')[1]
            valeur = value
            cf.insertion_value(valeur=valeur, groupe_age_id=id_grpe_age, indicator_id=mon_id_indicateur,
                              sous_prefecture_id=sous_prefecture_id, region_id=region_id, department_id=department_id, annee=annee)

    # Ajout d'un message flash pour informer l'utilisateur
    flash(f"Form submitted successfully! Annee: {annee}, Indicateur ID: {mon_id_indicateur}, Entite ID: {id_code_entite}")

    # Redirection vers la route d'affichage du formulaire
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
