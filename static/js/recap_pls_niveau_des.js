
 // Sexe
 var selectSexe = document.querySelector('select[name="nom_sexe"]');
 var selectedOptionSexe = selectSexe.options[selectSexe.selectedIndex];
 var nomSexe = selectedOptionSexe.getAttribute('data-nom'); // Récupère le nom pour l'afficher
 if (nomSexe) {
     desagregations.push("Sexe: " +nomSexe);
 }



var selectGroupeAge = document.querySelector('select[name="nom_groupe_age"]');
var selectedOptionGroupeAge = selectGroupeAge.options[selectGroupeAge.selectedIndex];
var nomGroupeAge = selectedOptionGroupeAge.textContent;  // Récupère le nom pour l'afficher
if (nomGroupeAge) {
    desagregations.push("Groupe d'âge: " + nomGroupeAge);
}

var selectCycle = document.querySelector('select[name="nom_cycle"]');
var selectedOptionCycle = selectCycle.options[selectCycle.selectedIndex];
var nomCycle = selectedOptionCycle.getAttribute('data-nom'); // Récupère le nom pour l'afficher
if (nomCycle) {
    desagregations.push("Cycle: " + nomCycle);
}

var selectPrescolaire = document.querySelector('select[name="nom_prescolaire"]');
var selectedOptionPrescolaire = selectPrescolaire.options[selectPrescolaire.selectedIndex];
var nomPrescolaire = selectedOptionPrescolaire.textContent; // Récupère le nom pour l'afficher
if (nomPrescolaire) {
    desagregations.push("Prescolaire: " + nomPrescolaire);
}

var selectPrimaire = document.querySelector('select[name="nom_primaire"]');
var selectedOptionPrimaire = selectPrimaire.options[selectPrimaire.selectedIndex];
var nomPrimaire = selectedOptionPrimaire.textContent; // Récupère le nom pour l'afficher
if (nomPrimaire) {
    desagregations.push("Primaire: " + nomPrimaire);
}

var selectSecondaire1er = document.querySelector('select[name="nom_secondaire_1er"]');
var selectedOptionSecondaire1er = selectSecondaire1er.options[selectSecondaire1er.selectedIndex];
var nomSecondaire1er = selectedOptionSecondaire1er.textContent; // Récupère le nom pour l'afficher
if (nomSecondaire1er) {
    desagregations.push("Secondaire 1er Cycle: " + nomSecondaire1er);
}

var selectSecondaire2nd = document.querySelector('select[name="nom_secondaire_2nd"]');
var selectedOptionSecondaire2nd = selectSecondaire2nd.options[selectSecondaire2nd.selectedIndex];
var nomSecondaire2nd = selectedOptionSecondaire2nd.textContent; // Récupère le nom pour l'afficher
if (nomSecondaire2nd) {
    desagregations.push("Secondaire 2nd Cycle: " + nomSecondaire2nd);
}

var selectTechnique = document.querySelector('select[name="nom_technique"]');
var selectedOptionTechnique = selectTechnique.options[selectTechnique.selectedIndex];
var nomTechnique = selectedOptionTechnique.textContent;  // Récupère le nom pour l'afficher
if (nomTechnique) {
    desagregations.push("Technique: " + nomTechnique);
}

var selectSuperieur = document.querySelector('select[name="nom_superieur"]');
var selectedOptionSuperieur = selectSuperieur.options[selectSuperieur.selectedIndex];
var nomSuperieur = selectedOptionSuperieur.textContent; // Récupère le nom pour l'afficher
if (nomSuperieur) {
    desagregations.push("Supérieur: " + nomSuperieur);
}

var selectProfessionnel = document.querySelector('select[name="nom_professionnel"]');
var selectedOptionProfessionnel = selectProfessionnel.options[selectProfessionnel.selectedIndex];
var nomProfessionnel = selectedOptionProfessionnel.textContent; // Récupère le nom pour l'afficher
if (nomProfessionnel) {
    desagregations.push("Professionnel: " + nomProfessionnel);
}

var selectExamenScolaire = document.querySelector('select[name="nom_type_examen_scolaire"]');
var selectedOptionExamenScolaire = selectExamenScolaire.options[selectExamenScolaire.selectedIndex];
var nomExamenScolaire = selectedOptionExamenScolaire.textContent; // Récupère le nom pour l'afficher
if (nomExamenScolaire) {
    desagregations.push("Type d'examen scolaire: " + nomExamenScolaire);
}


var selectInfrastructureSanitaire = document.querySelector('select[name="nom_infrastructure_sanitaire"]');
var selectedOptionInfrastructureSanitaire = selectInfrastructureSanitaire.options[selectInfrastructureSanitaire.selectedIndex];
var nomInfrastructureSanitaire = selectedOptionInfrastructureSanitaire.textContent; // Récupère le nom pour l'afficher
if (nomInfrastructureSanitaire) {
    desagregations.push("Infrastructure sanitaire: " + nomInfrastructureSanitaire);
}



var selectLieuAccouchement = document.querySelector('select[name="nom_lieu_accouchement"]');
var selectedOptionLieuAccouchement = selectLieuAccouchement.options[selectLieuAccouchement.selectedIndex];
var nomLieuAccouchement = selectedOptionLieuAccouchement.textContent;  // Récupère le nom pour l'afficher
if (nomLieuAccouchement) {
    desagregations.push("Lieu d'accouchement: " + nomLieuAccouchement);
}

var selectEtatVaccinal = document.querySelector('select[name="nom_etat_vaccinal"]');
var selectedOptionEtatVaccinal = selectEtatVaccinal.options[selectEtatVaccinal.selectedIndex];
var nomEtatVaccinal = selectedOptionEtatVaccinal.textContent;  // Récupère le nom pour l'afficher
if (nomEtatVaccinal) {
    desagregations.push("État vaccinal: " + nomEtatVaccinal);
}


var selectTypeVaccination = document.querySelector('select[name="nom_type_vaccination"]');
var selectedOptionTypeVaccination = selectTypeVaccination.options[selectTypeVaccination.selectedIndex];
var nomTypeVaccination = selectedOptionTypeVaccination.textContent;  // Récupère le nom pour l'afficher
if (nomTypeVaccination) {
    desagregations.push("Type de vaccination: " + nomTypeVaccination);
}


var selectPathologie = document.querySelector('select[name="nom_pathologie"]');
var selectedOptionPathologie = selectPathologie.options[selectPathologie.selectedIndex];
var nomPathologie = selectedOptionPathologie.textContent;  // Récupère le nom pour l'afficher
if (nomPathologie) {
    desagregations.push("Pathologie: " + nomPathologie);
}


var selectTrancheAge = document.querySelector('select[name="nom_tranche_age"]');
var selectedOptionTrancheAge = selectTrancheAge.options[selectTrancheAge.selectedIndex];
var nomTrancheAge = selectedOptionTrancheAge.textContent;  // Récupère le nom pour l'afficher
if (nomTrancheAge) {
    desagregations.push("Tranche d'âge: " + nomTrancheAge);
}



var selectMaladiePEV = document.querySelector('select[name="nom_maladie_pev"]');
var selectedOptionMaladiePEV = selectMaladiePEV.options[selectMaladiePEV.selectedIndex];
var nomMaladiePEV = selectedOptionMaladiePEV.textContent;  // Récupère le nom pour l'afficher
if (nomMaladiePEV) {
    desagregations.push("Maladies du PEV: " + nomMaladiePEV);
}

var selectMaladieInfectieuse = document.querySelector('select[name="nom_maladie_infectieuse"]');
var selectedOptionMaladieInfectieuse = selectMaladieInfectieuse.options[selectMaladieInfectieuse.selectedIndex];
var nomMaladieInfectieuse = selectedOptionMaladieInfectieuse.textContent; // Récupère le nom pour l'afficher
if (nomMaladieInfectieuse) {
    desagregations.push("Maladies infectieuses: " + nomMaladieInfectieuse);
}


var selectInfectionRespiratoire = document.querySelector('select[name="nom_infection_respiratoire"]');
var selectedOptionInfectionRespiratoire = selectInfectionRespiratoire.options[selectInfectionRespiratoire.selectedIndex];
var nomInfectionRespiratoire = selectedOptionInfectionRespiratoire.textContent; // Récupère le nom pour l'afficher
if (nomInfectionRespiratoire) {
    desagregations.push("Infection respiratoire: " + nomInfectionRespiratoire);
}


var selectMaladiesIST = document.querySelector('select[name="nom_maladies_ist"]');
var selectedOptionMaladiesIST = selectMaladiesIST.options[selectMaladiesIST.selectedIndex];
var nomMaladiesIST = selectedOptionMaladiesIST.textContent; // Récupère le nom pour l'afficher
if (nomMaladiesIST) {
    desagregations.push("Maladies IST: " + nomMaladiesIST);
}


var selectTypeMaladies = document.querySelector('select[name="nom_type_maladies"]');
var selectedOptionTypeMaladies = selectTypeMaladies.options[selectTypeMaladies.selectedIndex];
var nomTypeMaladies = selectedOptionTypeMaladies.textContent; // Récupère le nom pour l'afficher
if (nomTypeMaladies) {
    desagregations.push("Type de maladies: " + nomTypeMaladies);
}


var selectActivitesIEC = document.querySelector('select[name="nom_activites_iec"]');
var selectedOptionActivitesIEC = selectActivitesIEC.options[selectActivitesIEC.selectedIndex];
var nomActivitesIEC = selectedOptionActivitesIEC.textContent; // Récupère le nom pour l'afficher
if (nomActivitesIEC) {
    desagregations.push("Activités IEC: " + nomActivitesIEC);
}


var selectServicesMedicaux = document.querySelector('select[name="nom_services_medicaux"]');
var selectedOptionServicesMedicaux = selectServicesMedicaux.options[selectServicesMedicaux.selectedIndex];
var nomServicesMedicaux = selectedOptionServicesMedicaux.textContent; // Récupère le nom pour l'afficher
if (nomServicesMedicaux) {
    desagregations.push("Services médicaux: " + nomServicesMedicaux);
}

var selectInfrastructureOrganisation = document.querySelector('select[name="nom_infrastructure_organisation"]');
var selectedOptionInfrastructureOrganisation = selectInfrastructureOrganisation.options[selectInfrastructureOrganisation.selectedIndex];
var nomInfrastructureOrganisation = selectedOptionInfrastructureOrganisation.textContent; // Récupère le nom pour l'afficher
if (nomInfrastructureOrganisation) {
    desagregations.push("Infrastructure/Organisation sportive: " + nomInfrastructureOrganisation);
}

var selectDisciplineSportive = document.querySelector('select[name="nom_discipline_sportive"]');
var selectedOptionDisciplineSportive = selectDisciplineSportive.options[selectDisciplineSportive.selectedIndex];
var nomDisciplineSportive = selectedOptionDisciplineSportive.textContent; // Récupère le nom pour l'afficher
if (nomDisciplineSportive) {
    desagregations.push("Discipline sportive: " + nomDisciplineSportive);
}

var selectInfrastructureCulturelle = document.querySelector('select[name="nom_type_infrastructure_culturel"]');
var selectedOptionInfrastructureCulturelle = selectInfrastructureCulturelle.options[selectInfrastructureCulturelle.selectedIndex];
var nomInfrastructureCulturelle = selectedOptionInfrastructureCulturelle.textContent; // Récupère le nom pour l'afficher
if (nomInfrastructureCulturelle) {
    desagregations.push("Type d'infrastructure culturelle: " + nomInfrastructureCulturelle);
}

var selectTypePatrimoineCulturel = document.querySelector('select[name="nom_type_patrimoine_culturel"]');
var selectedOptionTypePatrimoineCulturel = selectTypePatrimoineCulturel.options[selectTypePatrimoineCulturel.selectedIndex];
var nomTypePatrimoineCulturel = selectedOptionTypePatrimoineCulturel.textContent; // Récupère le nom pour l'afficher
if (nomTypePatrimoineCulturel) {
    desagregations.push("Type de patrimoine culturel: " + nomTypePatrimoineCulturel);
}

var selectTypeActionsCulturelles = document.querySelector('select[name="nom_type_actions_culturelles"]');
var selectedOptionTypeActionsCulturelles = selectTypeActionsCulturelles.options[selectTypeActionsCulturelles.selectedIndex];
var nomTypeActionsCulturelles = selectedOptionTypeActionsCulturelles.textContent; // Récupère le nom pour l'afficher
if (nomTypeActionsCulturelles) {
    desagregations.push("Type d'actions culturelles: " + nomTypeActionsCulturelles);
}


var selectTypeOperateurOeuvreEsprit = document.querySelector('select[name="nom_type_operateur_oeuvre_esprit"]');
var selectedOptionTypeOperateurOeuvreEsprit = selectTypeOperateurOeuvreEsprit.options[selectTypeOperateurOeuvreEsprit.selectedIndex];
var nomTypeOperateurOeuvreEsprit = selectedOptionTypeOperateurOeuvreEsprit.textContent; // Récupère le nom pour l'afficher
if (nomTypeOperateurOeuvreEsprit) {
    desagregations.push("Type d'opérateur d'œuvres de l'esprit: " + nomTypeOperateurOeuvreEsprit);
}

var selectTypeGroupeCulturel = document.querySelector('select[name="nom_type_de_groupe_culturel"]');
var selectedOptionTypeGroupeCulturel = selectTypeGroupeCulturel.options[selectTypeGroupeCulturel.selectedIndex];
var nomTypeGroupeCulturel = selectedOptionTypeGroupeCulturel.textContent; // Récupère le nom pour l'afficher
if (nomTypeGroupeCulturel) {
    desagregations.push("Type de groupe culturel: " + nomTypeGroupeCulturel);
}

var selectTypeManifestationCulturelle = document.querySelector('select[name="nom_type_de_manifestation_culturelle"]');
var selectedOptionTypeManifestationCulturelle = selectTypeManifestationCulturelle.options[selectTypeManifestationCulturelle.selectedIndex];
var nomTypeManifestationCulturelle = selectedOptionTypeManifestationCulturelle.textContent; // Récupère le nom pour l'afficher
if (nomTypeManifestationCulturelle) {
    desagregations.push("Type de manifestation culturelle: " + nomTypeManifestationCulturelle);
}


var selectTrimestre = document.querySelector('select[name="nom_trimestre"]');
var selectedOptionTrimestre = selectTrimestre.options[selectTrimestre.selectedIndex];
var nomTrimestre = selectedOptionTrimestre.textContent; // Récupère le nom pour l'afficher
if (nomTrimestre) {
    desagregations.push("Trimestre: " + nomTrimestre);
}

var selectEtatOeuvres = document.querySelector('select[name="nom_etat_des_oeuvres"]');
var selectedOptionEtatOeuvres = selectEtatOeuvres.options[selectEtatOeuvres.selectedIndex];
var nomEtatOeuvres = selectedOptionEtatOeuvres.textContent; // Récupère le nom pour l'afficher
if (nomEtatOeuvres) {
    desagregations.push("État des œuvres: " + nomEtatOeuvres);
}


var selectTypeAbonnement = document.querySelector('select[name="nom_type_abonnement"]');
var selectedOptionTypeAbonnement = selectTypeAbonnement.options[selectTypeAbonnement.selectedIndex];
var nomTypeAbonnement = selectedOptionTypeAbonnement.textContent; // Récupère le nom pour l'afficher
if (nomTypeAbonnement) {
    desagregations.push("Type d'abonnement: " + nomTypeAbonnement);
}


var selectTypeSuivi = document.querySelector('select[name="nom_type_de_suivi"]');
var selectedOptionTypeSuivi = selectTypeSuivi.options[selectTypeSuivi.selectedIndex];
var nomTypeSuivi = selectedOptionTypeSuivi.textContent; // Récupère le nom pour l'afficher
if (nomTypeSuivi) {
    desagregations.push("Type de suivi: " + nomTypeSuivi);
}


var selectTypeVulnerabilite = document.querySelector('select[name="nom_type_de_vulnerabilite"]');
var selectedOptionTypeVulnerabilite = selectTypeVulnerabilite.options[selectTypeVulnerabilite.selectedIndex];
var nomTypeVulnerabilite = selectedOptionTypeVulnerabilite.textContent; // Récupère le nom pour l'afficher
if (nomTypeVulnerabilite) {
    desagregations.push("Type de vulnérabilité: " + nomTypeVulnerabilite);
}


var selectTypePriseCharge = document.querySelector('select[name="nom_type_de_prise_charge"]');
var selectedOptionTypePriseCharge = selectTypePriseCharge.options[selectTypePriseCharge.selectedIndex];
var nomTypePriseCharge = selectedOptionTypePriseCharge.textContent; // Récupère le nom pour l'afficher
if (nomTypePriseCharge) {
    desagregations.push("Type de prise en charge: " + nomTypePriseCharge);
}


var selectNiveau = document.querySelector('select[name="nom_niveau"]');
var selectedOptionNiveau = selectNiveau.options[selectNiveau.selectedIndex];
var nomNiveau = selectedOptionNiveau.textContent; // Récupère le nom pour l'afficher
if (nomNiveau) {
    desagregations.push("Niveau: " + nomNiveau);
}
