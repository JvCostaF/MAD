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

    def run():
        pass

def gerador_chegadas_jobs(env, taxaDeChegada, filaServidor1, statusSistema):
    while True:
        yield env.timeout(random.expovariate(taxaDeChegada)) # "Pausamos" o ambiente de simulação até a chegada de um job.
        statusSistema["qtdJobsNoSistema"] += 1
        tempoDeChegadaDoJob = env.now # O tempo atual no ambiente de simulação.
        job = {"jobID": statusSistema["qtdJobsNoSistema"], "tempoDeChegadaDoJob": tempoDeChegadaDoJob} # Criando o dicionário que irá representar um job no sistema.
        filaServidor1.put(job) # Adicionando esse novo job na fila do servidor 1.

def gerador_tempos_servicos():
    pass

def simula():
    pass


        