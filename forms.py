# Dictionnaire de correspondance des id_niveau_desagregation aux fonctions
import db_queries as ag
desagregation_map = {
    "1": ag.get_groupe_age,
    "2": ag.get_sexes,
    "3":ag.get_age,
    "4": ag.get_cycle,
    "5": ag.get_niveau_prescolaire,
    "6": ag.get_niveau_primaire,
    "7": ag.get_niveau_secondaire_1er_cycle,
    "8": ag.get_niveau_secondaire_2nd_cycle,
    "9": ag.get_niveau_technique,
    "10": ag.get_niveau_superieur,
    "11": ag.get_niveau_professionnel,
    "12": ag.get_type_examen,
    "13": ag.get_infrastructures_sanitaires,
    "14": ag.get_lieu_accouchement,
    "15": ag.get_etat_vaccinal,
    "16": ag.get_types_de_vaccination,
    "17": ag.get_pathologie,
    "18": ag.get_tranche_age,
    "19": ag.get_maladies_du_pev,
    "20": ag.get_maladies_infectieuses,
    "21": ag.get_infections_respiratoires,
    "22": ag.get_maladies_ist,
    "23": ag.get_type_de_maladie,
    "24": ag.get_activites_iec,
    "25": ag.get_service_medicaux,
    "26": ag.get_type_infrastructures_ou_organisations_sportives,
    "27": ag.get_disciplines_sportives,
    "28": ag.get_type_infrastructures_culturelles,
    "29": ag.get_type_de_patrimoines_culturels_immateriels,
    "30": ag.get_type_actions_culturelles_et_artistiques,
    "31": ag.get_type_operateurs_des_oeuvres_esprit,
    "32": ag.get_type_de_groupes_culturels,
    "33": ag.get_type_de_manifestations_culturelles,
    "34": ag.get_trimestre,
    "35": ag.get_etat_des_ouvrages,
    "36": ag.get_type_abonnement,
    "37": ag.get_type_suivi,
    "38": ag.get_type_de_vulnerabilite,
    "39": ag.get_type_suivi,
    "40": ag.get_niveau
}

# Fonction pour récupérer les noms en fonction du id_niveau_desagregation
def get_nom_desagregation(id_niveau_desagregation):
    # Vérifier si le niveau de désagrégation existe dans le dictionnaire
    if id_niveau_desagregation in desagregation_map:
        # Appeler la fonction correspondante
        return desagregation_map[id_niveau_desagregation]()
    else:
        # Gérer le cas où le niveau n'existe pas
        return None

