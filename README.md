# 🔐 Radmin Auto — Remote Connection Automation

This Python tool automates repetitive tasks in **Radmin Viewer** to quickly connect to a remote computer, log in with multiple credentials, and open **Event Viewer (System logs)**.
It is built with **Tkinter** for the GUI and **PyAutoGUI** for automation.

⚠️ **Note:** This is for educational and administrative use only. Credentials are currently **hardcoded** in the script—update them for your environment.

---

## ✨ Features

* Launches **Radmin Viewer** automatically.
* Connects to a target IP/Address with username + password.
* Activates the remote session tab.
* Sends **Ctrl+Alt+Del** and types a second password.
* Opens **Event Viewer → System logs** and refreshes them.
* GUI with Start/Stop buttons for ease of use.

---

## 📂 Project Structure

```
RadminAuto.py   # Main script
```

---

## 🛠 Requirements

Install dependencies via pip:

```bash
pip install pyautogui
```

This script uses built-in Python modules:

* `os`, `time`, `subprocess`, `threading`
* `tkinter`, `ttk`, `messagebox`

---

## ▶️ Usage

1. Update credentials in the script:

   ```python
   USERNAME = "administrator"
   FIRST_PASSWORD = "your_first_password"
   SECOND_PASSWORD = "your_second_password"
   ```
2. Run the script:

   ```bash
   python RadminAuto.py
   ```
3. Enter the **IP/Address** in the GUI field.
4. Click **Start** → automation begins:

   * Radmin launches.
   * Connects to the given address.
   * Logs in with both passwords.
   * Opens Event Viewer System logs.

---

## ⚙️ How It Works

* **Coordinates:** The script uses hardcoded screen coordinates for clicks (e.g., connect button, Ctrl+Alt+Del button).
* **Delays:** `time.sleep()` is used to allow windows to load before typing or clicking.
* **Stop Button:** Halts automation safely using a thread flag.

---

## 🚨 Notes & Limitations

* Coordinates (`CONNECT_BTN`, `CAD_BTN`, etc.) may need to be updated depending on your screen resolution and Radmin version.
* Credentials are stored in plain text → not secure for production.
* Requires **Radmin Viewer 3** installed.

---

## 📸 Example Workflow

1. Enter IP → `192.168.1.50`
2. Script launches Radmin.
3. Auto-fills username & password.
4. Activates remote tab.
5. Sends **Ctrl+Alt+Del** → second password.
6. Opens **Event Viewer → System logs → Refresh**.

---

## 📜 License

MIT License — free to use and modify with attribution.
