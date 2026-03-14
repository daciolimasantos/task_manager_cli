# 📚 Manual do Gerenciador de Tarefas - Explicado pra Galera dos Anos 90

*Senta aí no banco de trás do fusca e prepara o walkman porque a aula vai começar! Imagina que estamos em 1995, o som do modem discado ainda é música pros nossos ouvidos, e o Windows 95 acabou de lançar.*

---

## 🎯 VISÃO GERAL (Tipo a capa da revista INFO)

Esse código é um **Gerenciador de Tarefas** em Python. Funciona como uma agenda eletrônica (tipo um Palm Pilot, mas mais simples) que salva suas tarefas num arquivo. Você pode adicionar, remover, marcar como feita, listar e salvar tudo.

---

## 📼 LINHA POR LINHA (Põe fita K7 no videogame)

### As importações (tipo colocar cartucho no Mega Drive)

```python
import json
from typing import List, Dict
import json: Tá vendo esses cartuchos amarelos do Super Nintendo? O json é tipo isso. É uma biblioteca que permite a gente guardar informação num formato que qualquer um entende. É como escrever um bilhete pro amigo, mas que o computador consegue ler depois.

from typing import List, Dict: Isso é tipo uma etiqueta na fita VHS. A gente avisa pro Python: "Ei, vou usar Listas (coleções ordenadas) e Dicionários (que são como fichas de cadastro)".

A Classe TaskManager (Tipo um estojo escolar)
python
class TaskManager:
Classe é como se fosse uma forma de gelo. Você cria a forma, e cada gelo que sai dela é um objeto. Aqui, TaskManager é a forma que gerencia tarefas.

O Construtor init (Montando o estojo)
python
    def __init__(self, file_path: str = "tasks.json"):
__init__ é o que acontece QUANDO você tira o estojo novo da mochila. Ele configura tudo.

file_path: str = "tasks.json" - É o nome do arquivo no disquete onde vamos salvar as tarefas. Por padrão, é "tasks.json".

python
        self.file_path = file_path
        self.tasks: List[Dict] = []
        self.next_id = 1
self.file_path: Guarda o nome do arquivo (igual você guarda o disquete no bolso).

self.tasks: É a lista de tarefas vazia, tipo uma pasta nova sem folha.

self.next_id: É tipo o número da matrícula. Cada tarefa nova ganha um número. Começa no 1.

Método add_task (Colocando bilhete na agenda)
python
    def add_task(self, title: str, description: str = "") -> None:
Função pra adicionar tarefa. title é o título (obrigatório), description é a descrição (opcional). -> None significa que ela não devolve nada, só faz o serviço.

python
        task = {
            "id": self.next_id,
            "title": title,
            "description": description,
            "status": "pending"
        }
Aqui cria uma ficha da tarefa (um dicionário):

ID: O número de matrícula

Title: O nome da tarefa

Description: Detalhes

Status: Pendente (igual fita pra gravar)

python
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task added: {title}")
append: Adiciona a ficha na pasta

next_id += 1: Prepara o próximo número

print: Mostra no monitor verde que deu certo

Método remove_task (Jogando papel fora)
python
    def remove_task(self, task_id: int) -> bool:
Remove tarefa pelo número. Retorna True (verdadeiro) se achou, False se não.

python
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                print(f"Task removed: {task['title']}")
                return True
for task in tasks: É tipo folhear a agenda página por página

if task["id"] == task_id: "Esse número é o que tão procurando?"

remove: Arranca a página

return True: "Missão cumprida, capitão!"

python
        print(f"Task with ID {task_id} not found.")
        return False
Se terminar o loop e não achar: dá mensagem de erro e volta False.

Método complete_task (Passando de ano)
python
    def complete_task(self, task_id: int) -> bool:
Parecido com o remove, mas não apaga - só muda o status.

python
            if task["id"] == task_id:
                task["status"] = "completed"
                print(f"Task has been completed: {task['title']}")
task["status"] = "completed": Muda de "pending" pra "completed". É tipo passar de ano na escola - a ficha muda, mas continua lá.

Método list_tasks (Olhando a agenda)
python
    def list_tasks(self) -> None:
Mostra todas as tarefas na tela.

python
        if not self.tasks:
            print("No tasks avaiable.")
            return
Se não tem tarefa (lista vazia), avisa e sai.

python
        for task in self.tasks:
            status = "✅" if task["status"] == "completed" else "❌"
            print(f"{task['id']}: {task['title']} [{status}] - {task['description']}")
status = "✅" if...: Operador ternário! É tipo um "if" enxuto. Se tarefa completa, mostra ✅ (check bonitinho), senão ❌ (xis vermelho)

print: Mostra tipo "1: Comprar leite [❌] - Leite desnatado"

Método save_tasks (Salvando no disquete)
python
    def save_tasks(self) -> None:
Salva tudo no arquivo.

python
        data = {
            "next_id": self.next_id,
            "tasks": self.tasks
        }
Cria um "pacote" com duas coisas:

O próximo ID disponível (pra não repetir número quando carregar de novo)

A lista de tarefas

python
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
with open: "Comandante, abrindo arquivo pra escrita!"

as f: Apelidou o arquivo de f

json.dump: Joga o pacote data dentro do arquivo, com indentação bonitinha (espaços)

python
        print(f"Tasks sve to {self.file_path}")
Avisa que salvou (tem um errinho de digitação "sve" em vez de "saved" - esses programadores...)

Método load_tasks (Carregando do disquete)
python
    def load_tasks(self) -> None:
Carrega as tarefas salvas.

python
        try:
            with open(self.file_path, "r") as f:
                content = f.read().strip()
try: "Tenta fazer isso, mas se der pau..."

"r": Modo leitura

.strip(): Tira espaços em branco (tipo limpar a poeira do disquete)

python
                if content:
                    data = json.loads(content)
                    self.tasks = data.get("tasks", [])
                    self.next_id = data.get("next_id", 1)
if content: Se o arquivo não estiver vazio

json.loads: Lê o conteúdo e transforma de volta em dicionário

.get("tasks", []): Pega a lista de tarefas, se não tiver, pega lista vazia

.get("next_id", 1): Pega o próximo ID, senão começa do 1

python
                else:
                    self.tasks = []
                    self.next_id = 1
Se arquivo vazio: lista vazia, ID começa do 1.

python
            print(f"Tasks loaded from {self.file_path}")
Avisou que carregou.

python
        except FileNotFoundError:
            print(f"No file found at {self.file_path}, starting with empty task list.")
            self.tasks = []
            self.next_id = 1
except FileNotFoundError: Se o arquivo não existe (tipo disquete não inserido)

Cria lista vazia e começa do 1

python
        except json.JSONDecodeError:
            print(f"file{self.file_path} is corrupted. Starting with empty task list.")
            self.tasks = []
            self.next_id = 1
json.JSONDecodeError: Se o arquivo tá corrompido (disquete riscado)

Mesmo tratamento: começa do zero

🎓 CONCEITOS IMPORTANTES (Pra gabaritar a prova)
Conceito	Explicação
POO (Programação Orientada a Objetos)	Tudo organizado em classes, tipo gavetas organizadoras
Tipagem	: str, : int - é tipo colocar etiqueta no que é cada coisa
Persistência	Salvar em arquivo pra não perder quando desligar o PC (diferente da RAM que apaga)
Tratamento de erros	try/except - tipo cinto de segurança
JSON	Formato universal de dados (todo mundo entende, até PHP)
💡 DICA DE VELHO
Nos anos 90 a gente fazia isso com arquivo .txt e dava muito mais trabalho. Esse Python com JSON é mordomia!

Anotou tudo no seu caderno de folha pautada? Passa a fita pro amigo e manda bronca! 🤘