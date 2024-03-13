# interactor.py

import os
import subprocess
import json

class ProjectInteractor:
    # Chemin du dossier principal
    principal_folder_path = None

    @staticmethod
    def create_principal_folder(folder_name):
        # Déterminer le chemin du bureau de l'utilisateur
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        # Créer le chemin complet du dossier principal
        ProjectInteractor.principal_folder_path = os.path.join(desktop_path, folder_name)
        # Créer le dossier
        os.makedirs(ProjectInteractor.principal_folder_path, exist_ok=True)
        print(f"Dossier principal '{folder_name}' créé sur le bureau.")

    @staticmethod
    def create_folder(folder_name):
        # Assurez-vous que le dossier est créé dans le dossier principal
        folder_path = os.path.join(ProjectInteractor.principal_folder_path, folder_name) if ProjectInteractor.principal_folder_path else folder_name
        os.makedirs(folder_path, exist_ok=True)
        print(f"Dossier '{folder_name}' créé dans le dossier principal.")

    @staticmethod
    def create_file(file_name, file_path, content=""):
        full_path = os.path.join(ProjectInteractor.principal_folder_path, file_path, file_name) if ProjectInteractor.principal_folder_path else os.path.join(file_path, file_name)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)  # Crée le chemin s'il n'existe pas
        with open(full_path, 'w') as file:
            file.write(content)
        print(f"Fichier '{file_name}' créé avec le contenu spécifié dans '{file_path}'.")



    @staticmethod
    def execute_command(command):
        subprocess.run(command, shell=True, check=True, cwd=os.getcwd())
        print(f"Commande '{command}' exécutée.")

    @staticmethod
    def write_code(file_path, line, code):
        # Assure que le chemin complet inclut le dossier principal si défini
        full_path = os.path.join(ProjectInteractor.principal_folder_path, file_path) if ProjectInteractor.principal_folder_path else file_path
    
        # Assure que le dossier contenant le fichier existe
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
        # Vérifie si le fichier existe, sinon le crée en ouvrant en mode 'a+' pour append (et lire, si nécessaire)
        # Puis ferme le fichier pour permettre son ouverture en mode 'r+' après
        if not os.path.exists(full_path):
            with open(full_path, 'a+') as file:
                pass  # Juste pour créer le fichier s'il n'existe pas
    
        # Maintenant, ouvre le fichier pour lire et écrire ('r+'), ce qui nécessite que le fichier existe
        with open(full_path, 'r+') as file:
            contents = file.readlines()
            # Convertit la ligne en entier pour éviter les problèmes de comparaison
            line = int(line)
            if line <= len(contents):
                contents.insert(line - 1, code + '\n')
            else:
                # Assure qu'il y a suffisamment de lignes dans le fichier pour l'insertion
                contents += ['\n'] * (line - len(contents) - 1) + [code + '\n']
        
            file.seek(0)
            file.writelines(contents)
    
        print(f"Code écrit dans '{full_path}' à la ligne {line}.")


    @staticmethod
    def ask_folder(folder_name):
        if os.path.exists(folder_name):
            contents = os.listdir(folder_name)
            print(json.dumps(contents))  # Affiche le contenu du dossier
        else:
            print("Dossier non trouvé.")

    @staticmethod
    def ask_structure(project_root="."):
        structure = []
        for root, dirs, files in os.walk(project_root, topdown=True):
            level = root.replace(project_root, '').count(os.sep)
            indent = ' ' * 4 * (level)
            structure.append(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                structure.append(f"{subindent}{f}")
        print("\n".join(structure))  # Affiche la structure du projet

    @staticmethod
    def process_instructions(instructions):
        for instruction_line in instructions.split('\n'):
            if not instruction_line.strip():
                continue  # Ignore les lignes vides

            # Gestion spéciale pour $write_code pour éviter de diviser le code qui peut contenir des espaces
            if '$write_code' in instruction_line:
                parts = instruction_line.split(' ', 3)
                command = parts[0]
                file_path = parts[1]
                line = parts[2]
                code = parts[3].strip('"')  # Supprime les guillemets optionnels autour du code
                ProjectInteractor.write_code(file_path, line, code)
            else:
                parts = instruction_line.split()
                command = parts[0]
                args = parts[1:]

                if command == '$create_principal_folder':
                    ProjectInteractor.create_principal_folder(*args)
                elif command == '$create_folder':
                    ProjectInteractor.create_folder(*args)
                elif command == '$create_file':
                    # Assurez-vous que args contient le nom du fichier, le chemin, et potentiellement le contenu
                    ProjectInteractor.create_file(*args)
                elif command == '$execute_command':
                    # Reconstituer la commande entière si elle était divisée
                    command_to_execute = ' '.join(args)
                    ProjectInteractor.execute_command(command_to_execute)
                elif command == '$ask_folder':
                    ProjectInteractor.ask_folder(*args)
                elif command == '$ask_structure':
                    ProjectInteractor.ask_structure()
                else:
                    print(f"Instruction non reconnue : {instruction_line}")

# Exemple d'utilisation
if __name__ == "__main__":
    instructions = """
    $create_folder test_folder
    $create_file test.txt test_folder "Ceci est un test."
    $execute_command echo Hello, world!
    $write_code test_folder/test.txt 1 "Nouvelle ligne de code."
    $ask_folder test_folder
    $ask_structure
    """
    ProjectInteractor.process_instructions(instructions)
