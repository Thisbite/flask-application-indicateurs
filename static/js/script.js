 document.addEventListener("DOMContentLoaded", function() {
        // Vérifie la validité des données
        var duplicateWrapper = document.getElementById('duplicate-wrapper');
        var nomInd = duplicateWrapper ? duplicateWrapper.getAttribute('data-nom-ind') : null;
        var nomEntite = duplicateWrapper ? duplicateWrapper.getAttribute('data-nom-entite') : null;

        // Si l'indicateur ou l'entité géographique n'est pas valide, on cache le formulaire
        if (!nomInd || !nomEntite || nomInd === "" || nomEntite === "") {
            if (duplicateWrapper) {
                duplicateWrapper.style.display = 'none';
            }
        }

        // Remplit les champs du formulaire avec les données stockées
        fillFormData();
    });

    function saveFormData() {
        localStorage.setItem('id_indicateur', document.getElementById('id_indicateur').value);
        localStorage.setItem('id_code_entite', document.getElementById('id_code_entite').value);
        localStorage.setItem('id_niveau_desagregation', document.getElementById('id_niveau_desagregation').value);
    }

    function fillFormData() {
        if (localStorage.getItem('id_indicateur')) {
            document.getElementById('id_indicateur').value = localStorage.getItem('id_indicateur');
        }
        if (localStorage.getItem('id_code_entite')) {
            document.getElementById('id_code_entite').value = localStorage.getItem('id_code_entite');
        }
        if (localStorage.getItem('id_niveau_desagregation')) {
            document.getElementById('id_niveau_desagregation').value = localStorage.getItem('id_niveau_desagregation');
        }
    }

    document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.form-container').onsubmit = function(event) {
        event.preventDefault(); // Empêche la soumission immédiate du formulaire

        // Récupère les valeurs saisies
        var idIndicateur = document.getElementById('id_indicateur2').value;
        var idCodeEntite = document.getElementById('id_code_entite2').value;
        var anne = document.getElementById('anne').value;

        // Récupère les valeurs des groupes d'âge
        var desagregations = [];
        var sommeDesagregations = 0;

        {% if nom_groupe_age %}
        {% for id, nom in nom_groupe_age %}
            var valeur = document.querySelector('input[name="id_{{ id }}"]').value;
            if (valeur) {
                desagregations.push("{{ nom }} ans: " + valeur);
                sommeDesagregations += parseFloat(valeurNiveau);
            }
        {% endfor %}
        {% endif %}

        // Récupère les valeurs des niveaux "Primaire"
        {% if nom_primaire %}
        {% for id, nom in nom_primaire %}
            var valeurPrimaire = document.querySelector('input[name="idprimaire_{{ id }}"]').value;
            if (valeurPrimaire) {
                desagregations.push("{{ nom }}: " + valeurPrimaire);
            }
        {% endfor %}
        {% endif %}

        // Récupère les valeurs des niveaux "Sexe"
{% if nom_sexe %}
{% for id, nom in nom_sexe %}
    var valeurSexe = document.querySelector('input[name="sexe_{{ id }}"]').value;
    if (valeurSexe) {
        desagregations.push("{{ nom }}: " + valeurSexe);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Cycle"
{% if nom_cycle %}
{% for id, nom in nom_cycle %}
    var valeurCycle = document.querySelector('input[name="idcycle_{{ id }}"]').value;
    if (valeurCycle) {
        desagregations.push("{{ nom }}: " + valeurCycle);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Prescolaire"
{% if nom_prescolaire %}
{% for id, nom in nom_prescolaire %}
    var valeurPrescolaire = document.querySelector('input[name="idprescolaire_{{ id }}"]').value;
    if (valeurPrescolaire) {
        desagregations.push("{{ nom }}: " + valeurPrescolaire);
    }
{% endfor %}
{% endif %}

// Répéter pour toutes les autres sections...

// Exemple final pour toutes les sections
{% if nom_secondaire_1er %}
{% for id, nom in nom_secondaire_1er %}
    var valeurSecondaire1 = document.querySelector('input[name="idsecondaire1_{{ id }}"]').value;
    if (valeurSecondaire1) {
        desagregations.push("{{ nom }}: " + valeurSecondaire1);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Secondaire 2nd"
{% if nom_secondaire_2nd %}
{% for id, nom in nom_secondaire_2nd %}
    var valeurSecondaire2nd = document.querySelector('input[name="idsecondaire2_{{ id }}"]').value;
    if (valeurSecondaire2nd) {
        desagregations.push("{{ nom }}: " + valeurSecondaire2nd);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Technique"
{% if nom_technique %}
{% for id, nom in nom_technique %}
    var valeurTechnique = document.querySelector('input[name="idtechnique_{{ id }}"]').value;
    if (valeurTechnique) {
        desagregations.push("{{ nom }}: " + valeurTechnique);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Supérieur"
{% if nom_superieur %}
{% for id, nom in nom_superieur %}
    var valeurSuperieur = document.querySelector('input[name="idsuperieur_{{ id }}"]').value;
    if (valeurSuperieur) {
        desagregations.push("{{ nom }}: " + valeurSuperieur);
    }
{% endfor %}
{% endif %}
// Récupère les valeurs des niveaux "Professionnel"
{% if nom_professionnel %}
{% for id, nom in nom_professionnel %}
    var valeurProfessionnel = document.querySelector('input[name="idprofessionnel_{{ id }}"]').value;
    if (valeurProfessionnel) {
        desagregations.push("{{ nom }}: " + valeurProfessionnel);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Type Examen Scolaire"
{% if nom_type_examen_scolaire %}
{% for id, nom in nom_type_examen_scolaire %}
    var valeurExamenScolaire = document.querySelector('input[name="idtypeexamenscolaire_{{ id }}"]').value;
    if (valeurExamenScolaire) {
        desagregations.push("{{ nom }}: " + valeurExamenScolaire);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Infrastructure Sanitaire"
{% if nom_infrastructure_sanitaire %}
{% for id, nom in nom_infrastructure_sanitaire %}
    var valeurInfrastructureSanitaire = document.querySelector('input[name="idinfrastructure_{{ id }}"]').value;
    if (valeurInfrastructureSanitaire) {
        desagregations.push("{{ nom }}: " + valeurInfrastructureSanitaire);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Lieu d'accouchement"
{% if nom_lieu_accouchement %}
{% for id, nom in nom_lieu_accouchement %}
    var valeurLieuAccouchement = document.querySelector('input[name="idlieuaccouchement_{{ id }}"]').value;
    if (valeurLieuAccouchement) {
        desagregations.push("{{ nom }}: " + valeurLieuAccouchement);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "État Vaccinal"
{% if nom_etat_vaccinal %}
{% for id, nom in nom_etat_vaccinal %}
    var valeurEtatVaccinal = document.querySelector('input[name="idetatvaccinal_{{ id }}"]').value;
    if (valeurEtatVaccinal) {
        desagregations.push("{{ nom }}: " + valeurEtatVaccinal);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Type de Vaccination"
{% if nom_type_vaccination %}
{% for id, nom in nom_type_vaccination %}
    var valeurTypeVaccination = document.querySelector('input[name="idtypevaccination_{{ id }}"]').value;
    if (valeurTypeVaccination) {
        desagregations.push("{{ nom }}: " + valeurTypeVaccination);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Pathologie"
{% if nom_pathologie %}
{% for id, nom in nom_pathologie %}
    var valeurPathologie = document.querySelector('input[name="idpathologie_{{ id }}"]').value;
    if (valeurPathologie) {
        desagregations.push("{{ nom }}: " + valeurPathologie);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Tranche d'âge"
{% if nom_tranche_age %}
{% for id, nom in nom_tranche_age %}
    var valeurTrancheAge = document.querySelector('input[name="idtrancheage_{{ id }}"]').value;
    if (valeurTrancheAge) {
        desagregations.push("{{ nom }}: " + valeurTrancheAge);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Maladie PEV"
{% if nom_maladie_pev %}
{% for id, nom in nom_maladie_pev %}
    var valeurMaladiePEV = document.querySelector('input[name="idmaladiepev_{{ id }}"]').value;
    if (valeurMaladiePEV) {
        desagregations.push("{{ nom }}: " + valeurMaladiePEV);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Maladie Infectieuse"
{% if nom_maladie_infectieuse %}
{% for id, nom in nom_maladie_infectieuse %}
    var valeurMaladieInfectieuse = document.querySelector('input[name="idmaladieinfectieuse_{{ id }}"]').value;
    if (valeurMaladieInfectieuse) {
        desagregations.push("{{ nom }}: " + valeurMaladieInfectieuse);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Infection Respiratoire"
{% if nom_infection_respiratoire %}
{% for id, nom in nom_infection_respiratoire %}
    var valeurInfectionRespiratoire = document.querySelector('input[name="idinfectionrespiratoire_{{ id }}"]').value;
    if (valeurInfectionRespiratoire) {
        desagregations.push("{{ nom }}: " + valeurInfectionRespiratoire);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Maladie SIST"
{% if nom_maladie_sist %}
{% for id, nom in nom_maladie_sist %}
    var valeurMaladieSIST = document.querySelector('input[name="idmaladiesist_{{ id }}"]').value;
    if (valeurMaladieSIST) {
        desagregations.push("{{ nom }}: " + valeurMaladieSIST);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Type de Maladie"
{% if nom_type_maladie %}
{% for id, nom in nom_type_maladie %}
    var valeurTypeMaladie = document.querySelector('input[name="idtypemaladies_{{ id }}"]').value;
    if (valeurTypeMaladie) {
        desagregations.push("{{ nom }}: " + valeurTypeMaladie);
    }
{% endfor %}
{% endif %}


// Récupère les valeurs des niveaux "Activité SIEC"
{% if nom_activite_siec %}
{% for id, nom in nom_activite_siec %}
    var valeurActiviteSIEC = document.querySelector('input[name="idactivitesiec_{{ id }}"]').value;
    if (valeurActiviteSIEC) {
        desagregations.push("{{ nom }}: " + valeurActiviteSIEC);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Service Médical"
{% if nom_service_medical %}
{% for id, nom in nom_service_medical %}
    var valeurServiceMedical = document.querySelector('input[name="idservicesmedicaux_{{ id }}"]').value;
    if (valeurServiceMedical) {
        desagregations.push("{{ nom }}: " + valeurServiceMedical);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Infrastructure Organisation"
{% if nom_infrastructure_organisation %}
{% for id, nom in nom_infrastructure_organisation %}
    var valeurInfrastructureOrganisation = document.querySelector('input[name="idinfrastructureorganisation_{{ id }}"]').value;
    if (valeurInfrastructureOrganisation) {
        desagregations.push("{{ nom }}: " + valeurInfrastructureOrganisation);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Discipline Sportive"
{% if nom_discipline_sportive %}
{% for id, nom in nom_discipline_sportive %}
    var valeurDisciplineSportive = document.querySelector('input[name="iddisciplinesportive_{{ id }}"]').value;
    if (valeurDisciplineSportive) {
        desagregations.push("{{ nom }}: " + valeurDisciplineSportive);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Type Infrastructure Culturel"
{% if nom_type_infrastructure_culturel %}
{% for id, nom in nom_type_infrastructure_culturel %}
    var valeurTypeInfrastructureCulturel = document.querySelector('input[name="idtypeinfrastructureculturel_{{ id }}"]').value;
    if (valeurTypeInfrastructureCulturel) {
        desagregations.push("{{ nom }}: " + valeurTypeInfrastructureCulturel);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Type Patrimoine Culturel"
{% if nom_type_patrimoine_culturel %}
{% for id, nom in nom_type_patrimoine_culturel %}
    var valeurTypePatrimoineCulturel = document.querySelector('input[name="idtypepatrimoineculturel_{{ id }}"]').value;
    if (valeurTypePatrimoineCulturel) {
        desagregations.push("{{ nom }}: " + valeurTypePatrimoineCulturel);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Type Actions Culturelles"
{% if nom_type_actions_culturelles %}
{% for id, nom in nom_type_actions_culturelles %}
    var valeurTypeActionsCulturelles = document.querySelector('input[name="idtypeactionsculturelles_{{ id }}"]').value;
    if (valeurTypeActionsCulturelles) {
        desagregations.push("{{ nom }}: " + valeurTypeActionsCulturelles);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Type Œuvre Esprit"
{% if nom_type_oeuvre_esprit %}
{% for id, nom in nom_type_oeuvre_esprit %}
    var valeurTypeOeuvreEsprit = document.querySelector('input[name="idtypeoperateuroeuvreesprit_{{ id }}"]').value;
    if (valeurTypeOeuvreEsprit) {
        desagregations.push("{{ nom }}: " + valeurTypeOeuvreEsprit);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Type Groupe Culturel"
{% if nom_type_groupe_culturel %}
{% for id, nom in nom_type_groupe_culturel %}
    var valeurTypeGroupeCulturel = document.querySelector('input[name="idtypedegroupeculturel_{{ id }}"]').value;
    if (valeurTypeGroupeCulturel) {
        desagregations.push("{{ nom }}: " + valeurTypeGroupeCulturel);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Type Manifestation Culturelle"
{% if nom_type_manifestation_culturelle %}
{% for id, nom in nom_type_manifestation_culturelle %}
    var valeurTypeManifestationCulturelle = document.querySelector('input[name="idtypedemanifestationculturelle_{{ id }}"]').value;
    if (valeurTypeManifestationCulturelle) {
        desagregations.push("{{ nom }}: " + valeurTypeManifestationCulturelle);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Trimestre"
{% if nom_trimestre %}
{% for id, nom in nom_trimestre %}
    var valeurTrimestre = document.querySelector('input[name="idtrimestre_{{ id }}"]').value;
    if (valeurTrimestre) {
        desagregations.push("{{ nom }}: " + valeurTrimestre);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "État des Œuvres"
{% if nom_etat_oeuvres %}
{% for id, nom in nom_etat_oeuvres %}
    var valeurEtatOeuvres = document.querySelector('input[name="idetatdesoeuvres_{{ id }}"]').value;
    if (valeurEtatOeuvres) {
        desagregations.push("{{ nom }}: " + valeurEtatOeuvres);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Type Abonnement"
{% if nom_type_abonnement %}
{% for id, nom in nom_type_abonnement %}
    var valeurTypeAbonnement = document.querySelector('input[name="idtypeabonnement_{{ id }}"]').value;
    if (valeurTypeAbonnement) {
        desagregations.push("{{ nom }}: " + valeurTypeAbonnement);
    }
{% endfor %}
{% endif %}


// Récupère les valeurs des niveaux "Type Suivi"
{% if nom_type_suivi %}
{% for id, nom in nom_type_suivi %}
    var valeurTypeSuivi = document.querySelector('input[name="idtypedesuivi_{{ id }}"]').value;
    if (valeurTypeSuivi) {
        desagregations.push("{{ nom }}: " + valeurTypeSuivi);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Type Vulnérabilité"
{% if nom_type_vulnerabilite %}
{% for id, nom in nom_type_vulnerabilite %}
    var valeurTypeVulnerabilite = document.querySelector('input[name="idtypedevulnerabilite_{{ id }}"]').value;
    if (valeurTypeVulnerabilite) {
        desagregations.push("{{ nom }}: " + valeurTypeVulnerabilite);
    }
{% endfor %}
{% endif %}

// Récupère les valeurs des niveaux "Type Prise en Charge"
{% if nom_type_prise_charge %}
{% for id, nom in nom_type_prise_charge %}
    var valeurTypePriseCharge = document.querySelector('input[name="idtypedeprisecharge_{{ id }}"]').value;
    if (valeurTypePriseCharge) {
        desagregations.push("{{ nom }}: " + valeurTypePriseCharge);
    }
{% endfor %}
{% endif %}



// Continuez ainsi pour tous les autres niveaux...


        // Récupère les valeurs des niveaux "Cycle"
        {% if nom_niveau %}
        {% for id, nom in nom_niveau %}
            var valeurNiveau = document.querySelector('input[name="idniveau_{{ id }}"]').value;
            if (valeurNiveau) {
                desagregations.push("{{ nom }}: " + valeurNiveau);
            }
        {% endfor %}
        {% endif %}

        // Ajoutez les autres sections si nécessaire (comme Sexe, Type de prise en charge, etc.)

        // Insère les valeurs dans le tableau de confirmation
        document.getElementById('confirm-id-indicateur').textContent = idIndicateur;
        document.getElementById('confirm-id-code-entite').textContent = idCodeEntite;
        document.getElementById('confirm-anne').textContent = anne;
        document.getElementById('confirm-desagregations').innerHTML = desagregations.join('<br>');

     document.getElementById('confirm-somme-desagregations').textContent = "Total : " + sommeDesagregations;
        // Affiche la fenêtre modale
        var modal = document.getElementById('confirmation-modal');
        modal.style.display = 'flex';

        // Gère les boutons de confirmation et d'annulation
        document.getElementById('confirm-button').onclick = function() {
            document.querySelector('.form-container').submit(); // Soumet le formulaire si confirmé
        };

        document.getElementById('cancel-button').onclick = function() {
            modal.style.display = 'none'; // Ferme la fenêtre modale si annulé
        };

        return false; // Empêche la soumission immédiate du formulaire
    };
});