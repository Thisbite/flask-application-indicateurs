from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import logging
import config as cf
import db_queries as ag

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_login import UserMixin
import pandas as pd
app = Flask(__name__)
# Configuration du logging
logging.basicConfig(level=logging.DEBUG)

# Configuration de la clé secrète pour les sessions Flask
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', '774d8fe18f818cdb0f03a7d2471d55797c709a6aede6289dcc24481a7a92f40a')

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user_login'





""" 
+++++++++++++++++++++++Section de Connexion 
"""





# Fonction pour charger l'utilisateur selon l'ID
@login_manager.user_loader
def load_user(user_id):
    # Charger l'utilisateur en fonction de l'ID dans les trois tables
    return (Agent.query.get(int(user_id)) or 
            Superviseur.query.get(int(user_id)) or 
            Administrateur.query.get(int(user_id)))

# Modèles SQLAlchemy
class Superviseur(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_direction_statistique = db.Column(db.Integer, db.ForeignKey('direction_statistique.id'))
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), default='superviseur')

class Agent(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_sup = db.Column(db.Integer, db.ForeignKey('superviseur.id'))  # Corrigé pour correspondre à la clé étrangère
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), default='agent')

class Administrateur(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), default='administrateur')

# Route pour la page d'accueil
@app.route('/')
def home():
    return render_template('login.html')

# Route de connexion
@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Rechercher l'utilisateur parmi les trois tables
        user = (Agent.query.filter_by(email=email).first() or
                Superviseur.query.filter_by(email=email).first() or
                Administrateur.query.filter_by(email=email).first())

        if user:
            # Comparer directement le mot de passe sans hachage
            if user.password == password:
                login_user(user)
                # Redirection selon le rôle de l'utilisateur
                if isinstance(user, Agent):
                    return redirect(url_for('agents'))
                elif isinstance(user, Superviseur):
                    return redirect(url_for('superviseurs'))
                elif isinstance(user, Administrateur):
                    return redirect(url_for('administrateurs'))
            else:
                flash('Mot de passe incorrect.', 'danger')
        else:
            flash('Email non reconnu.', 'danger')
        return redirect(url_for('home'))
    
    return render_template('login.html')

#Deconnexion 
@app.route('/logout')
@login_required
def logout():
    logout_user()  # Déconnecte l'utilisateur actuel
    flash('Vous avez été déconnecté avec succès.', 'success')
    return redirect(url_for('home'))



@app.route('/agents')
def agents():
    if not isinstance(current_user, Agent):
        flash("Accès refusé : Vous devez être connecté en tant qu'agent pour accéder à cette page.", "danger")
        return redirect(url_for('home'))
    return render_template('agents.html')

@app.route('/superviseurs')
def superviseurs():
    if not isinstance(current_user, Superviseur):
        flash("Accès refusé : Vous devez être connecté en tant que superviseur pour accéder à cette page.", "danger")
        return redirect(url_for('home'))
    return render_template('superviseurs.html')

@app.route('/administrateurs')
def administrateurs():
    if not isinstance(current_user,Administrateur):
        flash("Accès refusé : Vous devez être connecté en tant qu'administrateur pour accéder à cette page.", "danger")
        return redirect(url_for('home'))
    return render_template('administrateurs.html')



import forms as fm
# Questionnaire de saisie de données

@app.route('/questionnaire', methods=['GET', 'POST'])
@login_required
def questionnaire():
    if not isinstance(current_user, Agent):
        flash("Accès refusé : Vous devez être connecté en tant qu'agent pour accéder à cette page.", "danger")
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
    nom_age=[]


# Cette partie est pour les indicateurs à plusieurs niveaux 
# Cette partie est pour les indicateurs à plusieurs niveaux 
    nom_groupe_age_A = fm.desagregation_map["1"]()
    nom_sexe_A = fm.desagregation_map["2"]()
    nom_age_A=fm.desagregation_map["3"]()
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
    import parametre as pa
# Fin bloc 
    indicator=None
    id_indicateurT=None
    niveau_choix=None
    cod_indicateur_comparaison=None
    all_lists=[]
    lists=pa.lists #Menu deroulant
    all_lists=pa.lists_all #Affichage dans java

    if request.method == 'POST':
        id_indicateur = request.form.get('id_indicateur')
        id_code_entite = request.form.get('id_code_entite')
        
        # Récupération des paramètres pour l'id_indicateur donné
        config = pa.indicateur_config.get(id_indicateur, {})

        # Extraction des valeurs communes
        if config.get('fetch_indicateur'):
            _, nom_ind = ag.get_indicators(id_indicateur)
        if config.get('fetch_sexe'):
            nom_sexe = ag.get_sexes()
        if config.get('fetch_groupe_age'):
            nom_groupe_age = ag.get_groupe_age()
        if config.get('fetch_cycle_scolaire'):
            nom_cycle = ag.get_cycle()
        if config.get('fetch_age'):
            nom_age=ag.get_age()

        # Extraction des valeurs spécifiques
        entite_geog = ag.get_geographical_entity_name(id_code_entite)
        cod_indicateur_comparaison = id_indicateur
        id_entite, nom_entite = entite_geog
        niveau_choix = config.get('niveau_choix', {})

        
       

    return render_template('questionnaire.html',
                all_lists=all_lists,
                lists =lists ,
                cod_indicateur_comparaison=cod_indicateur_comparaison,#Il sert à comparer
                niveau_choix=niveau_choix,# Niveau desagregation  
                nom_ind=nom_ind,#Nom de l'indicateur
                id_entite=id_entite, #Type entité géographie
                nom_entite=nom_entite, #Nom de l'entité geographie
                id_code_entite=id_code_entite, #Code Identifiant géographique 
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
                nom_niveau_A = nom_niveau_A,
                nom_age=nom_age,
                nom_age_A=nom_age_A
            )
    
# Importation
@app.route('/upload_questionnaire', methods=['GET'])
@login_required
def upload_questionnaire():
    return render_template('questionnaire_importer.html')

# Route pour gérer l'importation et l'insertion dans la base de données
@app.route('/handle_upload_questionnaire', methods=['POST'])
@login_required
def handle_upload_questionnaire():
    conn = None
    try:
        # Vérification de la présence du fichier
        if 'file' not in request.files:
            flash('Aucun fichier sélectionné.', 'danger')
            return redirect(url_for('upload_questionnaire'))
        file = request.files['file']  
        # Vérification du nom du fichier
        if file.filename == '':
            flash('Aucun fichier sélectionné.', 'danger')
            return redirect(url_for('upload_questionnaire'))        
        # Vérification de l'extension du fichier
        if file and file.filename.endswith('.xlsx'):
            try:
                df = pd.read_excel(file)
            except Exception as e:
                flash(f"Erreur lors de la lecture du fichier Excel : {str(e)}", 'danger')

                return redirect(url_for('upload_questionnaire'))    
        else:
            flash('Format de fichier non valide. Veuillez télécharger un fichier .xlsx.', 'danger')

    except Exception as e:
        flash(f"Erreur générale lors de l\'importation du fichier : {str(e)}", 'danger')
    return redirect(url_for('upload_questionnaire'))


#Importation des données par excel
import pandas as pd
from flask import request, jsonify

#Obtenir la list des feuilles excel
@app.route('/get_sheets', methods=['POST'])
@login_required
def get_sheets():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Aucun fichier sélectionné.'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'Aucun fichier sélectionné.'}), 400

        # Charger les feuilles de l'Excel
        excel_file = pd.ExcelFile(file)
        sheets = excel_file.sheet_names

        return jsonify({'sheets': sheets}), 200

    except Exception as e:
        return jsonify({'error': f"Erreur lors de la récupération des feuilles : {str(e)}"}), 500
    
    
# view des données importer
@app.route('/preview_data', methods=['POST'])
@login_required
def preview_data():
    try:
        if 'file' not in request.files or 'sheets' not in request.form:
            return jsonify({'error': 'Fichier ou feuilles manquants.'}), 400

        file = request.files['file']
        sheet_names = request.form.getlist('sheets')  # Récupérer la liste des feuilles sélectionnées

        if file.filename == '':
            return jsonify({'error': 'Aucun fichier sélectionné.'}), 400

        # Créer une chaîne HTML pour afficher les tableaux de toutes les feuilles sélectionnées
        all_tables_html = ""

        for sheet_name in sheet_names:
            # Lire les données de la feuille sélectionnée
            df = pd.read_excel(file, sheet_name=sheet_name)
            table_html = df.to_html(classes='table table-striped', index=False)

            # Ajouter un titre pour chaque feuille et son tableau correspondant
            all_tables_html += f"<h3>Feuille : {sheet_name}</h3>{table_html}<hr>"

        return jsonify({'table_html': all_tables_html}), 200

    except Exception as e:
        return jsonify({'error': f"Erreur lors de la lecture des données : {str(e)}"}), 500




#Confirmer avant validation et c'est la section d'insertion de données dans la base
@app.route('/confirm_insert_questionnaire', methods=['POST'])
@login_required
def confirm_insert_questionnaire():
    try:
        if 'file' not in request.files or 'sheets' not in request.form:
            return jsonify({'error': 'Fichier ou feuilles manquants.'}), 400

        file = request.files['file']
        sheet_names = request.form.getlist('sheets')  # Liste des feuilles sélectionnées
        processed_sheets = []  # Liste pour suivre les feuilles traitées

        # Charger le fichier Excel une fois
        excel_file = pd.ExcelFile(file)

        conn = cf.create_connection()
        cursor = conn.cursor()

        for sheet_name in sheet_names:
            # Vérifier que la feuille existe
            if sheet_name in excel_file.sheet_names:
                # Lire la feuille spécifique
                df = pd.read_excel(excel_file, sheet_name=sheet_name)

                # Vérifier que le nom de la feuille contient bien un tiret ('-')
                if '-' in sheet_name:
                    parts = sheet_name.split('-')
                    # Vérifier que la partie après le tiret existe bien et correspond à '1001'
                    if len(parts) > 1 and parts[1] == '1001':
                        # Insérer les données dans la base pour chaque feuille sélectionnée
                        for _, row in df.iterrows():
                            id = cf.generate_unique_key()
                            region = row['Région']
                            departement = row['Département']
                            sous_prefecture = row['Sous-prefecture']
                            sexe = row['Sexe']
                            groupe_age = row['Groupe d\'age']
                            age = row['Age']
                            valeur = row['Valeur']
                            annee = row['Annee']

                            sql = """
                                INSERT INTO valeur_indicateur_libelle (
                                    id, nom_region, nom_departement, nom_sousprefecture, sexe, groupe_age, age, Valeur, Annee
                                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """
                            cursor.execute(sql, (id, region, departement, sous_prefecture, sexe, groupe_age, age, valeur, annee))
                        
                        # Ajouter le nom de la feuille à la liste des feuilles traitées
                        processed_sheets.append(sheet_name)

        # Commit des données dans la base
        conn.commit()

        # Retourner un message avec les feuilles traitées
        if processed_sheets:
            message = f"Données insérées avec succès pour les feuilles : {', '.join(processed_sheets)}"
        else:
            message = "Aucune donnée n'a été insérée car aucune feuille ne correspondait à l'indicateur '1001'."
        
        return jsonify({'message': message}), 200

    except Exception as e:
        return jsonify({'error': f"Erreur lors de l'insertion des données : {str(e)}"}), 500

    finally:
        if conn:
            conn.close()

























































































#Approbation
@app.route('/approbation', methods=['GET'])
@login_required
def approbation():
    conn = cf.create_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Récupérer les données de la table 'valeur_indicateur_libelle' où le statut est 'Non approuvé'
        cursor.execute("SELECT * FROM valeur_indicateur_libelle WHERE statut = 'Non approuvé'")
        rows = cursor.fetchall()
    except Exception as e:
        flash(f"Erreur lors de la récupération des données : {str(e)}", "danger")
        rows = []
    finally:
        cursor.close()
        conn.close()

    return render_template('approbation.html', rows=rows)

@app.route('/approve_or_reject', methods=['POST'])
def approve_or_reject():
    conn = cf.create_connection()
    cursor = conn.cursor()
    id_valeur = request.form.get('id')
    action = request.form.get('action')
    commentaires = request.form.get('commentaires', '')

    try:
        if action == 'Approuver':
            # Mise à jour du statut à 'Approuvé'
            cursor.execute("UPDATE valeur_indicateur_libelle SET statut = 'Approuvé' WHERE id = %s", (id_valeur,))
            flash(f"Valeur ID {id_valeur} approuvée avec succès", "success")
        elif action == 'Rejeter':
            # Mise à jour du statut à 'Rejeté' avec commentaires et date de rejet
            cursor.execute("""
                UPDATE valeur_indicateur_libelle 
                SET statut = 'Rejeté', commentaires = %s, date_rejet = NOW() 
                WHERE id = %s
            """, (commentaires, id_valeur))
            flash(f"Valeur ID {id_valeur} rejetée avec succès", "success")
        else:
            flash("Action non reconnue", "danger")

        conn.commit()
    except Exception as e:
        conn.rollback()
        flash(f"Erreur lors de la mise à jour : {str(e)}", "danger")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('approbation'))






@app.route('/upload', methods=['GET'])
@login_required
def upload_page():
    return render_template('upload.html')



@app.route('/upload_file', methods=['POST'])
@login_required
#Fonction de rejet
def upload_file():
    conn = cf.create_connection()
    cursor = conn.cursor()
    try:
        # Vérification de la présence du fichier
        if 'file' not in request.files:
            flash('Aucun fichier sélectionné.', 'danger')
            return redirect(url_for('upload_page'))

        file = request.files['file']
        
        # Vérification du nom du fichier
        if file.filename == '':
            flash('Aucun fichier sélectionné.', 'danger')
            return redirect(url_for('upload_page'))
        
        # Vérification de l'extension du fichier
        if file and file.filename.endswith('.xlsx'):
            try:
                df = pd.read_excel(file)
            except Exception as e:
                flash(f"Erreur lors de la lecture du fichier Excel : {str(e)}", 'danger')
                print(f"Erreur lors de la lecture du fichier : {str(e)}")  # Affiche l'erreur dans la console
                return redirect(url_for('upload_page'))
            
            try:
                # Connexion à la base de données
                conn = cf.create_connection()
                cursor = conn.cursor()

                # Parcours des lignes du fichier et mise à jour des données
                for index, row in df.iterrows():
                    id_valeur = row['ID']
                    commentaires = row['Commentaires']
                    
                    sql = """
                        UPDATE valeur_indicateur_libelle
                        SET statut = 'Rejeté', commentaires = %s, date_rejet = NOW()
                        WHERE id = %s
                    """
                    cursor.execute(sql, (commentaires, id_valeur))

                conn.commit()
                flash('Fichier importé et données mises à jour avec succès.', 'success')
                print('Insertion des importations de rejetées ok')
            except Exception as e:
                flash(f"Erreur lors de la mise à jour des données : {str(e)}", 'danger')
            finally:
                if conn:
                    conn.close()
        else:
            flash('Format de fichier non valide. Veuillez télécharger un fichier .xlsx.', 'danger')

    except Exception as e:
        flash(f"Erreur générale lors de l'importation du fichier : {str(e)}", 'danger')
        print(f"Erreur générale lors de l'importation : {str(e)}")  # Affiche l'erreur générale dans la console
    
    finally:
        pass
    

    
    return redirect(url_for('upload_page'))



@app.route('/correction', methods=['GET'])
@login_required
def correction():
    conn = cf.create_connection()
    cursor = conn.cursor(dictionary=True)
    
    if current_user.role != 'agent':
        flash('Vous n\'êtes pas autorisé à accéder à cette page.')
        return redirect(url_for('home'))
    
    email_agent = current_user.email

    try:
        # Récupérer les données avec statut 'Rejeté' pour cet agent
        cursor.execute("""
            SELECT * FROM valeur_indicateur_libelle 
            WHERE statut = 'Rejeté' 
          """)
        
        rows = cursor.fetchall()
    except Exception as e:
        flash(f"Erreur lors de la récupération des données : {str(e)}", "danger")
        rows = []
    finally:
        cursor.close()
        conn.close()

    return render_template('correction.html', rows=rows)


@app.route('/submit_correction', methods=['POST'])
@login_required
def submit_correction():
    conn = cf.create_connection()
    cursor = conn.cursor()
    id_valeur = request.form.get('id')
    nom_region = request.form.get('nom_region')
    nom_departement = request.form.get('nom_departement')
    nom_sousprefecture = request.form.get('nom_sousprefecture')
    nom_indicateur = request.form.get('nom_indicateur')
    valeur_indicateur = request.form.get('valeur_indicateur')
    commentaires = request.form.get('commentaires')

    try:
        # Mise à jour des champs modifiés par l'agent
        cursor.execute("""
            UPDATE valeur_indicateur_libelle 
            SET nom_region = %s, nom_departement = %s, nom_sousprefecture = %s, 
                nom_indicateur = %s, Valeur = %s, commentaires = %s, statut = 'Corrigé'
            WHERE id = %s
        """, (nom_region, nom_departement, nom_sousprefecture, nom_indicateur, valeur_indicateur, commentaires, id_valeur))

        conn.commit()
        flash(f"Correction soumise avec succès pour l'ID {id_valeur}. Elle est en attente d'approbation.", "success")
    except Exception as e:
        conn.rollback()
        flash(f"Erreur lors de la soumission de la correction : {str(e)}", "danger")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('correction'))





unique_key=None
@app.route('/submit', methods=['POST'])
def submit():
    if current_user.role !='agent':
        flash('Vous n\'êtes pas autorisé à accéder à cette page.')
        return redirect(url_for('home')) 
    email_agent=current_user.email
    # Récupère les données passées à la route submit pour le deuxieme choix
    mon_id_indicateur = request.form.get('id_indicateur2')
    id_code_entite = request.form.get('id_code_entite2')
    
    idprimaire = request.form.get('nom_primaire')
    idsexe=request.form.get('nom_sexe')
    idgroupe_age = request.form.get('nom_groupe_age')
    idage=request.form.get('nom_age')
    idcycle = request.form.get('nom_cycle')
    idprescolaire = request.form.get('nom_prescolaire')
    idsecondaire_1er = request.form.get('nom_secondaire_1er')
    idsecondaire_2nd = request.form.get('nom_secondaire_2nd')
    idtechnique = request.form.get('nom_technique')
    idsuperieur = request.form.get('nom_superieur')
    idprofessionnel = request.form.get('nom_professionnel')
    idtype_examen_scolaire = request.form.get('nom_type_examen_scolaire')
    idinfrastructure_sanitaire = request.form.get('nom_infrastructure_sanitaire')
    idlieu_accouchement = request.form.get('nom_lieu_accouchement')
    idetat_vaccinal = request.form.get('nom_etat_vaccinal')
    idtype_vaccination = request.form.get('nom_type_vaccination')
    idpathologie = request.form.get('nom_pathologie')
    idtranche_age = request.form.get('nom_tranche_age')
    idmaladie_pev = request.form.get('nom_maladie_pev')
    idmaladie_infectieuse = request.form.get('nom_maladie_infectieuse')
    idinfection_respiratoire = request.form.get('nom_infection_respiratoire')
    idmaladies_ist = request.form.get('nom_maladies_ist')
    idtype_maladies = request.form.get('nom_type_maladies')
    idactivites_iec = request.form.get('nom_activites_iec')
    idservices_medicaux = request.form.get('nom_services_medicaux')
    idinfrastructure_organisation = request.form.get('nom_infrastructure_organisation')
    iddiscipline_sportive = request.form.get('nom_discipline_sportive')
    idtype_infrastructure_culturel = request.form.get('nom_type_infrastructure_culturel')
    idtype_patrimoine_culturel = request.form.get('nom_type_patrimoine_culturel')
    idtype_actions_culturelles = request.form.get('nom_type_actions_culturelles')
    idtype_operateur_oeuvre_esprit = request.form.get('nom_type_operateur_oeuvre_esprit')
    idtype_de_groupe_culturel = request.form.get('nom_type_de_groupe_culturel')
    idtype_de_manifestation_culturelle = request.form.get('nom_type_de_manifestation_culturelle')
    idtrimestre = request.form.get('nom_trimestre')
    idetat_des_oeuvres = request.form.get('nom_etat_des_oeuvres')
    idtype_abonnement = request.form.get('nom_type_abonnement')
    idsuivi = request.form.get('nom_type_de_suivi')
    idvulnerabilite = request.form.get('nom_type_de_vulnerabilite')
    idprise_charge = request.form.get('nom_type_de_prise_charge')
    idniveau = request.form.get('nom_niveau')


    

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
        'id_groupe_age_',
        'idages_',
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
        unique_key=cf.generate_unique_key()
        # Initialiser toutes les variables à None
        primaire = None
        id_grpe_age = None
        age=None
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
                elif prefix == 'id_groupe_age_':
                    id_grpe_age = key.split('_')[1]
                elif prefix == 'idages_':
                    age= key.split('_')[1]
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
            id=unique_key,valeur=value,
            indicator_id=mon_id_indicateur,
            sous_prefecture_id=sous_prefecture_id,
            region_id=region_id,
            department_id=department_id,
            annee=annee,
            groupe_age_id=idgroupe_age if idgroupe_age else id_grpe_age,
            niveau_primaire_id = idprimaire if idprimaire else primaire,
            age_id=idage if idage else age,
            sexe_id = idsexe if idsexe else sexe,
            cycle_id = idcycle if idcycle else cycle,
            niveau_prescolaire_id = idprescolaire if idprescolaire else prescolaire,
            niveau_secondaire_1er_cycle_id = idsecondaire_1er if idsecondaire_1er else secondaire_1er,
            niveau_secondaire_2nd_cycle_id = idsecondaire_2nd if idsecondaire_2nd else secondaire_2nd,
            niveau_technique_id = idtechnique if idtechnique else technique,
            niveau_superieur_id = idsuperieur if idsuperieur else superieur,
            niveau_professionnel_id = idprofessionnel if idprofessionnel else professionnel,
            type_examen_id = idtype_examen_scolaire if idtype_examen_scolaire else type_examen_scolaire,
            infrastructures_sanitaires_id = idinfrastructure_sanitaire if idinfrastructure_sanitaire else infrastructure_sanitaire,
            lieu_accouchement_id = idlieu_accouchement if idlieu_accouchement else lieu_accouchement,
            etat_vaccinal_id = idetat_vaccinal if idetat_vaccinal else etat_vaccinal,
            types_de_vaccination_id = idtype_vaccination if idtype_vaccination else type_vaccination,
            pathologie_id = idpathologie if idpathologie else pathologie,
            tranche_age_id = idtranche_age if idtranche_age else tranche_age,
            maladies_du_pev_id = idmaladie_pev if idmaladie_pev else maladie_pev,
            maladies_infectieuses_id = idmaladie_infectieuse if idmaladie_infectieuse else maladie_infectieuse,
            infection_respiratoire = idinfection_respiratoire if idinfection_respiratoire else infection_respiratoire,
            maladies_ist_id = idmaladies_ist if idmaladies_ist else maladies_ist,
            type_de_maladie_id = idtype_maladies if idtype_maladies else type_maladies,
            activites_iec_id = idactivites_iec if idactivites_iec else activites_iec,
            service_medicaux_id = idservices_medicaux if idservices_medicaux else services_medicaux,
            type_infrastructures_ou_organisations_sportives_id = idinfrastructure_organisation if idinfrastructure_organisation else infrastructure_organisation,
            disciplines_sportives_id = iddiscipline_sportive if iddiscipline_sportive else discipline_sportive,
            type_infrastructures_culturelles_id = idtype_infrastructure_culturel if idtype_infrastructure_culturel else type_infrastructure_culturel,
            f_type_de_patrimoines_culturels_immat_id= idtype_patrimoine_culturel if idtype_patrimoine_culturel else type_patrimoine_culturel,
            type_actions_culturelles_et_artistiques_id = idtype_actions_culturelles if idtype_actions_culturelles else type_actions_culturelles,
            type_operateurs_des_oeuvres_esprit_id = idtype_operateur_oeuvre_esprit if idtype_operateur_oeuvre_esprit else type_operateur_oeuvre_esprit,
            type_de_groupes_culturels_id = idtype_de_groupe_culturel if idtype_de_groupe_culturel else type_de_groupe_culturel,
            type_de_manifestations_culturelles_id = idtype_de_manifestation_culturelle if idtype_de_manifestation_culturelle else type_de_manifestation_culturelle,
            trimestre_id = idtrimestre if idtrimestre else trimestre,
            etat_des_ouvrages_id = idetat_des_oeuvres if idetat_des_oeuvres else etat_des_oeuvres,
            type_abonnement_id= idtype_abonnement if idtype_abonnement else type_abonnement,
            type_suivi_id = idsuivi if idsuivi else type_de_suivi,
            type_de_vulnerabilite_id =  idvulnerabilite if  idvulnerabilite else type_de_vulnerabilite,
            type_de_prise_charge_id = idprise_charge if idprise_charge else type_de_prise_charge,
            niveau_id = idniveau if idniveau else niveau

        )

    # Ajout d'un message flash pour informer l'utilisateur
    flash(f"Données envoyées avec succès!")

    # Redirection vers la route d'affichage du formulaire
    return redirect(url_for('questionnaire'))









































if __name__ == '__main__':
    app.run(debug=True)