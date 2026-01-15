# Climate Agent com MAF + FastAPI

Este projeto implementa um **Agente de Clima** seguindo o paradigma **MAF (Multi-Agent Framework)**, exposto via **FastAPI**.

## 🧠 Arquitetura MAF
- **Percepção**: coleta dados climáticos da OpenWeather API
- **Decisão**: interpreta dados atuais
- **Ação**: responde via API REST
- **Memória**: histórico temporal em memória

## 🚀 Execução

```bash
export OPENWEATHER_API_KEY=SUACHAVE
pip install fastapi uvicorn requests
uvicorn src.agent_clima:app --reload
```

## 📡 Endpoints
- `GET /climate` → clima atual
- `GET /memory` → memória interna do agente

## 📦 Extensões Futuras
- Persistência em banco
- Múltiplos agentes
- Planejamento e aprendizado

## ✅ Objetivo
Demonstrar agentes autônomos modulares aplicados a sistemas reais.
