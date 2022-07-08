# pypdf2_structures

## Français

Dans la bibliothèque [PyPDF2](https://pypi.org/project/PyPDF2/), les pages et
les champs des fichiers PDF sont des structures d'objets complexes. Ce dépôt
permet d'écrire dans des fichers texte une représentation de ces structures.

Utilisez cette commande pour installer les dépendances du dépôt.

```bash
pip install -r requirements.txt
```

### La fonction `write_pdf_obj_struct`

Elle prend comme arguments une structure d'objets et un flux d'écriture de
fichier (mode `a`, `a+`, `r+`, `w` ou `w+`) pour produire une représentation
textuelle des objets. Un troisième paramètre permet de limiter la profondeur de
l'exploration de la structure. Quand la profondeur limite est atteinte, les
objets au-delà ne sont pas inclus dans le fichier de sortie. Toutefois, si
l'objet au niveau de profondeur suivant n'est ni un dictionnaire, une liste, un
*set* ni un tuple, il est inscrit dans le flux même si la limite est atteinte.

`PyPDF2` utilise des objets indirects (type `IndirectObject`) comme références
à des objets qui n'ont pas encore été chargés en mémoire. La fonction
`write_pdf_obj_struct` résout la première occurrence de chaque objet indirect
puis remplace les occurrences suivantes par l'identification de l'objet
indirect.

### Les scripts `write_field_objects` et `write_page_objects`

Ils écrivent respectivement la structure d'objets des champs et des pages d'un
fichier PDF à l'aide de `write_pdf_obj_struct`. Ces scripts ont les mêmes
paramètres. Pour les découvrir, utilisez les commandes ci-dessous.

```bash
python write_field_objects.py -h
```

```bash
python write_page_objects.py -h
```

## English

In library [PyPDF2](https://pypi.org/project/PyPDF2/), the pages and fields of
PDF files are complex object structures. This repository allows to write a
representation of those structures in text files.

Use this command to install the repository's dependencies.

```bash
pip install -r requirements.txt
```

### Function `write_pdf_obj_struct`

It takes an object structure and a file writing stream (mode `a`, `a+`, `r+`,
`w` ou `w+`) as arguments to make a text representation of the objets. A third
parameter allows to limit the depth of the structure's exploration. When the
depth limit is reached, the objects beyond are not included in the output file.
However, if the object at the next depth level is not a dictionary, a list, a
set or a tuple, it is written in the stream even though the limit is reached.

`PyPDF2` uses indirect objects (type `IndirectObject`) as references to objects
that have not been loaded in memory. Function `write_pdf_obj_struct`resolves
the first occurrence of each indirect object then replaces the next occurrences
with the indirect object's identification.

### Scripts `write_field_objects` and `write_page_objects`

They respectively write the object structure of a PDF file's fields and pages
with `write_pdf_obj_struct`. Those scripts have the same parameters. To
discover them, use the commands below.

```bash
python write_field_objects.py -h
```

```bash
python write_page_objects.py -h
```
