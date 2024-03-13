# main.py
import openai_api
from interactor import ProjectInteractor
from tqdm import tqdm
import time
import subprocess
import threading

def simulate_instruction_execution(instructions):
    for instruction in tqdm(instructions.split('\n'), desc="Exécution des instructions"):
        time.sleep(0.5)
        print(instruction)

def main():
    user_prompt = input("Entrez votre idée de projet : ")
    print(f"Idée de projet reçue : {user_prompt}")
    
    instructions = openai_api.send_prompt_to_openai(user_prompt)
    print("Instructions reçues de l'API OpenAI.")

    for instruction in instructions.split('\n'):
        if instruction.startswith('$ask'):
        
            message = instruction.split('"')[1] if '"' in instruction else instruction
            response = input(f"{message} (oui/non) : ")
            if response.lower() != 'oui':
                print("Opération annulée par l'utilisateur.")
                break
        else:
            print("Continuer avec l'opération...")
            # Ici, tu peux traiter les autres instructions normalement
            # Par exemple, utiliser ProjectInteractor pour exécuter l'instruction
            ProjectInteractor.process_instructions(instruction)

if __name__ == "__main__":
    main()
