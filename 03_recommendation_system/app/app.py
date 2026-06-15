from fastapi import FastAPI, HTTPException
import joblib
from pathlib import Path

app = FastAPI()

# Carrega o modelo a partir do mesmo diretório deste arquivo
model_path = Path(__file__).resolve().parent / "recomendador_ceaps.sav"
if not model_path.exists():
    raise FileNotFoundError(f"Modelo não encontrado em {model_path}")
modelo = joblib.load(model_path)

similaridade_df = modelo["similaridade"]
matriz_interacoes = modelo["matriz"]

def recomendar_senadores(nome_senador, top_n=5):

    if nome_senador not in similaridade_df.index:
        raise KeyError(f"Senador '{nome_senador}' não encontrado.")

    serie = similaridade_df[nome_senador]

    similares = (
        serie.sort_values(ascending=False)
        .iloc[1:top_n+1]
    )

    senadores_similares = similares.index.tolist()

    despesas_media = (
        matriz_interacoes.loc[senadores_similares]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )

    return {
        "input": nome_senador,
        "similares": [
            {"senador": s, "similaridade": float(similares[s])}
            for s in senadores_similares
        ],
        "top_despesas": [
            {"tipo_despesa": d, "valor_medio": float(v)}
            for d, v in despesas_media.items()
        ]
    }

@app.get("/")
def home():
    return {"status": "API rodando"}

@app.get("/recomendar/{senador}")
def recomendar(senador: str):
    try:
        return recomendar_senadores(senador)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))