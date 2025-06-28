# Python Tab Completion Setup

**What it does:**
- Gives you tab completion in Python (like IDEs)
- Shows function help and documentation
- Makes learning Python commands easier

**Setup:**

1. **Install IPython:**
```bash
pip install ipython
```

2. **Use IPython instead of python:**
```bash
ipython
```

**Basic Usage:**

- **Tab completion:** Type `os.path.` then press Tab to see available functions
- **Help:** Type `len?` to see documentation for the len function
- **Magic commands:** Use `%ls` to list files, `%cd` to change directory
- **Shell commands:** Use `!git status` to run shell commands

**Example:**
```python
import os
os.path.  # Press Tab here to see all available functions
len?      # Shows help for len function
```

**Benefits:**
- Learn Python faster with auto-suggestions
- See function documentation instantly
- Run shell commands without leaving Python
- Works in any project automatically 