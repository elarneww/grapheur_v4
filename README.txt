Projet: Graphe d'une fonction du second degré

Deux routes sont utilisées:

@app.route("/", methods=["GET", "POST"])
La route "/" indique la racine du site
affiche la page acceuil 'acceuil.html' permemt de saisir les constantes a, b et c
de la fonction f(x) = ax² + bx +c
une fois les tests effectués,
il y a redirection vers la page "graphe.html" en passant les constantes:
constante a, b et c notées cst_a, cst_b et cst_c
Les contantes recues servent à établir 2 listes de valeurs pour les axes X et Y

@app.route("/graphe").
La page d'affichage du graphe 'graphe.html' utilise le "render_template"
se reporter au README dans le dossier /templates

Globalement le site est accessible avec l'URL : isn2src.pythonanywhere.com