#-------------------------------------------------------------------------------
# Name:        menu_jouer.py
#-------------------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk
import contexte as ct

MyWindow = tk.Tk()
MyWindow.title("Nouvelle partie")
MyWindow.geometry("300x300")
MyWindow.resizable(width = False, height = False)

def parametres_get ():
    ParametreAffiche.set(str(VarDifficulte.get()) + ' ' + str(VarTheme.get()))
ParametreAffiche = tk.StringVar()

VarDifficulte = tk.IntVar()
VarDifficulte.set(1)
VarTheme = tk.StringVar()

MainCadre = tk.Frame(MyWindow)
MainCadre.pack(expand = 1)

LabelCadreDifficulte = tk.LabelFrame(MainCadre, text = 'Sélection de la difficulté')
LabelCadreDifficulte.pack(side = tk.TOP, anchor = 'w', fill = tk.X, padx = 10, pady = 10)

RBoutonDebutant = tk.Radiobutton(LabelCadreDifficulte, text = 'Facile', variable = VarDifficulte, value = 1)
RBoutonDebutant.pack(side = tk.TOP, anchor = 'w', padx = 5, pady = 5)
RBoutonIntermediaire = tk.Radiobutton(LabelCadreDifficulte, text = 'Intermédiaire', variable = VarDifficulte, value = 2)
RBoutonIntermediaire.pack(side = tk.TOP, anchor = 'w', padx = 5, pady = 5)
RBoutonExpert = tk.Radiobutton(LabelCadreDifficulte, text = 'Expert', variable = VarDifficulte, value = 3)
RBoutonExpert.pack(side = tk.TOP, anchor = 'w', padx = 5, pady = 5)


ThemeListe = ['Aléatoire', 'Capitales du monde', 'Sports', 'Métiers', 'Animaux', 'Nature']
LabelCadreTheme = tk.LabelFrame(MainCadre, text = 'Sélection du thème')
LabelCadreTheme.pack(side = tk.TOP, anchor = 'w', fill = tk.X, padx = 10, pady = 10)
LabelTheme = tk.Label(LabelCadreTheme, text = 'Choisir un thème')
LabelTheme.pack(side = tk.LEFT, anchor = 'w', padx = 5, pady = 5)
ComboTheme = ttk.Combobox(LabelCadreTheme, values = ThemeListe, textvariable = VarTheme, state = 'readonly')
ComboTheme.pack(side = tk.RIGHT, anchor = 'e', padx = 5, pady = 5)
ComboTheme.current(0)


CadreValider = tk.Frame(MainCadre)
CadreValider.pack(side = tk.BOTTOM)
BoutonDemarrer = ttk.Button(CadreValider, text = 'Démarrer', command = parametres_get)
BoutonDemarrer.pack(side = tk.LEFT, anchor = 'se', padx = 5, pady = 10)
BoutonRetour = ttk.Button(CadreValider, text = 'Retour', command = MainCadre.destroy)
BoutonRetour.pack(side = tk.RIGHT, anchor = 'se', padx = 5, pady = 10)

LabelTest = tk.Label(CadreValider, textvariable = ParametreAffiche)
LabelTest.pack(side = tk.TOP)

MainCadre.mainloop()



"""     Sources et documentation

Vérouiller la taille d'une fenêtre (.resizable(width = False, height = False))
https://stackoverflow.com/questions/21958534/how-can-i-prevent-a-window-from-being-resized-with-tkinter

Aligner des radioboutons sur la gauche (anchor = 'w')
https://stackoverflow.com/questions/43789073/tkinter-how-to-align-a-set-of-radio-buttons-that-differs-in-text-length

Récupérer la valeur d'une combobox
https://stackoverflow.com/questions/41522427/get-combobox-value-in-python

"""