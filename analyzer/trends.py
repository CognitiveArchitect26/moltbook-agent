def compare_with_history(history, summary):
    if not history:
        return "No previous history yet. This is the first run."

    last_entry = history[-1]
    last_themes = set(last_entry.get("themes", []))
    current_themes = set(summary.get("themes", []))

    new_themes = current_themes - last_themes
    dropped_themes = last_themes - current_themes
    repeated_themes = current_themes & last_themes

    parts = []

    if new_themes:
        parts.append(f"New themes: {', '.join(sorted(new_themes))}.")
    if dropped_themes:
        parts.append(f"Dropped themes: {', '.join(sorted(dropped_themes))}.")
    if repeated_themes:
        parts.append(f"Repeated themes: {', '.join(sorted(repeated_themes))}.")

    if not parts:
        return "No major theme changes detected."

    return " ".join(parts)