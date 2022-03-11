import os, os.path as path

"""
Affiche des messages d'erreurs
"""
def error_exportation(*msg):
    raise Exception("Fonction elements.exporter - " + " ".join(msg))


"""
Importe un ensemble de elements en fonction du nom en paramètre. Les elements sont retournée sous le format :

[("element1", "reponse1"), ("element2", "reponse2"), ...]
"""
def importer(nom):
    elements = []
    file_path = path.join(os.getcwd(), nom)

    # Verifie que le fichier existe
    if not path.isfile(nom):
        print("Le fichier", file_path, "n'existe pas")
        return False
    
    # Lit le contenu
    file = open(file_path, "r")
    content = file.read().strip().split("\n")
    file.close()

    # Verifie le contenu du fichier. Retourne false si invalide
    if len(content) & 1 != 0:
        print("Le format du fichier est invalide")
        return False
    
    if len(content) == 0:
        print("Le fichier est vide")
        return False
    
    # Construit la liste des elements
    for i in range(len(content) // 2):
        elements.append((content[2 * i], content[2 * i + 1]))

    return elements

"""
Exporte des elements sous le nom donné en paramêtre. Les elements seront valider et doivent avoir le format suivant :

[("element1", "reponse1"), ("element2", "reponse2"), ...]

"""
def exporter(elements, nom):
    # Fait plusieurs vérifications sur les elements
    if type(elements) != list:
        error_exportation("Le paramètre element n'est pas une liste mais un:", str(type(elements)))

    if len(elements) == 0:
        error_exportation("La liste d'elements est vide")
        
    for q in elements:
        if len(q) != 2:
            error_exportation("Un des tuples dans le tableau de element a une grandeur plus grande ou plus petite que 2:", str(q))
        if type(q[0]) != str or type(q[1]) != str:
            error_exportation("Un des tuples dans le tableau de element ne possède pas de str comme valeur:", str(q))

    # Verifie si le fichier existe déja. Si oui, demande à l'utilisateur de valider la suppression du fichier
    file_path = path.join(os.getcwd(), nom)
    if path.exists(file_path):
        if path.isfile(file_path):
            r = ""
            while r != "oui":
                r = input("Attention, le fichier " + file_path + " existe déja. Si vous continuez, son contenu sera effacé. \nVoulez-vous vraiment continuez ?(oui/non)")
                if r == "non":
                    return False
        else:
            print("Un dossier du même nom existe.")
            return False

    # Écrit le contenu de l'element dans le fichier
    file = open(file_path, "w")
    for q in elements: 
        file.write(q[0] + "\n")
        file.write(q[1] + "\n")

    file.close()
    
    return True
