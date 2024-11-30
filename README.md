# Trabalho final de MAD - Simulacoes de Redes de Filas Abertas

Esse trabalho consiste em simular uma rede de filas aberta com tres servidores, divindido em tres situacoes diferentes:

1)

2) 

3)

## Guia para executar e testar as simulacoes

**Pré-requisitos:** Queueing-tool roda em Python 2.7 e 3.4-3.10. Queueing-tool
requer `networkx <https://networkx.org/>`__ e
`numpy <http://www.numpy.org/>`, e depende de
`matplotlib <http://matplotlib.org/>` se você quiser plotar.

Para instalar o Python 3.10:

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