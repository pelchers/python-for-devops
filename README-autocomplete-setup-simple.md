# Tab Completion Setup for Learning

**Purpose:**
Get IDE-like tab completion in terminal for faster Python and bash learning.

**What you get:**
- Python tab completion (like Cursor IDE)
- Bash terminal tab completion
- Function help and documentation
- Command discovery and learning

**Quick Setup:**

**1. Python Completion:**
```bash
pip install ipython
```
Then use `ipython` instead of `python`

**2. Bash Completion (WSL):**
Add to `~/.bashrc`:
```bash
if [ -f /etc/bash_completion ]; then . /etc/bash_completion; fi
bind 'set completion-ignore-case on'
bind '"\t": menu-complete'
```

**Files:**
- `quickstart-python-autocomplete-simple.md` - Python setup
- `quickstart-bash-terminal-autocomplete-simple.md` - Bash setup

**Benefits:**
- Learn commands faster
- Reduce typing and errors
- Discover new functions
- Works across all projects 