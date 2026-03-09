from scanner.api import ScanConfig, parse_ports, run_scan

def test_parse_ports_expands_ranges_and_removes_duplicates():
    ports = parse_ports("22,80,80,1000-1002")
    assert ports == [22, 80, 1000, 1001, 1002]


def test_run_scan_delegates_to_core(monkeypatch):
    captured = {}

    def fake_scan_ports(host, ports, timeout, threads):
        captured["args"] = (host, ports, timeout, threads)
        return [{"port": 80, "service": "HTTP", "status": "open", "banner": None}]

    monkeypatch.setattr("scanner.api.scan_ports", fake_scan_ports)

    config = ScanConfig(host="localhost", ports=[80], timeout=0.2, threads=10)
    results = run_scan(config)

    assert captured["args"] == ("localhost", [80], 0.2, 10)
    assert results[0]["port"] == 80