from flask import Flask

#__name__="__main__" sabemos assim que esta sendo executado de forma manual, não importado

app = Flask(__name__)#variavel name é o nome do projeto

@app.route("/")# decorador route, permite o a comunicação com o cliente, permite receba informações e devolvemos
#"/" é a rota padrão para o acesso no navegador
def hello_world():
    return "Hello, World!"#função que executa e retorna um texto 

@app.route("/about")
def about():
    return "Pagina sobre flask"
#As rotas são caminhos que o cliente pode acessar para obter informações do servidor



if __name__== "__main__":#garante que o arquivo é executado no servidor apenas de forma manual
    app.run(debug=True)#isso faz com que o codigo rode localmente, a propriedade dubg vai nos mostrar as infomações importantes
    

