# Python : Programmation Procédurale et Orientée Objet

.fx: title

---

## Déclaration d'une fonction

La déclaration d'une fonction en python se fait avec le mot-clé **def** :

    !python
    >>> def bonjour():
    ...     print("Bonjour")
    ...
        
Ensuite on peut l'appeler directement avec le nom de la fonction :

    !python
    >>> bonjour()
    Bonjour
---

## Fonctions python

On peut noter que la fonction est définie par une variable du même nom :

    !python
    >>> bonjour
    <function bonjour at 0x101505668>
    
Et oui, en python tout est objet, même les fonctions ! Il est possible de donner un autre libellé à cette fonction et de l'appeler :

    !python
    >>> fonction = bonjour
    >>> fonction()
    Bonjour
    

---

## Modes de déclaration des paramètres

Il y a plusieurs manières de déclarer des paramètres dans une fonction.

# Paramètres par ordre

Ces paramètres devront être passés obligatoirement lors de l'appel à la fonction.

Déclaration :

    !python
    >>> def fonction(parametre):
    ...     print(parametre)
    ...
    
Appel :
    
    !python
    >>> fonction("Coucou")
    Coucou
    
Le fonctionnement est globalement le même que dans les autres langages.

---

### Modes de déclaration des paramètres

# Paramètres avec valeur par défaut

Il est aussi possible en python de déclarer des paramètres avec des valeurs par défaut. Les paramètres avec des valeurs par défaut doivent être définis après ceux sans valeur par défaut :

    !python
    >>> def fonction(arg1, arg2 = "value"):
    ...     print(arg1)
    ...     print(arg2)
    ...
    
Appel :

    !python
    >>> fonction("Coucou")
    Coucou
    value
    >>> fonction("Coucou", "C moi")
    Coucou
    C moi
    
---

### Passage de paramètre par noms

Le fonctionnement normal du passage de paramètre est la passage par **ordre** (première valeur -> premier paramètre, etc...). Il est possible de passer les paramètres par **noms**, par exemple :

    !python
    >>> def fonction(arg1, arg2, arg3 = "val3", arg4 = "val4"):
    ...     print((arg1, arg2, arg3, arg4))
    ...
    
On peut ainsi modifier l'ordre des paramètres lors de l'appel :

    !python
    >>> fonction("val1", "val2")
    ('val1', 'val2', 'val3', 'val4')
    >>> fonction(arg2 = "val1", arg1 = "val2")
    ('val2', 'val1', 'val3', 'val4')
    
On peut aussi renseigner l'un des paramètre ayant une valeur par défaut sans les autres :

    !python
    >>> fonction("val1", "val2", arg4 = "val42")
    ('val1', 'val2', 'val3', 'val42')

---

## Paramètres spéciaux **\*args** et **\*\*kwargs**

Il existe deux paramètres spéciaux que l'on peut utiliser : **\*args** et **\*\*kwargs**.

# *args

*args est un paramètre qui va récupérer toutes les valeurs passées par ordre **en plus**. Il doit être placé après les paramètres normaux et avant les paramètres avec valeurs par défaut. Le nom de la variable est args et son type est un tuple :

    !python
    >>> def fonction(*args):
    ...     print(args)
    ...
    
Appel :

    !python
    >>> fonction(1)
    (1,)
    >>> fonction(1, '2', (3, 4))
    (1, '2', (3, 4))

---

### Paramètres spécial **\*args**
   
Il est possible de le combiner avec des paramètres normaux :

    !python
    >>> def fonction(arg1, *args):
    ...     print((artg1, args))
    ...
    
Appel :

    !python
    >>> fonction(1)
    (1, ())
    >>> fonction(1, '2', (3, 4))
    (1, ('2', (3, 4)))

---

### Paramètre spécial **\*\*kwargs**

Le fonction du paramètre **kwargs est relativement le même, il contiendra tous les paramètres passés par noms. Le nom de la variable est kwargs et son type est un dictionnaire :

    !python
    >>> def fonction(**kwargs):
    ...     print(kwargs)
    ...
    
Appel :

    !python
    >>> fonction(arg1 = 1)
    {'arg1': 1}
    >>> fonction(arg1 = 1, arg2 = 2)
    {'arg1': 1, 'arg2': 2}    

---

## Générateurs

Traditionnellement, quand on veut retourner plusieurs valeurs, on créer une liste intermédiaire qu'on va remplir au fur et à mesure et on la retournera à la fin de la fonction.

Python propose une manière plus efficace de retourner plusieurs valeurs : les **générateurs**, l'idée c'est d'**envoyer** chaque valeur l'une après l'autre. L'intérêt ? On ne transmet que les valeurs, pas la structure de donnée et de plus on ne stocke pas la structure de donnée entière, cela résulte en une grosse économie de mémoire.

Pour **envoyer** une valeur, on va utiliser le mot clé **yield**, par exemple :

    !python
    >>> def test():
    ...     for i in xrange(10):
    ...         yield i
    ...
    >>> test()
    --- <generator object test at 0x1014eafa0>
    
Quand on utilise le mot-clé yield, la fonction retourne un objet *generator*, qui est itérable, que l'on peut donc convertir en liste :

    !python
    >>> list(test())
    --- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

---

### Générateurs

Étant donné que c'est un itérable, on peut donc le parcourir.

# Fonction normale

    !python
    >>> def test():
    ...     d = []
    ...     for i in xrange(3):
    ...         print("Calcul")
    ...         d.append(i*2)
    ...     return d
    ...
    
# Parcours du résultat de la fonction normale

    !python
    >>> for i in test():
    ...     print("Boucle")
    ...     x = i
    ...
    Calcul
    Calcul
    Calcul
    Boucle
    Boucle
    Boucle

---

### Générateurs

# Générateur

    !python
    >>> def test():
    ...     for i in xrange(3):
    ...         print("Calcul")
    ...         yield i
    ...
    
# Parcours du résultat du générateur

    !python
    >>> for i in test():
    ...     print("Boucle")
    ...     x = i
    ...
    Calcul
    Boucle
    Calcul
    Boucle
    Calcul
    Boucle

---

### Générateurs conclusion

En conclusion il est préférable d'utiliser les générateurs quand vous le pouvez dans vos fonctions et surtout d'utiliser les fonctions retournant des générateurs dès que possible. Par exemple, xrange retourne un générateur, range une liste. À titre de comparaison, voici les temps d'exécution nécessaire pour sommer la liste des 1 000 000 premiers entiers :

* sum(range(1000000)) : 55ms
* sum(xrange(1000000)) : 14.7 ms

---

## Créer une classe

---

## Constructeurs

---

## Méthodes

---

## Attributs de classe et d'instance

---

## Propriétés

---

## Héritage

---

## Surcharge d'opérateurs

---

## Méthodes spéciales

http://docs.python.org/reference/datamodel.html#special-method-names

---

## Méthodes de classes et d'instance