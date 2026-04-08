import pyautogui
import pyperclip
import time
from datetime import datetime
import os
import glob

# ✅ Find any existing journal file automatically
files = glob.glob(r"F:\DailyJournalWriter\journal_*.txt")

if not files:
    print("❌ No journal files found in F:\\DailyJournalWriter\\")
    exit()

# ✅ Pick the most recent one
file_path = max(files, key=os.path.getctime)
print(f"📄 Found journal: {file_path}")

# ✅ Read journal content
with open(file_path, "r", encoding="utf-8") as file:
    journal_text = file.read()

pyautogui.FAILSAFE = True

# ✅ Open Notepad via Run dialog
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('notepad')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)

# ✅ Paste content using clipboard
full_content = "My Daily Journal\n\n" + journal_text
pyperclip.copy(full_content)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# ✅ Save as new file with today's date and time
today = datetime.now().strftime("%Y-%m-%d_%H-%M")
save_path = rf"F:\DailyJournalWriter\journal_{today}.txt"
pyautogui.hotkey('ctrl', 's')
time.sleep(2)
pyperclip.copy(save_path)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

print(f"✅ Journal saved as: journal_{today}.txt")