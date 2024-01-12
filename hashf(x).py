#XXXVIMMXVIII

import hashlib

def lobi_eko_leka_lelo(message):
    sha256 = hashlib.sha256()
    message_bytes = message.encode('utf-8')
    sha256.update(message_bytes)
    hash_value = sha256.hexdigest()
    return hash_value

def main():
    phrases = []
    nb_phrases = int(input("Veuillez entrer le nombre de phrases à traiter ! "))

    # Demande à l'utilisateur combien de phrases il souhaite hasher
    # et enregistre le nombre dans la variable nb_phrases

    for i in range(nb_phrases):
        phrase = input("Ecrivez la phrase {} : ".format(i+1))
        phrases.append(phrase)

    # Demande à l'utilisateur d'entrer chaque phrase et les ajoute
    # à la liste phrases

    print("\nhash Done :")
    for i, phrase in enumerate(phrases):
        hash_value = lobi_eko_leka_lelo(phrase)
        print("Phrase {}: {}".format(i+1, hash_value))

    # Effectue le hachage pour chaque phrase de la liste phrases
    # et affiche le résultat du hachage avec le numéro de phrase correspondant

if __name__ == "__main__":
    main()
