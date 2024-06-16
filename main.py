"""
Programa de cotação das principais moedas e conversão 
delas em qualquer outra moeda listada no programa

"""

from request import dolar, euro, libra
import os
import msvcrt

while True:
    os.system('cls')
    print("""
          _____COTAÇÃO E CONVERSÃO DE MOEDAS_____

          DIGITE UMA OPÇÃO:

          [1]- Cotação
          [2]- Conversão
          [3]- SAIR

          """)
    opcao = int(input(""))

    match(opcao):
        case 1:
            os.system('cls')
            print(f"""
            _____COTAÇÃO DE MOEDAS (MOEDA --> Real)_____ 

            - Dólar $ = R${dolar["value"]}
            - Euro € = R${euro["value"]}
            - Libra £ = R${libra["value"]}

            """)
            ch = msvcrt.getch()
            if ch == True:
                break
            else:
                continue
                
        case 2:
            while True:

                os.system('cls')
                print("""
            _____CONVERSÃO DE VALORES_____
            
            Converta outros valores em
            moeda estrangeira para o Real
            
            DIGITE A MOEDA A SER CONVERTIDA:
            
            [1]- Dólar
            [2]- Euro
            [3]- Libra
            [4]- SAIR
            
            """)
                opcao2 = int(input("Digite a opção:"))

                match(opcao2):
                    case 1:
                        os.system('cls')
                        valor_dolar = float(input(f"\nDigite o valor em dólar: $"))
                        dolar_to_real = float(dolar["value"].replace(",", ".")) * valor_dolar
                        print(f"\nValor do dólar hoje = R${float(dolar['value'].replace(',', '.'))}\nValor da conversão = R${dolar_to_real}\n")
                        ch = msvcrt.getch()
                        if ch == True:
                            break
                        else:
                            continue

                    case 2:
                        os.system('cls')
                        valor_euro = float(input(f"\nDigite o valor em euro: €"))
                        euro_to_real = float(euro["value"].replace(',', '.')) * valor_euro
                        print(f"\nValor do Euro hoje: €{float(euro['value'].replace(',', '.'))}\nValor da conversão = R${euro_to_real}\n")
                        ch = msvcrt.getch()
                        if ch == True:
                            break
                        else:
                            continue

                    case 3:
                        os.system('cls')
                        valor_libra = float(input(f"\nDigite o valor em libra: £"))
                        libra_to_real = float(libra["value"].replace(',', '.')) * valor_libra
                        print(f"\nValor da Libra Esterlina hoje: £{float(libra['value'].replace(',', '.'))}\nValor da conversão = R${libra_to_real}\n")
                        ch = msvcrt.getch()
                        if ch == True:
                            break
                        else:
                            continue

                    case 4:
                        break

                    case _:
                        print(f"\nOPÇÃO INVÁLIDA\n")
        case 3:
            print(f"\nPROGRAMA FINALIZADO!\n")
            break

        case _:
            print(f"\nOPÇÃO INVÁLIDA!\n")