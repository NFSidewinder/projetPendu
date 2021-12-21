#-------------------------------------------------------------------------------
# Name:        clavier_azerty.py
#-------------------------------------------------------------------------------

import tkinter as tk


#   1/ Création d'un fenêtre de test
MyWindow = tk.Tk()
MyWindow.title('clavier test')
MyWindow.geometry("500x200")
"""         Lignes de code temporaires afin de tester le clavier dans une fenêtre
            Pour assembler le clavier avec le reste des éléments, on remplacera probablement
            MyWindow par un tk.Frame
"""

#   2/ Création de la fonction qui va récupérer la lettre du bouton pressé
def letter_key(letter):
    Lettre.set(Lettre.get() + str(letter))

Lettre = tk.StringVar()
"""         Lettre.set(Lettre.get + str(letter)) concatène la lettre pressée à l'instant avec les précédentes lettres pressées
            Si on écrit Lettre.set(str(letter)), la lettre pressée remplace la précédente lettre en mémoire
"""

#   3/ Création des rangées vides du clavier
Rangee = []
for i in range(3):
    Rangee.append(tk.Frame(MyWindow))
    Rangee[i].pack(side = tk.TOP)
"""         tk.Frame sert à créer un objet cadre dans un objet fenêtre/cadre où pourront être placés des widgets dans cet objet cadre
            Il est possible de créer des listes de cadres
            Pour positionner le clavier sur l'écran "Nouvelle Partie", on remplacera le MyWindow par un cadre
"""

#   4/ Création des boutons qui se trouvent sur les rangées du clavier
alphabet = [['A','Z','E','R','T','Y','U','I','O','P'],
['Q','S','D','F','G','H','J','K','L','M'],
['W','X','C','V','B','N','-',' ']]
Clavier = []
for i in range(len(alphabet)):
    temp = []
    for j in range(len(alphabet[i])):
        temp.append(tk.Button(Rangee[i], text = alphabet[i][j]))
    Clavier.append(temp)
"""         On crée une liste de widgets Button en fonction de la liste alphabet
            Procédé de création de la liste similaire à celle d'une matrice
"""

#   5/ Création des commandes qui sont associées à chaque bouton du clavier + placement et dimensionnement de ces boutons
for i in range(len(Clavier)):
    for j in range(len(Clavier[i])):
        Clavier[i][j].config(command=lambda i=i, j=j: [letter_key(Clavier[i][j]['text']), Clavier[i][j].config(state='disabled')])
        Clavier[i][j].pack(side = tk.LEFT, ipadx = 10, ipady = 10)
Clavier[-1][-1].pack(side = tk.LEFT, ipadx = 50, ipady = 10)
"""         .config sert à ajouter des options supplémentaires au widget
            (une option est entre parenthèses du widget - exemple : tk.Button(option_1, option_2,...)
            command=lambda est une fonction anonyme :
               - elle permet de relier le widget à une fonction avec des paramètres d'entrée - exemple : command=lambda: fonction(x) au lieu de command=fonction
               - elle permet de relier plusieurs fonctions en même temps au widget - exemple : command=lambda: [fonction_1(x), fonction_2,...]
            i=i, j=j nécessaires car sinon tous les boutons retournent le dernier caractère à la fin des itérations (ici on a Clavier[2][7]['text'] = caractère espace ' ')
            on relie .config(state='disabled') aux boutons avec une command afin de créer le changement d'état du bouton après le click
            on a donc un .config dans un .config
            si state=disabled est en option du premier .config à l'extérieur de command=lambda, le bouton est initialisé désactivé
"""

#   6/ Création du label test d'affichage des lettres
LabelLettre = tk.Label(MyWindow, textvariable = Lettre)
LabelLettre.pack(side = tk.BOTTOM, padx = 5, pady = 5)

MyWindow.mainloop()



"""     Sources et documentation

Explication du command=lambda
https://www.tutorialspoint.com/tkinter-button-commands-with-lambda-in-python

Explication sur comment désactiver un bouton après avoir cliqué dessus (command=lambda: Clavier[i][j].config(state='disabled'))
https://stackoverflow.com/questions/55326738/how-do-you-disable-a-button-when-it-is-clicked
https://stackoverflow.com/questions/20596892/disabling-buttons-after-click-in-tkinter

Explication sur comment récupérer le texte écrit sur un bouton (Clavier[i][j]['text'])
https://stackoverflow.com/questions/26765218/get-the-text-of-a-button-widget

Explication du i=i après command=lambda
https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments
"""