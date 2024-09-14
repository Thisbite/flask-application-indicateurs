from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import logging
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from flask_login import UserMixin
import config as cf
import db_queries as ag
from models import Agent,Administrateur,Superviseur
import forms as fm
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
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user_login'

def questionnaire():
    if current_user.role !='agent':
        flash('Vous n\'êtes pas autorisé à accéder à cette page.')
        return redirect(url_for('home')) 
    nom_entite = ""
    nom_ind = None
    id_entite = None
    mon_id_indicateur = None
    id_code_entite = None
    id_indicateur = None
# Cette partie pour la liste deroulante dans le formulaire
    nom_groupe_age = []
    nom_sexe = []
    nom_cycle = []
    nom_prescolaire = []
    nom_primaire = []
    nom_secondaire_1er = []
    nom_secondaire_2nd = []
    nom_technique = []
    nom_superieur = []
    nom_professionnel = []
    nom_type_examen_scolaire = []
    nom_infrastructure_sanitaire = []
    nom_lieu_accouchement = []
    nom_etat_vaccinal = []
    nom_type_vaccination = []
    nom_pathologie = []
    nom_tranche_age = []
    nom_maladie_pev = []
    nom_maladie_infectieuse = []
    nom_infection_respiratoire = []
    nom_maladies_ist = []
    nom_type_maladies = []
    nom_activites_iec = []
    nom_services_medicaux = []
    nom_infrastructure_organisation = []
    nom_discipline_sportive = []
    nom_type_infrastructure_culturel = []
    nom_type_patrimoine_culturel = []
    nom_type_actions_culturelles = []
    nom_type_operateur_oeuvre_esprit = []
    nom_type_de_groupe_culturel = []
    nom_type_de_manifestation_culturelle = []
    nom_trimestre = []
    nom_etat_des_oeuvres = []
    nom_type_abonnement = []
    nom_type_de_suivi = []
    nom_type_de_vulnerabilite = []
    nom_type_de_prise_charge = []
    nom_niveau = []


# Cette partie est pour les indicateurs à plusieurs niveaux 
# Cette partie est pour les indicateurs à plusieurs niveaux 

    nom_groupe_age_A = fm.desagregation_map["1"]()
    nom_sexe_A = fm.desagregation_map["2"]()
    nom_cycle_A = fm.desagregation_map["4"]()
    nom_prescolaire_A = fm.desagregation_map["5"]()
    nom_primaire_A = fm.desagregation_map["6"]()
    nom_secondaire_1er_A = fm.desagregation_map["7"]()
    nom_secondaire_2nd_A = fm.desagregation_map["8"]()
    nom_technique_A = fm.desagregation_map["9"]()
    nom_superieur_A = fm.desagregation_map["10"]()
    nom_professionnel_A = fm.desagregation_map["11"]()
    nom_type_examen_scolaire_A = fm.desagregation_map["12"]()
    nom_infrastructure_sanitaire_A = fm.desagregation_map["13"]()
    nom_lieu_accouchement_A = fm.desagregation_map["14"]()
    nom_etat_vaccinal_A = fm.desagregation_map["15"]()
    nom_type_vaccination_A = fm.desagregation_map["16"]()
    nom_pathologie_A = fm.desagregation_map["17"]()
    nom_tranche_age_A = fm.desagregation_map["18"]()
    nom_maladie_pev_A = fm.desagregation_map["19"]()
    nom_maladie_infectieuse_A = fm.desagregation_map["20"]()
    nom_infection_respiratoire_A = fm.desagregation_map["21"]()
    nom_maladies_ist_A = fm.desagregation_map["22"]()
    nom_type_maladies_A = fm.desagregation_map["23"]()
    nom_activites_iec_A = fm.desagregation_map["24"]()
    nom_services_medicaux_A = fm.desagregation_map["25"]()
    nom_infrastructure_organisation_A = fm.desagregation_map["26"]()
    nom_discipline_sportive_A = fm.desagregation_map["27"]()
    nom_type_infrastructure_culturel_A = fm.desagregation_map["28"]()
    nom_type_patrimoine_culturel_A = fm.desagregation_map["29"]()
    nom_type_actions_culturelles_A = fm.desagregation_map["30"]()
    nom_type_operateur_oeuvre_esprit_A = fm.desagregation_map["31"]()
    nom_type_de_groupe_culturel_A = fm.desagregation_map["32"]()
    nom_type_de_manifestation_culturelle_A = fm.desagregation_map["33"]()
    nom_trimestre_A = fm.desagregation_map["34"]()
    nom_etat_des_oeuvres_A = fm.desagregation_map["35"]()
    nom_type_abonnement_A = fm.desagregation_map["36"]()
    nom_type_de_suivi_A = fm.desagregation_map["37"]()
    nom_type_de_vulnerabilite_A = fm.desagregation_map["38"]()
    nom_type_de_prise_charge_A = fm.desagregation_map["39"]()
    nom_niveau_A = fm.desagregation_map["40"]()
# Fin bloc

# Fin bloc 

    if request.method == 'POST':
        id_indicateur = request.form.get('id_indicateur')
        id_code_entite = request.form.get('id_code_entite')
        id_niveau_desagregation = request.form.get('id_niveau_desagregation')

        if id_indicateur and id_niveau_desagregation:
            indicator = ag.get_indicators(id_indicateur)
            entite_geog = ag.get_geographical_entity_name(id_code_entite)
            # Logique d'affectation en fonction du niveau de désagrégation
            if id_niveau_desagregation == "1":  # Groupe âge
                nom_groupe_age = fm.desagregation_map["1"]()
            elif id_niveau_desagregation == "2":  # Sexe
                nom_sexe =fm.desagregation_map["2"]()
            elif id_niveau_desagregation == "4":  # Cycle scolaire
                nom_cycle = fm.desagregation_map["4"]()
            elif id_niveau_desagregation == "5":  # Prescolaire
                nom_prescolaire = fm.desagregation_map["5"]()
            elif id_niveau_desagregation == "6":  # Primaire
                nom_primaire = fm.desagregation_map["6"]()
            elif id_niveau_desagregation == "7":  # secondaire 1er cycle
                nom_secondaire_1er = fm.desagregation_map["7"]()
            elif id_niveau_desagregation == "8":  # Secondaire 2nd cycle
                nom_secondaire_2nd = fm.desagregation_map["8"]()
            elif id_niveau_desagregation == "9":  # Technique
                nom_technique =fm.desagregation_map["9"]()
            elif id_niveau_desagregation == "10":  # Supérieur
                nom_superieur = fm.desagregation_map["10"]()
            elif id_niveau_desagregation == "11":  # Professionnel
                nom_professionnel =fm.desagregation_map["11"]()
            elif id_niveau_desagregation == "12":  # Type examen scolaire
                nom_type_examen_scolaire =fm.desagregation_map["12"]()
            elif id_niveau_desagregation == "13":  # Infrastructure sanitaire
                nom_infrastructure_sanitaire = fm.desagregation_map["13"]()
            elif id_niveau_desagregation == "14":  # Lieu d'accouchement
                nom_lieu_accouchement = fm.desagregation_map["14"]()
            elif id_niveau_desagregation == "15":  # Etat vaccinal
                nom_etat_vaccinal = fm.desagregation_map["15"]()
            elif id_niveau_desagregation == "16":  # Type de vaccination
                nom_type_vaccination = fm.desagregation_map["16"]()
            elif id_niveau_desagregation == "17":  # Pathologie
                nom_pathologie = fm.desagregation_map["17"]()
            elif id_niveau_desagregation == "18":  # Tranche d'âge
                nom_tranche_age = fm.desagregation_map["18"]()
            elif id_niveau_desagregation == "19":  # Maladies du PEV
                nom_maladie_pev = fm.desagregation_map["19"]()
            elif id_niveau_desagregation == "20":  # Maladies infectieuses
                nom_maladie_infectieuse = fm.desagregation_map["20"]()
            elif id_niveau_desagregation == "21":  # Infection respiratoire
                nom_infection_respiratoire =fm.desagregation_map["21"]()
            elif id_niveau_desagregation == "22":  # Maladie IST
                nom_maladies_ist = fm.desagregation_map["22"]()
            elif id_niveau_desagregation == "23":  # Type de maladies
                nom_type_maladies = fm.desagregation_map["23"]()
            elif id_niveau_desagregation == "24":  # Activités IEC
                nom_activites_iec =fm.desagregation_map["24"]()
            elif id_niveau_desagregation == "25":  # Services médicaux
                nom_services_medicaux = fm.desagregation_map["25"]()
            elif id_niveau_desagregation == "26":  # Infrastructure ou organisation sportive
                nom_infrastructure_organisation =fm.desagregation_map["26"]()
            elif id_niveau_desagregation == "27":  # Discipline sportive
                nom_discipline_sportive = fm.desagregation_map["27"]()
            elif id_niveau_desagregation == "28":  # Type infrastructure culturelle
                nom_type_infrastructure_culturel = fm.desagregation_map["28"]()
            elif id_niveau_desagregation == "29":  # Type de patrimoines culturel
                nom_type_patrimoine_culturel =fm.desagregation_map["29"]()
            elif id_niveau_desagregation == "30":  # Type actions culturelle
                nom_type_actions_culturelles =fm.desagregation_map["30"]()
            elif id_niveau_desagregation == "31":  # Type opérateurs oeuvres et esprit
                nom_type_operateur_oeuvre_esprit = fm.desagregation_map["31"]()
            elif id_niveau_desagregation == "32":  # Type de groupe culturel
                nom_type_de_groupe_culturel = fm.desagregation_map["32"]()
            elif id_niveau_desagregation == "33":  # Type de manifestation culturelle
                nom_type_de_manifestation_culturelle = fm.desagregation_map["33"]()
            elif id_niveau_desagregation == "34":  # Trimestre
                nom_trimestre = fm.desagregation_map["34"]()
            elif id_niveau_desagregation == "35":  # Etat des oeuvres
                nom_etat_des_oeuvres =fm.desagregation_map["35"]()
            elif id_niveau_desagregation == "36":  # Type d'abonnements
                nom_type_abonnement = fm.desagregation_map["36"]()
            elif id_niveau_desagregation == "37":  # Type de suivi
                nom_type_de_suivi = fm.desagregation_map["37"]()
            elif id_niveau_desagregation == "38":  # Type de vulnérabilités
                nom_type_de_vulnerabilite = fm.desagregation_map["38"]()
            elif id_niveau_desagregation == "39":  # Type de prise en charge
                nom_type_de_prise_charge =fm.desagregation_map["39"]()
            elif id_niveau_desagregation == "40":  # Niveau
                nom_niveau = fm.desagregation_map["40"]()

            if indicator:
                mon_id_indicateur, nom_ind = indicator
            else:
                nom_ind = "Indicateur non trouvé"
            if entite_geog:
                id_entite, nom_entite = entite_geog

    return render_template('questionnaire.html',
                nom_ind=nom_ind,
                id_entite=id_entite,
                nom_entite=nom_entite,
                id_code_entite=id_code_entite,
                id_indicateur=id_indicateur,
                nom_groupe_age = nom_groupe_age,
                nom_groupe_age_A = nom_groupe_age_A,
                nom_sexe = nom_sexe,
                nom_sexe_A = nom_sexe_A,
                nom_cycle = nom_cycle,
                nom_cycle_A = nom_cycle_A,
                nom_prescolaire = nom_prescolaire,
                nom_prescolaire_A = nom_prescolaire_A,
                nom_primaire = nom_primaire,
                nom_primaire_A = nom_primaire_A,
                nom_secondaire_1er = nom_secondaire_1er,
                nom_secondaire_1er_A = nom_secondaire_1er_A,
                nom_secondaire_2nd = nom_secondaire_2nd,
                nom_secondaire_2nd_A = nom_secondaire_2nd_A,
                nom_technique = nom_technique,
                nom_technique_A = nom_technique_A,
                nom_superieur = nom_superieur,
                nom_superieur_A = nom_superieur_A,
                nom_professionnel = nom_professionnel,
                nom_professionnel_A = nom_professionnel_A,
                nom_type_examen_scolaire = nom_type_examen_scolaire,
                nom_type_examen_scolaire_A = nom_type_examen_scolaire_A,
                nom_infrastructure_sanitaire = nom_infrastructure_sanitaire,
                nom_infrastructure_sanitaire_A = nom_infrastructure_sanitaire_A,
                nom_lieu_accouchement = nom_lieu_accouchement,
                nom_lieu_accouchement_A = nom_lieu_accouchement_A,
                nom_etat_vaccinal = nom_etat_vaccinal,
                nom_etat_vaccinal_A = nom_etat_vaccinal_A,
                nom_type_vaccination = nom_type_vaccination,
                nom_type_vaccination_A = nom_type_vaccination_A,
                nom_pathologie = nom_pathologie,
                nom_pathologie_A = nom_pathologie_A,
                nom_tranche_age = nom_tranche_age,
                nom_tranche_age_A = nom_tranche_age_A,
                nom_maladie_pev = nom_maladie_pev,
                nom_maladie_pev_A = nom_maladie_pev_A,
                nom_maladie_infectieuse = nom_maladie_infectieuse,
                nom_maladie_infectieuse_A = nom_maladie_infectieuse_A,
                nom_infection_respiratoire = nom_infection_respiratoire,
                nom_infection_respiratoire_A = nom_infection_respiratoire_A,
                nom_maladies_ist = nom_maladies_ist,
                nom_maladies_ist_A = nom_maladies_ist_A,
                nom_type_maladies = nom_type_maladies,
                nom_type_maladies_A = nom_type_maladies_A,
                nom_activites_iec = nom_activites_iec,
                nom_activites_iec_A = nom_activites_iec_A,
                nom_services_medicaux = nom_services_medicaux,
                nom_services_medicaux_A = nom_services_medicaux_A,
                nom_infrastructure_organisation = nom_infrastructure_organisation,
                nom_infrastructure_organisation_A = nom_infrastructure_organisation_A,
                nom_discipline_sportive = nom_discipline_sportive,
                nom_discipline_sportive_A = nom_discipline_sportive_A,
                nom_type_infrastructure_culturel = nom_type_infrastructure_culturel,
                nom_type_infrastructure_culturel_A = nom_type_infrastructure_culturel_A,
                nom_type_patrimoine_culturel = nom_type_patrimoine_culturel,
                nom_type_patrimoine_culturel_A = nom_type_patrimoine_culturel_A,
                nom_type_actions_culturelles = nom_type_actions_culturelles,
                nom_type_actions_culturelles_A = nom_type_actions_culturelles_A,
                nom_type_operateur_oeuvre_esprit = nom_type_operateur_oeuvre_esprit,
                nom_type_operateur_oeuvre_esprit_A = nom_type_operateur_oeuvre_esprit_A,
                nom_type_de_groupe_culturel = nom_type_de_groupe_culturel,
                nom_type_de_groupe_culturel_A = nom_type_de_groupe_culturel_A,
                nom_type_de_manifestation_culturelle = nom_type_de_manifestation_culturelle,
                nom_type_de_manifestation_culturelle_A = nom_type_de_manifestation_culturelle_A,
                nom_trimestre = nom_trimestre,
                nom_trimestre_A = nom_trimestre_A,
                nom_etat_des_oeuvres = nom_etat_des_oeuvres,
                nom_etat_des_oeuvres_A = nom_etat_des_oeuvres_A,
                nom_type_abonnement = nom_type_abonnement,
                nom_type_abonnement_A = nom_type_abonnement_A,
                nom_type_de_suivi = nom_type_de_suivi,
                nom_type_de_suivi_A = nom_type_de_suivi_A,
                nom_type_de_vulnerabilite = nom_type_de_vulnerabilite,
                nom_type_de_vulnerabilite_A = nom_type_de_vulnerabilite_A,
                nom_type_de_prise_charge = nom_type_de_prise_charge,
                nom_type_de_prise_charge_A = nom_type_de_prise_charge_A,
                nom_niveau = nom_niveau,
                nom_niveau_A = nom_niveau_A
            )
    