# OpenAI VSCode Project Generator

Ce projet automatise la création et la gestion de projets dans VSCode en utilisant OpenAI Codex. Basé sur un prompt utilisateur, il génère un projet complet avec des fichiers et des dossiers, et peut même exécuter des commandes spécifiques dans l'environnement de développement.

## Fonctionnalités

- Création automatique de dossiers et fichiers basée sur les instructions d'OpenAI Codex.
- Exécution de commandes dans le terminal de VSCode.
- Interface utilisateur simple avec barre de progression pour suivre l'exécution des instructions.

## Installation

Pour utiliser ce projet, suivez les étapes ci-dessous :

1. Clonez ce dépôt :

    git clone https://votre_repo.git

2. Installez les dépendances :

    pip install -r requirements.txt


## Configuration

1. Obtenez votre clé API OpenAI à [https://openai.com/](https://openai.com/) et ajoutez-la à un fichier `config.json` à la racine du projet :
```json
{
  "OPENAI_API_KEY": "votre_clé_api_ici"
}

Utilisation
Lancez le script principal :

python main.py

Suivez les instructions à l'écran pour entrer votre idée de projet. Le système générera automatiquement la structure du projet et exécutera les instructions nécessaires.

Contribution
Les contributions sont les bienvenues ! Pour contribuer, veuillez forker le dépôt, créer une branche avec vos modifications et soumettre une pull request.

Licence
MIT
