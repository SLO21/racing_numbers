from flask import Flask, render_template

#é recomendavel que o site se chame app . A variavle é __name__

app = Flask(__name__)

#criar a 1ªpagina do site
#3 coisas: route e função e template (dentro da pasta templates.serve para gravar o código html. route é o caminho que vem depois do caminho. funçaõ o que quer exibir.

@app.route("/")
#def é o nome da página (função do python: o que quero exibir na pagina)
def homepage():
    return render_template('homepage.html')


@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/usuarios/<nome>')
def usuarios(nome):
    return render_template('usuarios.html',nameusuario=nome)

#por o site no ar
if __name__ == "__main__":
    app.run(debug=True)