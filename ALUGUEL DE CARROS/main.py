taxa = 75.00

def comeco ():
    print('LOCADORA DE AUTOMÓVEIS')
    print('='*22)


def valor_veiculo(dinheiro):
    dinheiro = '%.2f' % dinheiro
    return 'R$ '+ str(dinheiro).replace('.',',')

def opcoes_all(opcao,diarias):

    contrato_ctr[opcao] = opcionais[opcao]

def pular():
    return '='*60 + '\n'

def arquivos(categoria,diarias,total_a,total_seguro,total):
    with open('aluguel.txt','w') as gravacao:
        gravacao.write('Tipo de Carro: ')
        gravacao.write(categoria + '\n')
        gravacao.write(str(diarias) + 'Diarias' + '\t\t\t' + 'total' + '\n')
        gravacao.write(str(diarias)+ 'x' + valor_veiculo(categoria[categoria])+ '\t\t\t\t' + str(total_a) +
                       '\n')
        gravacao.write(str(pular()))
        gravacao.write('Seguro do Carro' + '\n')
        gravacao.write(str(diarias)+ ' x ' + valor_veiculo(seguro_veiculo[categoria]
                       ))
        gravacao.write(str(pular()))
        for op,valor in contrato_ctr.items():
            gravacao.write(str(op)+ '-' + str(diarias) + 'x R$' + valor_veiculo(valor) + '\t\t' +
                           valor_veiculo(diarias*valor) + '\n')
        gravacao.write(str(pular()))
        gravacao.write('Taxa Administrativa' + valor_veiculo(taxa))
        gravacao.write('\n\n')
        gravacao.write('Total do alguel' + '\t\t\t' + total)
        gravacao.close()

categorias = {
    'Economico': 35.9,
    'Sedan': 49.9,
    'SUV': 84.9
}
seguro_veiculo = {
    'Economico': 9,
    'Sedan': 13,
    'SUV': 20

}

opcionais = {
    'GPS': 12,
    'Bebê Conforto': 15,
    'Cadeira de bebê': 15,
    'Assento de Elevação': 12
}

contrato_ctr = {}

comeco()
print('Infome a Categoria deseja alugar o carro ?')

for chave in categorias.keys():
    print(f'- {chave}')

diaria = input('Escolha: ')
qtde_diarias = int(input('Quantas Diarias ?'))
total_aluguel = qtde_diarias * categorias[diaria]
seguro = qtde_diarias * seguro_veiculo[diaria]

op = input('Voce deseja opcionais ? [S/N]:')
if op[0] in 'Ss':
    while True:
        for chave in opcionais.keys():
            print(f'- {chave}')
        extra = input()
        opcoes_all(extra, qtde_diarias)
        continua = input('Deseja adicionar outro opcional? [S/N] ')
        if continua in 'Nn':
            break
total_geral = total_aluguel + seguro + taxa
for o in contrato_ctr.values():
    total_geral += o * qtde_diarias

arquivos (diaria, qtde_diarias, valor_veiculo(total_aluguel), valor_veiculo(seguro),
               valor_veiculo(total_geral))



















