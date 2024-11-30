# Trabalho final de MAD - Simulacoes de Redes de Filas Abertas

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

**Pré-requisitos:** Queueing-tool roda em Python 2.7 e 3.4-3.10. Queueing-tool requer [networkx](https://networkx.org/) e [numpy](http://www.numpy.org/), e depende de [matplotlib](http://matplotlib.org/) se você quiser plotar.

Para instalar o Python 3.10 (Versao qual eu utilizei para implementar o projeto):

**NO WINDOWS:** 

```
> winget install -e --id Python.Python.3.10
``` 

**NO LINUX:** 

``` 
> sudo apt update && sudo apt upgrade
> sudo add-apt-repository ppa:deadsnakes/ppa
> sudo apt install python3.10 python3.10-venv python3.10-distutils
> python3.10 --version
``` 

**NO MAC:** 

``` 
> brew update
> brew install python@3.10
> python3.10 --version
```

Agora vamos criar um ambiente virtual com o Python para instalar os pacotes necessarios pelo programa de simulacoes sem impactar as instalacoes do Python globais no seu sistema. 

Para criar o ambiente virtual:
```
python3.10 -m venv ambiente_trabalhoFinal_py3_10
```

Para acessar e iniciar o ambiente virtual criado:

**NO WINDOWS:** 

```
> ambiente_trabalhoFinal_py3_10\Scripts\activate
```

**NO LINUX/MAC:** 

```
> source ambiente_trabalhoFinal_py3_10/bin/activate
```

Por fim, precisamos instalar os pacotes nas versoes necessarias.

```
> pip install queueing_tool
> pip uninstall nump
> pip install numpy==1.23
```

Apos isso basta chamar o interpretador do python para executar o programa com:

```
> python <nome_do_prorama>.py
```