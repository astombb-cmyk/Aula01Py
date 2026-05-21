import requests
import pandas as pd

# Exemplo de endpoint fictício de API
API_URL = "https://api.exemplo.com/vendas"
API_KEY = "SUA_CHAVE_API"

# Função para buscar dados da API
def get_sales_data():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        print("Erro ao acessar API:", response.status_code)
        return pd.DataFrame()

# Função para calcular lucro
def calculate_profit(df):
    df["lucro"] = df["preco_venda"] - df["custo"]
    return df

# Função para otimizar rotas (exemplo simples)
def optimize_routes(df):
    # Aqui você poderia integrar com Google Maps API ou OR-Tools
    # Exemplo fictício: ordenar entregas por distância
    df = df.sort_values("distancia_km")
    return df

def main():
    # 1. Buscar dados
    vendas = get_sales_data()
    if vendas.empty:
        return
    
    # 2. Calcular lucro
    vendas = calculate_profit(vendas)
    
    # 3. Otimizar rotas
    vendas = optimize_routes(vendas)
    
    # 4. Mostrar resultados
    print("📊 Relatório de Vendas e Lucro")
    print(vendas[["cliente", "produto", "preco_venda", "custo", "lucro", "distancia_km"]])

if __name__ == "__main__":
    main()
