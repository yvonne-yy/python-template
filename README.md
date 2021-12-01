# Environment Setup

- On Windows, the '3' can be dropped from the `python3` and `pip3` commands.

Create/activate virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

- Windows: `.\.venv\Scripts\activate`

Upgrade pip

```
python3 -m pip install --upgrade pip
```

Install packages

```
pip3 install wheel
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
```
