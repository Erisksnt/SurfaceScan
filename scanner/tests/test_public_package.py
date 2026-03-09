from surfacescan import ScanConfig, export_results, parse_ports, run_scan


def test_surfacescan_public_api_exports_expected_symbols():
    assert ScanConfig.__name__ == "ScanConfig"
    assert callable(parse_ports)
    assert callable(run_scan)
    assert callable(export_results)