def generate_report(summary, risks):
    report_lines = [
        "Daily Moltbook Brief",
        "--------------------",
        f"Posts reviewed: {summary['count']}",
        f"Themes detected: {', '.join(summary['themes']) if summary['themes'] else 'none'}",
        f"Summary: {summary['summary']}",
        f"Risks detected: {len(risks)}"
    ]

    if risks:
        report_lines.append("\nRisk Details:")
        for risk in risks:
            report_lines.append(
                f"- Post {risk['post_id']}: {risk['risk']} ({risk['matched_phrase']})"
            )

    return "\n".join(report_lines)