from core.analyzer import analyze_content


def scan_file(filepath):
    try:
        with open(filepath, "r", errors="ignore") as file:
            content = file.read()

        result = analyze_content(content)

        return {
            "file": filepath,
            "risk": result["risk"],
            "score": result["score"],
            "findings": result["findings"]
        }

    except Exception as e:
        return {
            "file": filepath,
            "error": str(e)
        }
