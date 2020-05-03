from flask import Flask, render_template, url_for, request, redirect
# render_template : pour l'affichage des pages HTML contenant des parametres {{...}}
# url_for : pour générer l'URL de retour de la page 'page_1.html' vers la racine du site
# request : pour la récupération des paramètres reournés par la méthode POST de l'HTML
# redirect : redirection vers l'autre page du site
app = Flask(__name__)
# retrait du mode debug quand le programme est au point
app.config["DEBUG"] = True

# _______________________ page d'acceuil : saisie des constantes _____________________________________________________
# @app.route() : "décorateur" de la fonction acceuil()
# designe la fonction lançée lorsque l'URL de la racine du site "/" est appellée
# dans notre cas il s'agit de "https://isn2src.pythonanywhere.com/" et de la fonction acceuil()
@app.route("/", methods=["GET", "POST"])
def acceuil():
    # recuperation des saisies par POST HTML
    errors = ""
    # teste indefiniment si les saisies sont des nombres :
    # l'instruction "try" lance la fonction float() qui retourne un nombre depuis un texte
    # l'instruction "except" gère l'erreur du "try" : si ce texte ne comporte pas que des chiffres
    if request.method == "POST":
        cst_a = None    # constante a
        cst_b = None    # constante b
        cst_c = None    # constante c
        try:
            cst_a = float(request.form["cst_a"])
        except:
            errors += "<p>{!r} n'est pas un nombre.</p>\n".format(request.form["cst_a"])
        try:
            cst_b = float(request.form["cst_b"])
        except:
            errors += "<p>{!r} n'est pas un nombre.</p>\n".format(request.form["cst_b"])
        try:
            cst_c = float(request.form["cst_c"])
        except:
            errors += "<p>{!r} n'est pas un nombre.</p>\n".format(request.form["cst_c"])

        if cst_a is not None and cst_b is not None and cst_c is not None:
            # toutes les saisies sont correctes : je redirige vers la page du graphe
            # en construisant l'URL suivie des valeurs des constantes a, b et c
            # cela donne par exemple : https://isn2src.pythonanywhere.com/graphe?cst_a=3&cst_b=2&cst_c=-10
            return redirect(url_for('graphe', cst_a=cst_a, cst_b=cst_b,cst_c=cst_c) )

    # page de saisie des constantes a, b et c
    # ATTENTION : c'est de l'HTML envoyé directement au serveur web, sans "render_template()"
    #             donc : pas de CSS, pas d'images, pas de JavaScript -et- même pas de commentaires <-- ... -->
    return '''
        <html>
                <center><strong>{errors}</strong></center>
            <body style="background-color: #CCFFFF">
                <center>
                <h1 style="font-size: 2em; color: rgb(0, 0, 0); font-family: &quot;Times New Roman&quot;; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-style: initial; text-decoration-color: initial;">
                    ISN - La Source - Ts -2019-2020</h1>
                <h3 style="font-size: x-large; color: rgb(0, 0, 0); font-family: &quot;Times New Roman&quot;; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-style: initial; text-decoration-color: initial;">
                    Graphe de<span>&nbsp;</span><strong>f(x) = ax² + bx +c</strong></h3>
                <p style="font-size: x-large; color: red">Merci de saisir vos propres constantes :</p>

                <form method="post" action=".">
                    <p style="font-size: x-large"><label for="cst_a">Constante a = </label><input name="cst_a" value="1"/></p>
                    <p style="font-size: x-large"><label for="cst_a">Constante b = </label><input name="cst_b" value="1"/></p>
                    <p style="font-size: x-large"><label for="cst_a">Constante c = </label><input name="cst_c" value="1"/></p>
                    <p style="font-size: x-large"><input type="submit" value="Afficher la courbe de la fonction"/></p>
                </form>
                </center>
            </body>
        </html>
    '''    .format(errors=errors)

# _______________________ page d'affichage courbe ________________________________________
# @app.route() : "décorateur" de la fonction suite()
# designe la fonction lançée lorsque l'URL de la racine du site suivie de /graphe est appellée
# dans notre cas il s'agit de "https://isn2src.pythonanywhere.com/graphet" et de la fonction graphe()
@app.route("/graphe")
def graphe():
    # recuperation des valeurs des constantes a,b et c passées par l'URL généré par la page d'acceuil
    cst_a = request.args.get('cst_a', None)
    cst_b = request.args.get('cst_b', None)
    cst_c = request.args.get('cst_c', None)

    # pour cette version on utilise une échelle standard
    axe_X = [-10,  -9,  -8,  -7,  -6,  -5,  -4,  -3,  -
              2,  -1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]

    # calcul du résultat Y = aX² + bX + c à partir de la liste des valeurs axe_X[]
    # resultat : construction de la liste axe_Y = []
    axe_Y = []
    if (not (cst_a == "0"))  and (not (cst_b == "0")) and (not (cst_c == "0")):
        for i, val in enumerate(axe_X):
            point = (float(cst_a)*float(val)*float(val))+(float(cst_b)*float(val))+float(cst_c)
            axe_Y.append(point)
    else:
        # toutes les constantes sont à 0 => il n'y a pas de fonction
        # probleme documentation : ni 'null' ni 'NaN' destinées à "sauter" un point
        # ne fonctionnent, donc choix de mettre une ligne à 0...
        axe_Y = [0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0]

    # ************** Dimension en pixels du cadre recevant la courbe *****************
    # après une installation du plugin zoom sur charts.js... qui ne répond pas au probleme
    # ( voir https://stackoverflow.com/questions/40086575/chart-js-draw-mathematical-function )
    # Il s'agit d'obtenir une indication des valeurs min et max de f(x) puis un ratio
    # de telle sorte à agir sur la hauteur/largeur du cadre (ratio_canvas) graphe affiché
    # pour que la représentation de la courbe soit la plus réaliste possible
    if (cst_a == "0")  and (cst_b == "0") :
        ratio_canvas = 1
    else:
        delta_Y = abs(max(axe_Y)) + abs(min(axe_Y))   # différence valeurs min et max de Y
        delta_X = abs(max(axe_X)) + abs(min(axe_X))   # différence valeurs min et max de X
        ratio_canvas = delta_Y/delta_X                # ratio hauteur largeur

    # reglage des dimensions "haut" "large" du cadre affiché dans la page "graphe.html"
    # la hauteur est choisie en pixels :
    haut = "500"
    # la largeur "large" se trouve en appliquant le ratio à la hauteur "haut"
    # en limitant les valeurs extremes et évitant toutes les constantes à 0
    if (not (ratio_canvas == 0)):
        large_value = int(haut)/ratio_canvas
        if large_value > 1000:
            large = "1000"
        else:
            large = str(large_value)
            if large_value < 400:
                large= "400"
    else:
        large= "400"
    # ******* NOTE : Impossible d'isoler le traitement ci-dessus dans un programe séparé "courbe.py"  *******

    # expression texte de la fonction avec les constantes siasies
    # destinée à être améliorée pour supprimer les "+" lorsque les constantes sont négatives
    fonction2nd = 'f(x) = ' + str(cst_a) + 'x² + ' + str(cst_b) + 'x + ' + str(cst_c)

    # render_template() : affichage de la page HTML "graphe.html" qui contient des variables et instructions Flask
    # c'est ce qui est appellé de "...l'HTML altéré..." à cause de la présence de ces variables {{...}}
    # toutes les pages .html doivent se situer dans le répertoire nommé /templates
    return render_template('graphe.html', values=axe_Y, labels=axe_X, cst_a=cst_a, cst_b=cst_b, cst_c=cst_c, haut=haut, large=large, fonction2nd=fonction2nd)

if __name__ == '__main__':
    app.run()
