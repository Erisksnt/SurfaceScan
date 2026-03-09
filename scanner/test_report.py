from scanner import ScanConfig, run_scan

if __name__ == "__main__":
    config = ScanConfig(host="localhost", ports=[22, 80, 443])
    results = run_scan(config)

    if not results:
        print("Nenhuma porta aberta encontrada.")
    else:
        for result in results:
            print(result)