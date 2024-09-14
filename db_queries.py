
import pandas as pd
import config as cf
from mysql.connector import Error
import mysql.connector
import bcrypt  # Utiliser bcrypt pour le hachage des mots de passe (ou une autre librairie sécurisée)

def get_indicators(id_indicateur):
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT indicateur_id, nom_indicateur FROM Indicateur WHERE indicateur_id = %s"
            cursor.execute(query, (id_indicateur,))
            indicators = cursor.fetchone()
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Exception in get_indicators: {e}")
        return None
    return indicators


def get_niveau_desagregation(code):
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT id, nom_niveau_desagregation FROM niveau_desagregation WHERE id = %s"
            cursor.execute(query, (code,))
            result = cursor.fetchone()

            if result:
                id, nom_niveau = result
                return id, nom_niveau
            else:
                return None, "Niveau de désagrégation non trouvé"

    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return None, f"Erreur de la base de données : {e}"
    except Exception as e:
        print(f"Exception in get_niveau_desagregation: {e}")
        return None, f"Exception: {e}"


def get_sexes():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT sexe_id, sexe FROM Sexe ")
            sexes = cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_sexes: {e}")
        return []
    return sexes

def get_groupe_age():
    try:
        with cf.create_connection()as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT grp_age_id, groupe_age FROM GroupeAge")
            groupe_age = cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_groue_age: {e}")
        return []
    return groupe_age

def get_regions():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT region_id, nom_region FROM Region")
            regions = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_regions: {e}")
        return []
    return regions

def get_departments(selected_region):
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT departement_id, nom_departement FROM Departement WHERE f_region_id = %s"
            cursor.execute(query, (selected_region,))
            departments = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_departments: {e}")
        return []
    return departments

def get_sous_prefectures(selected_department):
    try:
        with  cf.create_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT sousprefect_id, nom_sousprefecture FROM SousPrefectures WHERE f_departement_id = %s"
            cursor.execute(query, (selected_department,))
            sousprefectures = cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_sous_prefectures: {e}")
        return []
    return sousprefectures


def get_region_name(region_code):
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT nom_region FROM Region WHERE region_id = %s"
            cursor.execute(query, (region_code,))
            region_name = cursor.fetchone()
            if region_name:
                return region_name[0]
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Exception in get_region_name: {e}")
        return None

def get_department_name(department_code):
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT nom_departement FROM Departement WHERE departement_id = %s"
            cursor.execute(query, (department_code,))
            department_name = cursor.fetchone()
            if department_name:
                return department_name[0]
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Exception in get_department_name: {e}")
        return None

def get_sous_prefecture_name(sous_prefecture_code):
    try:
        with  cf.create_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT nom_sousprefecture FROM SousPrefectures WHERE sousprefect_id = %s"
            cursor.execute(query, (sous_prefecture_code,))
            sous_prefecture_name = cursor.fetchone()
            if sous_prefecture_name:
                return sous_prefecture_name[0]
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Exception in get_sous_prefecture_name: {e}")
        return None

def get_geographical_entity_name(code_entite):
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()

            # Recherche dans la table Region
            cursor.execute("SELECT nom_region FROM Region WHERE region_id = %s", (code_entite,))
            result = cursor.fetchone()
            if result:
                return "Region", result[0]

            # Recherche dans la table Departement
            cursor.execute("SELECT nom_departement FROM Departement WHERE departement_id = %s", (code_entite,))
            result = cursor.fetchone()
            if result:
                return "Departement", result[0]

            # Recherche dans la table SousPrefectures
            cursor.execute("SELECT nom_sousprefecture FROM SousPrefectures WHERE sousprefect_id = %s", (code_entite,))
            result = cursor.fetchone()
            if result:
                return "SousPrefecture", result[0]

            return None, None
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return None, None
    except Exception as e:
        print(f"Exception in get_geographical_entity_name: {e}")
        return None, None


def get_user_role_email(user_email, user_password):
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()

            # Recherche dans la table Agent
            cursor.execute("SELECT nom, password FROM Agent WHERE email = %s", (user_email,))
            result = cursor.fetchone()
            if result:
                
                if bcrypt.checkpw(user_password.encode('utf-8'), result[1].encode('utf-8')):  # Vérification du mot de passe
                    return "Agent", result[0]  # Retourne le rôle et le nom

            # Recherche dans la table Superviseur
            cursor.execute("SELECT nom, password FROM Superviseur WHERE email = %s", (user_email,))
            result = cursor.fetchone()
            if result:
                if bcrypt.checkpw(user_password.encode('utf-8'), result[1].encode('utf-8')):
                    return "Superviseur", result[0]

            # Recherche dans la table Administrateur
            cursor.execute("SELECT nom, password FROM Administrateur WHERE email = %s", (user_email,))
            result = cursor.fetchone()
            if result:
                if bcrypt.checkpw(user_password.encode('utf-8'), result[1].encode('utf-8')):
                    return "Administrateur", result[0]

            return None, None  # Si l'email et le mot de passe ne correspondent pas
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return None, None
    except Exception as e:
        print(f"Exception in get_user_role_email: {e}")
        return None, None

def get_cycle():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_cycle, nom_cycle FROM Cycle")
            cycles = cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_cycle: {e}")
        return []
    return cycles


def get_niveau_prescolaire():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT niv_prescolaire_id, nom_prescolaire FROM Niveau_Prescolaire")
            niveaux_prescolaires = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_prescolaire: {e}")
        return []
    return niveaux_prescolaires


def get_niveau_primaire():
    try:
        with cf.create_connection()as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT niv_primaire_id , nom_primaire FROM Niveau_Primaire")
            niveaux_primaires = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_primaire: {e}")
        return []
    return niveaux_primaires


def get_niveau_secondaire_1er_cycle():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT niv_secondaire_1er_cycle_id,nom_secondaire_1er_cycle FROM Niveau_Secondaire_1er_cycle")
            niveaux_secondaires_1er_cycle = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_secondaire_1er_cycle: {e}")
        return []
    return niveaux_secondaires_1er_cycle


def get_niveau_secondaire_2nd_cycle():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT niv_secondaire_2nd_cycle_id, nom_secondaire_2nd_cycle FROM Niveau_Secondaire_2nd_cycle")
            niveaux_secondaires_2nd_cycle = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_secondaire_2nd_cycle: {e}")
        return []
    return niveaux_secondaires_2nd_cycle


def get_niveau_technique():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT niv_technique_id,nom_technique FROM Niveau_Technique")
            niveaux_techniques = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_technique: {e}")
        return []
    return niveaux_techniques


def get_niveau_superieur():
    try:
        with cf.create_connection()as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT  niv_superieur_id, nom_superieur FROM Niveau_Superieur")
            niveaux_superieurs = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_superieur: {e}")
        return []
    return niveaux_superieurs


def get_niveau_professionnel():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT niv_professionnel_id, nom_professionnel FROM Niveau_Professionnel")
            niveaux_professionnels = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_professionnel: {e}")
        return []
    return niveaux_professionnels


def get_type_examen():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_type_examen, nom_type_examen FROM Type_examen")
            types_examens = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_examen: {e}")
        return []
    return types_examens


def get_infrastructures_sanitaires():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_infrastructures_sanitaires, nom_infrastructures_sanitaires FROM Infrastructures_sanitaires")
            infrastructures_sanitaires = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_infrastructures_sanitaires: {e}")
        return []
    return infrastructures_sanitaires


def get_lieu_accouchement():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_lieu_accouchement, nom_lieu_accouchement FROM Lieu_accouchement")
            lieux_accouchement = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_lieu_accouchement: {e}")
        return []
    return lieux_accouchement


def get_etat_vaccinal():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_etat_vaccinal, nom_etat_vaccinal FROM Etat_vaccinal")
            etats_vaccinaux = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_etat_vaccinal: {e}")
        return []
    return etats_vaccinaux


def get_types_de_vaccination():
    try:
        with cf.create_connection()as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_types_de_vaccination, nom_types_de_vaccination FROM Types_de_vaccination")
            types_de_vaccination = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_types_de_vaccination: {e}")
        return []
    return types_de_vaccination


def get_pathologie():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_pathologie, nom_pathologie FROM Pathologie")
            pathologies = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_pathologie: {e}")
        return []
    return pathologies


def get_tranche_age():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_tranche_age, nom_tranche_age FROM Tranche_age")
            tranches_age = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_tranche_age: {e}")
        return []
    return tranches_age


def get_maladies_du_pev():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_maladies_du_pev, nom_maladies_du_pev FROM Maladies_du_pev")
            maladies_du_pev = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_maladies_du_pev: {e}")
        return []
    return maladies_du_pev


def get_maladies_infectieuses():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_maladies_infectieuses, nom_maladies_infectieuses FROM Maladies_infectieuses")
            maladies_infectieuses = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_maladies_infectieuses: {e}")
        return []
    return maladies_infectieuses


def get_infections_respiratoires():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_infectieuses_respiratoire, nom_infectieuses_respiratoire FROM Infection_respiratoire")
            infections_respiratoires = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_infections_respiratoires: {e}")
        return []
    return infections_respiratoires


def get_maladies_ist():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_maladies_ist, nom_maladies_ist FROM Maladies_ist")
            maladies_ist = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_maladies_ist: {e}")
        return []
    return maladies_ist


def get_type_de_maladie():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_type_de_maladie, nom_type_de_maladie FROM Type_de_Maladie")
            types_de_maladie = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_de_maladie: {e}")
        return []
    return types_de_maladie


def get_activites_iec():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_activites_iec, nom_activites_iec FROM Activites_IEC")
            activites_iec = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_activites_iec: {e}")
        return []
    return activites_iec


def get_service_medicaux():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_service_medicaux, nom_service_medicaux FROM Service_Medicaux")
            services_medicaux = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_service_medicaux: {e}")
        return []
    return services_medicaux


def get_type_infrastructures_ou_organisations_sportives():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_type_infrastructures_sportives, nom_type_infrastructures_sportives FROM Type_infrastructures_ou_organisations_sportives")
            types_infrastructures_ou_organisations_sportives = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_infrastructures_ou_organisations_sportives: {e}")
        return []
    return types_infrastructures_ou_organisations_sportives


def get_disciplines_sportives():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_disciplines_sportives, nom_disciplines_sportives FROM Disciplines_sportives")
            disciplines_sportives = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_disciplines_sportives: {e}")
        return []
    return disciplines_sportives


def get_type_infrastructures_culturelles():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_type_infrastructures_culturelles, nom_type_infrastructures_culturelles FROM Type_infrastructures_culturelles")
            types_infrastructures_culturelles = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_infrastructures_culturelles: {e}")
        return []
    return types_infrastructures_culturelles


def get_type_de_patrimoines_culturels_immateriels():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_type_patrimoines_culturels_immatériels, nom_type_patrimoines_culturels_immatériels FROM Type_de_Patrimoines_culturels_immatériels")
            types_patrimoines_culturels_immatériels = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_de_patrimoines_culturels_immatériels: {e}")
        return []
    return types_patrimoines_culturels_immatériels


def get_type_actions_culturelles_et_artistiques():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_type_actions_culturelles_artistiques, nom_type_actions_culturelles_artistiques FROM Type_actions_culturelles_et_artistiques")
            types_actions_culturelles_et_artistiques = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_actions_culturelles_et_artistiques: {e}")
        return []
    return types_actions_culturelles_et_artistiques


def get_type_operateurs_des_oeuvres_esprit():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_type_operateurs_oeuvres_esprit, nom_type_operateurs_oeuvres_esprit FROM Type_operateurs_des_oeuvres_esprit")
            types_operateurs_des_oeuvres_esprit = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_operateurs_des_oeuvres_esprit: {e}")
        return []
    return types_operateurs_des_oeuvres_esprit


def get_type_de_groupes_culturels():
    try:
        with  cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_type_groupes_culturels, nom_type_groupes_culturels FROM Type_de_groupes_culturels")
            types_groupes_culturels = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_de_groupes_culturels: {e}")
        return []
    return types_groupes_culturels


def get_type_de_manifestations_culturelles():
    try:
        with cf.create_connection()as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_type_manifestations_culturelles, nom_type_manifestations_culturelles FROM Type_de_manifestations_culturelles")
            types_manifestations_culturelles = cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_de_manifestations_culturelles: {e}")
        return []
    return types_manifestations_culturelles



def get_trimestre():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_trimestre, nom_trimestre FROM Trimestre")
            trimestres = cursor.fetchall()
    except Error as e:
        print(f"Erreur de table trimestre: {e}")
        return []
    except Exception as e:
        print(f"Erreur de fonction trimestre: {e}")
        return []
    return trimestres


def get_etat_des_ouvrages():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_etat_des_ouvrages, nom_etat_des_ouvrages FROM Etat_des_ouvrages")
            etat_des_ouvrages = cursor.fetchall()
    except Error as e:
        print(f"Erreur de table etat ouvrages: {e}")
        return []
    except Exception as e:
        print(f"Erreur de fonction etat ouvrages: {e}")
        return []
    return etat_des_ouvrages


def get_type_abonnement():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_type_abonnement, nom_type_abonnement FROM Type_abonnement")
            types_abonnement = cursor.fetchall()
    except Error as e:
        print(f"Erreur de table type abonnement: {e}")
        return []
    except Exception as e:
        print(f"Erreur de fonction type abonnement: {e}")
        return []
    return types_abonnement


def get_type_suivi():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_type_suivi, nom_type_suivi FROM Type_suivi")
            types_suivi = cursor.fetchall()
    except Error as e:
        print(f"Erreur de table type suivi: {e}")
        return []
    except Exception as e:
        print(f"Erreur de fonction type suivi: {e}")
        return []
    return types_suivi


def get_type_de_vulnerabilite():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_type_de_vulnerabilite, nom_type_de_vulnerabilite FROM Type_de_vulnerabilite")
            types_vulnerabilite = cursor.fetchall()
    except Error as e:
        print(f"Erreur de table type de vulnerabilite: {e}")
        return []
    except Exception as e:
        print(f"Erreur de fonction type de vulnerabilite: {e}")
        return []
    return types_vulnerabilite


def get_type_de_prise_charge():
    try:
        with  cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_type_de_prise_charge, nom_type_de_prise_charge FROM Type_de_prise_charge")
            types_prise_charge = cursor.fetchall()
    except Error as e:
        print(f"Erreur de table type de prise en charge: {e}")
        return []
    except Exception as e:
        print(f"Erreur de fonction type de prise en charge: {e}")
        return []
    return types_prise_charge


def get_niveau():
    try:
        with cf.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_niveau, nom_niveau FROM Niveau")
            niveaux = cursor.fetchall()
    except Error as e:
        print(f"Erreur de table niveau: {e}")
        return []
    except Exception as e:
        print(f"Erreur de fonction niveau: {e}")
        return []
    return niveaux




import mysql.connector


def afficher_valeurs_indicateurs():
    conn = cf.create_connection()
    cursor = conn.cursor()

    query = """
        SELECT 
            VI.id,
            COALESCE(r.nom_region, r2.nom_region, r3.nom_region) AS nom_region, 
            COALESCE(d.nom_departement, d2.nom_departement) AS nom_departement, 
            SP.nom_sousprefecture,
            I.nom_indicateur,
            VI.Valeur,
            VI.Annee,
            S.sexe,
            GA.groupe_age,
            A.age,
            C.nom_cycle,
            NP.nom_prescolaire,
            N1C.nom_primaire,
            NS1C.nom_secondaire_1er_cycle,
            NS2C.nom_secondaire_2nd_cycle,
            NT.nom_technique,
            NS.nom_superieur,
            NP2.nom_professionnel,  -- Changé 'NP' en 'NP2' pour Niveau_Professionnel
            TE.nom_type_examen,
            SIS.nom_infrastructures_sanitaires,
            LA.nom_lieu_accouchement,
            EV.nom_etat_vaccinal,
            TV.nom_types_de_vaccination,
            P.nom_pathologie,
            TA.nom_tranche_age,
            MP.nom_maladies_du_pev,
            MI.nom_maladies_infectieuses,
            IRES.nom_infectieuses_respiratoire,
            IST.nom_maladies_ist,
            TM.nom_type_de_maladie,
            AI.nom_activites_iec,
            SM.nom_service_medicaux,
            TIS.nom_type_infrastructures_sportives,
            DS.nom_disciplines_sportives,
            TIC.nom_type_infrastructures_culturelles,
            PCI.nom_type_patrimoines_culturels_immatériels,
            ACA.nom_type_actions_culturelles_artistiques,
            OE.nom_type_operateurs_oeuvres_esprit,
            GC.nom_type_groupes_culturels,
            MC.nom_type_manifestations_culturelles,

            TRIM.nom_trimestre,
            TDO.nom_etat_des_ouvrages,
            TABO.nom_type_abonnement,
            TPSU.nom_type_suivi,
            TVUL.nom_type_de_vulnerabilite,
            TPCH.nom_type_de_prise_charge,
            NIVE.nom_niveau

        FROM ValeursIndicateurs VI

        LEFT JOIN Region R ON VI.f_region_id = R.region_id
        LEFT JOIN Departement D ON VI.f_departement_id = D.departement_id
        LEFT JOIN SousPrefectures SP ON VI.f_sous_prefecture_id = SP.sousprefect_id
        LEFT JOIN Indicateur I ON VI.f_indicateur_id = I.indicateur_id
        LEFT JOIN Sexe S ON VI.f_sexe_id = S.sexe_id
        LEFT JOIN GroupeAge GA ON VI.f_grp_age_id = GA.grp_age_id
        LEFT JOIN Age A ON VI.f_age_id = A.age_id
        LEFT JOIN Cycle C ON VI.f_cycle_id = C.id_cycle
        LEFT JOIN Niveau_Prescolaire NP ON VI.f_niveau_prescolaire_id = NP.niv_prescolaire_id
        LEFT JOIN Niveau_Primaire N1C ON VI.f_niveau_primaire_id = N1C.niv_primaire_id
        LEFT JOIN Niveau_Secondaire_1er_cycle NS1C ON VI.f_niveau_secondaire_1er_cycle_id = NS1C.niv_secondaire_1er_cycle_id
        LEFT JOIN Niveau_Secondaire_2nd_cycle NS2C ON VI.f_niveau_secondaire_2nd_cycle_id = NS2C.niv_secondaire_2nd_cycle_id
        LEFT JOIN Niveau_Technique NT ON VI.f_niveau_technique_id = NT.niv_technique_id
        LEFT JOIN Niveau_Superieur NS ON VI.f_niveau_superieur_id = NS.niv_superieur_id
        LEFT JOIN Niveau_Professionnel NP2 ON VI.f_niveau_professionnel_id = NP2.niv_professionnel_id  -- Utilisation de l'alias 'NP2'
        LEFT JOIN Type_examen TE ON VI.f_type_examen_id = TE.id_type_examen
        LEFT JOIN Infrastructures_sanitaires SIS ON VI.f_infrastructures_sanitaires_id = SIS.id_infrastructures_sanitaires
        LEFT JOIN Lieu_accouchement LA ON VI.f_lieu_accouchement_id = LA.id_lieu_accouchement
        LEFT JOIN Etat_vaccinal EV ON VI.f_etat_vaccinal_id = EV.id_etat_vaccinal
        LEFT JOIN Types_de_vaccination TV ON VI.f_types_de_vaccination_id = TV.id_types_de_vaccination
        LEFT JOIN Pathologie P ON VI.f_pathologie_id = P.id_pathologie
        LEFT JOIN Tranche_age TA ON VI.f_tranche_age_id = TA.id_tranche_age
        LEFT JOIN Maladies_du_PEV MP ON VI.f_maladies_du_pev_id = MP.id_maladies_du_pev
        LEFT JOIN Maladies_infectieuses MI ON VI.f_maladies_infectieuses_id = MI.id_maladies_infectieuses
        LEFT JOIN Infection_respiratoire IRES ON VI.f_infectieuses_respiratoire_id=IRES.id_infectieuses_respiratoire
        LEFT JOIN Maladies_IST IST ON VI.f_maladies_ist_id = IST.id_maladies_ist
        LEFT JOIN Type_de_Maladie TM ON VI.f_type_de_maladie_id = TM.id_type_de_maladie
        LEFT JOIN Activites_IEC AI ON VI.f_activites_iec_id = AI.id_activites_iec
        LEFT JOIN Service_Medicaux SM ON VI.f_service_medicaux_id = SM.id_service_medicaux
        LEFT JOIN Type_infrastructures_ou_organisations_sportives TIS ON VI.f_type_infrastructures_ou_organisations_sportives_id = TIS.id_type_infrastructures_sportives
        LEFT JOIN Disciplines_sportives DS ON VI.f_disciplines_sportives_id = DS.id_disciplines_sportives
        LEFT JOIN Type_infrastructures_culturelles TIC ON VI.f_type_infrastructures_culturelles_id = TIC.id_type_infrastructures_culturelles
        LEFT JOIN Type_de_Patrimoines_culturels_immatériels PCI ON VI.f_type_de_patrimoines_culturels_immat_id = PCI.id_type_patrimoines_culturels_immatériels
        LEFT JOIN Type_actions_culturelles_et_artistiques ACA ON VI.f_type_actions_culturelles_et_artistiques_id = ACA.id_type_actions_culturelles_artistiques
        LEFT JOIN Type_operateurs_des_oeuvres_esprit OE ON VI.f_type_operateurs_des_oeuvres_esprit_id = OE.id_type_operateurs_oeuvres_esprit
        LEFT JOIN Type_de_groupes_culturels GC ON VI.f_type_de_groupes_culturels_id = GC.id_type_groupes_culturels
        LEFT JOIN Type_de_manifestations_culturelles MC ON VI.f_type_de_manifestations_culturelles_id = MC.id_type_manifestations_culturelles

        LEFT JOIN Trimestre TRIM ON VI.f_trimestre_id=TRIM.id_trimestre
        LEFT JOIN Etat_des_ouvrages TDO ON VI.f_etat_des_ouvrages_id=TDO.id_etat_des_ouvrages
        LEFT JOIN Type_abonnement TABO ON VI.f_type_abonement_id=TABO.id_type_abonnement
        LEFT JOIN Type_suivi TPSU ON VI.f_type_suivi_id=TPSU.id_type_suivi
        LEFT JOIN Type_de_vulnerabilite  TVUL ON VI.f_type_de_vulnerabilite_id=TVUL.id_type_de_vulnerabilite
        LEFT JOIN Type_de_prise_charge TPCH ON VI.f_type_de_prise_charge_id=TPCH.id_type_de_prise_charge
        LEFT JOIN Niveau NIVE ON VI.f_niveau_id=NIVE.id_niveau
        LEFT JOIN Departement d2 ON sp.f_departement_id = d2.departement_id
        LEFT JOIN Region r2 ON d2.f_region_id = r2.region_id
        LEFT JOIN Region r3 ON d.f_region_id = r3.region_id
        """

    cursor.execute(query)
    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=[
        "ID", "Région", "Département", "Sous-préfecture", "Indicateur", "Valeur Indicateur", "Année de collecte", "Sexe",
        "Groupe d'âge", "Age", "Cycle scolaire", "Niveau préscolaire", "Niveau primaire", "Niveau Secondaire 1er cycle",
        "Niveau Secondaire 2nd cycle", "Niveau Technique", "Niveau Supérieur", "Niveau Professionnel", "Type d'examen",
        "Infrastructures sanitaires", "Lieu d'accouchement", "État vaccinal", "Types de vaccination", "Pathologie",
        "Tranche d'âge", "Maladies du PEV", "Maladies infectieuses","Infectieuses respiratoire", "Maladies IST", "Type de maladie", "Activités IEC",
        "Services médicaux", "Type d'infrastructures sportives", "Disciplines sportives", "Type d'infrastructures culturelles",
        "Type de patrimoines culturels immatériels", "Type d'actions culturelles et artistiques", "Type d'opérateurs des œuvres d'esprit",
        "Type de groupes culturels", "Type de manifestations culturelles","Trimestre","Etat des ouvrages","Type d'abonnement",
        "Type de suivi","Type de vulnerabilité","Type de prise en charge","Niveau"
    ])

    conn.close()
    return df


def insert_into_valeur_indicateur_libelle():
    conn = cf.create_connection()
    cursor = conn.cursor()

    # Sélectionner les données à insérer
    query_select = """
    SELECT 
       VI.id,
            COALESCE(r.nom_region, r2.nom_region, r3.nom_region) AS nom_region, 
            COALESCE(d.nom_departement, d2.nom_departement) AS nom_departement, 
            SP.nom_sousprefecture,
            I.nom_indicateur,
            VI.Valeur,
            VI.Annee,
            S.sexe,
            GA.groupe_age,
            A.age,
            C.nom_cycle,
            NP.nom_prescolaire,
            N1C.nom_primaire,
            NS1C.nom_secondaire_1er_cycle,
            NS2C.nom_secondaire_2nd_cycle,
            NT.nom_technique,
            NS.nom_superieur,
            NP2.nom_professionnel,  -- Changé 'NP' en 'NP2' pour Niveau_Professionnel
            TE.nom_type_examen,
            SIS.nom_infrastructures_sanitaires,
            LA.nom_lieu_accouchement,
            EV.nom_etat_vaccinal,
            TV.nom_types_de_vaccination,
            P.nom_pathologie,
            TA.nom_tranche_age,
            MP.nom_maladies_du_pev,
            MI.nom_maladies_infectieuses,
            IRES.nom_infectieuses_respiratoire,
            IST.nom_maladies_ist,
            TM.nom_type_de_maladie,
            AI.nom_activites_iec,
            SM.nom_service_medicaux,
            TIS.nom_type_infrastructures_sportives,
            DS.nom_disciplines_sportives,
            TIC.nom_type_infrastructures_culturelles,
            PCI.nom_type_patrimoines_culturels_immatériels,
            ACA.nom_type_actions_culturelles_artistiques,
            OE.nom_type_operateurs_oeuvres_esprit,
            GC.nom_type_groupes_culturels,
            MC.nom_type_manifestations_culturelles,

            TRIM.nom_trimestre,
            TDO.nom_etat_des_ouvrages,
            TABO.nom_type_abonnement,
            TPSU.nom_type_suivi,
            TVUL.nom_type_de_vulnerabilite,
            TPCH.nom_type_de_prise_charge,
            NIVE.nom_niveau

        FROM ValeursIndicateurs VI

        LEFT JOIN Region R ON VI.f_region_id = R.region_id
        LEFT JOIN Departement D ON VI.f_departement_id = D.departement_id
        LEFT JOIN SousPrefectures SP ON VI.f_sous_prefecture_id = SP.sousprefect_id
        LEFT JOIN Indicateur I ON VI.f_indicateur_id = I.indicateur_id
        LEFT JOIN Sexe S ON VI.f_sexe_id = S.sexe_id
        LEFT JOIN GroupeAge GA ON VI.f_grp_age_id = GA.grp_age_id
        LEFT JOIN Age A ON VI.f_age_id = A.age_id
        LEFT JOIN Cycle C ON VI.f_cycle_id = C.id_cycle
        LEFT JOIN Niveau_Prescolaire NP ON VI.f_niveau_prescolaire_id = NP.niv_prescolaire_id
        LEFT JOIN Niveau_Primaire N1C ON VI.f_niveau_primaire_id = N1C.niv_primaire_id
        LEFT JOIN Niveau_Secondaire_1er_cycle NS1C ON VI.f_niveau_secondaire_1er_cycle_id = NS1C.niv_secondaire_1er_cycle_id
        LEFT JOIN Niveau_Secondaire_2nd_cycle NS2C ON VI.f_niveau_secondaire_2nd_cycle_id = NS2C.niv_secondaire_2nd_cycle_id
        LEFT JOIN Niveau_Technique NT ON VI.f_niveau_technique_id = NT.niv_technique_id
        LEFT JOIN Niveau_Superieur NS ON VI.f_niveau_superieur_id = NS.niv_superieur_id
        LEFT JOIN Niveau_Professionnel NP2 ON VI.f_niveau_professionnel_id = NP2.niv_professionnel_id  -- Utilisation de l'alias 'NP2'
        LEFT JOIN Type_examen TE ON VI.f_type_examen_id = TE.id_type_examen
        LEFT JOIN Infrastructures_sanitaires SIS ON VI.f_infrastructures_sanitaires_id = SIS.id_infrastructures_sanitaires
        LEFT JOIN Lieu_accouchement LA ON VI.f_lieu_accouchement_id = LA.id_lieu_accouchement
        LEFT JOIN Etat_vaccinal EV ON VI.f_etat_vaccinal_id = EV.id_etat_vaccinal
        LEFT JOIN Types_de_vaccination TV ON VI.f_types_de_vaccination_id = TV.id_types_de_vaccination
        LEFT JOIN Pathologie P ON VI.f_pathologie_id = P.id_pathologie
        LEFT JOIN Tranche_age TA ON VI.f_tranche_age_id = TA.id_tranche_age
        LEFT JOIN Maladies_du_PEV MP ON VI.f_maladies_du_pev_id = MP.id_maladies_du_pev
        LEFT JOIN Maladies_infectieuses MI ON VI.f_maladies_infectieuses_id = MI.id_maladies_infectieuses
        LEFT JOIN Infection_respiratoire IRES ON VI.f_infectieuses_respiratoire_id=IRES.id_infectieuses_respiratoire
        LEFT JOIN Maladies_IST IST ON VI.f_maladies_ist_id = IST.id_maladies_ist
        LEFT JOIN Type_de_Maladie TM ON VI.f_type_de_maladie_id = TM.id_type_de_maladie
        LEFT JOIN Activites_IEC AI ON VI.f_activites_iec_id = AI.id_activites_iec
        LEFT JOIN Service_Medicaux SM ON VI.f_service_medicaux_id = SM.id_service_medicaux
        LEFT JOIN Type_infrastructures_ou_organisations_sportives TIS ON VI.f_type_infrastructures_ou_organisations_sportives_id = TIS.id_type_infrastructures_sportives
        LEFT JOIN Disciplines_sportives DS ON VI.f_disciplines_sportives_id = DS.id_disciplines_sportives
        LEFT JOIN Type_infrastructures_culturelles TIC ON VI.f_type_infrastructures_culturelles_id = TIC.id_type_infrastructures_culturelles
        LEFT JOIN Type_de_Patrimoines_culturels_immatériels PCI ON VI.f_type_de_patrimoines_culturels_immat_id = PCI.id_type_patrimoines_culturels_immatériels
        LEFT JOIN Type_actions_culturelles_et_artistiques ACA ON VI.f_type_actions_culturelles_et_artistiques_id = ACA.id_type_actions_culturelles_artistiques
        LEFT JOIN Type_operateurs_des_oeuvres_esprit OE ON VI.f_type_operateurs_des_oeuvres_esprit_id = OE.id_type_operateurs_oeuvres_esprit
        LEFT JOIN Type_de_groupes_culturels GC ON VI.f_type_de_groupes_culturels_id = GC.id_type_groupes_culturels
        LEFT JOIN Type_de_manifestations_culturelles MC ON VI.f_type_de_manifestations_culturelles_id = MC.id_type_manifestations_culturelles

        LEFT JOIN Trimestre TRIM ON VI.f_trimestre_id=TRIM.id_trimestre
        LEFT JOIN Etat_des_ouvrages TDO ON VI.f_etat_des_ouvrages_id=TDO.id_etat_des_ouvrages
        LEFT JOIN Type_abonnement TABO ON VI.f_type_abonnement_id=TABO.id_type_abonnement
        LEFT JOIN Type_suivi TPSU ON VI.f_type_suivi_id=TPSU.id_type_suivi
        LEFT JOIN Type_de_vulnerabilite  TVUL ON VI.f_type_de_vulnerabilite_id=TVUL.id_type_de_vulnerabilite
        LEFT JOIN Type_de_prise_charge TPCH ON VI.f_type_de_prise_charge_id=TPCH.id_type_de_prise_charge
        LEFT JOIN Niveau NIVE ON VI.f_niveau_id=NIVE.id_niveau
        LEFT JOIN Departement d2 ON sp.f_departement_id = d2.departement_id
        LEFT JOIN Region r2 ON d2.f_region_id = r2.region_id
        LEFT JOIN Region r3 ON d.f_region_id = r3.region_id
    """

    cursor.execute(query_select)
    rows = cursor.fetchall()

    # Insérer les données dans la nouvelle table
    query_insert = """
    INSERT INTO valeur_indicateur_libelle (
        id, nom_region, nom_departement, nom_sousprefecture, nom_indicateur, Valeur, Annee, sexe, groupe_age, age,
        nom_cycle, nom_prescolaire, nom_primaire, nom_secondaire_1er_cycle, nom_secondaire_2nd_cycle, nom_technique,
        nom_superieur, nom_professionnel, nom_type_examen, nom_infrastructures_sanitaires, nom_lieu_accouchement,
        nom_etat_vaccinal, nom_types_de_vaccination, nom_pathologie, nom_tranche_age, nom_maladies_du_pev,
        nom_maladies_infectieuses,nom_infectieuses_respiratoire ,nom_maladies_ist, nom_type_de_maladie, nom_activites_iec, nom_service_medicaux,
        nom_type_infrastructures_sportives, nom_disciplines_sportives, nom_type_infrastructures_culturelles,
        nom_type_patrimoines_culturels_immatériels, nom_type_actions_culturelles_artistiques, nom_type_operateurs_oeuvres_esprit,
        nom_type_groupes_culturels, nom_type_manifestations_culturelles, nom_trimestre, nom_etat_des_ouvrages,
        nom_type_abonnement, nom_type_suivi, nom_type_de_vulnerabilite, nom_type_de_prise_charge, nom_niveau
    ) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)
    ON DUPLICATE KEY UPDATE
        id = VALUES(id)

    """
    for row in rows:
        # Create a tuple with all values, including the id
        values = (row[0],) + row[1:]  # Add id at the beginning

        # Check if the row exists more efficiently
        cursor.execute("SELECT 1 FROM valeur_indicateur_libelle WHERE id = %s LIMIT 1", (row[0],))
        exists = cursor.fetchone() is not None

        if not exists:
            cursor.execute(query_insert, values)

    conn.commit()
    cursor.close()
    print('Insertion pour libellé indicateur ok')
    conn.close()

def insert_rejet():
    try:
        conn = cf.create_connection()
        cursor = conn.cursor()

        # Sélectionner les données à insérer
        query_select = """
            SELECT * FROM valeur_indicateur_libelle WHERE statut = 'Rejeté'
        """
        cursor.execute(query_select)
        rows = cursor.fetchall()

        # Générer dynamiquement la liste des colonnes et des valeurs
        columns = ', '.join([desc[0] for desc in cursor.description])
        placeholders = ', '.join(['%s'] * len(cursor.description))
        # Construire la requête d'insertion
        query_insert = f"""
            INSERT INTO valeur_rejet ({columns}) VALUES ({placeholders})
            ON DUPLICATE KEY UPDATE 
            {', '.join([f"{desc[0]} = VALUES({desc[0]})" for desc in cursor.description if desc[0] != 'id'])}
        """

        for row in rows:
            cursor.execute(query_insert, row)

        conn.commit()
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'insertion : {err}")
    finally:
        cursor.close()
        conn.close()

cf.fonction_suppression_automatique()
insert_into_valeur_indicateur_libelle()

#insert_rejet()




