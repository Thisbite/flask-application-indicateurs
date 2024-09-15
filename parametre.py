# Créez un dictionnaire pour les configurations spécifiques à chaque id_indicateur
indicateur_config = {
    '1001': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_groupe_age': True,
        'fetch_age':True,
        'niveau_choix': {'1': 'Sexe', '2': 'Groupe Age', '3': 'Âge'}
    },
    '1002': {
        'fetch_indicateur': True,
        'fetch_sexe': False,
        'fetch_groupe_age': True,
        'niveau_choix': {'2': 'Groupe Age', '3': 'Âge'}
    },
    '1003': {
        'fetch_indicateur': True,
        'fetch_sexe': False,
        'fetch_groupe_age': False,
        'niveau_choix': {}
    },
    '1004': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_groupe_age': False,
        'niveau_choix': {1: 'Sexe'}
    },
    '1005': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_groupe_age': False,
        'niveau_choix': {1: 'Sexe'}
    },
    '1006': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_groupe_age': False,
        'niveau_choix': {1: 'Sexe'}
    },
    '1007': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_groupe_age': False,
        'niveau_choix': {1: 'Sexe'}
    },
    '1008': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_groupe_age': False,
        'niveau_choix': {1: 'Sexe'}
    },
    '1009': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'niveau_choix': {1: 'Sexe'}
    },
    '1010': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_groupe_age': False,
        'niveau_choix': {1: 'Sexe'}
    },
    '1011': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_groupe_age': False,
        'niveau_choix': {1: 'Sexe'}
    },
    '1012': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_groupe_age': False,
        'niveau_choix': {1: 'Sexe'}
    },
    '1013': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_groupe_age': True,
        'niveau_choix': {1: 'Sexe'}
    },
    '1014': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_groupe_age': True,
        'niveau_choix': {1: 'Sexe'}
    },
    '1016': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_groupe_age': True,
        'niveau_choix': {1: 'Sexe'}
    },
    
    '2001': {
        'fetch_indicateur': True,
        'fetch_sexe': True,
        'fetch_cycle_scolaire':True,
        
        'niveau_choix': {1: 'Sexe',11:'Cycle'}
    }
}




#Cette liste permet de suivre le choix de l'agent et le niveau de desagregation
lists={
"1":"Sexe-list1",
"2":"Groupe-list2",
"3":"ages-list3",
"4":"Type-list4",
"5":"Source-list5",
"6":"Délai-list6",
"7":"Statut-list7",
"8":"Type-list8",
"9":"Type-list9",
"10":"Statut-list10",
"11":"Cycle-list11",
"12":"Niveau-list12",
"13":"Niveau-list13",
"14":"Niveau-list14",
"15":"Niveau-list15",
"16":"Niveau-list16",
"17":"Niveau-list17",
"18":"Niveau-list18",
"19":"Type-list19",
"20":"Commodités-list20",
"21":"Catégorie-list21",
"22":"Catégorie-list22",
"23":"Grade-list23",
"24":"Groupe-list24",
"25":"Lieu-list25",
"26":"Etat-list26",
"27":"Types-list27",
"28":"Pathologie-list28",
"29":"Tranche-list29",
"30":"Maladies-list30",
"31":"Maladies-list31",
"32":"Infections-list32",
"33":"Maladies-list33",
"34":"Type-list34",
"35":"Activités-list35",
"36":"Service-list36",
"37":"Types-list37",
"38":"Types-list38",
"39":"Type-list39",
"40":"Types-list40",
"41":"Types-list41",
"42":"Types-list42",
"43":"Niveau-list43",
"44":"Type-list44",
"45":"Trimestre-list45",
"46":"Type-list46",
"47":"Disciplines-list47",
"48":"Type-list48",
"49":"Type-list49",
"50":"Type-list50",
"51":"Type-list51",
"52":"Type-list52",
"53":"Type-list53",
"54":"Type-list54",
"55":"Type-list55",
"56":"type-list56",
"57":"type-list57",
"58":"type-list58",
"59":"type-list59",
"60":"Espèces-list60",
"61":"Type-list61",
"62":"Type-list62",
"63":"Produits-list63",
"64":"Type-list64",
"65":"Type-list65",
"66":"Type-list66",
"67":"Type-list67",
"68":"Type-list68",
"69":"Type-list69",
"70":"Etat-list70",
"71":"Type-list71",
"72":"Type-list72",
"73":"Types-list73",
"74":"Catégories-list74",
"75":"Type-list75",
"76":"Type-list76",
"77":"catégories-list77",
"78":"Compagnies-list78",
"79":"Type-list79",
"80":"type-list80",
"81":"nature-list81",
"82":"Catégorie-list82",
"83":"Nature-list83",
"84":"Nationalité-list84",
"85":"Secteur-list85",
"86":"Collectivités-list86",
"87":"Secteurs-list87",
"88":"Régime-list88",
"89":"Forme-list89",
"90":"Type-list90",
"91":"Type-list91",
"92":"Secteurs-list92",
"93":"Types-list93",
"94":"Types-list94",
"95":"Produits-list95",
"96":"Domaines-list96",
"97":"Espèces-list97",
"98":"Mois-list98",
"99":"Directions-list99",
"100":"Milieu-list100",
"101":"Situation-list101",
"102":"Branche-list102",
"103":"Secteur-list103",
"104":"Catégories-list104",
"105":"Secteur-list105",
"106":"Projets-list106",
"107":"Mois-list107",
"108":"Groupe-list108",
"109":"Type-list109",
"110":"Activités-list110",
"111":"Activités-list111",
"112":"Type-list112",
"113":"Nature-list113",
"114":"Niveau-list114",
"115":"Types-list115",
"116":"Types-list116",
"117":"Types-list117",
"118":"Type-list118",
"119":"Nature-list119",
"120":"Type-list120",
"121":"Type-list121",
"122":"Type-list122",
"123":"Type-list123",
"124":"Type-list124",
"125":"Type-list125",
"126":"Type-list126",
"127":"Parti-list127",
"129":"Mairies-list128"
}


#Cette permet la vue des champs

lists_all=[
"Sexe-list1",
"Groupe-list2",
"ages-list3",
"Type-list4",
"Source-list5",
"Délai-list6",
"Statut-list7",
"Type-list8",
"Type-list9",
"Statut-list10",
"Cycle-list11",
"Niveau-list12",
"Niveau-list13",
"Niveau-list14",
"Niveau-list15",
"Niveau-list16",
"Niveau-list17",
"Niveau-list18",
"Type-list19",
"Commodités-list20",
"Catégorie-list21",
"Catégorie-list22",
"Grade-list23",
"Groupe-list24",
"Lieu-list25",
"Etat-list26",
"Types-list27",
"Pathologie-list28",
"Tranche-list29",
"Maladies-list30",
"Maladies-list31",
"Infections-list32",
"Maladies-list33",
"Type-list34",
"Activités-list35",
"Service-list36",
"Types-list37",
"Types-list38",
"Type-list39",
"Types-list40",
"Types-list41",
"Types-list42",
"Niveau-list43",
"Type-list44",
"Trimestre-list45",
"Type-list46",
"Disciplines-list47",
"Type-list48",
"Type-list49",
"Type-list50",
"Type-list51",
"Type-list52",
"Type-list53",
"Type-list54",
"Type-list55",
"type-list56",
"type-list57",
"type-list58",
"type-list59",
"Espèces-list60",
"Type-list61",
"Type-list62",
"Produits-list63",
"Type-list64",
"Type-list65",
"Type-list66",
"Type-list67",
"Type-list68",
"Type-list69",
"Etat-list70",
"Type-list71",
"Type-list72",
"Types-list73",
"Catégories-list74",
"Type-list75",
"Type-list76",
"catégories-list77",
"Compagnies-list78",
"Type-list79",
"type-list80",
"nature-list81",
"Catégorie-list82",
"Nature-list83",
"Nationalité-list84",
"Secteur-list85",
"Collectivités-list86",
"Secteurs-list87",
"Régime-list88",
"Forme-list89",
"Type-list90",
"Type-list91",
"Secteurs-list92",
"Types-list93",
"Types-list94",
"Produits-list95",
"Domaines-list96",
"Espèces-list97",
"Mois-list98",
"Directions-list99",
"Milieu-list100",
"Situation-list101",
"Branche-list102",
"Secteur-list103",
"Catégories-list104",
"Secteur-list105",
"Projets-list106",
"Mois-list107",
"Groupe-list108",
"Type-list109",
"Activités-list110",
"Activités-list111",
"Type-list112",
"Nature-list113",
"Niveau-list114",
"Types-list115",
"Types-list116",
"Types-list117",
"Type-list118",
"Nature-list119",
"Type-list120",
"Type-list121",
"Type-list122",
"Type-list123",
"Type-list124",
"Type-list125",
"Type-list126",
"Parti-list127",
"Mairies-list128",
]
