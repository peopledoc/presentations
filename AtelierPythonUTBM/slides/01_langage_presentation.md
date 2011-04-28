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

# Un peu de lecture

Voici quelques ouvrages qui vous seront sûrement utiles lors de votre apprentissage du langage :

* [La documentation officielle](http://docs.python.org/)
* [Dive into Python](http://diveintopython.org/)
* [Traduction française de **Dive into python**](http://diveintopython.adrahon.org/)