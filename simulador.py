import numpy as np
import random
import simpy

class Servidor:
    
    def __init__(self, env, nome, tempoDeServico):
        self.env = env
        self.nome = nome
        self.tempoDeServico = tempoDeServico
        self.fila = simpy.Store(env)
        self.statusSistema = {"saidas": []}
        self.process = env.process(self.run())

    def run(self):
        while True:
            job = yield self.fila.get() # Pegamos os jobs em uma fila, aguardando no caso da fila estar vazia.

            tempoDeServico = self.tempoDeServico() # Pegamos o tempo de servico do servidor.
            yield self.env.timeout(tempoDeServico)

            job["tempoDeSaidaDoJob"] = self.env.now

            # Roteamento das saidas do servidor 1.
            if self.nome == "Servidor1":
                proximaFila = random.choice(["Servidor2", "Servidor3"])
                if proximaFila == "Servidor2":
                    servidor2.fila.put(job)
                else:
                    servidor3.fila.put(job)
            # Roteamento das saidas do servidor 2.
            elif self.nome == "Servidor2":
                if random.random() < 0.2: # Retro alimentacao do servidor 2.
                    self.fila.put(job)
                else:
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

def simula(situacao, taxaDeChegada, qtdJobsWarmUp, qtdJobsParaMedir):

    global servidor2, servidor3 # Cria globalmente os servidores 2 e 3. Nao foi necessario criar o servidor 1 pois ele nao e utilizado fora do escopo da funcao simula.

    env = simpy.Environment() # Inicia o Environment do Scimpy.
    statusSistema = {"qtdJobsNoSistema": 0} # Inicialmente nao temos nenhum job no sistema.

    servidor1 = Servidor(env, "Servidor1", gerador_tempos_servicos(situacao, 1)) 
    servidor2 = Servidor(env, "Servidor2", gerador_tempos_servicos(situacao, 2))
    servidor3 = Servidor(env, "Servidor3", gerador_tempos_servicos(situacao, 3))

    env.process(gerador_chegadas_jobs(env, taxaDeChegada, servidor1.fila, statusSistema)) # Inicia o processo de chegada de jobs ao sistema.

    env.run(until=(qtdJobsWarmUp+qtdJobsParaMedir)) # Define o tempo que o ambiente de simulacao ira funcionar.

    temposNoSistema = [job["tempoDeSaidaDoJob"] - job["tempoDeChegadaDoJob"] for job in servidor2.statusSistema["saidas"][qtdJobsWarmUp:] + servidor3.statusSistema["saidas"][qtdJobsWarmUp:]]
    tempoMedioNoSistema = np.mean(temposNoSistema)
    desvioPadraoTempMedSis = np.std(temposNoSistema)
    return tempoMedioNoSistema, desvioPadraoTempMedSis

# Configuracoes para simular
taxaDeChegada = 2
qtdJobsWarmUp = 10000
qtdJobsParaMedir = 10000

# Executa a simulação para cada cenário
for situacao in [1, 2, 3]:
    media, desvioPadrao = simula(situacao, taxaDeChegada, qtdJobsWarmUp, qtdJobsParaMedir)
    print(f"Situacao {situacao}: Tempo Medio de Sistema = {media:.4f}s, Desvio Padrao Tempo Medio de Sistema = {desvioPadrao:.4f}s")