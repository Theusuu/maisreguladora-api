from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo de dados esperado
class DataModel(BaseModel):
    id: int
    name: str
    funcionario: str
    carro: str
    value: float
    timestamp: str

# Endpoint para recepcionar os dados
@app.post("/receber-dados")
async def receive_data(data: DataModel):
    """
    Recebe os dados enviados via integração e processa.
    """
    # Aqui você pode tratar os dados como necessário
    # Por exemplo, salvar em um banco de dados ou realizar cálculos
    processed_data = {
        "ID": data.id,
        "Nome": data.name.upper(),
        "Funcionário": data.funcionario,
        "Carro": data.carro,
        "Valor": data.value * 2,
        "Data": data.timestamp,
    }

    # Retorna uma resposta ao cliente
    return {
        "status": "success",
        "message": "Dados processados com sucesso.",
        "processed_data": processed_data,
    }

# Endpoint de teste
@app.get("/")
def home():
    return {"message": "Web service funcionando!"}