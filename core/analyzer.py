SUSPICIOUS_PATTERNS = [
    "os.system",
    "subprocess",
    "eval(",
    "exec(",
    "base64",
    "socket",
    "pickle",
    "marshal",
    "wget",
    "curl"
]


def analyze_content(content):
    findings = []
    risk_score = 0

    for pattern in SUSPICIOUS_PATTERNS:
        if pattern in content:
            findings.append(pattern)
            risk_score += 10

    # Risk level
    if risk_score >= 50:
        risk = "HIGH"
    elif risk_score >= 20:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "risk": risk,
        "score": risk_score,
        "findings": findings
    }
