# main.py

from listener.fetch import fetch_posts
from analyzer.summarize import summarize_posts
from analyzer.risk import detect_risks
from reports.generate import generate_report


def run_agent():
    print("🔍 Moltbook Agent Starting...\n")

    # Step 1: Fetch posts
    posts = fetch_posts()
    print(f"Fetched {len(posts)} posts")

    # Step 2: Analyze content
    summary = summarize_posts(posts)
    print("Content summarized")

    # Step 3: Detect risks
    risks = detect_risks(posts)
    print(f"Detected {len(risks)} potential risks")

    # Step 4: Generate report
    report = generate_report(summary, risks)

    print("\n📊 REPORT\n")
    print(report)


if __name__ == "__main__":
    run_agent()