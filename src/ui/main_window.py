"""
Main UI window for Radmin Automation.

Provides a simple GUI for users to input IP address and control automation.
"""

import threading
import logging
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional
from src.automation.radmin_controller import RadminController
from src.automation.event_viewer import EventViewerAutomation
from src.utils.input_helper import InputHelper
from src.utils.window_manager import WindowManager

logger = logging.getLogger(__name__)


class AutomationWorker:
    """Worker thread for running automation tasks."""
    
    def __init__(self, address: str, radmin_controller: RadminController, 
                 event_viewer: EventViewerAutomation):
        """
        Initialize the automation worker.
        
        Args:
            address: IP address to connect to
            radmin_controller: RadminController instance
            event_viewer: EventViewerAutomation instance
        """
        self.address = address
        self.radmin_controller = radmin_controller
        self.event_viewer = event_viewer
        self.stop_flag = threading.Event()
    
    def run(self) -> None:
        """Execute the automation sequence."""
        logger.info(f"Starting automation for {self.address}")
        
        self.radmin_controller.window_manager.launch_radmin()
        self.radmin_controller.connect(self.address)
        self.radmin_controller.activate_remote_session()
        self.radmin_controller.send_windows_password()
        self.event_viewer.open_system_logs()
        
        logger.info("Automation completed")
    
    def stop(self) -> None:
        """Signal the automation to stop."""
        logger.info("Stop signal received")
        self.stop_flag.set()


class MainWindow:
    """Main application window."""
    
    def __init__(self, root: tk.Tk):
        """
        Initialize the main window.
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("Radmin Automation Tool")
        self.root.attributes("-topmost", True)
        
        # Initialize components
        self.input_helper = InputHelper()
        self.window_manager = WindowManager(self.input_helper)
        self.radmin_controller = RadminController(self.input_helper, self.window_manager)
        self.event_viewer = EventViewerAutomation(self.input_helper, self.window_manager)
        
        self.worker: Optional[threading.Thread] = None
        self.worker_instance: Optional[AutomationWorker] = None
        
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        """Set up the user interface components."""
        # Address input frame
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Address label and entry
        ttk.Label(frame, text="Remote Address/IP:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.address_var = tk.StringVar()
        address_entry = ttk.Entry(frame, textvariable=self.address_var, width=40)
        address_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Button frame
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Start button
        self.start_button = ttk.Button(button_frame, text="Start Automation", 
                                       command=self._start_automation)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        # Stop button
        self.stop_button = ttk.Button(button_frame, text="Stop", 
                                      command=self._stop_automation, state="disabled")
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
    
    def _start_automation(self) -> None:
        """Start the automation process in a separate thread."""
        address = self.address_var.get().strip()
        
        if not address:
            messagebox.showerror("Error", "Please enter a remote address or IP")
            logger.warning("Start attempted with empty address")
            return
        
        # Disable UI controls
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        
        # Create and start worker thread
        self.worker_instance = AutomationWorker(
            address, self.radmin_controller, self.event_viewer
        )
        self.worker = threading.Thread(target=self._run_automation, daemon=True)
        self.worker.start()
        
        logger.info(f"Automation started for {address}")
    
    def _run_automation(self) -> None:
        """Run the automation in a separate thread."""
        try:
            self.worker_instance.run()
            self.root.after(0, self._show_completion_message)
        except Exception as e:
            logger.error(f"Automation failed: {e}", exc_info=True)
            self.root.after(0, lambda: messagebox.showerror("Error", f"Automation failed:\n{str(e)}"))
        finally:
            self.root.after(0, self._reset_ui_controls)
    
    def _stop_automation(self) -> None:
        """Stop the running automation."""
        if self.worker_instance:
            self.worker_instance.stop()
        
        self._reset_ui_controls()
        logger.info("Automation stopped by user")
    
    def _reset_ui_controls(self) -> None:
        """Reset UI controls to enabled state."""
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
    
    def _show_completion_message(self) -> None:
        """Show completion message to user."""
        messagebox.showinfo("Success", "Automation completed successfully!")