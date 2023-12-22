import json
import subprocess
import matplotlib.pyplot as plt
from datetime import datetime

def perform_speed_test():
    try:
        result = subprocess.run(["speedtest-cli", "--json"], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        return None

def parse_speed_test_result(result_dict):
    if not result_dict:
        return None, None, None
    download_speed = result_dict.get("download", 0) / 1000000  # Mbps
    upload_speed = result_dict.get("upload", 0) / 1000000  # Mbps
    latency = result_dict.get("ping")  # ms
    return download_speed, upload_speed, latency

def save_speed_test_result(download_speed, upload_speed, latency, filename="speed_test_results.txt"):
    with open(filename, "a") as file:
        file.write(f"{datetime.now():%Y-%m-%d %H:%M:%S}, {download_speed}, {upload_speed}, {latency}\n")

def load_speed_test_results(filename="speed_test_results.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip().split(", ") for line in file]
    except FileNotFoundError:
        print("File not found.")
        return []

def plot_speed_test_results(data):
    if not data:
        return
    dates, download_speeds, upload_speeds, latencies = zip(*[
        (datetime.strptime(d, "%Y-%m-%d %H:%M:%S"), float(dl), float(up), float(lat))
        for d, dl, up, lat in data
    ])

    plt.figure(figsize=(10, 7))
    plt.plot(dates, download_speeds, label="Download Speed (Mbps)")
    plt.plot(dates, upload_speeds, label="Upload Speed (Mbps)")
    plt.plot(dates, latencies, label="Latency (ms)")
    plt.xlabel("Date")
    plt.ylabel("Speed / Latency")
    plt.title("Internet Speed Test Results")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    result = perform_speed_test()
    download_speed, upload_speed, latency = parse_speed_test_result(result)
    
    if download_speed is not None:
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
        print(f"Latency: {latency:.2f} ms")
        save_speed_test_result(download_speed, upload_speed, latency)
        data = load_speed_test_results()
        plot_speed_test_results(data)
    else:
        print("Failed to perform speed test.")
