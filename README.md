# Trabalho final de MAD - Simulacões de Redes de Filas Abertas

Esse trabalho consiste em simular uma rede de filas aberta com tres servidores, divindido em tres situacoes diferentes:

O sistema é constituído por três servidores, S1, S2 e S3, cada um com uma fila limitada. Cada job, ao chegar no sistema, precisa ser primeiramente servido por S1. Após concluir o serviço em S1, o job segue com probabilidade 0.5 para o servidor S2, e com probabilidade 0.5 para o servidor S3. Um job que sai do servidor S2 tem probabilidade 0.2 de retornar ao servidor S2 (voltando ao final da fila de S2, se ela não estiver vazia) para receber um novo serviço, independentemente de quantas vezes já tenha passado por S2. Ao sair definitivamente de S2, o job sai do sistema. Da mesma forma, ao sair de S3 (deterministicamente), o job sai do sistema.

As chegadas de jobs ao sistema constituem um processo de Poisson com taxa lambda = 2 jobs por segundo. Ou seja, o tempo entre as chegadas de dois jobs consecutivos é uma V.A. exponencial com média 1/lambda = 0.5 segundos (isto é, uma exponencial com taxa lambda).

As tres situacoes que precisamos simular sao:

1) Os tempos de serviço são fixos, determinísticos, e iguais a 0.4s, 0.6s e 0.95s, respectivamente;

2) Os tempos de serviço nos três servidores são V.A.s **uniformes** nos intervalos (0.1, 0.7), (0.1, 1.1) e (0.1, 1.8), respectivamente;

3) Os tempos de serviço são V.A.s **exponenciais** com médias 0.4s, 0.6s e 0.95s, respectivamente;

As métricas que você quer obter de forma experimental são:

- Tempo médio no sistema;
- Desvio padrão do tempo no sistema;

## Guia para executar e testar as simulacoes

**Pré-requisitos:** Precisamos obviamente do Python instalado além das libs [Random](https://docs.python.org/2/library/random.html), [Numpy](http://www.numpy.org/) e [Simpy](https://simpy.readthedocs.io/en/latest/contents.html).


```
$ pip install nump
$ pip install simpy
```

Apos isso basta chamar o interpretador do python para executar o programa com:

```
$ python simulador.py
```

## Links de referências consultadas para a implementação do trabalho

- [Aprenda a Utilizar o yield](https://awari.com.br/python-aprenda-a-utilizar-o-yield-para-otimizar-seu-codigo/)
- [Quando usar o yield no Python ](https://medium.com/@bernardo.costa/quando-usar-o-yield-no-python-ebae18b144ba)
- [Lambda Functions in Python](https://www.w3schools.com/python/python_lambda.asp)
- [Introdução ao Simpy](https://simpy.livrosimulacao.eng.br/parte-i-introducao/criando_as_primeiras_entidades)
- [Simpy - Environments](https://simpy.readthedocs.io/en/latest/topical_guides/environments.html)
- [Construindo um conjunto de objetos com Store](https://simpy.livrosimulacao.eng.br/parte-i-introducao/selecionando_um_recurso_especifico_para_um_processo)
- [PYTHON — Simulating SimPy A Summary in Python](https://laxfed.dev/python-simulating-simpy-a-summary-in-python-4bc1dc7c5930)