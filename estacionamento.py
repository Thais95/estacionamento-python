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
        
    def ocupar(self, placa):
        if self.livre:
            self.veiculo_estacionado = placa
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
            return print(f'Carro {carro.placa} já está estacionado.')
        
        if self.vagas_livres['Carro'] == 0:
            return print(f'[Carro {carro.placa}]: Não há vagas disponíveis.')
        
        for vaga in self.vagas['Carro']:
            if vaga.livre:
                vaga.ocupar(carro.placa)
                carro.estacionar()
                self.vagas_livres['Carro'] -= 1
                return print(f'[Carro {carro.placa}]: Foi estacionado na vaga {vaga.id}.')
            
    def remover_carro(self, carro):
        if not carro.estacionado:
            return print(f'Carro {carro.placa} não está estacionado.')
        
        for vaga in self.vagas['Carro']:
            if vaga.veiculo_estacionado == carro.placa:
                vaga.desocupar()
                carro.sair_da_vaga()
                self.vagas_livres['Carro'] += 1
                return print(f'Carro {carro.placa} saiu da vaga {vaga.id}.')
            
    
    def estacionar_moto(self, moto):
        if moto.estacionado:
            return print(f'Moto {moto.placa} já está estacionado.')
        
        tipo_da_vaga = ''
        
        if self.vagas_livres['Moto']:
            tipo_da_vaga = 'Moto'
        elif self.vagas_livres['Carro']:
            tipo_da_vaga = 'Carro'
        else:
            return print(f'Moto {moto.placa} não estacionou pois não há vagas disponíveis.')
        
        for vaga in self.vagas[tipo_da_vaga]:
            if vaga.livre:
                vaga.ocupar(moto.placa)
                moto.estacionar(tipo_da_vaga)
                self.vagas_livres[tipo_da_vaga] -= 1
                return print(f'[Moto {moto.placa}]: Foi estacionado na vaga {vaga.id}.')
        
    def remover_moto(self, moto):
        if not moto.estacionado:
            return print(f'Moto {moto.placa} não está estacionada.')
        
        for vaga in self.vagas[moto.tipo_da_vaga]:
            if vaga.veiculo_estacionado == moto.placa:
                self.vagas_livres[moto.tipo_da_vaga] += 1
                vaga.desocupar()
                moto.sair_da_vaga()
                return print(f'Moto {moto.placa} saiu da vaga {vaga.id}.')
            
    
    def __str__(self):        
        return f"""[Status do estacionamento]
Total de vagas livres: {self.vagas_livres['Carro']+self.vagas_livres['Moto']}
Vagas de carro livres: {self.vagas_livres['Carro']}
Vagas de moto livres: {self.vagas_livres['Moto']}
"""



carro_azul = Carro('298283')
estacionamento = Estacionamento(25, 25)
estacionamento.estacionar_carro(carro_azul)
estacionamento.remover_carro(carro_azul)
estacionamento.estacionar_carro(carro_azul)
moto_rosa = Moto('828SJ2')
estacionamento.estacionar_moto(moto_rosa)
estacionamento.remover_moto(moto_rosa)
estacionamento.estacionar_moto(moto_rosa)
print(estacionamento)