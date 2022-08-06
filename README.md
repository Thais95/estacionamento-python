# Exemplos de OO em Python
#### Estacionamento com gerenciamento de vagas para carros e motos
<br />

### Para rodar o script
```python
python main.py
```

### Criando um novo lote no estacionamento
```python
# (quantidade de vagas de carro, quantidade de vagas de moto)
nome_estacionamento = Estacionamento(5, 5)
```

### Criando um carro ou moto
```python
nome_carro = Carro('Placa do carro')
nome_moto = Moto('Placa da Moto')
```

### Estacionando e removendo das vagas
```python
nome_estacionamento.estacionar_carro(nome_carro)
nome_estacionamento.estacionar_moto(nome_moto)

nome_estacionamento.remover_carro(nome_carro)
nome_estacionamento.remover_moto(nome_moto)
```

### Vendo o relatório geral do estacionamento
```python
print(nome_estacionamento)
```