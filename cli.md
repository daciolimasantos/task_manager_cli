# 🖥️ Manual do TaskManager CLI - A Interface dos Comandos Mágicos

*Agora vamos entender como usar o TaskManager pelo terminal, igual aqueles programas de computador que a gente usava no DOS! Preparar, apontar, digitar!*

---

## 🎯 O QUE É ISSO?

Esse código cria uma **Interface de Linha de Comando (CLI)** para o nosso TaskManager. Sabe quando você jogava no MS-DOS e digitava `dir` pra ver os arquivos? Aqui é a mesma coisa: você digita comandos e o programa executa as tarefas.

É tipo ter um controle remoto pra controlar sua lista de tarefas!

---

## 📼 EXPLICAÇÃO LINHA POR LINHA

### As Importações (Tipo conectar os cabos)

```python
import argparse
from task_manager import TaskManager
import argparse: Essa biblioteca é tipo um intérprete de comandos. Ela entende o que você digita no terminal e organiza essa informação pro programa usar. É igual aqueles tradutores simultâneos de filme!

from task_manager import TaskManager: Aqui a gente tá importando a classe que criamos antes. É tipo pegar o controle remoto que já existia e colocar pilha nova.

A Função Principal (Onde tudo começa)
python
def main():
Essa é a função main (principal). É tipo a primeira cena do filme - tudo começa aqui. Quando o programa roda, é essa função que executa primeiro.

Criando o Interpretador de Comandos
python
    parser = argparse.ArgumentParser(description="TaskManager CLI")
parser: É o nosso tradutor de comandos

ArgumentParser: Cria um objeto que vai saber interpretar tudo que você digitar

description: É a descrição que aparece quando alguém pede ajuda (tipo --help)

python
    subparsers = parser.add_subparsers(dest="command")
subparsers: Isso permite criar subcomandos. É como ter um controle remoto com vários botões: um botão pra "add", outro pra "remove", etc.

dest="command": Guarda o nome do comando digitado numa variável chamada command

Comando ADD (Adicionar tarefa)
python
    # add a task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", help="Title of the task")
    parser_add.add_argument("-d", "--description", default="", help="Description of the task")
Aqui estamos configurando o comando add:

add_parser("add"): Cria o comando "add" (tipo digitar add no terminal)

add_argument("title"): Diz que depois do "add" a gente precisa passar um título (obrigatório)

add_argument("-d", "--description"): Cria uma opção -d pra colocar descrição. O default="" significa que se não passar, fica vazio

No terminal ficaria assim:

bash
python programa.py add "Comprar leite" -d "Desnatado, por favor"
Comando REMOVE (Remover tarefa)
python
    # remove a task
    parser_remove = subparsers.add_parser("remove", help="Remove a task by ID")
    parser_remove.add_argument("id", type=int, help="ID of the task to complete")
add_parser("remove"): Cria o comando "remove"

add_argument("id", type=int): Pede o número do ID (e garante que é número inteiro)

No terminal:

bash
python programa.py remove 3
Comando COMPLETE (Completar tarefa)
python
    # complete a task
    parser_complete = subparsers.add_parser("complete", help="Mark task as completed")
    parser_complete.add_argument("id", type=int, help="ID of the task to complete")
Mesma ideia do remove, mas pra marcar como concluída. O help é a mensagem que aparece quando alguém digita --help.

Comandos LIST, SAVE e LOAD
python
    # list the tasks
    subparsers.add_parser("list", help="List all tasks")
    
    # save the tasks
    subparsers.add_parser("save", help="Save tasks to file")
    
    # load the tasks
    subparsers.add_parser("load", help="Load tasks from file")
Esses são comandos simples, sem argumentos extras. É tipo botões de função do videocassete: PLAY, STOP, REC.

Parseando os Argumentos
python
    args = parser.parse_args()
parse_args(): É o momento mágico onde o tradutor entra em ação! Ele pega tudo que você digitou no terminal, interpreta e coloca dentro do objeto args. É tipo o seu professor corrigindo a prova e colocando as notas no diário.

Criando o Gerenciador de Tarefas
python
    manager = TaskManager()
    manager.load_tasks() # carrega uma vez no inicio
manager = TaskManager(): Pega a classe que criamos e cria um objeto de verdade. É tipo comprar o videogame depois de ver a propaganda.

manager.load_tasks(): Já carrega as tarefas salvas automaticamente quando o programa começa (esperto, né?)

O Grande Decisório (If/Elif)
python
    if args.command == "add":
        manager.add_task(args.title, args.description)
        manager.save_tasks()
Agora vem a parte das decisões. Dependendo do comando digitado, faz uma coisa diferente:

Se for ADD: Adiciona a tarefa com título e descrição, e já salva automaticamente

Acessa args.title e args.description porque esses argumentos foram guardados lá no parsing

python
    elif args.command == "remove":
        manager.remove_task(args.id)
        manager.save_tasks()
Se for REMOVE: Remove a tarefa com aquele ID e salva

python
    elif args.command == "complete":
        manager.complete_task(args.id)
        manager.save_tasks()
Se for COMPLETE: Marca como completa e salva

python
    elif args.command == "list":
        manager.list_tasks()
Se for LIST: Só mostra a lista (não precisa salvar, não mudou nada)

python
    elif args.command == "save":
        manager.save_tasks()
Se for SAVE: Só salva (útil se quiser forçar um salvamento)

python
    elif args.command == "load":
        manager.list_tasks()
ALERTA DE BUG! ⚠️ Aqui tem um erro! Deveria carregar as tarefas, mas tá listando. O correto seria manager.load_tasks(). Esses programadores...

python
    else:
        parser.print_help()
Se não for nenhum comando válido: Mostra a ajuda (todos os comandos disponíveis)

A Proteção do If Name Main
python
if __name__ == "__main__":
    main()
Essa é uma proteção esperta. Explicando em miúdos:

__name__ é uma variável especial do Python

Quando você roda o arquivo diretamente, __name__ vira "__main__"

Quando você importa esse arquivo em outro, __name__ vira o nome do arquivo

Traduzindo: Só executa o main() se você rodar esse arquivo diretamente. Se alguém importar ele, não executa. É tipo uma chave de segurança.

🎮 COMO USAR NO TERMINAL
Lista de Comandos Mágicos
Comando	Exemplo	O que faz
add	python app.py add "Estudar Python" -d "Capítulo 5"	Adiciona tarefa
remove	python app.py remove 2	Remove tarefa ID 2
complete	python app.py complete 1	Marca ID 1 como completa
list	python app.py list	Mostra todas tarefas
save	python app.py save	Salva no arquivo
load	python app.py load	Carrega do arquivo
help	python app.py --help	Mostra todos comandos
💡 CONCEITOS APRENDIDOS (Pro Enem da Computação)
Conceito	Explicação Anos 90
CLI (Interface de Linha de Comando)	É igual ao MS-DOS, você digita e o computador obedece
Parser	Tradutor de comandos humanos pra linguagem de máquina
Argumentos	Informações extras que você passa junto com o comando
Subcomandos	Tipo os botões do controle remoto: cada um faz uma coisa
Flag	Opções como -d que ativam funcionalidades extras
🐛 BUG ENCONTRADO (Erro de digitação)
No comando load tem um erro:

python
    elif args.command == "load":
        manager.list_tasks()  # 👈 ISSO ESTÁ ERRADO!
O correto seria:

python
    elif args.command == "load":
        manager.load_tasks()  # 👈 ASSIM QUE É!
        manager.list_tasks()   # Se quiser já mostrar depois de carregar