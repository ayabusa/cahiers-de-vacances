# Mes devoirs de vacances
Tous les exercices de la 2ème partie se trouvent dans les fichiers Pythons tandis que les questions sont dans README.md
## Questions
### Histoire de l’informatique
- Qui est considéré comme le père de l’informatique ?
>Alan Turing
- Quelles sont les dates clés du développement de l’informatique ? 
>La Pascaline, 1652
>
>Machine de Babbage, 1837
>
>ABC. John Atanasov, 1939
>
>ENIAC, 1945

### Architecture des ordinateurs
- Quels sont les principaux composants d’un ordinateur et leurs rôles respectifs ?
>Le CPU, il fait les calculs et possède différents registres pour stocker des valeurs rapidement
>
>La RAM, stocke les données volatiles des programmes et autre
>
>Disque dur, stocke les fichiers de l’OS et de l’utilisateur
>
>La carte mère, relie tous ces éléments ensemble
>
>Les différents périphériques, écran, clavier, micro etc…

- Quelle est la différence entre la mémoire RAM et la mémoire ROM ?
> La ROM est une mémoire persistante alors que la RAM est volatile
- Quels sont les différents types de mémoire ?
> La mémoire vive et la mémoire morte
- Qu’est-ce qu’un bus informatique et à quoi sert-il ?
> Il s’agit d’un système de communication qui transfère des données entre les différents composants de l’ordinateur ce qui leur permet de communiquer entre eux
### Bases de Python 
- Combien de types de base existe-t-il en Python et quels sont-ils ?
> Il y a 7 types de base en python et il s’agit de : int, float, bool, string, list, tuple, et dict
- Donnez des exemples de syntaxe pour déclarer une condition en Python.
```python
if maVar == 0 :
	print(‘maVar vaut 0’)
```
- Quelle est la syntaxe pour réaliser une boucle « pour » en Python ?
```python
for i in range(len(maListe)) :
	# faire quelque chose
```
- Comment écrire une fonction en Python et comment l’appeler ?
```python
def maFonction() :
	print(‘hello’)
maFonction()
```
- Quelle est la différence entre une liste et un tuple en Python ?
>Le tuple est immuable en python, alors que la liste elle peut être modifiée après création.
-Comment déclarer un dictionnaire en Python et quelle est la syntaxe pour accéder à une valeur dans un dictionnaire ?
```python
monDictionnaire = { "nom": "Albert", "âge": 42, "ville": "Paris" }
nom = monDictionaire["nom"]
```
### Représentation de l’information 
- Comment sont représentés les nombres entiers positifs en binaire et en hexadécimal ?  
> Ils sont représentés par des 0 et des 1 pour le binaire et des chiffres et des lettres de 0 à F pour l’hexadécimal.

- Comment sont représentés les nombres entiers relatifs en machine ?  
> Ils sont encodés de différentes manières en binaire, avec le complément à 1 par exemple.

- Comment sont représentés les textes en informatique ?  
> Avec différents encodages binaires comme l’UTF-8, le Latin ou encore l’ASCII.

- Qu’est-ce que l’encodage Unicode ?  
> Il s’agit d’un encodage universel qui contient presque tous les caractères de la plupart des langages ainsi que des émojis.
### Logique booléenne
- Quelles sont les principales opérations logiques ?  
  > Nom de l’opération | Représentation en programmation  
  > --- | ---  
  > AND | &&  
  > OR | ||  
  > NOT | !  
  > XOR | (Réponse manquante, vous pouvez la compléter ici.)

- Qu’est-ce qu’une table de vérité ?  
  > Il s’agit d’un tableau comme celui-ci :
  > 
  > | A | B | A OR B |  
  > |---|---|-------|  
  > | 0 | 1 |   1   |  
  > | 0 | 0 |   0   |  
  > | 1 | 1 |   1   |  
  > | 1 | 0 |   1   |
### Données en tables (fichiers CSV) 
- Qu’est-ce que le format CSV et à quoi sert-il ?  
  > Comma Separated Value (CSV) est un format de tableau qui sépare les valeurs par des virgules (ou des points-virgules dans certains cas).

- Quelle est la structure d’un fichier CSV ?  
  > Nom ; Âge ; Ville ;  
  > Albert ; 42 ; Paris ;  
  > Francis ; 36 ; Marseille ;

- Comment lire et écrire un fichier CSV en Python ?  
  > Il faut importer le module `csv`, puis utiliser :
  > 
  > ```python
  > import csv
  > 
  > with open('monFichier.csv', mode='r', newline='') as file:
  >     reader = csv.reader(file)
  >     for row in reader:
  >         print(row)
  > ```
### Web 
- Quel est le rôle du HTML dans la création d’un site Web ?  
  > Il s’agit d’un code de balisage qui permet de structurer sa page.

- Quelle est la structure d’une page HTML et comment la décrire avec des balises ?  
  > ```html
  > <!DOCTYPE html>
  > <html lang="fr">
  >   <head>
  >     <meta charset="utf-8">
  >     <title>titre</title>
  >     <link rel="stylesheet" href="style.css">
  >     <script src="script.js"></script>
  >   </head>
  >   <body>
  >     <!-- Ici on met le contenu -->
  >   </body>
  > </html>
  > ```

- Qu’est-ce qu’une feuille de style CSS ? À quoi sert-elle ?  
  > Elle permet de rendre la page jolie en définissant comment s’arrangent les éléments et leurs effets de style.

- Qu’est-ce que le protocole HTTP et comment fonctionne-t-il ?  
  > Le protocole HTTP est un protocole TCP/IP qui fonctionne de la façon suivante :
  > 
  > Le client envoie une requête qui peut ressembler à cet exemple demandant `index.html` :
  > 
  > ```
  > GET /index.html HTTP/1.1 
  > Host: www.ayabusa.dev 
  > User-Agent: Mozilla/5.0
  > ```
  > 
  > Le serveur répondra par un statut suivi de la page :
  > 
  > ```
  > HTTP/1.1 200 OK 
  > Content-Type: text/html 
  > <html>
  >  <head><title>Titre</title></head> 
  > <body><h1>Salut!</h1></body> 
  > </html>
  > ```
### Algorithmique
- Expliquez le principe du parcours séquentiel d’une liste.  
  > Le parcours séquentiel d'une liste consiste à accéder à chaque élément de la liste, un par un.

- Comment fonctionne la recherche dichotomique dans une liste triée ?  
  > Elle fonctionne en divisant le domaine de recherche en deux parties à chaque étape.

- Qu’est-ce que la complexité d’un algorithme et comment la mesurer ?  
  > Il s’agit du fait de déterminer la quantité de ressources (calcul par l’ordinateur) que le programme demande.

- Expliquez le principe des algorithmes gloutons et donnez un exemple d’application.  
  > Les algorithmes gloutons prennent des décisions locales optimales à chaque étape dans l'espoir que ces choix mèneront à une solution globale optimale. On peut les utiliser pour un algorithme de rendu de monnaie.

- Comment fonctionne l’algorithme des k plus proches voisins et quelles sont ses applications ?  
  > Il s’agit d’un modèle très rudimentaire de machine learning qui permet de classer une donnée en fonction de ses données voisines les plus proches. On peut l’utiliser pour la reconnaissance d’une espèce de fleur par exemple.
### Réseaux 
- Quels sont les principaux composants d’un réseau informatique et quel est leur rôle ?  
  > (Réponse manquante, vous pouvez la compléter ici.)

- Quels sont les principaux protocoles utilisés sur Internet ?  
  > UDP et TCP/IP.

- Qu’est-ce que le protocole TCP/IP et comment fonctionne-t-il ?  
  > Il s’agit d’un protocole fonctionnant sur le modèle client/serveur et qui vérifie que chaque paquet de données a bien été reçu. Sinon, il le renvoie.

- Expliquez la différence entre les adresses IP et les adresses MAC.  
  > Une adresse IP est attribuée par le routeur et identifie une machine sur un réseau, tandis que l’adresse MAC est spécifique à la machine et ne change pas.

- Citez des commandes Linux relatives au réseau.  
  > Ping, ifconfig, arp.
### Systèmes 
- Qu’est-ce qu’un système d’exploitation et quel est son rôle ?  
  > Il s’agit du logiciel qui gère les périphériques et permet à l’utilisateur d’utiliser ses fichiers, d’ouvrir un navigateur, etc.

- Quelles sont les principales différences entre Linux, Windows et MacOS ?  
  > Premièrement, leur kernel et leur mode de fonctionnement : Windows est basé sur du DOS, alors que macOS et Linux sont plus proches de l'Unix. Deuxièmement, Linux est le seul des trois systèmes d'exploitation à être open source.

- Citez des exemples de commandes Linux et leur usage.  
  > `ls` – liste les répertoires  
  > `cd` – change de répertoire  
  > `sudo` – lance une commande en super utilisateur
