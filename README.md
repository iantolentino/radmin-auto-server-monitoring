# Radmin Automation Tool

A Python-based automation tool for Radmin Viewer that automates remote desktop connections, credential entry, and Event Viewer access.

## Overview 

This tool automates the entire workflow of connecting to remote Windows machines via Radmin Viewer:
1. Launches Radmin Viewer automatically
2. Connects to specified remote address
3. Enters username and password credentials
4. Activates the remote session
5. Sends Windows login password
6. Opens Event Viewer and navigates to System logs

## Features

- **Fully Automated** - One-click automation of the entire connection workflow
- **User-Friendly GUI** - Simple interface for entering remote addresses
- **Thread-Safe Execution** - Runs automation in background thread, UI remains responsive
- **Stop Functionality** - Ability to halt automation mid-execution
- **Comprehensive Logging** - Detailed logs for debugging and monitoring
- **Error Handling** - Graceful error handling with user notifications
- **Configurable** - Easy to modify credentials, coordinates, and timing delays
- **Safety Features** - PyAutoGUI failsafe (move mouse to corner to abort)

## Requirements

### System Requirements
- Windows 7/8/10/11
- Python 3.7 or higher
- Radmin Viewer 3 installed

### Python Dependencies
```
pyautogui==0.9.54
Pillow==10.1.0
```

## Installation

### 1. Clone or Download the Project

```bash
git clone https://github.com/yourusername/radmin-automation.git
cd radmin-automation
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Settings

Edit `src/config/settings.py` to set your credentials:

```python
# Credentials
USERNAME = "your_username_here"
FIRST_PASSWORD = "your_password_here"
SECOND_PASSWORD = "your_password_here"
```

## Configuration Guide

### Screen Coordinates

If the automation clicks in the wrong places, you may need to adjust screen coordinates:

1. **Find the coordinates** of any UI element using tools like:
   - PyAutoGUI's `pyautogui.displayMousePosition()`
   - Windows Snipping Tool (shows cursor position)
   - Any screen coordinate utility

2. **Update coordinates** in `settings.py`:

```python
COORDINATES = {
    "connect_button": (445, 265),        # "Connect to an address" button
    "remote_tab": (810, 15),             # Remote session tab
    "cad_button": (225, 35),             # Ctrl+Alt+Del button
    "event_viewer": {
        "windows_logs": (175, 170),      # Windows Logs section
        "system": (245, 245),            # System logs
        "refresh": (1048, 600)           # Refresh button
    }
}
```

### Timing Delays

If the automation runs too fast or too slow, adjust timing delays:

```python
DELAYS = {
    "radmin_launch": 5,                  # Wait for Radmin to open
    "connect_delay": 1,                  # After clicking connect
    "auth_delay": 2,                     # After entering credentials
    "remote_tab_activation": 5,          # After connecting
    "password_delay": 2,                 # After clicking CAD button
    "event_viewer_launch": 5,            # Wait for Event Viewer
    "run_command_delay": 1,              # After Win+R
    "event_viewer_load": 8,              # Wait for Event Viewer to load
    "click_delay": 1,                    # Between clicks
    "type_interval": 0.05,               # Between keystrokes
    "command_interval": 0.08,            # Between commands
}
```

### Radmin Installation Paths

If Radmin is installed in a custom location, add the path:

```python
RADMIN_PATHS = [
    r"C:\Program Files\Radmin Viewer 3\radmin.exe",
    r"C:\Program Files (x86)\Radmin Viewer 3\radmin.exe",
    r"D:\Custom\Path\radmin.exe",        # Add custom path here
]
```

## Usage

### Starting the Application

```bash
python -m src.main
```

Or directly:
```bash
python src/main.py
```

### Using the Tool

1. **Enter Remote Address**
   - Type the IP address or hostname of the remote machine
   - Example: `192.168.1.100` or `server01.domain.com`

2. **Start Automation**
   - Click "Start Automation" button
   - The tool will run the automation sequence in the background

3. **Monitor Progress**
   - Watch the automation as it controls your mouse and keyboard
   - Check the console or log file for detailed progress

4. **Stop if Needed**
   - Click "Stop" button to halt automation
   - Or move mouse to corner (PyAutoGUI failsafe)

### What Happens During Automation

1. **Radmin Launch** (5 seconds)
   - Tool searches for Radmin in standard installation paths
   - Opens Radmin Viewer

2. **Connection** (1-3 seconds)
   - Clicks "Connect to an address"
   - Types remote address and presses Enter

3. **Authentication** (2-3 seconds)
   - Enters username
   - Tabs to password field
   - Enters first password and submits

4. **Session Activation** (5 seconds)
   - Double-clicks remote session tab
   - Waits for session to become active

5. **Windows Login** (2-4 seconds)
   - Clicks Ctrl+Alt+Del button
   - Types Windows password and presses Enter

6. **Event Viewer** (8-10 seconds)
   - Opens Event Viewer via Win+R
   - Navigates to System logs
   - Refreshes the view

## Project Structure

```
radmin_automation/
├── src/
│   ├── __init__.py
│   ├── main.py                      # Application entry point
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py              # Configuration (credentials, paths, coordinates)
│   ├── automation/
│   │   ├── __init__.py
│   │   ├── radmin_controller.py     # Radmin automation logic
│   │   └── event_viewer.py          # Event Viewer automation logic
│   ├── ui/
│   │   ├── __init__.py
│   │   └── main_window.py           # GUI implementation
│   └── utils/
│       ├── __init__.py
│       ├── input_helper.py          # Keyboard/mouse automation wrapper
│       └── window_manager.py        # Application launching utilities
├── requirements.txt                 # Python dependencies
├── radmin_automation.log           # Application log file (created at runtime)
└── README.md                       # This file
```

## Logging

The application creates a log file `radmin_automation.log` in the project directory with detailed information:

- Timestamps for all actions
- Debug information for troubleshooting
- Error messages with stack traces
- User actions and automation progress

Example log output:
```
2026-03-20 14:30:15,123 - src.main - INFO - Starting Radmin Automation Tool
2026-03-20 14:30:20,456 - src.automation.radmin_controller - INFO - Connecting to address: 192.168.1.100
2026-03-20 14:30:21,789 - src.utils.input_helper - DEBUG - Clicking at (445, 265)
```

## Troubleshooting

### Common Issues and Solutions

#### Automation clicks in wrong places
- **Solution**: Update screen coordinates in `settings.py` for your screen resolution
- **Tip**: Use `pyautogui.displayMousePosition()` to find correct coordinates

#### Radmin doesn't launch
- **Solution**: Add custom installation path to `RADMIN_PATHS` in `settings.py`
- **Check**: Verify Radmin Viewer 3 is actually installed

#### Credentials not entered correctly
- **Solution**: Increase delays in `DELAYS` dictionary
- **Tip**: Check if focus is on correct window during automation

#### Event Viewer doesn't open
- **Solution**: Increase `event_viewer_load` delay
- **Check**: Ensure Windows Event Viewer is accessible

#### PyAutoGUI failsafe triggered
- **Solution**: Don't move mouse to corners during automation
- **Note**: Move mouse to any corner to abort automation

### Debug Mode

To enable more detailed logging, change the logging level in `src/main.py`:

```python
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    # ... rest of configuration
)
```

## Safety Considerations

1. **Credentials Storage**: Passwords are stored in plain text. Consider using environment variables for production use.
2. **Mouse/Keyboard Control**: The automation takes control of mouse and keyboard. Keep hands away during execution.
3. **Failsafe**: Move mouse to corner to abort if something goes wrong.
4. **Backup Plan**: Keep a keyboard and mouse handy to regain control if needed.

## Security Recommendations

For production environments:
- Store credentials in environment variables
- Use encrypted configuration files
- Implement additional authentication where possible
- Log all automation activities for audit trails

## Limitations

- Screen resolution dependent (coordinates must match your setup)
- Requires Radmin Viewer to be installed
- Windows-specific (uses Win+R for Event Viewer)
- Timing may need adjustment on slower/faster systems

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with clear description of changes

## License

This project is licensed under the MIT License - see below:

```
MIT License

Copyright (c) 2026 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Support

For issues or questions:
1. Check the troubleshooting section above 
2. Review the log file for error messages
3. Open an issue on GitHub with:
   - Error description
   - Log file contents
   - Your environment details (Windows version, Python version, etc.)

## Version History

- **1.0.0** - Initial release
  - Basic Radmin automation
  - Event Viewer integration
  - GUI interface
  - Thread-safe execution

---

**Disclaimer**: This tool is for legitimate administrative purposes only. Ensure you have proper authorization before connecting to any remote systems. The authors assume no liability for misuse of this software.
