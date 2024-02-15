# File Organization in Python

**This Python script organizes files in the current directory into separate folders based on their file extensions.** 
  
### How it works:
1. The script first attempts to create folders for different file types (`Documents`, `Video`, `Audio`, `Pictures`, `Others`).
2. Lists are defined for each category of file extensions: `audio`, `video`, `documents`, `pictures`.
3. It iterates through all files in the current directory and checks their file extensions.
4. Based on the file extension, it moves each file to the appropriate folder.
5. If a file extension doesn't match any category, it is moved to the `Others` folder.

### Clone Repository  
1. Clone or download the script to your local machine.
2. Run the script using a Python interpreter.  
   ```bash
   python Organize.py
   ```

### Local Usage:
1. Save the script in the directory containing the files you want to organize.
2. Run the script.

### Note:
- Make sure to review the script and customize the file extensions/categories as per your requirements.
- This script assumes it's run from the directory containing the files to be organized.
