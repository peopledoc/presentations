# Python : Les structures de contrôle classiques

.fx: title

---

## Conditions

---

## Les itérables

En python, les itérables sont des conteneurs qui contiennent une collection d'autre objets et capable de retourner leurs membres un par un. Un itérator est un objet qui va permettre de parcourir la collection de parcourir un itérable. Les objets qui sont itérables sont :

* Les collections (tableau, ensemble, table de hachages)
* Les chaînes de caractère
* Les fichiers
* Toute classe ayant une méthode **\_\_iter\_\_** renvoyant un objet respectant l'interface des **itérators**.

L'intérêt des iterateurs est de fournir une méthode unique pour parcourir différent type de conteneurs et ainsi de pouvoir leur appliquer des algorithmes sans se soucier du type de conteneur traversé. Ainsi, vous pouvez créer des objets itérables (on le verra plus tard) et utiliser des fonctions déjà existantes dans python sans devoir les recoder. Par exemple, parcours simple, tri d'un conteneur (nécessite des méthodes de comparaison), inversion d'un conteneur ou somme des éléments d'un conteneur (nécessite la méthode d'addition).

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
    
Comme les chaînes de caractères sont aussi des itérables, on peut les itérer de la même manière : 

    !python
    >>> x = 'Hello'
    >>> for i in x:
    ...     print i
    ...
    H
    e
    l
    l
    o
    
---

### Tri d'un itérable

De la même manière, python fournit par défaut une manière de trier un itérable (à condition d'avoir définit les méthodes de comparaison pour les objets contenus).

    !python
    >>> x = [1, 3, 2, 4]
    >>> sorted(x)
    --- [1, 2, 3, 4]
    
Comme auparavant, il est aussi possible de trier les chaînes de caractères :

    !python
    >>> x = 'hello world'
    >>> sorted(x)
    --- [' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
    
---

### Inversion d'un itérable

Dernier exemple, l'inversion d'un itérable. Attention la fonction **reversed** renvoie un objet peu lisible, à convertir en liste si on veut en avoir une représentation plus lisible :

    !python
    >>> x = [1, 2, 3, 4]
    >>> list(reversed(x))
    --- [4, 3, 2, 1]

L'exemple marche aussi avec les chaînes de caractères, mais on ne peut le convertir directement en string : 

    !python
    >>> x = 'hello world'
    >>> list(reversed(x))
    --- ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
    >>> str(reversed(x))
    --- '<reversed object at 0x101554c90>'
    
Comment faire dans ce cas ?

---

### Création d'une chaîne à partir d'un itérable

Il suffit de recréer une string à partir de l'itérable

# Exemples

    !python
    >>> ''.join(['1', '2', '3'])
    --- '123'
    >>> ','.join(['1', '2', '3'])
    --- '1,2,3'

# Solution

Ainsi dans l'exemple de la slide précédente, il suffit de faire :

    !python
    >>> ''.join(list(reversed('hello world')))
    --- 'dlrow olleh'
    
On peut même faire mieux :

    !python
    >>> ''.join(reversed('hello world'))
    --- 'dlrow olleh'
    
En effet la fonction reversed renvoi lui aussi un objet itérable.

---

## Les listes compréhensives

Les listes compréhensives sont un moyen de créer de manière concise des listes à partir d'autres itérables. Par exemple, si on veut obtenir la longueur des mots de la phrase "Je suis ici pour apprendre le python !" mais sans compter le mot "le". On peut réaliser celà avec le code suivant :

La notation est la suivante :

    !python
    phrase = "Je suis ici pour apprendre le python !"
    mots = phrase.split()
    longueurs = []
    for mot in mots:
        if mot != "le":
            longueurs.append(len(mot))
            
Les dernières lignes peuvent être raccourcies avec la notation suivante :

    !python
    longueurs = [len(mot) for mot in mots if mot != "le"]

---

## Exceptions

---

## Gestion des exceptions