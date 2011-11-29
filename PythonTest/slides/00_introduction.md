# Faire des tests en Python

.fx: home

---

# Pourquoi faire des tests ?


* Avant tout pour maîtriser sa peur.
* À tout moment on peut lancer les tests pour se rassurer que le code marche toujours (ou pas :p).
* Mais aussi pour assurer la qualité du logiciel produit.

---

# Les tests en python

La librairie standard fournit une libraire de tests: **unittest**. L'api est très classique et très proche de l'api XUnit:

* assertEqual
* assertNotEqual
* assertTrue
* assertFalse
* assertRaises
* assertAlmostEqual

Les cas de test doivent hériter de **unittest.TestCase** et toute méthode commençant par test sera considéré comme un test.

Si le TestCase définit une méthode setUp, elle sera exécutée avant chaque test et sert à préparer l'environnement de test (DB, fichiers, instancier des objets).

Si le TestCase définit une méthode tearDown, elle sera exécutée après chaque test et sert à nettoyer l'environnement de test (effacer une DB).

---

# Exemple

	!python
	import random
	import unittest

	class TestSequenceFunctions(unittest.TestCase):

	    def setUp(self):
	        self.seq = range(10)

	    def test_shuffle(self):
	        # make sure the shuffled sequence does not lose any elements
	        random.shuffle(self.seq)
	        self.seq.sort()
	        self.assertEqual(self.seq, range(10))

	        # should raise an exception for an immutable sequence
	        self.assertRaises(TypeError, random.shuffle, (1,2,3))

	    def test_choice(self):
	        element = random.choice(self.seq)
	        self.assertTrue(element in self.seq)

	if __name__ == '__main__':
	    unittest.main()

---

# Python 2.7

Python 2.7 a vu arriver de nombreuses nouveautés dans unittest, en commençant par de nouvelles méthodes d'assertions:

* assertGreater / assertLess / assertGreaterEqual / assertLessEqual
* assertRegexpMatches(text, regexp) - verifies that regexp search matches text
* assertNotRegexpMatches(text, regexp)
* assertIn(value, sequence) / assertNotIn - assert membership in a container
* assertIs(first, second) / assertIsNot - assert identity
* assertIsNone / assertIsNotNone
* Et encore plus…

Les messages d'erreurs ont aussi étés grandement améliorés comme lors de la comparaison entre 2 strings qui montre maintenant la différence entre elles.

Ces nouveautés ont étés backportés dans les version 2.4, 2.5 et 2.6 de python dans le paquet <a href="http://www.voidspace.org.uk/python/articles/unittest2.shtml">unittest2</a>.

---

# Les nouveautés (assert_raises)

	!python
	# access the exception object
	with self.assertRaises(TypeError) as cm:
	    do_something()

	exception = cm.exception
	self.assertEqual(exception.error_code, 3)

---

# Les nouveautés (assert_equal)

	!python
	list1 = range(5)
	list2 = range(2, 7)
	self.assertEqual(list1, list2)

Sortie de l'exécution:

	!bash
	======================================================================
	FAIL: test (__main__.TestCase)
	----------------------------------------------------------------------
	Traceback (most recent call last):
	  File "sources/test_equal.py", line 7, in test
	    self.assertEqual(list1, list2)
	AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,... != [2, 3, 4, 5, 6, 7, 8, 9, 10, 1...

	First differing element 0:
	0
	2

	- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	?  ------

	+ [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
	?                                            ++++++++

---

# Test discovery

Unittest jusqu'à python-2.7 ne proposait pas de système de découverte automatique de test. Depuis il est possible d'utiliser la découverte de test en ligne de commande avec:

	python -m unittest discover

---

# Nose

Unittest est suffisant pour faire la plupart des tests mais le lancement des tests est un point noir quand l'on veut lancer rapidement certains tests . De plus nose fournit des fonctionalités intéressantes comme:

* Capture de la sortie standard et d'erreur par tests.
* Des plugins pour avoir le code coverage, un résumé des tests en XML (compatible Xunit) ou pour lancer le déboggeur sur un test en erreur.
* Une manière moins verbeuse d'écrire des tests.

---

# Exemple

	!python
	class Sample(object):

		def test(self, a, b, c):
			print "Divider", b - c
			return a / (b - c)

	import unittest

	class TestCase(unittest.TestCase):

		def test_first(self):
			self.assertEqual(Sample().test(1, 4, 2), 1/2)

		def test_second(self):
			self.assertEqual(Sample().test(0, 2, 1), 0)

		def test_third(self):
			self.assertEqual(Sample().test(4, 3, 3), None)

	if __name__ == '__main__':
		unittest.main()

---

# Exécution

* Exécution avec python:

	<pre>
	$ python test_output.py
	Divider 2
	.Divider 1
	.Divider 0
	E
	======================================================================
	ERROR: test_third (__main__.TestCase)
	\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
	Traceback (most recent call last):
	  File "test_output.py", line 18, in test_third
	    self.assertEqual(Sample().test(4, 3, 3), None)
	  File "test_output.py", line 5, in test
	    return a / (b - c)
	ZeroDivisionError: integer division or modulo by zero
	\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
	Ran 3 tests in 0.002s

	FAILED (errors=1)
	</pre>

---

* Exécution avec nosetests

	<pre>
	$ nosetests
	..E
	======================================================================
	ERROR: test_third (test_output.TestCase)
	\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
	Traceback (most recent call last):
	  File "/Users/lothiraldan/Labo/presentations/PythonTest/sources/test_output.py", line 18, in test_third
	    self.assertEqual(Sample().test(4, 3, 3), None)
	  File "/Users/lothiraldan/Labo/presentations/PythonTest/sources/test_output.py", line 5, in test
	    return a / (b - c)
	ZeroDivisionError: ZeroDivisionError: integer division or modulo by zero
	\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- >> begin captured stdout << \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
	Divider 0
	\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- >> end captured stdout << \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
	\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
	Ran 3 tests in 0.005s

	FAILED (errors=1)
	</pre>

---

# Écrire des tests avec nose

	!python
	EMAIL_REGEXP = r'[\S.]+@[\S.]+'

	def test_email_regexp():
	   # a regular e-mail address should match
	   assert re.match(EMAIL_REGEXP, 'test@nowhere.com')

	   # no domain should fail
	   assert not re.match(EMAIL_REGEXP, 'test@')

Sortie avec nosetests:

	!bash
	======================================================================
	FAIL: nose_example.test_email_regexp
	----------------------------------------------------------------------
	Traceback (most recent call last):
	  File "/Library/Python/2.5/site-packages/nose-1.1.2-py2.5.egg/nose/case.py", line 197, in runTest
	    self.test(*self.arg)
	  File "/Users/lothiraldan/Labo/presentations/PythonTest/sources/nose_example.py", line 13, in test_email_regexp
	    assert not re.match(EMAIL_REGEXP, 'test@nowhere')
	AssertionError

	----------------------------------------------------------------------
	Ran 1 test in 0.001s

	FAILED (failures=1)

---

# Des librairies intéressantes:

* Mock (http://www.voidspace.org.uk/python/mock/) : Vous permet de "Mocker" certaines parties de votre programme pour mieux isoler vos tests.
* Unittest templates (https://bitbucket.org/lothiraldan/unittest-templates) : Vous permet de réutiliser vos méthodes de tests pour tester plusieurs cas.
* Fusil (https://bitbucket.org/haypo/fusil/wiki/Home) : Outil de fuzzing écrit en python.
* Plus (Web testing, Gui testing) : http://pycheesecake.org/wiki/PythonTestingToolsTaxonomy