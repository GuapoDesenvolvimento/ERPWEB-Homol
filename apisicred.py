import requests

# Configurações
client_id = "SEU_CLIENT_ID"
client_secret = "SEU_CLIENT_SECRET"
cert_path = "caminho/para/seu_certificado.pem"
key_path = "caminho/para/sua_chave_privada.pem"
# base_url = "https://api.sicredi.com.br/pix"  # Verifique o endpoint correto na documentação oficial
base_url = 'https://api-pix-h.sicredi.com.br' # URL de Homol

# Função para obter o token de acesso
def obter_token():
    # url = f"{base_url}/oauth/token"
    url = f"{base_url}/oauth/token?grant_type=client_credentials&scope=cob.write+cob.read+webhook.read+webhook.write"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}
    
    try:
        response = requests.post(
            url,
            headers=headers,
            data=data,
            auth=(client_id, client_secret),
            cert=(cert_path, key_path),
            timeout=10  # Timeout para evitar travamentos
        )
        
        response.raise_for_status()  # Levanta exceções para códigos de erro HTTP
        return response.json().get("access_token")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter token: {e}")
        return None

# Função para consultar uma cobrança Pix
def consultar_pix(token, txid):
    if not token:
        print("Token inválido ou não obtido.")
        return None

    url = f"{base_url}/v2/cob/{txid}"  # Endpoint para consultar cobrança
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(
            url,
            headers=headers,
            cert=(cert_path, key_path),
            timeout=10  # Timeout para evitar travamentos
        )
        response.raise_for_status()  # Levanta exceções para códigos de erro HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na consulta Pix: {e}")
        return None

# Função principal para execução do programa
def main():
    try:
        token = obter_token()
        if not token:
            print("Não foi possível obter o token. Verifique as configurações e tente novamente.")
            return

        txid = "EXEMPLO_TXID"  # Substitua pelo TXID real
        resultado = consultar_pix(token, txid)
        if resultado:
            print("Resultado da consulta:", resultado)
        else:
            print("Não foi possível realizar a consulta Pix.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Execução do programa
if __name__ == "__main__":
    main()
