class Veiculo:
    def __init__(self, placa, tipo):
        self.placa = placa
        self.estacionado = False
        self.tipo = tipo


class Carro(Veiculo):
    def __init__(self, placa):
        super().__init__(placa, 'Carro')
        
    def estacionar(self):
        if not self.estacionado:
            self.estacionado = True
            
    def sair_da_vaga(self):
        if self.estacionado:
            self.estacionado = False
            

class Moto(Veiculo):
    def __init__(self, placa):
        super().__init__(placa, 'Moto')
        self.tipo_da_vaga = None
        
    def estacionar(self, tipo_da_vaga):
        if not self.estacionado:
            self.estacionado = True
            self.tipo_da_vaga = tipo_da_vaga
            
    def sair_da_vaga(self):
        if self.estacionado:
            self.estacionado = False
            self.tipo_da_vaga = None

            
class Vaga:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
        self.veiculo_estacionado = None
        self.livre = True
        
    def ocupar(self, veiculo):
        if self.livre:
            self.veiculo_estacionado = veiculo
            self.livre = False
            
    def desocupar(self):
        if not self.livre:
            self.livre = True
            self.veiculo_estacionado = None
            
            
class Estacionamento:
    def __init__(self, numero_vagas_carro, numero_vagas_moto):
        self.vagas_livres = {
            'Carro': numero_vagas_carro,
            'Moto': numero_vagas_moto
        }
        self.vagas = {
            'Carro': [],
            'Moto': []
        }
        
        for id in range (1, numero_vagas_carro+1):
            self.vagas['Carro'].append(Vaga(id, 'Carro'))
            
        for id in range (numero_vagas_carro+1, numero_vagas_carro + numero_vagas_moto+1):
            self.vagas['Moto'].append(Vaga(id, 'Moto'))
            
    
    def estacionar_carro(self, carro):
        if carro.estacionado:
            return print(f'Carro [placa {carro.placa}] já está estacionado.')
        
        if self.vagas_livres['Carro'] == 0:
            return print(f'Carro [placa {carro.placa}] não estacionou pois não há vagas disponíveis.')
        
        for vaga in self.vagas['Carro']:
            if vaga.livre:
                vaga.ocupar(carro)
                carro.estacionar()
                self.vagas_livres['Carro'] -= 1
                return print(f'Carro [placa {carro.placa}] foi estacionado na vaga {vaga.id}.')
            
    def remover_carro(self, carro):
        if not carro.estacionado:
            return print(f'Carro [placa {carro.placa}] não está estacionado.')
        
        for vaga in self.vagas['Carro']:
            if vaga.veiculo_estacionado == carro.placa:
                vaga.desocupar()
                carro.sair_da_vaga()
                self.vagas_livres['Carro'] += 1
                return print(f'Carro [placa {carro.placa}] saiu da vaga {vaga.id}.')
            
    
    def estacionar_moto(self, moto):
        if moto.estacionado:
            return print(f'Moto [placa {moto.placa}] já está estacionada.')
        
        tipo_da_vaga = ''
        
        if self.vagas_livres['Moto']:
            tipo_da_vaga = 'Moto'
        elif self.vagas_livres['Carro']:
            tipo_da_vaga = 'Carro'
        else:
            return print(f'Moto [placa {moto.placa}] não estacionou pois não há vagas disponíveis.')
        
        for vaga in self.vagas[tipo_da_vaga]:
            if vaga.livre:
                vaga.ocupar(moto)
                moto.estacionar(tipo_da_vaga)
                self.vagas_livres[tipo_da_vaga] -= 1
                return print(f'Moto [placa {moto.placa}] foi estacionada na vaga {vaga.id}.')
        
    def remover_moto(self, moto):
        if not moto.estacionado:
            return print(f'Moto [placa {moto.placa}] não está estacionada.')
        
        for vaga in self.vagas[moto.tipo_da_vaga]:
            if vaga.veiculo_estacionado == moto.placa:
                self.vagas_livres[moto.tipo_da_vaga] += 1
                vaga.desocupar()
                moto.sair_da_vaga()
                return print(f'Moto [placa {moto.placa}] saiu da vaga {vaga.id}.')
            
    
    def __veiculos_estacionados(self):
        string_carro = string_moto = ''
        quantidade_carro = quantidade_moto = 0
        for vaga in (self.vagas['Moto'] + self.vagas['Carro']):
            if vaga.livre:
                continue
            if vaga.veiculo_estacionado.tipo == 'Carro':
                string_carro += f"Vaga {vaga.id}: Placa {vaga.veiculo_estacionado.placa}\n"
                quantidade_carro += 1
            else:
                string_moto += f"Vaga {vaga.id}: Placa {vaga.veiculo_estacionado.placa}\n"
                quantidade_moto += 1
        return string_carro, string_moto, quantidade_carro, quantidade_moto
    
    
    def __str__(self):        
        string_carro, string_moto, quantidade_carro, quantidade_moto = self.__veiculos_estacionados()
        
        return f"""
[Relatório do estacionamento]

Total de vagas ocupadas: {quantidade_carro + quantidade_moto}
Total de vagas livres: {self.vagas_livres['Carro'] + self.vagas_livres['Moto']}
Vagas de carro livres: {self.vagas_livres['Carro']}
Vagas de moto livres: {self.vagas_livres['Moto']}

Carros estacionados ({quantidade_carro})
{string_carro}
Motos estacionadas ({quantidade_moto})
{string_moto}"""


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

print(estacionamento)