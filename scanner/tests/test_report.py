import json
from scanner.api import export_results

def test_export_results_generates_csv_and_json(tmp_path):
    data = [{"port": 80, "service": "HTTP", "status": "open", "banner": None}]

    paths = export_results(data, output_dir=str(tmp_path), base_name="scan")

    csv_path = tmp_path / "scan.csv"
    json_path = tmp_path / "scan.json"

    assert paths["csv"] == str(csv_path)
    assert paths["json"] == str(json_path)
    assert csv_path.exists()
    assert json_path.exists()

    loaded = json.loads(json_path.read_text(encoding="utf-8"))
    assert loaded[0]["port"] == 80