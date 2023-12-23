# project4py-ocr
projet4py-ocr est un projet de formation développeur Python de chez OpenClassrooms. Il consiste à lancer un jeu d'échecs codé en langage Python.

## Etape 1 : Cloner le projet.
Premièrement,il faut cloner le projet en faisant la commande 

```bash
git clone https://github.com/MentalDeFer972/project4py-ocr
```


 sur le Terminal(sur Mac/Linux)/invite de commandes(sur Windows),ensuite ouvrir ce projet avec Visual Studio Code ou PyCharm,sur Windows/Mac/Linux.

## Etape 2 : Créer et activer l'environnement virtuel.
Deuxièment,il faut créer l'environnement virtuel en faisant la commande 


```bash
ls project4py-ocr

# create virtual environment
python -m venv env

cd env/Scripts/
# activate venv 
activate.bat
```


## Etape 3 : Installer les modules avec le fichier "requirements.txt"
Et enfin,pour installer les modules Python,il faut faire la commande 
```bash
pip install -r requirements.txt
```
dans l'environnement virtuel du projet.

## Etape 4 : Exécuter ce projet.
Sur l'invite de commandes (Windows) ou le Terminal(Mac/Linux),lancer la commande 

```bash 
python main.py
```

Vous pouvez aussi le lancer à traver Visual Studio Code ou PyCharm.

Et voilà! Vous avez lancé le projet.

## Informations importantes
Il faut lancer la commande suivante:

```bash
cd src
flake8 --format=html --htmldir=flake-report
```

Le rapport flake8-html est situé dans le dossier /src/flake-report/index.html 
