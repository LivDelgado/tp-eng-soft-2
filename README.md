# TP Engenharia de Software 2
Trabalho prático da disciplina de Engenharia de Software. Sistemas de Informação UFMG - 2022/2


# Grupo
- Lívia Delgado
- Pedro Luis Mucci

# Sobre o sistema
Sistema de lista de compras.
Cadastrar listas, adicionar itens nas listas e cadastrar compras feitas em mercados.
Indica onde comprar um item ou onde comprar uma lista inteira a partir de comparação de valores das listas no histórico.

# Tecnologias utilizadas

- Python 3.10
- Typer - Python CLI
- Pytest + Unittest
- Lizard

# Utilizando o App

- Instalar dependências
```bash

pip install -r requirements.txt

```

- Executar app
```bash

python lista-compras.py --help

```

- Executar testes
```bash
pytest
```

- Contar número de linhas:
```bash

pygount --format=summary --suffix=py --folders-to-skip tests
```

- Executar lizard
```bash
lizard . -x"./tests/*"
```

Salvando relatório html
```bash
lizard . -x"./tests/*" -o lizard/report.html
```
