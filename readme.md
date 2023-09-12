# Plot clipboard contents

Assumes:
- markdown format
- first column is date
- other columns are numerical
- one non-numerical column can exist, will be
  used to annotate the plot

# Dev
Install python 3+

```sh
python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
```

# Usage
Copy a markdown table, then run

    cat /dev/clipboard | python plot.py

# Making a standalone executable
```sh
pyinstaller -F plot.py
```

This creates a single executable file.

# Todo
- nicer message on error parsing clipboard
