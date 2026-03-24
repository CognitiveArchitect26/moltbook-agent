import os
from datetime import datetime


def save_report(report_text):
    # Create reports directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Create timestamped filename
    filename = datetime.now().strftime("report_%Y%m%d_%H%M%S.txt")
    filepath = os.path.join("output", filename)

    # Save report
    with open(filepath, "w") as file:
        file.write(report_text)

    return filepath