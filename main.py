from pathlib import Path
import shutil
from datetime import datetime

shutil.unpack_archive('organizador.zip', 'arquivos')

for arquivo in Path("arquivos").glob("*.pdf"):
    
