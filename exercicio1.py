# Um novo paciente chamada João deu entrada no hospital.
# Ele tem 20 anos e é um novo paciente
# Defina variáveis para armazenar o nome desse paciente,
# sua idade e se ele é um novo paciente
# Mostre as informações coletadas


nome_paciente = 'João' #str
idade = 20 #int
novo_paciente = True
mensagem = 'o paciente ' + nome_paciente + ' de ' + str(idade) + ' anos'


if(novo_paciente):
    print(mensagem + 'é um novo paciente')
else:
    print(mensagem + 'NÃO é um novo paciente')
