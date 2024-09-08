from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error
from flask import Flask,g

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

import mysql.connector

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,Table,MetaData,delete


# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Utiliser les variables d'environnement
host = os.getenv('MYSQL_HOST')
database = os.getenv('MYSQL_DATABASE')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')

def create_connection():
    try:
        conn = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if conn.is_connected():
            print("Connexion à la base de données MySQL réussie")
            return conn
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL : {e}")
        return None

def get_db():
    if 'db' not in g:
        g.db = create_connection()
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()





def insertion_value(id,indicator_id, region_id, department_id, sous_prefecture_id, valeur, annee, sexe_id=None,
                    groupe_age_id=None, age_id=None, cycle_id=None, niveau_prescolaire_id=None,
                    niveau_primaire_id=None, niveau_secondaire_1er_cycle_id=None,
                    niveau_secondaire_2nd_cycle_id=None, niveau_technique_id=None,
                    niveau_superieur_id=None, niveau_professionnel_id=None, type_examen_id=None,
                    infrastructures_sanitaires_id=None, lieu_accouchement_id=None, etat_vaccinal_id=None,
                    types_de_vaccination_id=None, pathologie_id=None, tranche_age_id=None,
                    maladies_du_pev_id=None, maladies_infectieuses_id=None, infection_respiratoire=None,
                    maladies_ist_id=None, type_de_maladie_id=None, activites_iec_id=None,
                    service_medicaux_id=None, type_infrastructures_ou_organisations_sportives_id=None,
                    disciplines_sportives_id=None, type_infrastructures_culturelles_id=None,
                    f_type_de_patrimoines_culturels_immat_id=None, type_actions_culturelles_et_artistiques_id=None,
                    type_operateurs_des_oeuvres_esprit_id=None, type_de_groupes_culturels_id=None,
                    type_de_manifestations_culturelles_id=None, trimestre_id=None, etat_des_ouvrages_id=None,
                    type_abonnement_id=None, type_suivi_id=None, type_de_vulnerabilite_id=None,
                    type_de_prise_charge_id=None, niveau_id=None):
    if valeur == '':
        valeur = None
    try:
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO ValeursIndicateurs (
                    id,Valeur, Annee, f_sexe_id, f_grp_age_id, f_age_id, f_cycle_id, f_region_id, f_departement_id,
                    f_sous_prefecture_id, f_indicateur_id, f_niveau_prescolaire_id, f_niveau_primaire_id,
                    f_niveau_secondaire_1er_cycle_id, f_niveau_secondaire_2nd_cycle_id, f_niveau_technique_id,
                    f_niveau_superieur_id, f_niveau_professionnel_id, f_type_examen_id, f_infrastructures_sanitaires_id,
                    f_lieu_accouchement_id, f_etat_vaccinal_id, f_types_de_vaccination_id, f_pathologie_id,
                    f_tranche_age_id, f_maladies_du_pev_id, f_maladies_infectieuses_id, f_infectieuses_respiratoire_id,
                    f_maladies_ist_id, f_type_de_maladie_id, f_activites_iec_id, f_service_medicaux_id,
                    f_type_infrastructures_ou_organisations_sportives_id, f_disciplines_sportives_id,
                    f_type_infrastructures_culturelles_id, f_type_de_patrimoines_culturels_immat_id,
                    f_type_actions_culturelles_et_artistiques_id, f_type_operateurs_des_oeuvres_esprit_id,
                    f_type_de_groupes_culturels_id, f_type_de_manifestations_culturelles_id, f_trimestre_id,
                    f_etat_des_ouvrages_id, f_type_abonnement_id, f_type_suivi_id, f_type_de_vulnerabilite_id,
                    f_type_de_prise_charge_id, f_niveau_id
                )
                VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)
            """, (id,valeur, annee, sexe_id, groupe_age_id, age_id, cycle_id, region_id, department_id, sous_prefecture_id,
                  indicator_id, niveau_prescolaire_id, niveau_primaire_id, niveau_secondaire_1er_cycle_id,
                  niveau_secondaire_2nd_cycle_id, niveau_technique_id, niveau_superieur_id, niveau_professionnel_id,
                  type_examen_id, infrastructures_sanitaires_id, lieu_accouchement_id, etat_vaccinal_id,
                  types_de_vaccination_id, pathologie_id, tranche_age_id, maladies_du_pev_id,
                  maladies_infectieuses_id, infection_respiratoire, maladies_ist_id, type_de_maladie_id,
                  activites_iec_id, service_medicaux_id, type_infrastructures_ou_organisations_sportives_id,
                  disciplines_sportives_id, type_infrastructures_culturelles_id, f_type_de_patrimoines_culturels_immat_id,
                  type_actions_culturelles_et_artistiques_id, type_operateurs_des_oeuvres_esprit_id,
                  type_de_groupes_culturels_id, type_de_manifestations_culturelles_id, trimestre_id,
                  etat_des_ouvrages_id, type_abonnement_id, type_suivi_id, type_de_vulnerabilite_id,
                  type_de_prise_charge_id, niveau_id))

            conn.commit()
            print("Insertion réussie.")
    except mysql.connector.Error as e:
        print(f"Erreur de table valeur indicateur: {e}")
    except Exception as e:
        print(f"Erreur de fonction insertion de valeur indicateur: {e}")
        


import random

# Fonction pour générer une clé unique
def generate_unique_key():
    part1 = str(random.randint(0, 99)).zfill(2)
    part2 = str(random.randint(0, 99)).zfill(2)
    part3 = str(random.randint(0, 99)).zfill(2)
    part4 = str(random.randint(0, 99)).zfill(2)
    
    unique_key = f"{part1}-{part2}-{part3}-{part4}"
    return unique_key






app = Flask(__name__)

# Configuration de la clé secrète pour les sessions Flask
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', '774d8fe18f818cdb0f03a7d2471d55797c709a6aede6289dcc24481a7a92f40a')

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)



def fonction_suprression_vide():
    
    
    try:
        # Création de l'engine et de la session
        engine = create_engine(url=f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}")
        Session = sessionmaker(bind=engine)
        session = Session()

        # Chargement de la table avec autoload
        meta = MetaData()
        valeur_indicateurs = Table('ValeursIndicateurs', meta, autoload_with=engine)

        # Suppression des lignes avec des valeurs NULL
        supprime_vide = delete(valeur_indicateurs).where(valeur_indicateurs.c.Valeur==valeur_indicateurs.c.Annee)
        session.execute(supprime_vide)
        session.commit()

        print('Connexion réussie Ok')

    except Exception as e:
        print(f"Erreur lors de la connexion: {e}")

    finally:
        # Nettoyage de la session
        pass
