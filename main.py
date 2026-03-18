from pathlib import Path
import shutil
from datetime import datetime

if not Path("arquivos").exists():
    shutil.unpack_archive('organizador.zip', 'arquivos')

for arquivo in Path("arquivos").glob("*"):
    if arquivo.glob("*.pdf"):
        pdf = Path("arquivos/pdf")
        pdf.mkdir(parents=True, exist_ok=True)
        shutil.move(arquivo, pdf)
    

    
