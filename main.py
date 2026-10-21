import os
import shutil

pasta = "C:/Users/keisyyDU/Downloads"

GAVETAS = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Musicas": [".mp3", ".wav"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Instaladores": [".exe", ".msi"]
}

arquivos = os.listdir(pasta)

for arquivo in arquivos:
    caminho_antigo = os.path.join(pasta, arquivo)

    if os.path.isdir(caminho_antigo):
        continue

    nome, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()

    pasta_destino_nome = None
    for nome_da_gaveta, lista_de_extensoes in GAVETAS.items():
        if extensao in lista_de_extensoes:
            pasta_destino_nome = nome_da_gaveta
            break

    if pasta_destino_nome:
        pasta_destino = os.path.join(pasta, pasta_destino_nome)
        os.makedirs(pasta_destino, exist_ok=True)

        caminho_novo = os.path.join(pasta_destino, arquivo)
        shutil.move(caminho_antigo, caminho_novo)
        print(f"Organizado: {arquivo} ➡️ {pasta_destino_nome}")

print("✨ Limpeza concluída com sucesso! ✨")





