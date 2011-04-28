# Python de A à M

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
