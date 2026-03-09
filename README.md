# 🔍 SurfaceScan

Um **scanner de portas TCP** desenvolvido em Python, com foco em performance, organização de código e boas práticas profissionais.\
Projeto pensado para demonstrar habilidades em **redes, segurança, threading, design modular e uso real de CLI**.

---

## 🚀 Visão Geral

Esta ferramenta permite escanear portas TCP de um host, identificando portas abertas de forma **rápida e eficiente**, com suporte a:

- 🔹 Threading (scan paralelo)
- 🔹 Timeout configurável
- 🔹 Modo verbose
- 🔹 Exportação de resultados (JSON / CSV)
- 🔹 Estrutura modular (CLI + Library)

## 📦 Instalação

Instale diretamente via **pip**:

```bash
pip install surfacescan
```
### 2) Use a API Python diretamente

```python
from surfacescan import ScanConfig, parse_ports, run_scan, export_results

config = ScanConfig(
    host="scanme.nmap.org",
    ports=parse_ports("22,80,443,8080-8090"),
    timeout=1.0,
    threads=80,
)

results = run_scan(config)
paths = export_results(results, output_dir="./data/imports", base_name="scan-siem")

print(results)
print(paths)  # {'csv': '.../scan-siem.csv', 'json': '.../scan-siem.json'}
```

### 3) Integração sugerida no fluxo do SIEM

- Rodar `run_scan()` via job agendado.
- Persistir JSON bruto em storage de ingestão.
- Parsear eventos por porta/serviço no pipeline do SurfaceLog.
- Correlacionar com logs de firewall/IDS para alertas.

## 🖥️ Uso da Ferramenta (CLI)

### Execução básica

```bash
python -m surfacescan 127.0.0.1 -p 1-1000
```

### Com timeout customizado

```bash
python -m surfacescan 127.0.0.1 -p 1-1000 --timeout 1
```

### Modo verbose

```bash
python -m surfacescan 127.0.0.1 -p 1-1000 -v
```

### Exportação de resultados

```bash
# JSON
python -m surfacescan scanme.nmap.org -p 1-1000 --json

# CSV
python -m surfacescan scanme.nmap.org -p 1-1000 --csv
```

📁 Os arquivos são salvos automaticamente na pasta `scans/`.

---

## ⚙️ Tecnologias e Conceitos Utilizados

- Python 3
- `argparse` (CLI profissional)
- `socket` (networking)
- `concurrent.futures.ThreadPoolExecutor`
- Threading e paralelismo
- Design modular

## 🔐 Contexto de Segurança

Este projeto foi desenvolvido com foco educacional e defensivo para diagnóstico de rede e auditorias autorizadas.

- Diagnóstico de rede
- Auditorias básicas
- Estudos de segurança
- Troubleshooting

Não deve ser utilizado para atividades não autorizadas.

---

## 👤 Autor

Desenvolvido por **Erick**.

---
