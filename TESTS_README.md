# Guide des Tests Automatisés / Automated Tests Guide

## Vue d'ensemble / Overview

Ce projet inclut maintenant une suite complète de tests automatisés pour valider le comportement du simulateur de combat.

This project now includes a comprehensive automated test suite to validate the battle simulator behavior.

## Structure des Tests / Test Structure

Les tests sont organisés par fichier selon les composants qu'ils testent:

Tests are organized by file according to the components they test:

- `test_character.py` - Tests pour la classe de base Character
- `test_soldier.py` - Tests pour la classe Soldier
- `test_mage.py` - Tests pour la classe Mage
- `test_elf.py` - Tests pour la classe Elf
- `test_king.py` - Tests pour la classe King
- `test_main.py` - Tests pour les fonctions principales et type_map
- `run_tests.py` - Script de lancement des tests

## Exécuter les Tests / Running Tests

### Tous les tests / All tests

Pour exécuter tous les tests:

To run all tests:

```bash
python3 run_tests.py
```

### Tests spécifiques / Specific tests

Pour exécuter un fichier de test spécifique:

To run a specific test file:

```bash
python3 run_tests.py test_character
python3 run_tests.py test_soldier
python3 run_tests.py test_mage
python3 run_tests.py test_elf
python3 run_tests.py test_king
python3 run_tests.py test_main
```

### Avec unittest directement / With unittest directly

Vous pouvez aussi utiliser le module unittest de Python directement:

You can also use Python's unittest module directly:

```bash
# Tous les tests / All tests
python3 -m unittest discover -v

# Un fichier spécifique / A specific file
python3 -m unittest test_character -v

# Une classe spécifique / A specific class
python3 -m unittest test_character.TestCharacter -v

# Un test spécifique / A specific test
python3 -m unittest test_character.TestCharacter.test_is_alive_when_healthy -v
```

## Couverture des Tests / Test Coverage

Les tests couvrent les fonctionnalités suivantes:

The tests cover the following functionality:

### Character (Classe de base / Base class)
- ✅ Initialisation des personnages
- ✅ Vérification de l'état vivant/mort
- ✅ Prise de dégâts
- ✅ Attaque et défense
- ✅ Mort après dégâts suffisants

### Soldier
- ✅ Héritage de Character
- ✅ Attaque spéciale avec bonus de dégâts (+10)
- ✅ Attaque normale

### Mage
- ✅ Héritage de Character
- ✅ Boule de feu quand la santé > 40
- ✅ Soin quand la santé ≤ 40
- ✅ Attaque normale

### Elf
- ✅ Héritage de Character
- ✅ Esquive (40% de chance)
- ✅ Défense normale
- ✅ Capacité d'attaque conservée

### King
- ✅ Héritage de Character
- ✅ Super attaque (20 dégâts)
- ✅ Contre-attaque avec poison (10 dégâts)
- ✅ Attaque et défense normales

### Fonctions principales / Main functions
- ✅ Fonction battle_round
- ✅ Contre-attaque du défenseur
- ✅ Pas de contre-attaque si le défenseur meurt
- ✅ Type_map et création de personnages depuis JSON

## Résultats Attendus / Expected Results

Tous les tests devraient réussir:

All tests should pass:

```
----------------------------------------------------------------------
Ran 37 tests in 0.006s

OK
```

## Ajouter de Nouveaux Tests / Adding New Tests

Pour ajouter de nouveaux tests:

To add new tests:

1. Créez un nouveau fichier `test_*.py` ou ajoutez des méthodes à un fichier existant
2. Héritez de `unittest.TestCase`
3. Créez des méthodes de test commençant par `test_`
4. Utilisez les assertions (assertEqual, assertTrue, etc.)
5. Exécutez les tests pour vérifier

Example:

```python
import unittest
from character import Character

class TestNewFeature(unittest.TestCase):
    def setUp(self):
        self.character = Character(...)
    
    def test_new_feature(self):
        # Votre test ici / Your test here
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
```

## Dépannage / Troubleshooting

### Import Errors

Si vous obtenez des erreurs d'import, assurez-vous d'être dans le bon répertoire:

If you get import errors, make sure you're in the correct directory:

```bash
cd /path/to/battle_simulator
python3 run_tests.py
```

### Tests qui échouent / Failing tests

Si un test échoue, le message d'erreur vous indiquera:
- Le nom du test qui a échoué
- L'assertion qui a échoué
- Les valeurs attendues vs obtenues

If a test fails, the error message will show:
- The name of the failing test
- The failed assertion
- Expected vs actual values

## Framework de Test / Testing Framework

Ce projet utilise le framework `unittest` intégré à Python, qui ne nécessite aucune installation supplémentaire.

This project uses Python's built-in `unittest` framework, which requires no additional installation.

## Contribution

Lors de l'ajout de nouvelles fonctionnalités, veuillez:
1. Ajouter des tests pour couvrir les nouveaux comportements
2. S'assurer que tous les tests existants passent toujours
3. Maintenir une couverture de test élevée

When adding new features, please:
1. Add tests to cover the new behavior
2. Ensure all existing tests still pass
3. Maintain high test coverage
