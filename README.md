# ReprRW

## Français

Cette bibliothèque écrit la représentation d'objets Python dans un fichier
texte et lit le fichier pour recréer les objets. Une représentation d'objet
est une chaîne de caractères renvoyée par la fonction `repr`.

La fonction `write_reprs` écrit la représentation d'objets Python dans un
fichier texte. Chaque ligne du fichier est une représentation d'objet. Si le
fichier spécifié existe déjà, cette fonction l'écrase.

La fonction `read_reprs` lit les fichiers texte qui contiennent des
représentations d'objet Python dans le but de recréer ces objets. Chaque ligne
doit être une représentation d'objet. Les lignes vides sont ignorées.

Consultez la documentation des fonctions et la démo dans le dépôt de code pour
plus d'informations.

## English

This library writes Python object representations in a text file and reads the
file to recreate the objects. An object representation is a string returned by
function `repr`.

Function `write_reprs` writes the representation of Python objects in a text
file. Each line in the file is an object representation. If the specified file
already exists, this function overwrites it.

Function `read_reprs` reads text files that contain the representation of
Python objetcs in order to recreate those objects. Each line must be an object
representation. Empty lines are ignored.

Consult the functions' documentation and the demo in the code repository for
the complete information.
