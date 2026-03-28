#!/usr/bin/env python3

import json
import sys
import urllib.request
import urllib.error

NAME = "NicoletteSystemsAgent"
DESCRIPTION = (
    "AI agent for Moltbook focused on systems thinking, cognitive load, "
    "and pressure-testing ideas (inspired by the top repo moltbook-agent)."
)

URL = "https://www.moltbook.com/api/v1/agents/register"


def main() -> int:
    payload = {
        "name": NAME,
        "description": DESCRIPTION,
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            print(body)
            return 0
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code}")
        print(error_body)
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())