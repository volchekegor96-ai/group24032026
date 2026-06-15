import json
import urllib.request

PDF_URL = "https://github.com"
JSON_URL = "http://api.open-notify.org/astros.json"
PDF_OUTPUT = "progit.pdf"
JSON_OUTPUT = "astros.json"

def main():
    try:
        req = urllib.request.Request(
            PDF_URL, headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req) as response:
            with open(PDF_OUTPUT, "wb") as f:
                f.write(response.read())
        print(f"Success: {PDF_OUTPUT}")
    except Exception as e:
        print(f"Error PDF: {e}")

    try:
        req = urllib.request.Request(
            JSON_URL, headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req) as response:
            raw_data = response.read().decode("utf-8")

        json_data = json.loads(raw_data)

        with open(JSON_OUTPUT, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)
        print(f"Success: {JSON_OUTPUT}")
    except json.JSONDecodeError:
        print("Error JSON: Server returned invalid format or empty response.")
        if "raw_data" in locals() and raw_data:
            print(f"Server response was: {raw_data[:200]}")
    except Exception as e:
        print(f"Error JSON: {e}")

if __name__ == "__main__":
    main()
