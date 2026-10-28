# Projetct1Pyfirmata

Mini projet Python + Arduino utilisant la bibliothèque `pyfirmata` pour piloter un afficheur 7 segments et faire défiler les chiffres de 0 à 9.

## Description

Ce script se connecte à une carte Arduino sur le port COM3, active les broches numériques correspondant aux segments d'un afficheur 7 segments, puis affiche successivement les chiffres de 0 à 9 avec une pause entre chaque changement.

Le programme est simple, pédagogique et peut servir de base pour des projets plus avancés avec Arduino et Python.

## Matériel nécessaire

- Arduino UNO ou compatible
- Afficheur 7 segments
- Fils de connexion
- Résistances (recommandé : 220 Ω à 330 Ω par segment)
- Ordinateur avec Python 3 installé
- Câble USB pour l'Arduino

## Prérequis

Installer le package Python nécessaire :

```bash
pip install pyfirmata
```

## Configuration

Avant de lancer le projet, vérifie le port série de ton Arduino :

- Windows : `COM3`, `COM4`, etc.
- Linux/macOS : `/dev/ttyUSB0`, `/dev/ttyACM0`, etc.

Dans le script, la ligne suivante doit correspondre au bon port :

```python
board = Arduino('COM3')
```

Tu peux la modifier selon ton port Arduino.

## Branchement

Le programme utilise les broches numériques suivantes :

- 2 : segment `e`
- 3 : segment `d`
- 4 : segment `c`
- 5 : segment `b`
- 6 : segment `a`
- 7 : segment `f`
- 8 : segment `g`

Chaque segment est configuré en sortie (`o`) avec `board.get_pin('d:X:o')`.

## Utilisation

Lance le script depuis le dossier du projet :

```bash
python Projetct1Pyfirmata.py
```

Le programme va alors :

1. Se connecter à l'Arduino
2. Afficher les chiffres de 0 à 9
3. Faire une pause entre chaque chiffre
4. S'arrêter proprement avec `Ctrl + C`

## Exemple de comportement

Le script contient des groupes de segments pour chaque chiffre :

- `led_0` à `led_9`
- chaque liste représente les segments à allumer pour afficher un chiffre
- les segments sont activés puis éteints successivement pour simuler un affichage numérique

## Structure du projet

```text
Projetct1Pyfirmata/
├── Projetct1Pyfirmata.py
├── README.md
└── ...
```

## Remarques

- Le projet est idéal pour apprendre la communication Python ↔ Arduino.
- Il peut être adapté pour afficher d'autres motifs, messages ou animations.
- Le port COM peut varier selon la machine et le modèle d'Arduino.

