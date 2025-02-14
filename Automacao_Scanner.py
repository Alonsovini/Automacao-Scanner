# Limpar Pasta FilaScanner

import shutil
import os
import time
import schedule

# Caminho da pasta que terá o conteúdo excluído
caminho_para_excluir = r'Y:'

# Caminho da pasta que será copiada
caminho_para_copiar = r'C:\Users\vinicius.alonso\Downloads\Scanner'

    # Função para excluir todo o conteúdo da pasta
def excluir_conteudo_pasta(caminho):
    for filename in os.listdir(caminho):
        try:
            file_path = os.path.join(caminho, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Exclui arquivo ou link simbólico
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Exclui diretório
        except Exception as e:
            print(f'Erro ao excluir {file_path}. Razão: {e}')

# Função para copiar todo o conteúdo de uma pasta para outra
def copiar_conteudo_pasta(origem, destino):
    try:
        shutil.copytree(origem, destino, dirs_exist_ok=True)
    except Exception as e:
        print(f'Erro ao copiar conteúdo de {origem} para {destino}. Razão: {e}')

def tarefa_semanal():
    # Executa as funções
    excluir_conteudo_pasta(caminho_para_excluir)
    copiar_conteudo_pasta(caminho_para_copiar, caminho_para_excluir)
    print("Processo concluído, Pasta da FilaScanner Zerada.")

schedule.every().friday.at("17:50").do(tarefa_semanal)

# Mantém o código rodando para verificar o agendamento
while True:
    schedule.run_pending()
    time.sleep(60)

