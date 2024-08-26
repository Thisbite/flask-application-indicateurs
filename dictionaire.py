from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

# Utiliser les variables d'environnement
host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database = 'mabase'
def create_connection2():
    try:
        # Connexion initiale sans spécifier la base de données
        initial_connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
        engine = create_engine(initial_connection_string)

        # Créer la base de données si elle n'existe pas
        with engine.connect() as conn:
            print(f"Base de données `{database}` créée ou déjà existante.")

        # Connexion à la base de données spécifiée
        connection_string_with_db = f"mysql+mysqlconnector://{user}:{password}@{host}/"
        engine_with_db = create_engine(connection_string_with_db)

        # Vérifier la connexion
        with engine_with_db.connect() as connection:
            print("Connexion à la base de données MySQL réussie avec la base spécifiée.")
            return engine_with_db

    except Exception as e:
        print(f"Erreur lors de la connexion à MySQL : {e}")
        return None
create_connection2()