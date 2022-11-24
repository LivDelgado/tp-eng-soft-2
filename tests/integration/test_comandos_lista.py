from unittest import TestCase
from typer.testing import CliRunner

from lista_compras import app

class TestComandosLista(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.runner.invoke(app, ["limpar"])

    def tearDown(self):
        self.runner.invoke(app, ["limpar"])

    def test_adicionar_listas_de_compras_WHEN_nenhuma_lista_THEN_retorna_erro_nenhuma_lista(self):
        result = self.runner.invoke(app, ["listas", "listar"])

        self.assertEqual("Nenhuma lista encontrada", str(result.exception))

    def test_adicionar_listas_de_compras_WHEN_adiciona_lista_THEN_retorna_lista_ao_obter_todas(self):
        result = self.runner.invoke(
            app,
            ["listas", "adicionar", "listaTeste"],
            input="Cafe\nN\n"
        )

        result = self.runner.invoke(app, ["listas", "listar"])

        self.assertTrue("listaTeste" in result.stdout)

    