# 🧹 Organizador Automático de Arquivos em Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

Um script de automação em Python que varre diretórios desorganizados (como a pasta **Downloads**) e separa automaticamente os arquivos em categorias específicas, mantendo o computador limpo e organizado.

---

## 🚀 Como Funciona?

O script lê todos os arquivos da pasta informada, analisa a extensão de cada item e move automaticamente para a pasta correspondente:

| Pasta de Destino | Tipos de Arquivos Suportados |
| :--- | :--- |
| **📁 Imagens** | `.png`, `.jpg`, `.jpeg`, `.gif` |
| **📁 Documentos** | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx` |
| **📁 Vídeos** | `.mp4`, `.mkv`, `.avi` |
| **📁 Músicas** | `.mp3`, `.wav` |
| **📁 Compactados** | `.zip`, `.rar`, `.7z` |
| **📁 Instaladores** | `.exe`, `.msi` |

> 🛡️ **Segurança:** O script não mexe em pastas já existentes, evitando alterações indesejadas na estrutura do sistema.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Módulo `os`:** para leitura do diretório, identificação de pastas e criação de novos diretórios.
* **Módulo `shutil`:** para a movimentação segura dos arquivos no disco.

---

## 💻 Como Executar no seu Computador

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/SEU-USUARIO/organizador-arquivos-python.git