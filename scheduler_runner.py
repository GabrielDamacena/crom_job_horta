import requests
import logging
from datetime import datetime

# Configuração de logging
logging.basicConfig(
    filename='previsao_task.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def disparar_previsao_clima():
    logging.info("🚀 Iniciando disparo da previsão do clima...")

    try:
        response = requests.post(" https://backendhorta.onrender.com/api_horta/previsao-amanha/")
        logging.info(f"✅ Status da resposta: {response.status_code}")
        logging.debug(f"Conteúdo: {response.text}")
    except Exception as e:
        logging.error(f"❌ Erro ao enviar requisição: {e}")

if __name__ == "__main__":
    disparar_previsao_clima()
