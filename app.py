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
cf.fonction_suprression_vide()

@app.route('/', methods=['GET', 'POST'])
def index():

    nom_entite = ""
    nom_ind = None
    id_entite = None
    mon_id_indicateur = None
    id_code_entite = None
    id_indicateur = None
    # Initialisation des listes
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
    if request.method == 'POST':
        id_indicateur = request.form.get('id_indicateur')
        id_code_entite = request.form.get('id_code_entite')
        id_niveau_desagregation = request.form.get('id_niveau_desagregation')

        if id_indicateur and id_niveau_desagregation:
            indicator = ag.get_indicators(id_indicateur)
            entite_geog = ag.get_geographical_entity_name(id_code_entite)
            id_desagregation, nom_desagregation = ag.get_niveau_desagregation(id_niveau_desagregation)



            # Logique d'affectation en fonction du niveau de désagrégation
            if id_niveau_desagregation == "1":  # Groupe âge
                nom_groupe_age = ag.get_groupe_age()
            elif id_niveau_desagregation == "2":  # Sexe
                nom_sexe = ag.get_sexes()
            elif id_niveau_desagregation == "4":  # Cycle scolaire
                nom_cycle = ag.get_cycle()
            elif id_niveau_desagregation == "5":  # Prescolaire
                nom_prescolaire = ag.get_niveau_prescolaire()
            elif id_niveau_desagregation == "6":  # Primaire
                nom_primaire = ag.get_niveau_primaire()
            elif id_niveau_desagregation == "7":  # secondaire 1er cycle
                nom_secondaire_1er = ag.get_niveau_secondaire_1er_cycle()
            elif id_niveau_desagregation == "8":  # Secondaire 2nd cycle
                nom_secondaire_2nd = ag.get_niveau_secondaire_2nd_cycle()
            elif id_niveau_desagregation == "9":  # Technique
                nom_technique = ag.get_niveau_technique()
            elif id_niveau_desagregation == "10":  # Supérieur
                nom_superieur = ag.get_niveau_superieur()
            elif id_niveau_desagregation == "11":  # Professionnel
                nom_professionnel = ag.get_niveau_professionnel()
            elif id_niveau_desagregation == "12":  # Type examen scolaire
                nom_type_examen_scolaire = ag.get_type_examen()
            elif id_niveau_desagregation == "13":  # Infrastructure sanitaire
                nom_infrastructure_sanitaire = ag.get_infrastructures_sanitaires()
            elif id_niveau_desagregation == "14":  # Lieu d'accouchement
                nom_lieu_accouchement = ag.get_lieu_accouchement()
            elif id_niveau_desagregation == "15":  # Etat vaccinal
                nom_etat_vaccinal = ag.get_etat_vaccinal()
            elif id_niveau_desagregation == "16":  # Type de vaccination
                nom_type_vaccination = ag.get_types_de_vaccination()
            elif id_niveau_desagregation == "17":  # Pathologie
                nom_pathologie = ag.get_pathologie()
            elif id_niveau_desagregation == "18":  # Tranche d'âge
                nom_tranche_age = ag.get_tranche_age()
            elif id_niveau_desagregation == "19":  # Maladies du PEV
                nom_maladie_pev = ag.get_maladies_du_pev()
            elif id_niveau_desagregation == "20":  # Maladies infectieuses
                nom_maladie_infectieuse = ag.get_maladies_infectieuses()
            elif id_niveau_desagregation == "21":  # Infection respiratoire
                nom_infection_respiratoire = ag.get_infections_respiratoires()
            elif id_niveau_desagregation == "22":  # Maladie IST
                nom_maladies_ist = ag.get_maladies_ist()
            elif id_niveau_desagregation == "23":  # Type de maladies
                nom_type_maladies = ag.get_type_de_maladie()
            elif id_niveau_desagregation == "24":  # Activités IEC
                nom_activites_iec = ag.get_activites_iec()
            elif id_niveau_desagregation == "25":  # Services médicaux
                nom_services_medicaux = ag.get_service_medicaux()
            elif id_niveau_desagregation == "26":  # Infrastructure ou organisation sportive
                nom_infrastructure_organisation = ag.get_type_infrastructures_ou_organisations_sportives()
            elif id_niveau_desagregation == "27":  # Discipline sportive
                nom_discipline_sportive = ag.get_disciplines_sportives()
            elif id_niveau_desagregation == "28":  # Type infrastructure culturelle
                nom_type_infrastructure_culturel = ag.get_type_infrastructures_culturelles()
            elif id_niveau_desagregation == "29":  # Type de patrimoines culturel
                nom_type_patrimoine_culturel = ag.get_type_de_patrimoines_culturels_immateriels()
            elif id_niveau_desagregation == "30":  # Type actions culturelle
                nom_type_actions_culturelles = ag.get_type_actions_culturelles_et_artistiques()
            elif id_niveau_desagregation == "31":  # Type opérateurs oeuvres et esprit
                nom_type_operateur_oeuvre_esprit = ag.get_type_operateurs_des_oeuvres_esprit()
            elif id_niveau_desagregation == "32":  # Type de groupe culturel
                nom_type_de_groupe_culturel = ag.get_type_de_groupes_culturels()
            elif id_niveau_desagregation == "33":  # Type de manifestation culturelle
                nom_type_de_manifestation_culturelle = ag.get_type_de_manifestations_culturelles()
            elif id_niveau_desagregation == "34":  # Trimestre
                nom_trimestre = ag.get_trimestre()
            elif id_niveau_desagregation == "35":  # Etat des oeuvres
                nom_etat_des_oeuvres = ag.get_etat_des_ouvrages()
            elif id_niveau_desagregation == "36":  # Type d'abonnements
                nom_type_abonnement = ag.get_type_abonnement()
            elif id_niveau_desagregation == "37":  # Type de suivi
                nom_type_de_suivi = ag.get_type_suivi()
            elif id_niveau_desagregation == "38":  # Type de vulnérabilités
                nom_type_de_vulnerabilite = ag.get_type_de_vulnerabilite()
            elif id_niveau_desagregation == "39":  # Type de prise en charge
                nom_type_de_prise_charge = ag.get_type_suivi()
            elif id_niveau_desagregation == "40":  # Niveau
                nom_niveau = ag.get_niveau()

            if indicator:
                mon_id_indicateur, nom_ind = indicator
            else:
                nom_ind = "Indicateur non trouvé"
            if entite_geog:
                id_entite, nom_entite = entite_geog

    return render_template('index.html',
                nom_ind=nom_ind,
                id_entite=id_entite,
                nom_entite=nom_entite,
                id_code_entite=id_code_entite,
                id_indicateur=id_indicateur,
                nom_groupe_age=nom_groupe_age,
                nom_sexe=nom_sexe,
                nom_cycle=nom_cycle,
                nom_prescolaire=nom_prescolaire,
                nom_primaire=nom_primaire,
                nom_secondaire_1er=nom_secondaire_1er,
                nom_secondaire_2nd=nom_secondaire_2nd,
                nom_technique=nom_technique,
                nom_superieur=nom_superieur,
                nom_professionnel=nom_professionnel,
                nom_type_examen_scolaire=nom_type_examen_scolaire,
                nom_infrastructure_sanitaire=nom_infrastructure_sanitaire,
                nom_lieu_accouchement=nom_lieu_accouchement,
                nom_etat_vaccinal=nom_etat_vaccinal,
                nom_type_vaccination=nom_type_vaccination,
                nom_pathologie=nom_pathologie,
                nom_tranche_age=nom_tranche_age,
                nom_maladie_pev=nom_maladie_pev,
                nom_maladie_infectieuse=nom_maladie_infectieuse,
                nom_infection_respiratoire=nom_infection_respiratoire,
                nom_maladies_ist=nom_maladies_ist,
                nom_type_maladies=nom_type_maladies,
                nom_activites_iec=nom_activites_iec,
                nom_services_medicaux=nom_services_medicaux,
                nom_infrastructure_organisation=nom_infrastructure_organisation,
                nom_discipline_sportive=nom_discipline_sportive,
                nom_type_infrastructure_culturel=nom_type_infrastructure_culturel,
                nom_type_patrimoine_culturel=nom_type_patrimoine_culturel,
                nom_type_actions_culturelles=nom_type_actions_culturelles,
                nom_type_operateur_oeuvre_esprit=nom_type_operateur_oeuvre_esprit,
                nom_type_de_groupe_culturel=nom_type_de_groupe_culturel,
                nom_type_de_manifestation_culturelle=nom_type_de_manifestation_culturelle,
                nom_trimestre=nom_trimestre,
                nom_etat_des_oeuvres=nom_etat_des_oeuvres,
                nom_type_abonnement=nom_type_abonnement,
                nom_type_de_suivi=nom_type_de_suivi,
                nom_type_de_vulnerabilite=nom_type_de_vulnerabilite,
                nom_type_de_prise_charge=nom_type_de_prise_charge,
                nom_niveau=nom_niveau)



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
    # Liste des préfixes que vous pourriez rencontrer
    prefixes = [
        'idprimaire_',
        'id_',
        'sexe_',
        'idcycle_',
        'idprescolaire_',
        'idsecondaire1_',
        'idsecondaire2_',
        'idtechnique_',
        'idsuperieur_',
        'idprofessionnel_',
        'idtypeexamenscolaire_',
        'idinfrastructure_',
        'idlieuaccouchement_',
        'idetatvaccinal_',
        'idtypevaccination_',
        'idpathologie_',
        'idtrancheage_',
        'idmaladiepev_',
        'idmaladieinfectieuse_',
        'idinfectionrespiratoire_',
        'idmaladiesist_',
        'idtypemaladies_',
        'idactivitesiec_',
        'idservicesmedicaux_',
        'idinfrastructureorganisation_',
        'iddisciplinesportive_',
        'idtypeinfrastructureculturel_',
        'idtypepatrimoineculturel_',
        'idtypeactionsculturelles_',
        'idtypeoperateuroeuvreesprit_',
        'idtypedegroupeculturel_',
        'idtypedemanifestationculturelle_',
        'idtrimestre_',
        'idetatdesoeuvres_',
        'idtypeabonnement_',
        'idtypedesuivi_',
        'idtypedevulnerabilite_',
        'idtypedeprisecharge_',
        'idniveau_'
    ]

    for key, value in data.items():
        # Initialiser toutes les variables à None
        primaire = None
        id_grpe_age = None
        sexe = None
        cycle = None
        prescolaire = None
        secondaire_1er = None
        secondaire_2nd = None
        technique = None
        superieur = None
        professionnel = None
        type_examen_scolaire = None
        infrastructure_sanitaire = None
        lieu_accouchement = None
        etat_vaccinal = None
        type_vaccination = None
        pathologie = None
        tranche_age = None
        maladie_pev = None
        maladie_infectieuse = None
        infection_respiratoire = None
        maladies_ist = None
        type_maladies = None
        activites_iec = None
        services_medicaux = None
        infrastructure_organisation = None
        discipline_sportive = None
        type_infrastructure_culturel = None
        type_patrimoine_culturel = None
        type_actions_culturelles = None
        type_operateur_oeuvre_esprit = None
        type_de_groupe_culturel = None
        type_de_manifestation_culturelle = None
        trimestre = None
        etat_des_oeuvres = None
        type_abonnement = None
        type_de_suivi = None
        type_de_vulnerabilite = None
        type_de_prise_charge = None
        niveau = None

        # Parcourir les préfixes
        for prefix in prefixes:
            if key.startswith(prefix):
                if prefix == 'idprimaire_':
                    primaire = key.split('_')[1]
                elif prefix == 'id_':
                    id_grpe_age = key.split('_')[1]
                elif prefix == 'sexe_':
                    sexe = key.split('_')[1]
                elif prefix == 'idcycle_':
                    cycle = key.split('_')[1]
                elif prefix == 'idprescolaire_':
                    prescolaire = key.split('_')[1]
                elif prefix == 'idsecondaire1_':
                    secondaire_1er = key.split('_')[1]
                elif prefix == 'idsecondaire2_':
                    secondaire_2nd = key.split('_')[1]
                elif prefix == 'idtechnique_':
                    technique = key.split('_')[1]
                elif prefix == 'idsuperieur_':
                    superieur = key.split('_')[1]
                elif prefix == 'idprofessionnel_':
                    professionnel = key.split('_')[1]
                elif prefix == 'idtypeexamenscolaire_':
                    type_examen_scolaire = key.split('_')[1]
                elif prefix == 'idinfrastructure_':
                    infrastructure_sanitaire = key.split('_')[1]
                elif prefix == 'idlieuaccouchement_':
                    lieu_accouchement = key.split('_')[1]
                elif prefix == 'idetatvaccinal_':
                    etat_vaccinal = key.split('_')[1]
                elif prefix == 'idtypevaccination_':
                    type_vaccination = key.split('_')[1]
                elif prefix == 'idpathologie_':
                    pathologie = key.split('_')[1]
                elif prefix == 'idtrancheage_':
                    tranche_age = key.split('_')[1]
                elif prefix == 'idmaladiepev_':
                    maladie_pev = key.split('_')[1]
                elif prefix == 'idmaladieinfectieuse_':
                    maladie_infectieuse = key.split('_')[1]
                elif prefix == 'idinfectionrespiratoire_':
                    infection_respiratoire = key.split('_')[1]
                elif prefix == 'idmaladiesist_':
                    maladies_ist = key.split('_')[1]
                elif prefix == 'idtypemaladies_':
                    type_maladies = key.split('_')[1]
                elif prefix == 'idactivitesiec_':
                    activites_iec = key.split('_')[1]
                elif prefix == 'idservicesmedicaux_':
                    services_medicaux = key.split('_')[1]
                elif prefix == 'idinfrastructureorganisation_':
                    infrastructure_organisation = key.split('_')[1]
                elif prefix == 'iddisciplinesportive_':
                    discipline_sportive = key.split('_')[1]
                elif prefix == 'idtypeinfrastructureculturel_':
                    type_infrastructure_culturel = key.split('_')[1]
                elif prefix == 'idtypepatrimoineculturel_':
                    type_patrimoine_culturel = key.split('_')[1]
                elif prefix == 'idtypeactionsculturelles_':
                    type_actions_culturelles = key.split('_')[1]
                elif prefix == 'idtypeoperateuroeuvreesprit_':
                    type_operateur_oeuvre_esprit = key.split('_')[1]
                elif prefix == 'idtypedegroupeculturel_':
                    type_de_groupe_culturel = key.split('_')[1]
                elif prefix == 'idtypedemanifestationculturelle_':
                    type_de_manifestation_culturelle = key.split('_')[1]
                elif prefix == 'idtrimestre_':
                    trimestre = key.split('_')[1]
                elif prefix == 'idetatdesoeuvres_':
                    etat_des_oeuvres = key.split('_')[1]
                elif prefix == 'idtypeabonnement_':
                    type_abonnement = key.split('_')[1]
                elif prefix == 'idtypedesuivi_':
                    type_de_suivi = key.split('_')[1]
                elif prefix == 'idtypedevulnerabilite_':
                    type_de_vulnerabilite = key.split('_')[1]
                elif prefix == 'idtypedeprisecharge_':
                    type_de_prise_charge = key.split('_')[1]
                elif prefix == 'idniveau_':
                    niveau = key.split('_')[1]
                break  # Sortir de la boucle des préfixes une fois trouvé

        # Insertion dans la base de données
        cf.insertion_value(
            valeur=value,
            groupe_age_id=id_grpe_age,
            indicator_id=mon_id_indicateur,
            sous_prefecture_id=sous_prefecture_id,
            region_id=region_id,
            department_id=department_id,
            annee=annee,
            niveau_primaire_id=primaire,
            sexe_id=sexe,
            cycle_id=cycle,
            niveau_prescolaire_id=prescolaire,
            niveau_secondaire_1er_cycle_id=secondaire_1er,
            niveau_secondaire_2nd_cycle_id=secondaire_2nd,
            niveau_technique_id=technique,
            niveau_superieur_id=superieur,
            niveau_professionnel_id=professionnel,
            type_examen_id=type_examen_scolaire,
            infrastructures_sanitaires_id=infrastructure_sanitaire,
            lieu_accouchement_id=lieu_accouchement,
            etat_vaccinal_id=etat_vaccinal,
            types_de_vaccination_id=type_vaccination,
            pathologie_id=pathologie,
            tranche_age_id=tranche_age,
            maladies_du_pev_id=maladie_pev,
            maladies_infectieuses_id=maladie_infectieuse,
            infection_respiratoire=infection_respiratoire,
            maladies_ist_id=maladies_ist,
            type_de_maladie_id=type_maladies,
            activites_iec_id=activites_iec,
            service_medicaux_id=services_medicaux,
            type_infrastructures_ou_organisations_sportives_id=infrastructure_organisation,
            disciplines_sportives_id=discipline_sportive,
            type_infrastructures_culturelles_id=type_infrastructure_culturel,
            f_type_de_patrimoines_culturels_immat_id=type_patrimoine_culturel,
            type_actions_culturelles_et_artistiques_id=type_actions_culturelles,
            type_operateurs_des_oeuvres_esprit_id=type_operateur_oeuvre_esprit,
            type_de_groupes_culturels_id=type_de_groupe_culturel,
            type_de_manifestations_culturelles_id=type_de_manifestation_culturelle,
            trimestre_id=trimestre,
            etat_des_ouvrages_id=etat_des_oeuvres,
            type_abonnement_id=type_abonnement,
            type_suivi_id=type_de_suivi,
            type_de_vulnerabilite_id=type_de_vulnerabilite,
            type_de_prise_charge_id=type_de_prise_charge,
            niveau_id=niveau
        )

    # Ajout d'un message flash pour informer l'utilisateur
    flash("Données envoyées avec succès!")

    # Redirection vers la route d'affichage du formulaire
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)