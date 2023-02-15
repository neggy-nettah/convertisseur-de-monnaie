from tkinter import *
from tkinter import ttk
import csv


# Création de la fenêtre principale de l'application
window = Tk()
window.title("Convertisseur De Monnaie")

# Création d'un label pour afficher "entre le montant :"
amount_label = Label(window, text="entre le montant :", font=("Arial", 23))
amount_label.pack()

# Création d'un champ d'entrée pour saisir le montant à convertir
amount_field = Entry(window, width=15, borderwidth=5, font=("Arial", 23))
amount_field.pack(padx=50, pady=20)

# Création d'un label pour afficher "De :"
from_label = Label(window, text="De :", font=("Arial", 23))
from_label.pack()

# Liste des devises disponibles dans le menu déroulant "De :"
from_currencies = ["USD", "EUR", "JPY", "GBP"]
# Création d'un menu déroulant pour sélectionner la devise "De :"
combo = ttk.Combobox(window, values=from_currencies, font=("Arial", 23))
combo.current(0)
combo.pack()

# Création d'un label pour afficher "Vers :"
to_label = Label(window, text="Vers :", font=("Arial", 23))
to_label.pack()

# Liste des devises disponibles dans le menu déroulant "Vers :"
to_currencies = ["USD", "EUR", "JPY", "GBP"]
# Création d'un menu déroulant pour sélectionner la devise "Vers :"
combo2 = ttk.Combobox(window, values=to_currencies, font=("Arial", 23))
combo2.current(0)
combo2.pack()

# Création d'un label pour afficher "Résultat :"
result_label = Label(window, text="Résultat :", font=("Arial", 23))
result_label.pack()

# Création d'une zone de texte pour afficher le résultat de la conversion
convert_field = Listbox(window, width=40, height=4)
convert_field.pack(padx=50, pady=20)

# Taux de change fixes pour effectuer les conversions
USD_TO_EUR = 0.92
USD_TO_JPY = 128.74
EUR_TO_JPY = 139.37
USD_TO_GBP = 0.80
EUR_TO_GBP = 0.87
JPY_TO_GBP = 0.0016

# Fonction pour vérifier si les devises sélectionnées sont différentes
def check_diff_currencies(from_currency, to_currency):
    if from_currency == to_currency:
        print("la conversion est impossible")
        return False
    return True

# Fonction pour calculer la conversion
def calculate_conversion(amount, from_currency, to_currency):
    if from_currency == 'USD':
        if to_currency == 'EUR':
            return amount * USD_TO_EUR
        elif to_currency == 'JPY':
            return amount * USD_TO_JPY
        elif to_currency == "GBP":
            return amount * USD_TO_GBP
    elif from_currency == 'EUR':
        if to_currency == 'USD':
            return amount / USD_TO_EUR
        elif to_currency == 'JPY':
            return amount * EUR_TO_JPY
        elif to_currency == 'GBP':
            return amount * EUR_TO_GBP
    elif from_currency == 'JPY':
        if to_currency == 'USD':
            return amount / USD_TO_JPY
        elif to_currency == 'EUR':
            return amount / EUR_TO_JPY
        elif to_currency == 'GBP':
            return amount * JPY_TO_GBP
    elif from_currency == 'GBP':
        if to_currency == 'EUR':
            return amount / EUR_TO_GBP
        elif to_currency == 'JPY':
            return amount / JPY_TO_GBP
        elif to_currency == "USD":
            return amount / USD_TO_GBP

# Fonction appelée lorsque le bouton "Convertir" est cliqué
def on_convert_clicked():
    # Récupération de la valeur saisie dans le champ "Montant"
    amount = float(amount_field.get())
    # Récupération de la devise sélectionnée dans le menu déroulant "De :"
    from_currency = combo.get()
    # Récupération de la devise sélectionnée dans le menu déroulant "Vers :"
    to_currency = combo2.get()
    # Vérification que les devises sélectionnées sont différentes
    if check_diff_currencies(from_currency, to_currency):
        result = calculate_conversion(amount, from_currency, to_currency)
        convert_field.delete(0, END)
        convert_field.insert(0, result)

    # Enregistrement de la conversion dans un fichier CSV
    with open("historique.csv", 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([amount, from_currency, " = ",  result, to_currency])

# Création du bouton "Convertir"
convert_button = Button(window, text="Convertir", borderwidth=5, bg='green', font=("Arial", 23), command=on_convert_clicked)
convert_button.pack()

# Lancement de la fenêtre principale de l'application
window.mainloop()
