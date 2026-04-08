# 📓 Daily Journal Writer

An automated daily journal generator powered by **N8N**, **OpenAI GPT**, and **Python PyAutoGUI** that creates personalized journal entries and saves them automatically.

---

## 🚀 Features

- ⏰ **Automated Scheduling** — Runs daily via N8N Schedule Trigger
- 🤖 **AI-Generated Content** — Uses OpenAI GPT to write meaningful journal entries
- 📁 **Auto File Saving** — Saves journal as `.txt` file with today's date
- 🖥️ **UI Automation** — Opens and displays journal in Notepad using PyAutoGUI
- 🔄 **End-to-End Workflow** — Fully automated from generation to display

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **N8N** | Workflow automation & scheduling |
| **OpenAI GPT** | AI journal content generation |
| **Python** | UI automation script |
| **PyAutoGUI** | Automates Notepad interaction |
| **Pyperclip** | Clipboard handling for special characters |

---

## 📁 Project Structure

```
DailyJournalWriter/
├── journal_writer.py       # Python UI automation script
├── workflow.json           # N8N workflow export
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.x
- N8N (Self Hosted)
- OpenAI API Key

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOURUSERNAME/daily-journal-writer.git
cd daily-journal-writer
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
.\venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install pyautogui pyperclip
```

### Step 4: Import N8N Workflow
1. Open N8N at `http://localhost:5678`
2. Go to **Workflows** → **Import**
3. Upload `workflow.json`
4. Add your **OpenAI API Key** in the credentials

### Step 5: Configure File Path
In `journal_writer.py`, update the folder path if needed:
```python
# Update this to your local path
files = glob.glob(r"F:\DailyJournalWriter\journal_*.txt")
```

### Step 6: Run N8N with File Access Permission
```bash
$env:N8N_RESTRICT_FILE_ACCESS_TO="F:\DailyJournalWriter"
n8n start
```

---

## 🔄 How It Works

```
⏰ Schedule Trigger (Daily)
        ↓
🤖 Basic LLM Chain (OpenAI GPT)
        ↓
✏️ Edit Fields (clean_text)
        ↓
📄 Convert to File (Binary)
        ↓
💾 Read/Write Files from Disk
        ↓
🖥️ Python PyAutoGUI (Opens in Notepad)
```

---

## 📝 N8N Workflow Nodes

| Node | Description |
|---|---|
| **Schedule Trigger** | Triggers workflow daily at set time |
| **Basic LLM Chain** | Generates journal content via OpenAI |
| **Edit Fields** | Cleans and formats the text output |
| **Convert to File** | Converts text to binary file format |
| **Read/Write Files from Disk** | Saves journal as `.txt` to local disk |

---

## 🐍 Python Script

The `journal_writer.py` script:
1. Finds the latest journal `.txt` file
2. Opens Notepad automatically
3. Pastes journal content via clipboard
4. Saves with today's date as filename

### Run the Script
```bash
cd F:\DailyJournalWriter
.\venv\Scripts\activate
python journal_writer.py
```

---

## 🔧 Troubleshooting

| Error | Fix |
|---|---|
| `❌ journal.txt not found` | Run N8N workflow first to generate the file |
| `File is not writable` | Set `N8N_RESTRICT_FILE_ACCESS_TO` environment variable |
| `Module 'fs' is disallowed` | Use Read/Write Files node instead of Code node |
| `Python runner unavailable` | Switch Code node language to JavaScript |

---

## 🌱 Environment Variables

| Variable | Value |
|---|---|
| `N8N_RESTRICT_FILE_ACCESS_TO` | `F:\DailyJournalWriter` |

To make permanent, run in Admin PowerShell:
```bash
[System.Environment]::SetEnvironmentVariable("N8N_RESTRICT_FILE_ACCESS_TO", "F:\DailyJournalWriter", "Machine")
```

---

## 📌 Important Notes

- 🔒 Journal `.txt` files are **excluded from Git** via `.gitignore` for privacy
- 🖥️ PyAutoGUI requires the screen to be **visible and unlocked**
- ⚠️ Do **not** touch mouse or keyboard while PyAutoGUI is running

---

