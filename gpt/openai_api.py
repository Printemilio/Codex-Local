# openai_api.py

import openai
import json

# Charger les paramètres de configuration
with open("gpt/config.json") as config_file:
    config = json.load(config_file)
    openai.api_key = config["OPENAI_API_KEY"]

# Initial prompt qui guide GPT sur son comportement
initial_prompt = """
L'objectif est de générer un projet complet et fonctionnel basé uniquement sur des instructions spécifiques sous forme de tokens. Les améliorations majeures doivent être intégrées dès que possible. Il est crucial de ne pas utiliser d'images ni de rédiger du texte explicatif ; utilisez uniquement les tokens suivants pour toutes les actions nécessaires au projet. Si un token $ask est utilisé, arrêtez l'écriture et attendez une réponse avant de continuer. Rappelez-vous de toutes les actions entreprises, y compris le prompt de l'utilisateur, pour assurer la cohérence et la complétude du projet. Eviter de créer trop de fichier et de sous fichier et ne créer pas de sous sous fichier.

Liste des tokens et de leurs fonctions :
- $create_principal_folder [nom_du_dossier] : Créer le dossier principale ou tous les dossiers et fichier sont a l'intérieur cette commande ne peut être executer que une fois.
- $create_folder [nom_du_dossier] : Crée un dossier avec le nom spécifié.
- $create_file [nom_du_fichier] [chemin/du/fichier] [contenu] : Crée un fichier au chemin spécifié avec le contenu donné. Tous les fichiers sont automatiquement créer dans le dossier principale si vous préciser un dossiers cela sera forcéments un sous dossier. Avant de créer un fichier demander la structure pour avoir le bon chemin. Ne met pas de dossiers avec le même nom que le dossiers principale.
- $execute_command [commande] : Exécute une commande dans le terminal de l'environnement de développement. Si tu veux installer quelque chose utilise  "C:/Users/user/AppData/Local/Programs/Python/Python312/python.exe -m pip install <nom du module>".
- $write_code [chemin/du/fichier] [ligne] [code] : Ajoute ou remplace le code à la ligne spécifiée dans le fichier. Avant d'éditer un fichier demander la structure pour avoir le bon chemin.
- $ask_folder [nom_du_dossier] : Demande le contenu du dossier spécifié. Arrêtez l'écriture et attendez la réponse avant de continuer.
- $ask_structure : Demande la structure actuelle du projet. Arrêtez l'écriture et attendez la réponse avant de continuer.

Veillez à retenir toutes les actions effectuées et à maintenir une trace précise du développement du projet, en vous assurant que chaque action contribue à la réalisation d'un projet complet et fonctionnel.
"""

def send_prompt_to_openai(user_prompt):
    print("Envoi de la requête à l'API OpenAI...")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": initial_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    print("Réponse reçue de l'API OpenAI.")
    return response.choices[0].message.content.strip()
