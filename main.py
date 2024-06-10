from forex_python.converter import CurrencyRates

valor = str(input('Informe o valor a ser convertido ou Enter para encerrar o programa: '))
valor = float(valor.replace(',', '.'))
moeda_origem = input('Digite a moeda de origem (exemplo: USD, EUR, BRL): ').upper()
moeda_destino = input('Digite a moeda de destino (exemplo: USD, EUR, BRL): ').upper()

# faz a conversão
resultado = CurrencyRates().convert(moeda_origem, moeda_destino, valor)

# exibe o resultado na tela
print(f'$ {valor:,2f} {moeda_origem} = $ {resultado:,.2f} {moeda_destino}.')