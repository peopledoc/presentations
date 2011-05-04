# Python : les structures de données classiques

.fx: title

---

## Les itérables

En python, les itérables sont des conteneurs qui contiennent une collection d'autre objets et capable de retourner leurs membres un par un. Un itérator est un objet qui va permettre de parcourir la collection de parcourir un itérable. Les objets qui sont itérables sont :

* Les collections (tableau, ensemble, table de hachages)
* Les chaînes de caractère
* Les fichiers

L'intérêt des iterateurs est de fournir une méthode unique pour parcourir différent type de conteneurs et ainsi de pouvoir leur appliquer des algorithmes sans se soucier du type de conteneur traversé. Ainsi, vous pouvez créer des objets itérables (on le verra plus tard) et utiliser des fonctions déjà existantes dans python sans devoir les recoder. Par exemple, parcours simple, test d'appartenance, tri d'un conteneur (nécessite des méthodes de comparaison) ou somme des éléments d'un conteneur (nécessite la méthode d'addition).

---

### Parcours d'un itérable

Python fournit un moyen très simple pour parcourir un itérable :

    !python
    >>> x = [1, 2, 3]
    >>> for i in x:
    ...     print i
    ...
    1
    2
    3

#Création d'une chaîne à partir d'un itérable

    !python
    >>> ''.join(['1', '2', '3'])
    --- '123'
    >>> ','.join(['1', '2', '3'])
    --- '1,2,3'

---

## Slicing

---

## Les listes

---

## Les listes compréhensives

---

## Les tuples

---

## Les dictionnaires

---

## Les ensembles

---

## Les sets

---

## Les frozensets