#!/bin/sh
echo '=== Début du build Render ==='
ls -la
echo '=== Vérification requirements.txt ==='
find . -name requirements.txt
echo '=== Installation des dépendances ==='
pip install --upgrade pip
pip install -r requirements.txt