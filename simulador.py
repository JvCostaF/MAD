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
        self.process = env.process(self.processaJobs())

    def processaJobs(self): # 
        while True:
            job = yield self.fila.get() # Pegamos os jobs em uma fila, aguardando no caso da fila estar vazia.

            tempoDeServico = self.tempoDeServico() # Pegamos o tempo de servico do servidor.
            yield self.env.timeout(tempoDeServico) # Aqui processamos os jobs, simulando o tempo de servico em que o servidor fica ocupado.

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

def geradorChegadasJobs(env, taxaDeChegada, filaServidor1, statusSistema):
    while True:
        u = np.random.uniform(0,1)
        Chegada = -(np.log(1-u)/taxaDeChegada)
        yield env.timeout(Chegada)
        statusSistema["qtdJobsNoSistema"] += 1
        tempoDeChegadaDoJob = env.now # O tempo atual no ambiente de simulacao.
        job = {"jobID": statusSistema["qtdJobsNoSistema"], "tempoDeChegadaDoJob": tempoDeChegadaDoJob} # Criando o dicionario que ira representar um job no sistema.
        filaServidor1.put(job) # Adicionando esse novo job na fila do servidor 1.

# def geradorChegadasJobs(env, taxaDeChegada, filaServidor1, statusSistema):
#     while True:
#         yield env.timeout(random.expovariate(taxaDeChegada)) # "Pausamos" o ambiente de simulacaoo ate a chegada de um job.
#         statusSistema["qtdJobsNoSistema"] += 1
#         tempoDeChegadaDoJob = env.now # O tempo atual no ambiente de simulacao.
#         job = {"jobID": statusSistema["qtdJobsNoSistema"], "tempoDeChegadaDoJob": tempoDeChegadaDoJob} # Criando o dicionario que ira representar um job no sistema.
#         filaServidor1.put(job) # Adicionando esse novo job na fila do servidor 1.

def geradorTemposServicos(situacao, servidor):
    if situacao == 1:
        return lambda: [0.4, 0.6, 0.95][servidor - 1]
    elif situacao == 2:
        return lambda: random.uniform(0.1,[0.7, 1.1, 1.8][servidor - 1])
    elif situacao == 3:
        return lambda: random.expovariate(1/[0.4, 0.6, 0.95][servidor - 1])

def simula(situacao, taxaDeChegada, tempoDeSimulacao, qtdJobsWarmUp):

    global servidor2, servidor3 # Cria globalmente os servidores 2 e 3. Nao foi necessario criar o servidor 1 pois ele nao e utilizado fora do escopo da funcao simula.

    env = simpy.Environment() # Inicia o Environment do Scimpy.
    statusSistema = {"qtdJobsNoSistema": 0} # Inicialmente nao temos nenhum job no sistema.

    servidor1 = Servidor(env, "Servidor1", geradorTemposServicos(situacao, 1)) 
    servidor2 = Servidor(env, "Servidor2", geradorTemposServicos(situacao, 2))
    servidor3 = Servidor(env, "Servidor3", geradorTemposServicos(situacao, 3))

    env.process(geradorChegadasJobs(env, taxaDeChegada, servidor1.fila, statusSistema)) # Inicia o processo de chegada de jobs ao sistema.

    env.run(until=tempoDeSimulacao) # Define o tempo que o ambiente de simulacao ira funcionar.

    temposNoSistema = [job["tempoDeSaidaDoJob"] - job["tempoDeChegadaDoJob"] for job in servidor2.statusSistema["saidas"][qtdJobsWarmUp:] + servidor3.statusSistema["saidas"][qtdJobsWarmUp:]] # Descarta o tempo de sistema dos qtdJobsWarmUp sejam descartados.
    tempoMedioNoSistema = np.mean(temposNoSistema)
    desvioPadraoTempMedSis = np.std(temposNoSistema)
    qtdJobs = statusSistema["qtdJobsNoSistema"]
    return tempoMedioNoSistema, desvioPadraoTempMedSis, qtdJobs

# Configuracoes para simular
taxaDeChegada = 2
tempoDeSimulacao = 100000 # Essa variavel e a quantidade de tempo que o ambiente de simulacao sera executado.
qtdJobsWarmUp = 10000 # Essa variavel pode ser alterada, mas com a observacao que nao podemos definir uma quantidade de warm up tao proxima do tempo de simulacao.

# Executa a simulação para cada cenário
for situacao in [1, 2, 3]:
    media, desvioPadrao, qtdJobsNoSistema = simula(situacao, taxaDeChegada, tempoDeSimulacao, qtdJobsWarmUp)
    print(f"Situacao {situacao}: Tempo Medio de Sistema = {round(media, 4)}s, Desvio Padrao Tempo Medio de Sistema = {round(desvioPadrao, 4)}s com {qtdJobsNoSistema} jobs que passaram pela Rede de Filas.")
