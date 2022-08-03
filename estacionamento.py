class Veiculo:
    def __init__(self, placa, tipo):
        self.placa = placa
        self.estacionado = False
        self.tipo = tipo
        
    def andar(self):
        print(f'{self.tipo} andou')
        

class Carro(Veiculo):
    def __init__(self, placa):
        super().__init__(placa, 'Carro')        
        
    def estacionar(self):
        if self.estacionado == False:
            self.estacionado = True
            print('Carro - Vaga estacionada')
            

class Moto(Veiculo):
    def __init__(self, placa):
        super().__init__(placa, 'Moto')        
        
    def estacionar(self):
        if self.estacionado == False:
            self.estacionado = True
            print('Moto - Vaga estacionada')

            
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
            print(f'Vaga {self.id} ocupada por {self.veiculo_estacionado}.')
            
    def desocupar(self):
        if not self.livre:
            self.livre = True
            self.veiculo_estacionado = None
            print(f'Vaga {self.id} desocupada.')
            
            
class Estacionamento:
    def __init__(self, numero_vagas_carro, numero_vagas_moto):
        self.vagas = {
            'Carro': [],
            'Moto': []
        }
        
        for id in range (1, numero_vagas_carro+1):
            self.vagas['Carro'].append(Vaga(id, 'Carro'))
            
        for id in range (numero_vagas_carro+1, numero_vagas_carro + numero_vagas_moto+1):
            self.vagas['Moto'].append(Vaga(id, 'Moto'))
            
            
Estacionamento_novo = Estacionamento(25, 25)
Estacionamento_novo.vagas['Carro'][4].ocupar('0292193')
Estacionamento_novo.vagas['Carro'][4].desocupar()