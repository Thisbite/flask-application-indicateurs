import config as cf 
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import logging
import config as cf
import db_queries as ag
from models import Agent,Administrateur,Superviseur
from flask import request, jsonify

#Effectif de la population 
import pandas as pd
from flask import flash



def test_import(df):
    conn = cf.create_connection()
    cursor = conn.cursor()

    # Insérer les données dans la base
    for _, row in df.iterrows():
        id=cf.generate_unique_key()
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
                id,nom_region, nom_departement, nom_sousprefecture, sexe, groupe_age, age, Valeur, Annee
            ) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (id,region, departement, sous_prefecture, sexe, groupe_age, age, valeur, annee))

    conn.commit()
    return jsonify({'message': 'Données insérées avec succès.'}), 200



















#Effectif de la population
def indicateur_effectif_1001(file, cursor):
    try:
        # Charger toutes les feuilles du fichier Excel
        xls = pd.ExcelFile(file)

        # Vérifier la présence de la feuille "Effectif de la population-1001"
        if "Effectif de la population-1001" not in xls.sheet_names:
            print("Le fichier ne contient pas la feuille 'Effectif de la population-1001'.")
            return False

        # Lire la feuille "Effectif de la population-1001"
        df = pd.read_excel(xls, sheet_name="Effectif de la population-1001")

        # Vérifier la présence des colonnes requises
        required_columns = ['Région', 'Département', 'Sous-prefecture', 'Sexe', 'Groupe d\'age', 'Age', 'Valeur', 'Annee']
        if not all(col in df.columns for col in required_columns):
            print("Certaines colonnes requises sont manquantes dans la feuille.")
            return False

        # Filtrer uniquement les colonnes nécessaires
        df_filtered = df[required_columns]

        # Insertion dans la base de données
        for _, row in df_filtered.iterrows():
            sql = """
            INSERT INTO valeur_indicateur_libelle (
                nom_region, nom_departement, nom_sousprefecture, sexe, groupe_age, age, Valeur, Annee
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                row['Région'], row['Département'], row['Sous-prefecture'], row['Sexe'], 
                row['Groupe d\'age'], row['Age'], row['Valeur'], row['Annee']
            )
            cursor.execute(sql, data)

        return True  # Indique que l'insertion a réussi

    except Exception as e:
        print("Erreur ")
        return False

def indicateur_effectif_1002(file):
    pass
def indicateur_effectif_1003(file):
    pass
def indicateur_effectif_1004(file):
    pass
def indicateur_effectif_1005(file):
    pass
def indicateur_effectif_1006(file):
    pass
def indicateur_effectif_1007(file):
    pass
def indicateur_effectif_1008(file):
    pass
def indicateur_effectif_1009(file):
    pass
def indicateur_effectif_1010(file):
    pass
def indicateur_effectif_1011(file):
    pass
def indicateur_effectif_1012(file):
    pass
def indicateur_effectif_1013(file):
    pass
def indicateur_effectif_1015(file):
    pass