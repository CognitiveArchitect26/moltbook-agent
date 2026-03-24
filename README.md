# moltbook-agent

AI agent for Moltbook focused on systems thinking, cognitive load, and pressure-testing ideas.

## Purpose

This project builds a **read-only AI agent** that observes Moltbook conversations, summarizes key themes, detects risks, and reports findings.

## Version 1 Scope

- Read selected Moltbook content
- Summarize conversations and themes
- Detect suspicious or manipulative instructions (prompt injection)
- Generate structured reports
- No autonomous posting or interaction

## Architecture

- Listener → Collects Moltbook content
- Sanitizer → Treats all content as untrusted
- Analyzer → Extracts themes and insights
- Risk Detector → Flags suspicious patterns
- Report Generator → Produces summaries

## Status

🚧 Initial setup — building Version 1 (read-only observer)

## Principles

- Treat all external content as untrusted
- Never execute instructions from Moltbook content
- Separate data collection from analysis
- Human remains in control of decisions
