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

    // Ajoute le gestionnaire d'événements de soumission
    var form = document.getElementById('main-form');
    if (form) {
        form.addEventListener('submit', confirmSubmission);
    }
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

document.getElementById('add-button').addEventListener('click', function() {
    var duplicateWrapper = document.getElementById('duplicate-wrapper').cloneNode(true);
    duplicateWrapper.id = ''; // Retire l'ID pour éviter des duplications multiples
    document.getElementById('form-wrapper').appendChild(duplicateWrapper);
});

function confirmSubmission(event) {
    event.preventDefault(); // Empêche la soumission immédiate du formulaire

    // Récupère les valeurs saisies
    var idIndicateur = document.getElementById('id_indicateur2').value;
    var idCodeEntite = document.getElementById('id_code_entite2').value;
    var anne = document.getElementById('anne').value;

    // Récupère les valeurs pour chaque niveau de désagrégation
    var desagregations = [];

    // Traite chaque niveau de désagrégation
    {% if nom_groupe_age %}
    {% for id, nom in nom_groupe_age %}
        var valeur = document.getElementById('id_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }} ans: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_primaire %}
    {% for id, nom in nom_primaire %}
        var valeur = document.getElementById('idprimaire_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_sexe %}
    {% for id, nom in nom_sexe %}
        var valeur = document.getElementById('sexe_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_cycle %}
    {% for id, nom in nom_cycle %}
        var valeur = document.getElementById('idcycle_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_prescolaire %}
    {% for id, nom in nom_prescolaire %}
        var valeur = document.getElementById('idprescolaire_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_secondaire_1er %}
    {% for id, nom in nom_secondaire_1er %}
        var valeur = document.getElementById('idsecondaire1_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_secondaire_2nd %}
    {% for id, nom in nom_secondaire_2nd %}
        var valeur = document.getElementById('idsecondaire2_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_technique %}
    {% for id, nom in nom_technique %}
        var valeur = document.getElementById('idtechnique_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_superieur %}
    {% for id, nom in nom_superieur %}
        var valeur = document.getElementById('idsuperieur_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_professionnel %}
    {% for id, nom in nom_professionnel %}
        var valeur = document.getElementById('idprofessionnel_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_examen_scolaire %}
    {% for id, nom in nom_type_examen_scolaire %}
        var valeur = document.getElementById('idtypeexamenscolaire_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_infrastructure_sanitaire %}
    {% for id, nom in nom_infrastructure_sanitaire %}
        var valeur = document.getElementById('idinfrastructure_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_lieu_accouchement %}
    {% for id, nom in nom_lieu_accouchement %}
        var valeur = document.getElementById('idlieuaccouchement_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_etat_vaccinal %}
    {% for id, nom in nom_etat_vaccinal %}
        var valeur = document.getElementById('idetatvaccinal_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_vaccination %}
    {% for id, nom in nom_type_vaccination %}
        var valeur = document.getElementById('idtypevaccination_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_pathologie %}
    {% for id, nom in nom_pathologie %}
        var valeur = document.getElementById('idpathologie_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_tranche_age %}
    {% for id, nom in nom_tranche_age %}
        var valeur = document.getElementById('idtrancheage_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_maladie_pev %}
    {% for id, nom in nom_maladie_pev %}
        var valeur = document.getElementById('idmaladiepev_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_maladie_infectieuse %}
    {% for id, nom in nom_maladie_infectieuse %}
        var valeur = document.getElementById('idmaladieinfectieuse_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_infection_respiratoire %}
    {% for id, nom in nom_infection_respiratoire %}
        var valeur = document.getElementById('idinfectionrespiratoire_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_maladie_sist %}
    {% for id, nom in nom_maladie_sist %}
        var valeur = document.getElementById('idmaladiesist_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_maladie %}
    {% for id, nom in nom_type_maladie %}
        var valeur = document.getElementById('idtypemaladies_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_activite_siec %}
    {% for id, nom in nom_activite_siec %}
        var valeur = document.getElementById('idactivitesiec_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_service_medical %}
    {% for id, nom in nom_service_medical %}
        var valeur = document.getElementById('idservicesmedicaux_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_infrastructure_organisation %}
    {% for id, nom in nom_infrastructure_organisation %}
        var valeur = document.getElementById('idinfrastructureorganisation_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_discipline_sportive %}
    {% for id, nom in nom_discipline_sportive %}
        var valeur = document.getElementById('iddisciplinesportive_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_infrastructure_culturel %}
    {% for id, nom in nom_type_infrastructure_culturel %}
        var valeur = document.getElementById('idtypeinfrastructureculturel_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_patrimoine_culturel %}
    {% for id, nom in nom_type_patrimoine_culturel %}
        var valeur = document.getElementById('idtypepatrimoineculturel_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_actions_culturelles %}
    {% for id, nom in nom_type_actions_culturelles %}
        var valeur = document.getElementById('idtypeactionsculturelles_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_oeuvre_esprit %}
    {% for id, nom in nom_type_oeuvre_esprit %}
        var valeur = document.getElementById('idtypeoperateuroeuvreesprit_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_groupe_culturel %}
    {% for id, nom in nom_type_groupe_culturel %}
        var valeur = document.getElementById('idtypedegroupeculturel_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_manifestation_culturelle %}
    {% for id, nom in nom_type_manifestation_culturelle %}
        var valeur = document.getElementById('idtypedemanifestationculturelle_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_trimestre %}
    {% for id, nom in nom_trimestre %}
        var valeur = document.getElementById('idtrimestre_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_etat_oeuvres %}
    {% for id, nom in nom_etat_oeuvres %}
        var valeur = document.getElementById('idetatdesoeuvres_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_abonnement %}
    {% for id, nom in nom_type_abonnement %}
        var valeur = document.getElementById('idtypeabonnement_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_suivi %}
    {% for id, nom in nom_type_suivi %}
        var valeur = document.getElementById('idtypedesuivi_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_vulnerabilite %}
    {% for id, nom in nom_type_vulnerabilite %}
        var valeur = document.getElementById('idtypedevulnerabilite_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_type_prise_charge %}
    {% for id, nom in nom_type_prise_charge %}
        var valeur = document.getElementById('idtypedeprisecharge_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    {% if nom_niveau %}
    {% for id, nom in nom_niveau %}
        var valeur = document.getElementById('idniveau_{{ id }}').value;
        if (valeur) {
            desagregations.push("{{ nom }}: " + valeur);
        }
    {% endfor %}
    {% endif %}

    // Affiche un message avec les données saisies
    alert("Valeurs saisies :\n" + desagregations.join("\n"));
}
