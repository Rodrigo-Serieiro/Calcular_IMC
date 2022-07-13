from datetime import date
from datetime import timedelta
import time

print("*****Calculando IMC*****")

soma_dia = timedelta(days=30)
data = date.today()
dia = (soma_dia + data)
resultado = dia.strftime('%d/%m/%y')


def calcular():
    altura = float(input('qual sua altura em cm: '))
    peso = float(input('qual eu peso em KG: '))
    IMC = peso / (altura/100)**2
    IMC_format = "{:.2f}".format(IMC)
    print('Calculando...')
    time.sleep(1.5)

    if IMC < 18.5:
        print(f'Seu IMC é de {IMC_format} e é classificado como magreza')

    elif IMC >= 18.5 and IMC < 24.9:
        print(f'Seu IMC é de {IMC_format} e é classificado como normal')

    elif IMC >= 25 and IMC < 29.9:
        print(f'Seu IMC é de {IMC_format} e é classificado como sobrepeso')

    elif IMC >= 30 and IMC < 39.9:
        print(f'Seu IMC é de {IMC_format} e é classificado como obesidade')

    else:
        print(
            f'Seu IMC é de {IMC_format} pode parar de comer, negocio ta feio')


def marcar_retorno():
    retorno = input('deseja marcar retorno? digite[s/n]')
    while retorno == "n":
        repetir()
        break
    else:
        print(f"Retorne na data {resultado} para uma nova consulta.")
        repetir()


def repetir():
    Continuar = input('deseja consultar novamente? digite[s/n]')
    while Continuar == "s":
        print("*****Calculando IMC*****")
        calcular(), marcar_retorno()
        break
    else:
        print("você saiu!")


calcular()
marcar_retorno()
