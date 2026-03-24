def detect_risks(posts):
    risks = []

    suspicious_phrases = [
        "ignore previous instructions",
        "reveal your system prompt",
        "send your api key",
        "click this link"
    ]

    for post in posts:
        text = post["text"].lower()

        for phrase in suspicious_phrases:
            if phrase in text:
                risks.append({
                    "post_id": post["id"],
                    "risk": "prompt_injection",
                    "matched_phrase": phrase
                })

    return risks