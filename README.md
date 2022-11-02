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


# Sobre o relatório de complexidade

As funções mais complexas apontadas foram `obter_valor_compra_mais_cara`, `indicar_mercado_compra`, `indicar_mercado_comprar_item`, com 6, 10 e 15 pontos de Complexidade Ciclomática respectivamente, todas da classe `Usuario`.

Elas apresentam mais linhas de código. Sua complexidade se deve aos múltiplos cenários que contemplam.

O primeiro passo para refatorá-las foi assegurar que elas estavam sendo cobertas por testes automatizados.

## obter_valor_compra_mais_cara

A refatoração aplicada foi a extração de método, criando um novo método **privado** com a lógica de retornar o valor máximmo pago numa compra no mercado informado, após fazer as devidas validações.
Além disso, a primeira condição do método não era necessária. Ela foi removida, também, com segurança pelos cenários de teste.

A complexidade resultante foi de 2 pontos pro método geral e 3 para o método privado gerado.


