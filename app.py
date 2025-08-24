from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

class ToDo:
    contador = 0
    def __init__(self, descricao):
        ToDo.contador += 1
        self.id = ToDo.contador
        self._descricao = descricao
        self._feito = False
        
    @property
    def descricao(self):
        return self._descricao

    @property
    def feito(self):
        return 'Feito' if self._feito else 'Nao Feito'
    
    def concluir_tarefa(self):
        self._feito = True
        
    def reabrir_tarefa(self):
        self._feito = False
        
    def __str__(self):
        return f'ID: {self.id}, Tarefa: {self.descricao}, status: {self.feito}'
    
    
tarefa1 = ToDo('Terminar essa primeira aplicacao sozinho')
tarefa2 = ToDo('Resolver os bugs que apareceram')
tarefa3 = ToDo('Rodar o ToDo dentro da pagina')

dict_tarefas = [tarefa1,tarefa2,tarefa3]

@app.route('/')
def hello():
    return render_template('index.html', titulo = 'Lista de Tarefas', tarefas = dict_tarefas)

@app.route('/criar')
def criar():
    return render_template('criar.html', titulo='Criar Nova Tarefa')

@app.route('/concluir/<int:id>')
def concluir(id):
    for tarefa in dict_tarefas:
        if tarefa.id == id:
            tarefa.concluir_tarefa()
            break
    return redirect(url_for('hello'))
      
@app.route('/reabrir/<int:id>')
def reabrir(id):
    for tarefa in dict_tarefas:
        if tarefa.id == id:
            tarefa.reabrir_tarefa()
            break
    return redirect(url_for('hello'))  

@app.route('/excluir/<int:id>')
def excluir(id):
    for tarefa in dict_tarefas:
        if tarefa.id == id:
            dict_tarefas.remove(tarefa)
            break
    return redirect(url_for('hello'))  

@app.route('/criar_tarefa', methods = ['POST'])
def criar_tarefa():
    tarefa = request.form['tarefa']
    nova_tarefa = ToDo(tarefa)
    dict_tarefas.append(nova_tarefa)
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run(debug=True)