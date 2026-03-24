from listener.fetch import fetch_posts
from analyzer.summarize import summarize_posts
from analyzer.risk import detect_risks
from analyzer.trends import compare_with_history
from reports.generate import generate_report
from reports.save import save_report
from reports.emailer import send_email_report
from storage.history import load_history, save_history
from config import REPORT_TITLE, REPORT_EMAIL


def run_agent():
    print("Moltbook Agent Starting...\n")

    # Step 1: Fetch posts
    posts = fetch_posts()
    print(f"Fetched {len(posts)} posts")

    # Step 2: Summarize posts
    summary = summarize_posts(posts)
    print("Content summarized")

    # Step 3: Detect risks
    risks = detect_risks(posts)
    print(f"Detected {len(risks)} potential risks")

    # Step 4: Compare with history
    history = load_history()
    trend_summary = compare_with_history(history, summary)
    print("Trend comparison complete")

    # Step 5: Generate report
    report = generate_report(summary, risks)
    report += f"\