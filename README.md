# driver-monitoring-system

A simple driver monitoring system that detects driver attention and alerts on unsafe conditions. This repository contains the core scripts and utilities to run and develop the project locally.

**Features:**

- Detect face/eyes using camera input
- Issue alerts when drowsiness or distraction is detected
- Small utilities for preprocessing and evaluation

**Prerequisites**

- Python 3.8 or newer
- A webcam for live testing

## Local development setup

1. Clone the repository (if not already cloned):

```bash
git clone https://github.com/rahul152-ai/driver-monitoring-system.git
cd driver-monitoring-system
```

2. Create and activate a virtual environment

- Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

- Windows (cmd):

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

- macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install Python dependencies

If a `requirements.txt` file exists:

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt`, install the packages you need (example):

```bash
pip install opencv-python numpy
```

4. Configuration

- If the project requires environment variables or model files, place them according to the repo layout or update the config in `dms_utils.py` / `main.py`.

5. Run the project

```bash
python main.py
```

On Windows, run the same `python main.py` command from the activated virtual environment.

6. Development tips

- To work on a feature branch:

```bash
git checkout -b feature/your-feature
```

- Keep your branch up-to-date with `origin/main` by either merging or rebasing regularly:

```bash
git fetch origin main
git merge origin/main         # or
git rebase origin/main
```

7. Tests & linting

- If tests/linting tools are present, run them here (example):

```bash
pytest
flake8
```

## Contributing

This project is open source — issues and contributions are welcome. Feel free to open issues for bugs or feature requests.

Please submit pull requests with a clear description of the change, related issue (if any), and tests or examples when possible. Maintain a clean commit history and follow the project's coding style.

## Contact

For questions, open an issue in the repository.
