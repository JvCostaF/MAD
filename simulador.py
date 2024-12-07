import numpy as np
import random
import simpy

class Servidor:
    
    def __init__(self, env, nome, tempoDeServico):
        self.env = env
        self.nome = nome
        self.tempoDeServico = tempoDeServico
        self.fila = simpy.Store(env)
        self.statusSistema = {"saídas": []}
        self.process = env.process(self.run())

    def run(self):
        job = yield self.fila.get() # Pegamos os jobs em uma fila, aguardando no caso da fila estar vazia.

        tempoDeServico = self.gerador_tempos_servicos() # Pegamos o tempo de servico do servidor.
        yield self.env.timeout(tempoDeServico)

        job["tempoDeSaida"] = self.env.now

        # Roteamento das saidas do servidor 1.
        if self.nome == "Servidor1":
            proximaFila = random.choice(["Servidor2", "Servidor3"])
            if proximaFila == "Servidor2":
                servidor2.fila.put(job)
            elif proximaFila == "Servidor3":
                servidor3.fila.put(job)
        # Roteamento das saidas do servidor 2.
        elif self.nome == "Servidor2":
            if random.random() < 0.2: # Retro alimentacao do servidor 2.
                servidor2.fila.put(job)

            self.statusSistema["saidas"].append(job) # Determina uma saida do sistema.
        # Roteamentos das saidas do servidor 3.
        elif self.nome == "Servidor3":
            self.statusSistema["saidas"].append(job) # Determina uma saida do sistema

def gerador_chegadas_jobs(env, taxaDeChegada, filaServidor1, statusSistema):
    while True:
        yield env.timeout(random.expovariate(taxaDeChegada)) # "Pausamos" o ambiente de simulacaoo ate a chegada de um job.
        statusSistema["qtdJobsNoSistema"] += 1
        tempoDeChegadaDoJob = env.now # O tempo atual no ambiente de simulacoo.
        job = {"jobID": statusSistema["qtdJobsNoSistema"], "tempoDeChegadaDoJob": tempoDeChegadaDoJob} # Criando o dicionario que ira representar um job no sistema.
        filaServidor1.put(job) # Adicionando esse novo job na fila do servidor 1.

def gerador_tempos_servicos(situacao, servidor):
    if situacao == 1:
        return lambda: [0.4, 0.6, 0.95][servidor - 1]
    elif situacao == 2:
        return lambda: random.uniform(0.1,[0.7, 1.1, 1.8][servidor - 1])
    elif situacao == 3:
        return lambda: random.expovariate(1/[0.4, 0.6, 0.95][servidor - 1])

def simula():
    pass


        