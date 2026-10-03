from datetime import datetime
from winotify import Notification, audio
import os
import sys

# BLINDAGEM DO CAMINHO: Descobre automaticamente a pasta onde o executável está rodando
if getattr(sys, 'frozen', False):
    # Se for um executável .exe, usa a pasta do .exe
    DIRETORIO = os.path.dirname(sys.executable)
else:
    # Se for o script .py original, usa a pasta do script
    DIRETORIO = os.path.dirname(os.path.abspath(__file__))

ARQUIVO_TXT = os.path.join(DIRETORIO, "aniversarios.txt")

# Pega o dia e mês atual no formato DD/MM (ex: "03/10")
hoje = datetime.now().strftime("%d/%m")

try:
    # Verifica se o arquivo de aniversários existe
    if os.path.exists(ARQUIVO_TXT):
        with open(ARQUIVO_TXT, "r", encoding="utf-8") as f:
            linhas = f.readlines()
        
        linhas_notificacao = []
        for linha in linhas:
            if "," in linha:
                # Remove espaços em branco
                partes = [p.strip() for p in linha.split(",")]
                
                # CORREÇÃO: Garante que a linha tem exatamente os 3 elementos e distribui da forma correta
                if len(partes) >= 3:
                    nome = partes[0]
                    data = partes[1]
                    telefone = partes[2]
                    
                    if data == hoje:
                        linhas_notificacao.append(f"🎁 {nome} ({data}) - Tel: {telefone}")
        
        # Se houver aniversariantes, envia a notificação
        if linhas_notificacao:
            mensagem_final = "\n".join(linhas_notificacao)
            
            toast = Notification(
                app_id="Lembrete de Aniversário",
                title="🎈 Aniversariante(s) de Hoje!",
                msg=mensagem_final,
                duration="long"
            )
            toast.set_audio(audio.Reminder, loop=False)
            toast.show()
    else:
        # Se o arquivo .txt não for encontrado, avisa na tela para você saber onde ele deveria estar
        print(f"Erro: O arquivo '{ARQUIVO_TXT}' nao foi encontrado!")
        input("\nPressione Enter para fechar...") # Evita que a janela feche direto no teste manual

except Exception as e:
    # Se der qualquer outro erro interno, mostra na tela em vez de apenas fechar
    print(f"Ocorreu um erro no programa: {e}")
    input("\nPressione Enter para fechar...")
