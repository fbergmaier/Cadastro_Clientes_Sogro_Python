from datetime import datetime
from winotify import Notification, audio
import os

# Define a pasta onde estão os arquivos (ajuste para o seu caminho)
DIRETORIO = r"C:\Users\Admin\Desktok\SISTEMA"
ARQUIVO_TXT = os.path.join(DIRETORIO, "aniversarios.txt")

# Pega o dia e mês atual no formato DD/MM (ex: "03/10")
hoje = datetime.now().strftime("%d/%m")

# Verifica se o arquivo de aniversários existe
if os.path.exists(ARQUIVO_TXT):
    with open(ARQUIVO_TXT, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    
    # Procura aniversariantes do dia
    linhas_notificacao = []
    for linha in linhas:
        if "," in linha:
            partes = [p.strip() for p in linha.split(",")]
            
            # Garante que a linha tem os 3 elementos (Nome, Data, Telefone)
            if len(partes) >= 3:
                nome, data, telefone = partes[0], partes[1], partes[2]
                
                if data == hoje:
                    # Cria uma linha formatada para a mensagem
                    linhas_notificacao.append(f"{nome} ({data}) - Tel: {telefone}")
    
    # Se houver aniversariantes, envia a notificação
    if os.path.exists(ARQUIVO_TXT) and linhas_notificacao:
        # Junta todos os aniversariantes separados por uma quebra de linha
        mensagem_final = "\n".join(linhas_notificacao)
        
        toast = Notification(
            app_id="Lembrete de Aniversário",
            title="Aniversariante(s) de Hoje!",
            msg=mensagem_final,
            duration="long"
        )
        toast.set_audio(audio.Reminder, loop=False)
        toast.show()
