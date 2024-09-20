# tests/test_youtube_audio.py
import unittest
import os
from extrator_audio.doau import extrair_audio

class TestYouTubeAudio(unittest.TestCase):
    def test_extrair_audio(self):
        # Exemplo de URL de teste (substitua por uma URL válida para realizar o teste)
        url = "https://www.youtube.com/watch?v=adV8-_hgL4g"
        
        # Diretório temporário para salvar o arquivo de áudio
        caminho_saida = "C:\Users\Joao Victor\Downloads"
        
        # Executar a função de extração de áudio
        resultado = extrair_audio(url, caminho_saida=caminho_saida)
        
        # Verificar se o arquivo foi criado corretamente
        self.assertIsNotNone(resultado)
        self.assertTrue(resultado.endswith('.mp3'))
        self.assertTrue(os.path.exists(resultado))

        # Limpar após o teste (remover o arquivo gerado)
        os.remove(resultado)

if __name__ == '__main__':
    unittest.main()
