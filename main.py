# coding=utf-8
import random
import elements


# affiches les elements du menu principal ainsi que le nombre d'elements
def enteteMenuPrincipal(elements):
    print(str(elements) + " élément(s)) Bonjour, veuillez choisir parmi les options suivante :")
    print("1 - Faire un test !")
    print("2 - Ajouter un élément")
    print("3 - Chercher un élément avec un mot-clé")
    print("4 - Afficher les éléments")
    print("5 - Exporter les éléments")
    print("6 - Importer des éléments")
    print("q - Quitter l'application")


# selectionne une question aleatoirement dans la banque de question
# la fonction prends liste d'elements en memoire comme parametre
def faireUnTest(element_en_memoire):
    banqueDeQuestion = []
    # copie les items dans la liste d'elements pour pouvoir supprimer les questions reussies
    for item in element_en_memoire:
        banqueDeQuestion.append(item)

    # choisi un index au hazard correspondant a un tuple de question et reponses
    element = random.randint(0, len(banqueDeQuestion) - 1)
    questionEtReponse = banqueDeQuestion[element]
    # separer les questions des reponses
    question = questionEtReponse[0]
    reponseAfficher = questionEtReponse[1]

    print("(écrire « stop  » pour revenir au menu principal)")
    reponse = input(question)

    while len(banqueDeQuestion) != 0 and reponse != "stop":
        print("La réponse est " + reponseAfficher)
        reussi = input("Avez-vous eu la réponse ? (oui/non)")
        # Demandes a l'utilisateur de entrer une valeur valide
        while reussi != "non" and reussi != "oui":
            print("Entree invalide")
            reussi = input("Avez-vous eu la réponse ? (oui/non)")
        # si la question est reussi elle est enlever de la banque de question
        if reussi == "oui":
            banqueDeQuestion.pop(element)
        # une autre question est choisi au hazard jusqua ce qu'il n y aie plus de question ou l'utilisateur ecrive stop
        if (len(banqueDeQuestion) != 0):
            element = random.randint(0, len(banqueDeQuestion) - 1)
            questionEtReponse = banqueDeQuestion[element]
            question = questionEtReponse[0]
            reponseAfficher = questionEtReponse[1]
            reponse = input(question)

    # si la banque est vide le message retourner au menu principal est ecrit
    if len(banqueDeQuestion) == 0:
        print("Il n'y a plus d'élément... retourner au menu principal")


# fonction pour ajouter un tuple a la liste
def ajouterUnElement(element_en_memoire):
    print("(écrire « stop  » pour revenir au menu principal)")
    print("Ajouter un élément")

    # l'utilisateur entre une question et une reponse
    question = input("Élement :")
    reponse = input("Réponse:")

    # si stop n'est pas ecrit alors l'element est ajouter avec la reponse dans la liste et l'utilsateur peut continuer d'enter des valuers
    while reponse != "stop" and question != "stop":
        questionEtReponse = (question, reponse)
        element_en_memoire.append(questionEtReponse)
        question = input("Élement :")
        if question == "stop":
            break
        reponse = input("Réponse : ")


# fonction pour effectuer la recherche d'un mot cle
def chercherUnElement(element_en_memoire):
    print("Mot-clé à chercher (stop pour arrêter la rechercher) :")

    motCle = input()
    question = []
    reponse = []
    # creer une liste de contenat uniquement des questions
    for item in element_en_memoire:
        question.append(item[0])
    # chercher tout les elements de list de question contenant le mot cle et les ajouter a une liste de reponse
    while motCle != "stop":
        for item in question:
            if motCle in item:
                reponse.append(item)
        # imprimer les elements dans la liste de reponse
        print("Éléments liées :")
        for item in reponse:
            print(item)
        reponse = []
        # l'utilsateur peut rechercher un autre mot cle ou enter stop pour arreter
        motCle = input("Mot-clé à chercher : ")


# fonction pour afficher les elements
def afficherLesElements(element_en_memoire):
    choix = input("Voulez-vous afficher les réponses ? (oui/non)")
    while choix != "non" and choix != "oui":
        print("Entree invalide")
        choix = input("Voulez-vous afficher les réponses ? (oui/non)")
    if choix == "oui":
        # afficher les questions et les reponses dans la liste 'elements en memoire
        for item in range(len(element_en_memoire)):
            print("Élément " + str(item + 1) + " : " + element_en_memoire[item][0])
            print("Réponse " + str(item + 1) + " : " + element_en_memoire[item][1])

    else:
        # afficher uniquement les questions
        for item in range(len(element_en_memoire)):
            print("Élément " + str(item + 1) + " : " + element_en_memoire[item][0])


# fonction pour exporter les elements
def exporterLesElements(element_en_memoire):
    # l'utilisateur entre le nom du fichier a exporter
    nom = input("Quel nom voulez-vous donner au fichier à sauvegarder ?")
    # exporter les elements
    importation_reussi = elements.exporter(element_en_memoire, nom)
    if importation_reussi:
        print("Les éléments ont été sauvegardées")
    else:
        print("une erreur est subvenue")


# fonction pour exporter les elements
def importerLesElements(element_en_memoire):
    fichier = input("De quel fichier voulez-vous prendre les questions ?")
    counter = 0
    # elements importer
    element = elements.importer(fichier)
    # ajouter les elements importer aux elements en memoire
    while not element:
        print("Entree invalide")
        fichier = input("De quel fichier voulez-vous prendre les questions ?")
        element = elements.importer(fichier)

    # ajouter les elements non-dupliques
    for item in element:
        if item not in element_en_memoire:
            element_en_memoire.append(item)
            counter += 1
    print(str(counter) + " éléments ont été ajoutées")


# menu principal
def MenuPrincipal(element_en_memoire):
    # l'utilisateur entre son choix parmis les options de l'entete et la fonction correspondante est appele
    choix = input()
    while choix != 'q':
        if choix == '1':
            faireUnTest(element_en_memoire)
        elif choix == '2':
            ajouterUnElement(element_en_memoire)
        elif choix == '3':
            chercherUnElement(element_en_memoire)
        elif choix == '4':
            afficherLesElements(element_en_memoire)
        elif choix == '5':
            exporterLesElements(element_en_memoire)
        elif choix == '6':
            importerLesElements(element_en_memoire)
        else:
            print("Entree invalide ")
        # une fois l'option terminer les functions ramenent l'utilisateur a la fonction du menu principal
        enteteMenuPrincipal(len(element_en_memoire))
        choix = input()


if __name__ == '__main__':
    element_en_memoire = []
    # l'entete est appele une seule fois dans le main
    enteteMenuPrincipal(len(element_en_memoire))
    # le menuprincipal est un boucle qui peut uniquement etre quitter en appuyant sur q lorsque demander
    MenuPrincipal(element_en_memoire)
