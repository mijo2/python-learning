# Python Learning CLI Tool

This is an interactive CLI tool to learn advanced Python concepts through exercises.

## Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the CLI tool:
   ```bash
   python run_all.py
   ```

## Structure

Each concept folder contains:
- notes.md → Concept explanation
- examples.py → Working examples
- exercises.py → Practice exercises
- solutions.py → Solutions
- tests/ → Unit tests for exercises

## Progress Tracking

Your progress is tracked in `progress_tracker.json` (ignored in .gitignore).

## Individual Testing

You can still run individual files directly:
```bash
python concepts/list_comprehensions/examples.py
```
