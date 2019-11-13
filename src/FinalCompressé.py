# Ce fichier permet d'isoler les logins de personnes qui se sont connectées en dehors des heures de travail
# Il permet aussi d'établir une liste de suspects en croisant leur activité sur le réseau avec une liste d'ip suspectes

# On importe une collection
import collections

# On attribue une variable aux dossiers que l'on va utiliser
connexion = "/home/folken/Programmation/Python/Projet/connexion.log"    
user = "/home/folken/Programmation/Python/Projet/Utilisateurs.txt"      
warning = "/home/folken/Programmation/Python/Projet/warning.txt"        
inter = "/home/folken/Programmation/Python/Projet/inter.txt"
suspect = "/home/folken/Programmation/Python/Projet/suspect_final.txt"

# On créé plusieurs listes selon les besoins
liste_utilisateur = []  # Liste des utilisateurs
adresse_liste = []      # Liste des ip du fichier connexion
liste_heure = []        # Liste des heures du fichier connexion
warning_liste = []      # liste des ip du fichier warning
suspect_liste = []      # Liste des suspects

   
compteur = 0        # initialisation d'un compteur
suspect_map = {}    # initialisation d'une bibliothèque des suspects

# On ouvre le fichier connexion en lecture
with open(connexion, "r") as f:
    for donnee in f:
        adresse,login,time = donnee.split(";")    # On sépare les éléments en 3 blocs (ip/login/date-heure)
        liste_heure = donnee.split(" ")           # On récupère la liste des heures de connexion
        adresse_liste = adresse                    # un fichier a été créé

## On créé le fichier utilisateur en y inscrivant les logins des personnes
        with open(user, "a") as w:    
            w.write(login + "\n")
            

# impression uniquemement des ID et IP
        if liste_heure[1] <= str("07:59") or liste_heure[1] >= str("19:00"):
            print(liste_heure[1].strip("\n") + " " + login + " " + adresse)
print("Un fichier utilisateurs a été créé")

# On ouvre le fichier warning pour créér une liste qui va rajouter les ip à la suite
with open(warning, "r") as w:
    for ipwar in w:
        warning_liste.append(ipwar.strip())

# J'ouvre le fichier connexion en lecture et le fichier inter en écriture
# J'attribue une valeur à la liste_utilisateur en séparant les items par bloc
    with open(connexion, "r") as h:
        with open(inter, "w") as it:
            for ip in h:
                liste_utilisateur = ip.split(";")

# On compare les ip du fichier connexion à celle du fichier warning
# On créé un fichier qui liste les utilisateurs                
                if liste_utilisateur[0] in warning_liste:
                    it.write(liste_utilisateur[1] + "\n")

# On ouvre le fichier inter et on nettoie les données avec un strip
with open(inter, "r") as potentiel:
    for nom in potentiel:
        nom = nom.strip()
# On met dans la bibliothèque les noms des suspects
# On compte le nombre de fois où ces noms apparaissent et à chaque fois on augmente le compteur de 1              
        suspect_map[nom] = suspect_map.get(nom, 0) +1    
 
# On trie la bibliothèque par ordre lexicographique
# Item sert à isoler le couple clé-valeur
suspect_map = collections.OrderedDict(sorted(suspect_map.items()))

# On ouvre le fichier suspect en écriture afin d'y inscrire
# la liste des suspects et le nombre de fois où il sont se connectés
with open(suspect, "w") as s:
    for user, nb in suspect_map.items():
        s.write(user + ";" + str(nb) + "\n")    # Un fichier a été créé
print("Le fichier suspect a été créé")


