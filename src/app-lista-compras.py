import typer
from rich.prompt import Prompt
from typing import List, Optional

from lista import ListaService
from usuario import UsuarioService

app = typer.Typer()

lista_app = typer.Typer()
compras_app = typer.Typer()
mercados_app = typer.Typer()

app.add_typer(lista_app, name="listas")
app.add_typer(compras_app, name="compras")
app.add_typer(mercados_app, name="mercados")

usuario = None

@lista_app.command("listar")
def listas_listas_de_compras():
    listas = ListaService.obter_listas(usuario)
    for lista in listas:
        print(lista)

@lista_app.command("adicionar")
def adicionar_listas_de_compras(nome: str, descricao: Optional[str] = None):
    pedir_item = True
    itens: List[str] = []
    while pedir_item:
        nome_item = Prompt.ask("Qual item quer adicionar?")
        itens.append(nome_item)
        pedir_item = typer.confirm("Adicionar outro?")

    ListaService.adicionar_lista(usuario, nome, descricao, itens)
    UsuarioService.salvar_dados_usuario(usuario)

@lista_app.command("remover")
def remover_listas_de_compras(nome: str):
    ListaService.remover_lista(usuario, nome)
    UsuarioService.salvar_dados_usuario(usuario)

@lista_app.command("itens")
def ver_itens_lista(nome: str):
    ListaService.listar_itens(usuario, nome)

@lista_app.command("adicionar-item")
def adicionar_item_lista(nome: str):
    nome_item = Prompt.ask("Qual item quer adicionar?")
    ListaService.adicionar_item_lista(usuario, nome, nome_item)
    UsuarioService.salvar_dados_usuario(usuario)

@lista_app.command("remover-item")
def remover_item_lista(nome: str):
    nome_item = Prompt.ask("Qual item quer remover?")
    ListaService.remover_item_lista(usuario, nome, nome_item)
    UsuarioService.salvar_dados_usuario(usuario)

if __name__ == "__main__":
    usuario = UsuarioService.obter_usuario_salvo_ou_criar_default()
    try:
        app()
    except Exception as error:
        print(error)
