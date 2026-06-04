from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Definimos cómo se ven los datos
class SolicitudCredito(BaseModel):
    edad: int
    ingresos: float
    deudas: float

@app.get("/")
def read_root():
    return {"mensaje": "API de FinTech Nova - Laboratorio 1 Activo"}

# 1. Endpoint de Monitoreo (VERDE)
@app.get("/status")
def get_status():
    return {"status": "healthy", "version": "1.0"}

# 2. Endpoint Principal (AZUL) - Evalua riesgo
@app.post("/evaluar-riesgo")
def evaluar_riesgo(data: SolicitudCredito):
    # Lógica simple para el laboratorio
    if data.ingresos > (data.deudas * 2) and data.edad >= 18:
        return {"resultado": "Aprobado"}
    elif data.ingresos > data.deudas:
        return {"resultado": "En Revision"}
    else:
        return {"resultado": "Rechazado"}

# 3. Endpoint Vulnerable (ROJO) - Sin Autenticación
@app.get("/datos-financieros/{id}")
def get_datos_financieros(id: str):
    # ⚠️ VULNERABLE: Cualquiera puede acceder sin contraseña
    return {
        "id_cliente": id, 
        "advertencia": "ENDPOINT VULNERABLE - SIN AUTENTICACION",
        "saldo": 5000.00,
        "ultimos_movimientos": ["Compra Tienda", "Pago Nomina"]
    }