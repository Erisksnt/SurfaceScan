from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from scanner.core.scanner import scan_ports
from scanner.report import export_to_csv, export_to_json


@dataclass(frozen=True)
class ScanConfig:
    host: str
    ports: list[int]
    timeout: float = 1.0
    threads: int = 50


def parse_ports(ports_expr: str) -> list[int]:
    """Converte expressões como '22,80,443,8000-8100' em uma lista ordenada sem duplicados."""
    ports: set[int] = set()

    for item in ports_expr.split(","):
        token = item.strip()
        if not token:
            continue

        if "-" in token:
            start, end = map(int, token.split("-", 1))
            if start > end:
                raise ValueError(f"Faixa inválida: {token}")
            ports.update(range(start, end + 1))
        else:
            ports.add(int(token))

    invalid = [p for p in ports if p < 1 or p > 65535]
    if invalid:
        raise ValueError("Portas devem estar no intervalo 1-65535")

    return sorted(ports)


def run_scan(config: ScanConfig) -> list[dict]:
    """API principal para execução de scan, pronta para integração em outros projetos."""
    return scan_ports(
        host=config.host,
        ports=config.ports,
        timeout=config.timeout,
        threads=config.threads,
    )


def export_results(results: Iterable[dict], *, output_dir: str = "scans", base_name: str) -> dict[str, str]:
    """Exporta resultados para JSON e CSV e retorna os caminhos gerados."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    csv_path = out / f"{base_name}.csv"
    json_path = out / f"{base_name}.json"

    materialized = list(results)
    export_to_csv(str(csv_path), materialized)
    export_to_json(str(json_path), materialized)

    return {"csv": str(csv_path), "json": str(json_path)}