"""
Radmin Automation Tool - Main Entry Point

This tool automates the process of connecting to remote machines via Radmin,
sending credentials, and opening Event Viewer to view system logs.
"""

import logging
import sys
import tkinter as tk
from src.ui.main_window import MainWindow

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('radmin_automation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Main entry point for the application."""
    try:
        logger.info("Starting Radmin Automation Tool")
        root = tk.Tk()
        app = MainWindow(root)
        root.mainloop()
    except KeyboardInterrupt:
        logger.info("Application terminated by user")
    except Exception as e:
        logger.error(f"Application failed: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()