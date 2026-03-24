from listener.fetch import fetch_posts
from analyzer.summarize import summarize_posts
from analyzer.risk import detect_risks
from reports.generate import generate_report


def run_agent():
    print("Moltbook Agent Starting...\n")

    posts = fetch_posts()
    print(f"Fetched {len(posts)} posts")

    summary = summarize_posts(posts)
    print("Content summarized")

    risks = detect_risks(posts)
    print(f"Detected {len(risks)} potential risks")

    report = generate_report(summary, risks)

    print("\nREPORT\n")
    print(report)


if __name__ == "__main__":
    run_agent()