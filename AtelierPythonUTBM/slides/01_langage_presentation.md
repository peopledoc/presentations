# Caractéristiques de *Python*

.fx: title

---

## Forces de python

.fx: bigbullet

* Portable.
* Gratuit.
* Syntaxe simple -> Facile à apprendre.
* **Garbage collector** included.
* Extensible.
* **Batteries included**.
* Gestion des exceptions.

---

## Syntaxe python

La syntaxe python est très simple, très concise et impose d'utiliser l'indentation des lignes de code ce qui rend les programmes plus faciles à lire.

# Exemple

    !python
    if True:
        print("Condition is true")
    
    print("Outside condition")

---

## Implémentations de python

Il existe plusieurs implémentations de python qui permettent d'étendre le langage avec des librairies dans d'autres langages :

* CPython : L'interpréteur de référence de python. Il génère du byte-code python (fichier *.pyc) et est écrit en C; il permet d'étendre le langage avec des librairies C.
* Jython : Interpréteur qui permet de coupler du python et du java dans le même programme, génère du byte-code JAVA.
* IronPython : Implémentation de python qui vise .Net et Mono, permet de coupler python avec le framework .Net.
* Pypy : Implémentation de Python en Python; projet de recherche pour obtenir une implémentation plus rapide que l'implémentation de référence (CPython).

---

## Typage des données Python

Python est un langage à typage fort dynamique.

# Typage Fort

> Un langage est fortement typé si :

>   1) La compilation ou l'exécution peuvent détecter des erreurs de typage. Si ces erreurs ne sont jamais reconnues, le langage est faiblement typé (c'est, par exemple, le cas de PHP).
   
>   2) Les conversions implicites de types sont formellement interdites. Si de telles conversions sont possibles, le langage est faiblement typé. Exemples répondant à ce critère : OCaml, Haskell.
   
<p class="cite">— <a href="http://fr.wikipedia.org/wiki/Typage_fort">Wikipedia</a></p>

---

### Typage dynamique

> Un langage est typé dynamiquement si la déclaration des variables se fait sans spécifier le type.

<p class="cite">— <a href="http://fr.wikipedia.org/wiki/Typage_dynamique">Wikipedia</a></p>

---

## Python : un langage Objet

Python est avant tout un langage objet, même si il permet d'utiliser d'autres paradigmes que la **programmation orientée objet**, au final on ne manipule que des objets en Python (C'est très important et on le reverra plus tard.).

---

### Zen python


> Beautiful is better than ugly.

> Explicit is better than implicit.

> Simple is better than complex.

> Complex is better than complicated.

> Flat is better than nested.

> Sparse is better than dense.

> Readability counts.

> Special cases aren't special enough to break the rules.

---

### Zen python

> Although practicality beats purity.

> Errors should never pass silently.

> Unless explicitly silenced.

> In the face of ambiguity, refuse the temptation to guess.

> There should be one-- and preferably only one --obvious way to do it.

> Although that way may not be obvious at first unless you're Dutch.

> Now is better than never.

---

### Zen python

> Although never is often better than *right* now.

> If the implementation is hard to explain, it's a bad idea.

> If the implementation is easy to explain, it may be a good idea.

> Namespaces are one honking great idea -- let's do more of those!


<p class="cite">- The Zen of Python, by Tim Peters</p>

    !python
    >>> import this

---

# Un peu de lecture

Voici quelques ouvrages qui vous seront sûrement utiles lors de votre apprentissage du langage :

* [La documentation officielle](http://docs.python.org/)
* [Dive into Python](http://diveintopython.org/)
* [Traduction française de **Dive into python**](http://diveintopython.adrahon.org/)