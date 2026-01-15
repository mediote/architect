# Architect

## Agente de Clima (MAF)

Este projeto agora inclui um **Agente de Clima** utilizando um modelo simples de **MAF (Multi-Agent Framework)**.

O agente segue o ciclo clássico:
- **Perceber** (consultar API de clima)
- **Decidir** (interpretar dados)
- **Agir** (retornar resposta textual)

### Requisitos

```bash
pip install requests
```

### Variável de ambiente

Configure a chave da API OpenWeather:

```bash
export OPENWEATHER_API_KEY="sua_chave_aqui"
```

### Executar

```bash
python src/agent_clima.py
```

---

Projeto base para experimentos de arquitetura, agentes e organização de código.