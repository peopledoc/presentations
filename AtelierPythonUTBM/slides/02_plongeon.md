# Python de A à Z

.fx: title

---

## Exemple classique

Voici l'exemple classique du **Hello World** en python

# exemples/hello_world.py

    !python
    # -*- coding: utf-8 -*-
    
    print("Hello World !")
    
# Exécution

    !bash
    $ python hello_world.py
    Hello World !
    
---

## Jouons un peu avec python

Avant d'aller plus loin, nous allons jouer un peu avec l'interpréteur python.

# Lancer l'interpréteur en mode interactif

    !bash
    python
    
# Ou sinon

    !bash
    ipython

Il n'est pas nécessaire d'afficher le résultat d'appel aux fonctions quand on utilise l'interpréteur interactif, par exemple :

    !python
    >>> type(3)
    ... <type 'int'>
    
Le résultat attendu peut-être surprenant, mais la fonction type n'affiche rien du tout, c'est l'interpréteur qui l'affiche. (Ipython différencie les affichages normaux des retours fonction).

---

## Quelques fonctions utiles

Obtenir le type d'une variable :

#Type

    !python
    >>> type(3)
    ... <type 'int'>
    >>> type('')
    ... <type 'str'>
    >>> type(None)
    ... <type 'NoneType'>
    
Obtenir l'identifiant d'une variable :

#id

    !python
    >>> x = 4
    >>> y = 3
    >>> id(x)
    ... 4298185472
    >>> id(y)
    ... 4298185496

---

## Affectation

Comme dit auparavant, les variables ne sont pas déclarées avec un type. L'opérateur d'affectation est le très classique **=**.

# Exemple

    !python
    >>> x = 3
    
Comme expliqué auparavant, le type des variables est dynamique.

# Typage dynamique

    !python
    >>> type(x)
    ... <type 'int'>
    >>> x = 'chaine'
    >>> type(x)
    ... <type 'str'>

---

### Affectation
    
L'affectation multiple est possible en python :

# Affectation multiple

    !python
    >>> x, y = 0
    >>> x
    ... 0
    >>> y
    ... 0

# Extraire les parties d'un itérable

    !python
    >>> z = (1, 2) #Tuple de deux éléments
    >>> x, y = z
    >>> x
    ... 1
    >>> y
    ... 2
    
---

## Chaîne de caractères

En python, les chaînes de caractères sont représentés par des instances de la classe str.

    !python
    >>> x = ''
    >>> type(x)
    ... <type 'str'>
    >>> x = str()
    >>> type(x)
    ... <type 'str'>
    
La construction d'une chaîne est élémentaire (avec des **simples quotes** ou des **double quotes**):

    !python
    >>> x = 'string'
    
    
Il faut faire attention aux caractères spéciaux et les échapper au besoin :

    !python
    >>> x = 'j\'aime'

---

Pour pouvoir déclarer une chaîne sur plusieurs lignes, il faut tout simplement échapper le retour à la ligne

    !python
    >>> x = 'string sur plusieurs \
        lignes'
    >>> x
    ... 'string sur plusieurs lignes'
    
Vous pouvez aussi utiliser les **triples-quotes** (mais les sauts à la ligne ne sont pas supprimés) :

    !python
    >>> x = '''string sur plusieurs
        lignes'''
    >>> x
    ... 'string sur plusieurs\nlignes'
    
Les chaînes de caractères sont des objets itérables (on en reparlera plus tard).
    
---

## Opérations sur les chaînes

#Concaténation

    !python
    >>> 'abc' + 'cdf'
    ... 'abcdef'
    
#Création d'une chaîne à partir d'un itérable

    !python
    >>> ''.join(['1', '2', '3'])
    ... '123'
    >>> ','.join(['1', '2', '3'])
    ... '1,2,3'
    
# Chaîne standardisée

    !python
    >>> x = 'sTaNdArD'
    >>> x.capitalize()
    ... 'Standard'
    
Pour plus d'informations voir la documentation directement : [http://docs.python.org/library/stdtypes.html#string-methods](http://docs.python.org/library/stdtypes.html#string-methods).

---

## Formatage de chaîne

Python dispose d'un moyen simple de formater des chaînes de caractère à la manière de **sprintf** en C.

Pour plus d'informations, voir la documentation : [http://docs.python.org/library/stdtypes.html#string-formatting-operations](http://docs.python.org/library/stdtypes.html#string-formatting-operations).