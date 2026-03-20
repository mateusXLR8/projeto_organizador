from pathlib import Path
import shutil
from datetime import datetime

if not Path("organizador").exists():
    shutil.unpack_archive('organizador.zip', 'organizador')

if not Path("arquivos_organizados").exists():
    arquivos_organizados = Path("arquivos_organizados")
    arquivos_organizados.mkdir(exist_ok=True)

arquivos_movidos = 0
extensao_encontrada = []
for arquivo in Path("organizador").iterdir():
    extensao = arquivo.suffix.lower().replace(".", "")
    pasta_destino = arquivos_organizados/extensao
    pasta_destino.mkdir(exist_ok=True)
    shutil.move(str(arquivo), str(pasta_destino))
    arquivos_movidos += 1
    extensao_encontrada.append(extensao)
    hora = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    with open("registro.log", "a", encoding='utf-8') as registro:
        registro.write(f"{hora}, Nome do arquivo: {arquivo}, Destino final: {pasta_destino}\n")

print(f"Arquivos organizados: {arquivos_movidos}\nExtensões encontradas: {extensao_encontrada}")



    

    
