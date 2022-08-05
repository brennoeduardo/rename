import os
import shutil

folder = os.chdir('C://Users//user//Downloads') # Pasta fonte aonde se encontra os arquivos baixados



# Função para excluir os arquivos existentes e renomea-los conforme seu nome
def renomear_loop():
    os.remove('C://Users//user//Prime Control//Controladoria - General//Controladoria//2022//04 - Reportes Mensais//Validação de Horas//1 - Ocorrências.csv')
    os.remove('C://Users//user//Prime Control//Controladoria - General//Controladoria//2022//04 - Reportes Mensais//Validação de Horas//2 - Solicitações.csv')
    os.remove('C://Users//user//Prime Control//Controladoria - General//Controladoria//2022//04 - Reportes Mensais//Validação de Horas//5 - Rabbiit.csv')
    os.remove('C://Users//user//Prime Control//Controladoria - General//Controladoria//2022//04 - Reportes Mensais//Validação de Horas//ex - Pontomais-decimal.csv')
    for arquivo in os.listdir(folder):
        if 'Ocorrências' in arquivo:
            os.rename(arquivo, '1 - Ocorrências.csv')
        if 'Solicitações' in arquivo:
            os.rename(arquivo, '2 - Solicitações.csv')
        if 'rabbiit' in arquivo:
            os.rename(arquivo, '5 - Rabbiit.csv')
        if 'Resumo_da_jornada' in arquivo:
            os.rename(arquivo, 'ex - Pontomais-decimal.csv')


renomear_loop()

# Código para mover da pasta onde foi baixado para a pasta certa
source = r'C://Users//user//Downloads'
destination = r'C://Users//user//Prime Control//Controladoria - General//Controladoria//2022//04 - Reportes Mensais//Validação de Horas'
files = os.listdir(source)
for file in files:
    new_path = shutil.move(f"{source}/{file}", destination)
    print(new_path)

