from classes import Estacionamento, Carro, Moto

# EXEMPLOS

# Criando um lote no estacionamento (quantidade de vagas de carro, quantidade de vagas de moto)
estacionamento = Estacionamento(5, 5)

# Criando um carro, estacionando e removendo da vaga
carro_azul = Carro('KPB-3944')
estacionamento.estacionar_carro(carro_azul)
estacionamento.remover_carro(carro_azul)

# Criando um carro e o deixando estacionado
carro_preto = Carro('KZD-8380')
estacionamento.estacionar_carro(carro_preto)

# Criando motos e estacionando / removendo
moto_rosa = Moto('LQD-9413')
moto_dourada = Moto('KQW-5409')
estacionamento.estacionar_moto(moto_rosa)
estacionamento.estacionar_moto(moto_dourada)
estacionamento.remover_moto(moto_rosa)
estacionamento.estacionar_moto(moto_rosa)

# Para ver o relatório do estacionamento
print(estacionamento)
