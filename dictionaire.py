# Dictionnaire pour mapper les niveaux de désagrégation aux fonctions correspondantes
import db_queries as ag
desagregation_functions = {
                "1": ag.get_groupe_age,
                "2": ag.get_sexes,
                "3": ag.get_niveau_primaire,
                "4":ag.get_cycle
                # Ajoutez ici d'autres mappings pour d'autres niveaux
            }

import config as cf

try:
  # Connect to the database
  conn = cf.create_connection()
  cursor = conn.cursor()

  # DELETE statement with comments explaining each part
  cursor.execute("""
    DELETE FROM ValeursIndicateurs
    WHERE Valeur = 2066 AND Annee=2066 ;
  """)

  # Commit the changes
  conn.commit()

except Exception as e:
  print(f"An error occurred: {e}")

finally:
  # Always close the cursor and connection, even if errors occur
  if cursor:
    cursor.close()
  if conn:
    conn.close()

print("Duplicate rows deleted successfully!")



