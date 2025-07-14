# File Organizer

A Python script that automatically sorts files in a directory into categorized folders based on their file extensions.

## Features

- Supports organizing Images, Documents, Audio, Videos, Archives, Scripts, and Others
- Creates folders automatically if not present
- Moves files to respective folders

## How to Run

1. Make sure Python 3 is installed.
2. Run the script and input the full path of the folder you want to organize:

```bash
python main.py
```
## Notes
- The script only moves files in the specified folder, not in nested subfolders.
- Files with unknown extensions will be moved to an "Others" folder.