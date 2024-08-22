import secrets

secret_key = secrets.token_hex(32)  # Génère une clé de 64 caractères hexadécimaux
print(secret_key)
