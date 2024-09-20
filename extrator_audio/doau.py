import yt_dlp

def extrair_audio(url, caminho_saida="."):
    """
    Faz o download de um vídeo do YouTube e extrai o áudio em formato MP3.
    
    parametro url: A URL do vídeo do YouTube.
    parametro caminho_saida: O diretório onde o arquivo de áudio será salvo.
    return: O caminho do arquivo de áudio salvo.
    """
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{caminho_saida}/%(title)s.%(ext)s'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Áudio extraído com sucesso.")
    except Exception as e:
        print(f"Erro ao tentar baixar o áudio: {e}")

