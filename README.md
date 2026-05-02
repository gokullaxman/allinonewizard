# All-in-One Wizard 🧙

> A Python desktop application built with Tkinter that fuses voice recognition, text-to-speech, live weather, a to-do list, a Hangman game, a real-time clock, and one-click website shortcuts into a single GUI window.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows-blue)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack & Dependencies](#tech-stack--dependencies)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Required Asset Files](#required-asset-files)
  - [API Key Setup](#api-key-setup)
  - [Running the App](#running-the-app)
- [Application Layout](#application-layout)
- [Module Breakdown](#module-breakdown)
  - [Voice Recognition](#1-voice-recognition)
  - [Voice Commands Reference](#2-voice-commands-reference)
  - [Text-to-Speech](#3-text-to-speech)
  - [Real-Time Clock](#4-real-time-clock)
  - [Weather Widget](#5-weather-widget)
  - [To-Do List Manager](#6-to-do-list-manager)
  - [Hangman Game](#7-hangman-game)
  - [Website Shortcuts](#8-website-shortcuts)
  - [Browser Games](#9-browser-games)
  - [Output Text Box](#10-output-text-box)
- [Global Variables](#global-variables)
- [Function Reference](#function-reference)
- [Configuration & Customization](#configuration--customization)
- [Known Issues & Limitations](#known-issues--limitations)
- [Future Improvements](#future-improvements)

---

## Overview

**All-in-One Wizard** is a single-file Python desktop application (`c.s project 1.py`) that packages ten different utilities into one Tkinter window. It is designed as a personal assistant dashboard — you can speak a command to open a website, check the weather in Chennai, jot down tasks, or play Hangman, all without switching between apps.

The app was built to demonstrate Python GUI programming, third-party library integration, REST API consumption, and basic speech-processing pipelines.

---

## Features

| Feature | Description |
|---|---|
| 🎤 **Voice Recognition** | Listens via microphone and routes spoken commands to the correct action |
| 🔊 **Text-to-Speech** | Speaks back confirmations and responses using `pyttsx3` |
| 🕐 **Real-Time Clock** | Live digital clock (DD-MM-YYYY \| HH:MM:SS AM/PM) that ticks every second |
| 🌤️ **Weather Widget** | Fetches current temperature and description for Chennai via Weatherstack API |
| ✅ **To-Do List** | Add and remove tasks from a persistent in-session list with a Listbox UI |
| 🎯 **Hangman Game** | Word-guessing game using all country names from `pycountry`; 6 lives per round |
| 🌐 **Website Shortcuts** | One-click buttons for Google, YouTube, Gmail, Wikipedia, WhatsApp, Music, and a custom site |
| ♟️ **Chess (Browser)** | Opens Master Chess on MSN Games in the default browser |
| 🏓 **Neon Pong (Browser)** | Opens Neon Pong on MSN Games in the default browser |
| 📝 **Output Text Box** | Scrollable text area displaying voice recognition results, status messages, and errors |

---

## Tech Stack & Dependencies

### Standard Library (no install needed)

| Module | Purpose |
|---|---|
| `tkinter` | GUI framework — all windows, widgets, and layout |
| `tkinter.messagebox` | Pop-up dialogs for errors and game messages |
| `webbrowser` | Opens URLs in the system's default browser |
| `time.strftime`, `time.sleep` | Clock formatting and timed close delay |
| `random` | Selects a random word for each Hangman round |
| `hashlib` | (imported via `requests` dependency tree) |

### Third-Party (install required)

| Package | Install Command | Purpose |
|---|---|---|
| `Pillow` | `pip install Pillow` | Load and resize the voice recognition button image (`PIL.Image`, `PIL.ImageTk`) |
| `SpeechRecognition` | `pip install SpeechRecognition` | Microphone capture and Google Speech-to-Text transcription |
| `pyttsx3` | `pip install pyttsx3` | Offline text-to-speech synthesis |
| `googlesearch-python` | `pip install googlesearch-python` | Google search fallback for "open \<site\>" voice commands |
| `requests` | `pip install requests` | HTTP calls to Weatherstack API |
| `pycountry` | `pip install pycountry` | ISO 3166 country name list used as Hangman word pool |
| `PyAudio` | `pip install PyAudio` | Microphone hardware interface (required by SpeechRecognition) |

> **Windows note:** `PyAudio` may require a pre-built wheel. If `pip install PyAudio` fails, download the matching `.whl` from [Gohlke's Unofficial Python Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install with `pip install <file>.whl`.

---

## Project Structure

```
allinonewizard-main/
├── c.s project 1.py      # Main application — entire source code (single file)
├── icon.ico              # ⚠️ Required — window taskbar icon (not included in repo)
├── voice-recognition.png # ⚠️ Required — image for the microphone button (not included in repo)
├── README.md             # Original brief readme
└── LICENSE               # MIT License
```

> The repo ships **only the Python source file and license**. The two asset files (`icon.ico` and `voice-recognition.png`) must be supplied separately — see [Required Asset Files](#required-asset-files).

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- A working microphone (for voice recognition)
- Internet connection (for weather, Google Speech API, and website shortcuts)
- Windows OS (tested; `pyttsx3` voice index `[1]` targets the Windows SAPI5 female voice)

### Installation

```bash
# 1. Unzip or clone the project
cd allinonewizard-main

# 2. Install all required packages
pip install Pillow SpeechRecognition pyttsx3 googlesearch-python requests pycountry PyAudio
```

Or install from a one-liner requirements file (create it manually if needed):

```
# requirements.txt
Pillow
SpeechRecognition
pyttsx3
googlesearch-python
requests
pycountry
PyAudio
```

```bash
pip install -r requirements.txt
```

### Required Asset Files

The application references two local files that are **not included** in the repository. You must provide them before running:

| File | Used For | Notes |
|---|---|---|
| `icon.ico` | Window and taskbar icon | Any `.ico` file works; place it in the same directory as the `.py` file |
| `voice-recognition.png` | Image displayed on the microphone button | Resized to 100×100 px at runtime; any PNG works |

Both files must be in the **same directory** as `c.s project 1.py`, or update the hardcoded paths in `main()`:

```python
# Line in main() — update paths if needed
root.iconbitmap(r"icon.ico")
img_speech = Image.open(r"voice-recognition.png")
```

### API Key Setup

The weather feature uses the **Weatherstack API** (free tier available at [weatherstack.com](https://weatherstack.com)).

The API key is hardcoded in `main()`:

```python
api_key = '383ab22653eaf8f8a69284a15952ab00'   # ← replace with your own key
city_name = 'Chennai'                            # ← change city as needed
```

> **Important:** The hardcoded key in the repository may be expired or rate-limited. Register for a free Weatherstack account and replace it with your own key.

### Running the App

```bash
python "c.s project 1.py"
```

The main window opens immediately. The clock starts ticking, and you can interact with any feature right away.

---

## Application Layout

The GUI is a single `tk.Tk()` root window laid out using a grid system across **4 columns**:

```
┌───────────────────────────────────────────────────────────────┐
│  Col 0           │  Col 1          │  Col 2       │  Col 3    │
│                  │                 │              │           │
│  [🎤 Voice Btn]  │  [Clock Label]  │  [Text Box]  │  [To-Do]  │
│  (rowspan=5)     │  Google         │  (rowspan=5) │  Frame    │
│                  │  Youtube        │              │  Entry    │
│                  │  Mail           │              │  Add Task │
│                  │  Wikipedia      │              │  Listbox  │
│                  │  whatsapp       │              │  Remove   │
│                  │  Music          │              │           │
│                  │  Ssm website    │              │           │
│                  │  Hangman        │              │           │
│                  │  chess          │  [Close Btn] │           │
│                  │  neon pong      │              │           │
│                  │                 │ [Refresh Wx] │           │
│                  │                 │ [Temperature]│           │
│                  │                 │ [Description]│           │
└───────────────────────────────────────────────────────────────┘
```

**Background color:** `#DCDCDC` (light grey)  
**Clock label background:** `#FFFFFF` | foreground: `#4E342E` (warm brown)  
**Weather labels background:** `#FFFFFF`  
**To-Do frame background:** `#CDCDC1`

---

## Module Breakdown

### 1. Voice Recognition

**Function:** `voice_recognition()`  
**Triggered by:** Microphone button click (image button, `bd=0`) or any button mapped to `"Speech"`

The function uses `speech_recognition.Recognizer` with `sr.Microphone()` as the audio source:

1. Displays `"say something....."` in the text box
2. Adjusts for ambient noise (`duration=0.8` seconds)
3. Listens for audio input
4. Displays `"TIME OVER."` while processing
5. Sends audio to **Google Speech Recognition** (`recognize_google`)
6. Displays the recognized text and routes to the appropriate action

**Error handling:**

| Exception | Response |
|---|---|
| `sr.UnknownValueError` | Speaks and displays: "your majesty i could not understand audio." |
| `sr.RequestError` | Speaks and displays network/API error message |
| Generic `Exception` | Displays and speaks the error message |

---

### 2. Voice Commands Reference

The recognized text is matched using simple `in` / `==` string checks:

| Spoken Phrase (example) | Action |
|---|---|
| `"YouTube <query>"` | Opens `https://www.youtube.com/results?search_query=<query>` |
| `"time"` (exact) | Speaks the current time (HH:MM AM/PM) |
| `"search <query>"` | Opens `https://www.google.com/search?q=<query>` |
| `"tell about <topic>"` | Opens the Wikipedia article for `<topic>` |
| `"close"` | Calls `close()` — waits 1 second, then destroys the root window |
| `"play <query>"` | Opens `https://open.spotify.com/search/<query>` |
| `"open <site>"` | Calls `the_boss(<site>)` — Google-searches and opens the top result |

> **Note:** Command matching is case-sensitive in some places (e.g., `"YouTube"` requires a capital Y). Unrecognized commands still display the transcribed text in the output box but take no action.

---

### 3. Text-to-Speech

**Function:** `speech_output(text)`  
**Engine:** `pyttsx3` (offline, no API call)

```python
def speech_output(text):
    speech = pyttsx3.init()
    f_voice(speech)             # Sets voice to index [1] (female on Windows SAPI5)
    speech.say(f"sir: {text}")  # Prepends "sir:" to all spoken output
    speech.runAndWait()
```

**Voice selection (`f_voice`):** Sets `voice` property to `voices[1]` — on Windows this is typically the female SAPI5 voice. Change the index to `0` for the default male voice.

---

### 4. Real-Time Clock

**Function:** `time()`  
**Widget:** `tk.Label` (column 1, row 0) — font `calibri 40 bold`

Uses `strftime('%d-%m-%Y-|-%I:%M:%S %p')` to format the current date and time.  
Calls `lbl.after(1000, time)` to reschedule itself every second — a non-blocking recursive tick.

**Format example:** `08-03-2026-|-02:45:32 PM`

---

### 5. Weather Widget

**API:** Weatherstack (`http://api.weatherstack.com/current`)  
**Default city:** Chennai  
**Functions:** `get_weather(api_key, city)`, `update_weather(...)`

**`get_weather`** makes a GET request with `access_key` and `query` params and returns the parsed JSON. Returns `None` on any `requests.exceptions.RequestException`.

**`update_weather`** reads `data['current']['temperature']` and `data['current']['weather_descriptions'][0]` and updates two `tk.Label` widgets:
- `label_temperature` → `"Temperature: 32°C"`
- `label_description` → `"Description: Partly Cloudy"`

Weather is **not fetched automatically on startup** — the user must click the **"Refresh Weather"** button (row 7, column 2) to trigger the first update.

> **Note:** `get_weather` is defined twice in the source file; the second definition (identical) overwrites the first. This is a minor code duplication issue with no functional impact.

---

### 6. To-Do List Manager

**Widgets:** `tk.Entry`, `tk.Button` (Add), `tk.Listbox`, `tk.Button` (Remove)  
**Container:** `tk.Frame` (column 3, rowspan 5, background `#CDCDC1`)  
**Data store:** Module-level `tasks = []` list

#### `add_task()`
- Reads text from `task_entry`
- Appends to `tasks` list and inserts into `task_listbox`
- Clears the entry field on success
- Shows a messagebox warning if the entry is empty

#### `remove_task()`
- Reads the selected index from `task_listbox.curselection()`
- Deletes from both `tasks` list and `task_listbox`
- Shows a messagebox warning if nothing is selected

> Tasks exist only for the current session — there is no file persistence.

---

### 7. Hangman Game

**Opens in:** `tk.Toplevel` window (separate, non-blocking child window)  
**Word list:** All country names from `pycountry.countries` (250 countries)  
**Lives:** 6 per game

#### `open_hangman_window()`
Builds the Toplevel window with:
- `word_label` — masked word display (`_ _ _ _ _`)
- Letter guess `Entry` + `Guess` button
- `guessed_label` — running list of all guessed letters
- `life_label` — remaining life points

#### `get_display_word()`
Iterates through `word` and returns each letter if it's in `guesses`, else `"_"`.

#### `make_guess()`
1. Validates input: must be a single alphabetic character
2. Checks for duplicate guesses (shows messagebox if already guessed)
3. Appends to `guesses`, updates the display word
4. Decrements `life_points` if the guess is wrong
5. Checks win condition (`"_" not in display_word`) → congratulations + reset
6. Checks loss condition (`life_points == 0`) → reveals word + reset

#### `reset_game()`
Picks a new random country name, clears `guesses`, resets `life_points` to 6, and resets all labels.

---

### 8. Website Shortcuts

**Dictionary:** `w_urls` (defined at module level)

```python
w_urls = {
    "Google":      "https://www.google.com",
    "Youtube":     "https://www.youtube.com",
    "Mail":        "https://mail.google.com",
    "Wikipedia":   "https://www.wikipedia.org",
    "whatsapp":    "https://web.whatsapp.com/",
    "Music":       "https://wynk.in/music",
    "Ssm website": "https://ssmetrust.in/ssm63/default.aspx"
}
```

**`button_click(site)`** dispatches button presses:
- `"Speech"` → `voice_recognition()`
- `"chess"` → `open_chess()`
- `"neon pong"` → `open_pong()`
- Anything else → `webbrowser.open(w_urls.get(site, "https://www.google.com"))`

Buttons are created in a loop using `create_button()` and placed in column 1, rows 1–10.

---

### 9. Browser Games

Both games open MSN Games URLs in the default browser via `webbrowser.open()`.

| Button | Function | URL |
|---|---|---|
| `chess` | `open_chess()` | MSN — Master Chess |
| `neon pong` | `open_pong()` | MSN — Neon Pong |

---

### 10. Output Text Box

**Widget:** `tk.Text(root, height=10, width=40)` — column 2, rowspan 5

Displays real-time status messages from voice recognition:
- "say something....."
- "TIME OVER."
- "You said: \<transcribed text\>"
- Actions taken (e.g., "opening youtube", "searching in google")
- Error messages

Initialized with a brief description of the app's voice-control features. Cleared and updated on each voice recognition cycle using `.delete("1.0", tk.END)` and `.insert(tk.END, ...)`.

---

## Global Variables

The application uses several module-level globals to share state between functions:

| Variable | Type | Purpose |
|---|---|---|
| `root` | `tk.Tk` | Main window reference |
| `lbl` | `tk.Label` | Clock label — updated every second by `time()` |
| `t_entry` | `tk.Text` | Output text box — written to by voice recognition |
| `img_speech` | `ImageTk.PhotoImage` | Held in global scope to prevent garbage collection |
| `word` | `str` | Current Hangman target word |
| `guesses` | `list` | Letters guessed so far in Hangman |
| `life_points` | `int` | Remaining lives in Hangman (starts at 6) |
| `word_label` | `tk.Label` | Hangman masked word display label |
| `guess_entry` | `tk.Entry` | Hangman letter input field |
| `guessed_label` | `tk.Label` | Hangman guessed-letters label |
| `life_label` | `tk.Label` | Hangman lives-remaining label |
| `tasks` | `list` | In-session to-do task list |
| `task_entry` | `tk.Entry` | To-do input field |
| `task_listbox` | `tk.Listbox` | To-do display listbox |
| `word_list` | `list` | All country names (populated when Hangman window opens) |

---

## Function Reference

| Function | Parameters | Description |
|---|---|---|
| `main()` | — | Entry point; builds and starts the root Tkinter window |
| `time()` | — | Recursive 1-second clock tick using `lbl.after(1000, time)` |
| `voice_recognition()` | — | Microphone listen → Google STT → command dispatch |
| `speech_output(text)` | `text: str` | Speaks `"sir: <text>"` using pyttsx3 |
| `f_voice(speech_engine)` | `speech_engine` | Sets TTS voice to index `[1]` (female SAPI5) |
| `on_click(event)` | `event` | Bound event handler that calls `voice_recognition()` |
| `button_click(site)` | `site: str` | Routes button press to correct action or URL |
| `open_chess()` | — | Opens MSN Master Chess in browser |
| `open_pong()` | — | Opens MSN Neon Pong in browser |
| `the_boss(_link)` | `_link: str` | Google-searches `_link` and opens top result |
| `close()` | — | Inserts closing message, sleeps 1s, destroys root window |
| `get_weather(api_key, city)` | `api_key: str`, `city: str` | Fetches JSON from Weatherstack API |
| `update_weather(api_key, city, lbl_t, lbl_d)` | labels + config | Updates temperature and description labels |
| `add_task()` | — | Reads `task_entry`, appends to `tasks` + `task_listbox` |
| `remove_task()` | — | Deletes selected item from `tasks` + `task_listbox` |
| `get_places()` | — | Returns list of all country names from `pycountry` |
| `open_hangman_window()` | — | Creates `tk.Toplevel` Hangman window, initializes word |
| `get_display_word()` | — | Returns masked string (letters or `_`) for current word |
| `make_guess()` | — | Processes one letter guess; checks win/loss conditions |
| `reset_game()` | — | Picks new word, resets guesses and life points |
| `create_button(root, text, row, col, command)` | various | Factory for grid-placed `tk.Button` widgets |

---

## Configuration & Customization

### Change the Default City for Weather

In `main()`:
```python
city_name = 'Chennai'   # ← change to any city
```

### Add or Remove Website Shortcuts

Edit the `w_urls` dictionary and `button_list` in `main()`:
```python
w_urls = {
    "Google": "https://www.google.com",
    # Add your sites here
    "GitHub": "https://www.github.com",
}

button_list = ["Google", ..., "GitHub"]   # add to the list
```

### Change the TTS Voice

In `f_voice()`, change the index:
```python
speech_engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female (Windows)
```

### Change the App Background Color

In `main()`:
```python
root.config(bg='#DCDCDC')   # any valid Tkinter color string
```

### Add New Voice Commands

In `voice_recognition()`, add a new `elif` branch:
```python
elif "weather" in text:
    update_weather(api_key, city_name, label_temperature, label_description)
```

---

## Known Issues & Limitations

| Issue | Impact | Notes |
|---|---|---|
| **Asset files not included** (`icon.ico`, `voice-recognition.png`) | App crashes on startup with `FileNotFoundError` | Must supply these files manually before running |
| **Hardcoded API key** | Key may be expired/rate-limited | Replace with your own Weatherstack key |
| **Hardcoded city** (`Chennai`) | Weather always shows Chennai | No input field to change city at runtime |
| **`get_weather` defined twice** | Second definition silently replaces first | Harmless duplicate; should be cleaned up |
| **Weather not auto-loaded** | Labels show "Loading..." until button is clicked | No `after()` call on startup to trigger first fetch |
| **No task persistence** | To-do list resets when the app closes | No file or database save/load |
| **Voice recognition is blocking** | UI freezes while microphone is listening | Should run in a background thread (`threading.Thread`) |
| **`the_boss()` uses `t_entry` as callable** | `t_entry(tk.END, ...)` is incorrect — `t_entry` is a `tk.Text` widget, not a function | Line `t_entry(tk.END, f'{txt}')` would crash; should be `t_entry.insert(...)` |
| **Hangman reuses globals across windows** | Opening multiple Hangman windows would conflict | Single game instance only |
| **Voice commands case-sensitive** | `"youtube"` (lowercase) won't trigger YouTube action | Only `"YouTube"` (capital Y) matches |
| **Windows-only TTS voice** | `voices[1]` may not exist on macOS/Linux | Causes `IndexError` on non-Windows systems |

---

## Future Improvements

| Area | Suggestion |
|---|---|
| **Threading** | Run `voice_recognition()` in a daemon thread so the UI stays responsive while listening |
| **Task persistence** | Save to-do tasks to a JSON or SQLite file and reload on startup |
| **Dynamic city input** | Add a text entry field so the user can type any city for weather |
| **Auto weather refresh** | Use `root.after(600000, ...)` to refresh weather every 10 minutes automatically |
| **Hangman visuals** | Draw the classic hangman figure on a `tk.Canvas` as lives decrease |
| **Settings panel** | Let users configure city, TTS voice, and button URLs through a settings dialog |
| **Package as executable** | Use `PyInstaller` to bundle the app into a standalone `.exe` with bundled assets |
| **Broader platform support** | Abstract voice-index selection so it works on macOS and Linux |
| **Error-resilient `the_boss()`** | Fix the `t_entry(...)` bug and add rate-limiting/retry logic for Google Search |
| **Command history** | Show a scrollable history of all past voice commands in the output box |
| **Keyword wake word** | Add a background listener for a wake word (e.g., "Hey Wizard") to trigger recognition without clicking |

---

## License

MIT — see `LICENSE` for full terms.
