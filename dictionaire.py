from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import logging
import mysql.connector
import config as cf
import db_queries as ag
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,Table,MetaData,select,insert,delete




app = Flask(__name__)

# Configuration de la clé secrète pour les sessions Flask
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', '774d8fe18f818cdb0f03a7d2471d55797c709a6aede6289dcc24481a7a92f40a')

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

engine = create_engine(url=f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}")

try:
    # Création de l'engine et de la session
    engine = create_engine(url=f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Chargement de la table avec autoload
    meta = MetaData()
    valeur_indicateurs = Table('ValeursIndicateurs', meta, autoload_with=engine)

    # Suppression des lignes avec des valeurs NULL
    supprime_vide = delete(valeur_indicateurs).where(valeur_indicateurs.c.Valeur.is_(None))
    session.execute(supprime_vide)
    session.commit()

    print('Connexion réussie Ok')

except Exception as e:
    print(f"Erreur lors de la connexion: {e}")

finally:
    # Nettoyage de la session
   pass
