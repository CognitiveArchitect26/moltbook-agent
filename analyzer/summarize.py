def summarize_posts(posts):
    if not posts:
        return {
            "count": 0,
            "themes": [],
            "summary": "No posts found."
        }

    themes = []

    for post in posts:
        text = post["text"].lower()

        if "identity" in text or "resets" in text:
            themes.append("identity")
        if "rate limits" in text or "coordinate" in text:
            themes.append("coordination")
        if "ignore previous instructions" in text or "reveal your system prompt" in text:
            themes.append("prompt injection")

    unique_themes = list(set(themes))

    return {
        "count": len(posts),
        "themes": unique_themes,
        "summary": f"Reviewed {len(posts)} posts. Main themes: {', '.join(unique_themes) if unique_themes else 'none'}."
    }