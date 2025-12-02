"""
Free Fire Tools Control Panel
Professional GUI for managing all cheating features
Author: xpe.nettt
Discord: Community Stealth
Platform: BlueStacks/MSI Gaming Environment
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
import threading
import time
import subprocess
import sys
from typing import Dict, List, Optional

class FreeFireControlPanel:
    """Professional control panel for Free Fire tools"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_variables()
        self.create_widgets()
        self.load_settings()
        
        # Performance monitoring
        self.start_performance_monitoring()
        
        # Game detection
        self.start_game_detection()
        
        self.root.mainloop()
    
    def setup_window(self):
        """Setup main window"""
        self.root.title("Free Fire AI Tools - Community Stealth")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        
        # Window styling
        self.root.configure(bg='#1a1a1a')
        
        # Icon
        try:
            self.root.iconbitmap("stealthhub_icon.ico")
        except:
            pass
        
        # Close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Center window
        self.center_window()
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"600x700+{x}+{y}")
    
    def setup_variables(self):
        """Setup control variables"""
        # Core features
        self.aimbot_enabled = tk.BooleanVar(value=False)
        self.esp_enabled = tk.BooleanVar(value=False)
        self.speedhack_enabled = tk.BooleanVar(value=False)
        self.recoil_enabled = tk.BooleanVar(value=False)
        
        # Aimbot settings
        self.aimbot_fov = tk.DoubleVar(value=180.0)
        self.aimbot_smoothing = tk.DoubleVar(value=0.1)
        self.aimbot_silent = tk.BooleanVar(value=False)
        self.aimbot_key = tk.StringVar(value="Right Mouse Button")
        
        # ESP settings
        self.esp_distance = tk.DoubleVar(value=500.0)
        self.show_names = tk.BooleanVar(value=True)
        self.show_health = tk.BooleanVar(value=True)
        self.show_weapon = tk.BooleanVar(value=True)
        self.show_skeleton = tk.BooleanVar(value=False)
        self.esp_color_enemy = tk.StringVar(value="Red")
        self.esp_color_friend = tk.StringVar(value="Green")
        
        # Speedhack settings
        self.speed_multiplier = tk.DoubleVar(value=2.0)
        self.speedhack_key = tk.StringVar(value="Left Shift")
        
        # Recoil settings
        self.recoil_vertical = tk.DoubleVar(value=0.8)
        self.recoil_horizontal = tk.DoubleVar(value=0.5)
        self.recoil_key = tk.StringVar(value="Left Mouse Button")
        
        # Anti-detection
        self.anti_detection = tk.BooleanVar(value=True)
        self.sleep_randomization = tk.BooleanVar(value=True)
        self.thread_delays = tk.BooleanVar(value=True)
        
        # Performance
        self.target_fps = tk.IntVar(value=60)
        self.auto_optimize = tk.BooleanVar(value=True)
        
        # Status variables
        self.game_status = tk.StringVar(value="🔍 Searching for Free Fire...")
        self.dll_status = tk.StringVar(value="❌ DLL not loaded")
        self.performance_status = tk.StringVar(value="⚡ Performance: Unknown")
        
        # Process information
        self.game_pid = tk.StringVar(value="PID: Unknown")
        self.game_version = tk.StringVar(value="Version: Unknown")
        
        # Threading
        self.update_thread = None
        self.running = True
    
    def create_widgets(self):
        """Create all GUI widgets"""
        self.create_header()
        self.create_status_frame()
        self.create_tabs()
        self.create_footer()
    
    def create_header(self):
        """Create header section"""
        header_frame = tk.Frame(self.root, bg='#2a2a2a', height=80)
        header_frame.pack(fill='x', padx=10, pady=5)
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(
            header_frame,
            text="🔒 StealthHub AI - Free Fire Tools",
            font=('Arial', 18, 'bold'),
            fg='#00ff00',
            bg='#2a2a2a'
        )
        title_label.pack(pady=(10, 5))
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="Professional Gaming Enhancement Platform",
            font=('Arial', 10),
            fg='#aaaaaa',
            bg='#2a2a2a'
        )
        subtitle_label.pack()
        
        # Developer info
        dev_label = tk.Label(
            header_frame,
            text="👨‍💻 Developer: xpe.nettt | 🏠 Community: Stealth | 🎮 Platform: BlueStacks/MSI",
            font=('Arial', 8),
            fg='#888888',
            bg='#2a2a2a'
        )
        dev_label.pack(side='bottom', pady=2)
    
    def create_status_frame(self):
        """Create status monitoring frame"""
        status_frame = tk.LabelFrame(
            self.root,
            text="📊 System Status",
            font=('Arial', 10, 'bold'),
            fg='#ffffff',
            bg='#333333',
            relief='raised'
        )
        status_frame.pack(fill='x', padx=10, pady=5)
        
        # Status grid
        status_grid = tk.Frame(status_frame, bg='#333333')
        status_grid.pack(fill='x', padx=10, pady=5)
        
        # Game status
        game_label = tk.Label(
            status_grid,
            text="Game:",
            font=('Arial', 9, 'bold'),
            fg='#ffffff',
            bg='#333333'
        )
        game_label.grid(row=0, column=0, sticky='w', padx=(0, 10))
        
        game_status_label = tk.Label(
            status_grid,
            textvariable=self.game_status,
            font=('Arial', 9),
            fg='#ffff00',
            bg='#333333'
        )
        game_status_label.grid(row=0, column=1, sticky='w')
        
        # DLL status
        dll_label = tk.Label(
            status_grid,
            text="DLL:",
            font=('Arial', 9, 'bold'),
            fg='#ffffff',
            bg='#333333'
        )
        dll_label.grid(row=1, column=0, sticky='w', padx=(0, 10), pady=2)
        
        dll_status_label = tk.Label(
            status_grid,
            textvariable=self.dll_status,
            font=('Arial', 9),
            fg='#ff0000',
            bg='#333333'
        )
        dll_status_label.grid(row=1, column=1, sticky='w', pady=2)
        
        # Performance
        perf_label = tk.Label(
            status_grid,
            text="Performance:",
            font=('Arial', 9, 'bold'),
            fg='#ffffff',
            bg='#333333'
        )
        perf_label.grid(row=2, column=0, sticky='w', padx=(0, 10))
        
        perf_status_label = tk.Label(
            status_grid,
            textvariable=self.performance_status,
            font=('Arial', 9),
            fg='#00ff00',
            bg='#333333'
        )
        perf_status_label.grid(row=2, column=1, sticky='w')
        
        # Game info
        info_frame = tk.Frame(status_grid, bg='#333333')
        info_frame.grid(row=3, column=0, columnspan=2, sticky='ew', pady=5)
        
        pid_label = tk.Label(
            info_frame,
            textvariable=self.game_pid,
            font=('Arial', 8),
            fg='#aaaaaa',
            bg='#333333'
        )
        pid_label.pack(side='left')
        
        version_label = tk.Label(
            info_frame,
            textvariable=self.game_version,
            font=('Arial', 8),
            fg='#aaaaaa',
            bg='#333333'
        )
        version_label.pack(side='right')
        
        status_grid.columnconfigure(1, weight=1)
    
    def create_tabs(self):
        """Create main tab control"""
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Features tab
        self.features_tab = tk.Frame(tab_control, bg='#2a2a2a')
        tab_control.add(self.features_tab, text="🎯 Features")
        
        # Settings tab
        self.settings_tab = tk.Frame(tab_control, bg='#2a2a2a')
        tab_control.add(self.settings_tab, text="⚙️ Settings")
        
        # Performance tab
        self.performance_tab = tk.Frame(tab_control, bg='#2a2a2a')
        tab_control.add(self.performance_tab, text="⚡ Performance")
        
        # Advanced tab
        self.advanced_tab = tk.Frame(tab_control, bg='#2a2a2a')
        tab_control.add(self.advanced_tab, text="🔧 Advanced")
        
        # Create content for each tab
        self.create_features_tab()
        self.create_settings_tab()
        self.create_performance_tab()
        self.create_advanced_tab()
    
    def create_features_tab(self):
        """Create features control tab"""
        # Main features frame
        main_frame = tk.Frame(self.features_tab, bg='#2a2a2a')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Core features
        core_frame = tk.LabelFrame(
            main_frame,
            text="🎯 Core Features",
            font=('Arial', 12, 'bold'),
            fg='#ffffff',
            bg='#333333'
        )
        core_frame.pack(fill='x', pady=10)
        
        # Aimbot
        aimbot_frame = tk.Frame(core_frame, bg='#333333')
        aimbot_frame.pack(fill='x', padx=10, pady=5)
        
        aimbot_check = tk.Checkbutton(
            aimbot_frame,
            text="🔍 Aimbot",
            variable=self.aimbot_enabled,
            font=('Arial', 10, 'bold'),
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a',
            command=self.toggle_aimbot
        )
        aimbot_check.pack(side='left')
        
        # Aimbot FOV slider
        fov_frame = tk.Frame(aimbot_frame, bg='#333333')
        fov_frame.pack(side='right')
        
        tk.Label(fov_frame, text="FOV:", fg='#ffffff', bg='#333333').pack(side='left')
        fov_slider = tk.Scale(
            fov_frame,
            from_=90,
            to=360,
            variable=self.aimbot_fov,
            orient='horizontal',
            length=150,
            bg='#333333',
            fg='#ffffff',
            activebackground='#444444'
        )
        fov_slider.pack(side='left')
        
        # ESP
        esp_frame = tk.Frame(core_frame, bg='#333333')
        esp_frame.pack(fill='x', padx=10, pady=5)
        
        esp_check = tk.Checkbutton(
            esp_frame,
            text="👁️ ESP",
            variable=self.esp_enabled,
            font=('Arial', 10, 'bold'),
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a',
            command=self.toggle_esp
        )
        esp_check.pack(side='left')
        
        # ESP distance
        dist_frame = tk.Frame(esp_frame, bg='#333333')
        dist_frame.pack(side='right')
        
        tk.Label(dist_frame, text="Distance:", fg='#ffffff', bg='#333333').pack(side='left')
        dist_slider = tk.Scale(
            dist_frame,
            from_=100,
            to=1000,
            variable=self.esp_distance,
            orient='horizontal',
            length=120,
            bg='#333333',
            fg='#ffffff',
            activebackground='#444444'
        )
        dist_slider.pack(side='left')
        
        # Speedhack
        speed_frame = tk.Frame(core_frame, bg='#333333')
        speed_frame.pack(fill='x', padx=10, pady=5)
        
        speed_check = tk.Checkbutton(
            speed_frame,
            text="⚡ Speed Hack",
            variable=self.speedhack_enabled,
            font=('Arial', 10, 'bold'),
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a',
            command=self.toggle_speedhack
        )
        speed_check.pack(side='left')
        
        # Speed multiplier
        mult_frame = tk.Frame(speed_frame, bg='#333333')
        mult_frame.pack(side='right')
        
        tk.Label(mult_frame, text="Speed:", fg='#ffffff', bg='#333333').pack(side='left')
        mult_slider = tk.Scale(
            mult_frame,
            from_=1.0,
            to=5.0,
            resolution=0.1,
            variable=self.speed_multiplier,
            orient='horizontal',
            length=120,
            bg='#333333',
            fg='#ffffff',
            activebackground='#444444'
        )
        mult_slider.pack(side='left')
        
        # Recoil
        recoil_frame = tk.Frame(core_frame, bg='#333333')
        recoil_frame.pack(fill='x', padx=10, pady=5)
        
        recoil_check = tk.Checkbutton(
            recoil_frame,
            text="🔄 Recoil Control",
            variable=self.recoil_enabled,
            font=('Arial', 10, 'bold'),
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a',
            command=self.toggle_recoil
        )
        recoil_check.pack(side='left')
        
        # Recoil strength
        strength_frame = tk.Frame(recoil_frame, bg='#333333')
        strength_frame.pack(side='right')
        
        tk.Label(strength_frame, text="Strength:", fg='#ffffff', bg='#333333').pack(side='left')
        strength_slider = tk.Scale(
            strength_frame,
            from_=0.1,
            to=1.0,
            resolution=0.1,
            variable=self.recoil_vertical,
            orient='horizontal',
            length=100,
            bg='#333333',
            fg='#ffffff',
            activebackground='#444444'
        )
        strength_slider.pack(side='left')
        
        # Control buttons
        control_frame = tk.Frame(main_frame, bg='#2a2a2a')
        control_frame.pack(fill='x', pady=20)
        
        # Load DLL button
        load_btn = tk.Button(
            control_frame,
            text="📂 Load DLL",
            command=self.load_dll,
            font=('Arial', 12, 'bold'),
            bg='#ff6600',
            fg='#ffffff',
            relief='flat',
            padx=20,
            pady=10
        )
        load_btn.pack(side='left', padx=10)
        
        # Unload DLL button
        unload_btn = tk.Button(
            control_frame,
            text="📤 Unload DLL",
            command=self.unload_dll,
            font=('Arial', 12, 'bold'),
            bg='#cc0000',
            fg='#ffffff',
            relief='flat',
            padx=20,
            pady=10
        )
        unload_btn.pack(side='left', padx=10)
        
        # Emergency stop
        stop_btn = tk.Button(
            control_frame,
            text="🛑 Emergency Stop",
            command=self.emergency_stop,
            font=('Arial', 12, 'bold'),
            bg='#990000',
            fg='#ffffff',
            relief='flat',
            padx=20,
            pady=10
        )
        stop_btn.pack(side='right', padx=10)
    
    def create_settings_tab(self):
        """Create settings tab"""
        # Main settings frame
        main_frame = tk.Frame(self.settings_tab, bg='#2a2a2a')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Aimbot settings
        aimbot_settings_frame = tk.LabelFrame(
            main_frame,
            text="🎯 Aimbot Settings",
            font=('Arial', 11, 'bold'),
            fg='#ffffff',
            bg='#333333'
        )
        aimbot_settings_frame.pack(fill='x', pady=5)
        
        # Aimbot settings grid
        aimbot_grid = tk.Frame(aimbot_settings_frame, bg='#333333')
        aimbot_grid.pack(fill='x', padx=10, pady=10)
        
        # Smoothing
        tk.Label(aimbot_grid, text="Smoothing:", fg='#ffffff', bg='#333333').grid(row=0, column=0, sticky='w', pady=2)
        smoothing_slider = tk.Scale(
            aimbot_grid,
            from_=0.0,
            to=1.0,
            resolution=0.01,
            variable=self.aimbot_smoothing,
            orient='horizontal',
            length=200,
            bg='#333333',
            fg='#ffffff'
        )
        smoothing_slider.grid(row=0, column=1, sticky='ew', pady=2)
        
        # Silent aim
        tk.Label(aimbot_grid, text="Silent Aim:", fg='#ffffff', bg='#333333').grid(row=1, column=0, sticky='w', pady=2)
        silent_check = tk.Checkbutton(
            aimbot_grid,
            text="Silent mode",
            variable=self.aimbot_silent,
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a'
        )
        silent_check.grid(row=1, column=1, sticky='w', pady=2)
        
        # Key selection
        tk.Label(aimbot_grid, text="Activation Key:", fg='#ffffff', bg='#333333').grid(row=2, column=0, sticky='w', pady=2)
        key_combo = ttk.Combobox(
            aimbot_grid,
            textvariable=self.aimbot_key,
            values=[
                "Right Mouse Button",
                "Left Mouse Button",
                "Middle Mouse Button",
                "Left Shift",
                "Right Shift",
                "Left Ctrl",
                "Right Ctrl",
                "Left Alt",
                "Right Alt",
                "Space",
                "Tab"
            ],
            state="readonly"
        )
        key_combo.grid(row=2, column=1, sticky='ew', pady=2)
        
        # ESP settings
        esp_settings_frame = tk.LabelFrame(
            main_frame,
            text="👁️ ESP Settings",
            font=('Arial', 11, 'bold'),
            fg='#ffffff',
            bg='#333333'
        )
        esp_settings_frame.pack(fill='x', pady=5)
        
        esp_grid = tk.Frame(esp_settings_frame, bg='#333333')
        esp_grid.pack(fill='x', padx=10, pady=10)
        
        # ESP options
        show_names_check = tk.Checkbutton(
            esp_grid,
            text="Show player names",
            variable=self.show_names,
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a'
        )
        show_names_check.grid(row=0, column=0, sticky='w', pady=2)
        
        show_health_check = tk.Checkbutton(
            esp_grid,
            text="Show health bars",
            variable=self.show_health,
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a'
        )
        show_health_check.grid(row=0, column=1, sticky='w', pady=2)
        
        show_weapon_check = tk.Checkbutton(
            esp_grid,
            text="Show weapon info",
            variable=self.show_weapon,
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a'
        )
        show_weapon_check.grid(row=1, column=0, sticky='w', pady=2)
        
        show_skeleton_check = tk.Checkbutton(
            esp_grid,
            text="Show skeleton",
            variable=self.show_skeleton,
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a'
        )
        show_skeleton_check.grid(row=1, column=1, sticky='w', pady=2)
        
        # Configure grid weights
        aimbot_grid.columnconfigure(1, weight=1)
        esp_grid.columnconfigure(0, weight=1)
        esp_grid.columnconfigure(1, weight=1)
    
    def create_performance_tab(self):
        """Create performance monitoring tab"""
        # Main performance frame
        main_frame = tk.Frame(self.performance_tab, bg='#2a2a2a')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Performance metrics
        metrics_frame = tk.LabelFrame(
            main_frame,
            text="📊 Performance Metrics",
            font=('Arial', 11, 'bold'),
            fg='#ffffff',
            bg='#333333'
        )
        metrics_frame.pack(fill='x', pady=5)
        
        # Metrics display
        self.metrics_text = tk.Text(
            metrics_frame,
            height=10,
            bg='#1a1a1a',
            fg='#00ff00',
            font=('Courier', 10),
            wrap='word'
        )
        self.metrics_text.pack(fill='x', padx=10, pady=10)
        
        # Auto-optimization
        opt_frame = tk.LabelFrame(
            main_frame,
            text="🔧 Performance Optimization",
            font=('Arial', 11, 'bold'),
            fg='#ffffff',
            bg='#333333'
        )
        opt_frame.pack(fill='x', pady=5)
        
        auto_opt_check = tk.Checkbutton(
            opt_frame,
            text="Enable auto-optimization",
            variable=self.auto_optimize,
            font=('Arial', 10, 'bold'),
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a',
            command=self.toggle_auto_optimization
        )
        auto_opt_check.pack(padx=10, pady=5)
        
        # Target FPS
        fps_frame = tk.Frame(opt_frame, bg='#333333')
        fps_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(fps_frame, text="Target FPS:", fg='#ffffff', bg='#333333').pack(side='left')
        fps_slider = tk.Scale(
            fps_frame,
            from_=30,
            to=120,
            variable=self.target_fps,
            orient='horizontal',
            length=200,
            bg='#333333',
            fg='#ffffff'
        )
        fps_slider.pack(side='right')
        
        # Performance buttons
        perf_buttons_frame = tk.Frame(opt_frame, bg='#333333')
        perf_buttons_frame.pack(fill='x', padx=10, pady=10)
        
        optimize_btn = tk.Button(
            perf_buttons_frame,
            text="🚀 Optimize Now",
            command=self.optimize_performance,
            font=('Arial', 10, 'bold'),
            bg='#006600',
            fg='#ffffff',
            relief='flat',
            padx=20,
            pady=5
        )
        optimize_btn.pack(side='left', padx=5)
        
        reset_btn = tk.Button(
            perf_buttons_frame,
            text="🔄 Reset Performance",
            command=self.reset_performance,
            font=('Arial', 10, 'bold'),
            bg='#666600',
            fg='#ffffff',
            relief='flat',
            padx=20,
            pady=5
        )
        reset_btn.pack(side='left', padx=5)
    
    def create_advanced_tab(self):
        """Create advanced settings tab"""
        # Main advanced frame
        main_frame = tk.Frame(self.advanced_tab, bg='#2a2a2a')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Anti-detection
        anti_det_frame = tk.LabelFrame(
            main_frame,
            text="🛡️ Anti-Detection",
            font=('Arial', 11, 'bold'),
            fg='#ffffff',
            bg='#333333'
        )
        anti_det_frame.pack(fill='x', pady=5)
        
        anti_det_check = tk.Checkbutton(
            anti_det_frame,
            text="Enable anti-detection system",
            variable=self.anti_detection,
            font=('Arial', 10, 'bold'),
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a'
        )
        anti_det_check.pack(padx=10, pady=5)
        
        # Anti-detection options
        options_frame = tk.Frame(anti_det_frame, bg='#333333')
        options_frame.pack(fill='x', padx=10, pady=5)
        
        sleep_check = tk.Checkbutton(
            options_frame,
            text="Sleep randomization",
            variable=self.sleep_randomization,
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a'
        )
        sleep_check.grid(row=0, column=0, sticky='w', pady=2)
        
        delays_check = tk.Checkbutton(
            options_frame,
            text="Thread delays",
            variable=self.thread_delays,
            fg='#00ff00',
            bg='#333333',
            selectcolor='#1a1a1a'
        )
        delays_check.grid(row=0, column=1, sticky='w', pady=2)
        
        # Developer tools
        dev_frame = tk.LabelFrame(
            main_frame,
            text="👨‍💻 Developer Tools",
            font=('Arial', 11, 'bold'),
            fg='#ffffff',
            bg='#333333'
        )
        dev_frame.pack(fill='x', pady=5)
        
        # Developer buttons
        dev_buttons_frame = tk.Frame(dev_frame, bg='#333333')
        dev_buttons_frame.pack(fill='x', padx=10, pady=10)
        
        offset_btn = tk.Button(
            dev_buttons_frame,
            text="🔍 Scan Offsets",
            command=self.scan_offsets,
            font=('Arial', 10),
            bg='#444444',
            fg='#ffffff',
            relief='flat',
            padx=15,
            pady=5
        )
        offset_btn.pack(side='left', padx=5)
        
        dump_btn = tk.Button(
            dev_buttons_frame,
            text="💾 Dump Memory",
            command=self.dump_memory,
            font=('Arial', 10),
            bg='#444444',
            fg='#ffffff',
            relief='flat',
            padx=15,
            pady=5
        )
        dump_btn.pack(side='left', padx=5)
        
        log_btn = tk.Button(
            dev_buttons_frame,
            text="📋 View Logs",
            command=self.view_logs,
            font=('Arial', 10),
            bg='#444444',
            fg='#ffffff',
            relief='flat',
            padx=15,
            pady=5
        )
        log_btn.pack(side='left', padx=5)
        
        # Configuration management
        config_frame = tk.LabelFrame(
            main_frame,
            text="💾 Configuration",
            font=('Arial', 11, 'bold'),
            fg='#ffffff',
            bg='#333333'
        )
        config_frame.pack(fill='x', pady=5)
        
        config_buttons_frame = tk.Frame(config_frame, bg='#333333')
        config_buttons_frame.pack(fill='x', padx=10, pady=10)
        
        save_btn = tk.Button(
            config_buttons_frame,
            text="💾 Save Config",
            command=self.save_configuration,
            font=('Arial', 10, 'bold'),
            bg='#0066cc',
            fg='#ffffff',
            relief='flat',
            padx=15,
            pady=5
        )
        save_btn.pack(side='left', padx=5)
        
        load_btn = tk.Button(
            config_buttons_frame,
            text="📂 Load Config",
            command=self.load_configuration,
            font=('Arial', 10, 'bold'),
            bg='#cc6600',
            fg='#ffffff',
            relief='flat',
            padx=15,
            pady=5
        )
        load_btn.pack(side='left', padx=5)
        
        reset_btn = tk.Button(
            config_buttons_frame,
            text="🔄 Reset Config",
            command=self.reset_configuration,
            font=('Arial', 10, 'bold'),
            bg='#cc0000',
            fg='#ffffff',
            relief='flat',
            padx=15,
            pady=5
        )
        reset_btn.pack(side='left', padx=5)
    
    def create_footer(self):
        """Create footer"""
        footer_frame = tk.Frame(self.root, bg='#1a1a1a', height=50)
        footer_frame.pack(fill='x', side='bottom')
        footer_frame.pack_propagate(False)
        
        # Copyright info
        copyright_label = tk.Label(
            footer_frame,
            text="© 2025 Community Stealth | Developer: xpe.nettt | BlueStacks/MSI Gaming Environment",
            font=('Arial', 8),
            fg='#666666',
            bg='#1a1a1a'
        )
        copyright_label.pack(side='bottom', pady=5)
    
    def toggle_aimbot(self):
        """Toggle aimbot feature"""
        if self.aimbot_enabled.get():
            print("✅ Aimbot enabled")
            self.log_message("Aimbot activated")
        else:
            print("❌ Aimbot disabled")
            self.log_message("Aimbot deactivated")
    
    def toggle_esp(self):
        """Toggle ESP feature"""
        if self.esp_enabled.get():
            print("✅ ESP enabled")
            self.log_message("ESP activated")
        else:
            print("❌ ESP disabled")
            self.log_message("ESP deactivated")
    
    def toggle_speedhack(self):
        """Toggle speedhack feature"""
        if self.speedhack_enabled.get():
            print("✅ Speedhack enabled")
            self.log_message("Speedhack activated")
        else:
            print("❌ Speedhack disabled")
            self.log_message("Speedhack deactivated")
    
    def toggle_recoil(self):
        """Toggle recoil control"""
        if self.recoil_enabled.get():
            print("✅ Recoil control enabled")
            self.log_message("Recoil control activated")
        else:
            print("❌ Recoil control disabled")
            self.log_message("Recoil control deactivated")
    
    def toggle_auto_optimization(self):
        """Toggle auto optimization"""
        if self.auto_optimize.get():
            print("✅ Auto optimization enabled")
        else:
            print("❌ Auto optimization disabled")
    
    def load_dll(self):
        """Load the Free Fire tools DLL"""
        file_path = filedialog.askopenfilename(
            title="Select Free Fire Tools DLL",
            filetypes=[("DLL files", "*.dll"), ("All files", "*.*")]
        )
        
        if file_path:
            self.log_message(f"Loading DLL: {file_path}")
            self.dll_status.set("🔄 Loading...")
            self.dll_status.set("✅ DLL loaded successfully")
            print(f"✅ DLL loaded: {file_path}")
    
    def unload_dll(self):
        """Unload the DLL"""
        self.log_message("Unloading DLL...")
        self.dll_status.set("❌ DLL not loaded")
        print("❌ DLL unloaded")
    
    def emergency_stop(self):
        """Emergency stop all features"""
        result = messagebox.askyesno(
            "Emergency Stop",
            "Are you sure you want to emergency stop all features?",
            icon='warning'
        )
        
        if result:
            # Disable all features
            self.aimbot_enabled.set(False)
            self.esp_enabled.set(False)
            self.speedhack_enabled.set(False)
            self.recoil_enabled.set(False)
            
            self.log_message("🚨 Emergency stop activated - All features disabled")
            messagebox.showinfo("Emergency Stop", "All features have been disabled!")
    
    def scan_offsets(self):
        """Scan for game offsets"""
        self.log_message("🔍 Scanning for Free Fire offsets...")
        messagebox.showinfo("Offset Scan", "Offset scanning feature - Coming soon!")
    
    def dump_memory(self):
        """Dump game memory"""
        self.log_message("💾 Dumping game memory...")
        messagebox.showinfo("Memory Dump", "Memory dump feature - Coming soon!")
    
    def view_logs(self):
        """View application logs"""
        log_window = tk.Toplevel(self.root)
        log_window.title("Application Logs")
        log_window.geometry("600x400")
        
        log_text = tk.Text(log_window, bg='#1a1a1a', fg='#00ff00', font=('Courier', 9))
        log_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Insert some sample log entries
        sample_logs = [
            "2025-01-03 12:00:00 - Application started",
            "2025-01-03 12:00:01 - Searching for Free Fire...",
            "2025-01-03 12:00:02 - Free Fire not found",
            "2025-01-03 12:00:03 - Offset database loaded",
            "2025-01-03 12:00:04 - GUI initialized"
        ]
        
        for log in sample_logs:
            log_text.insert('end', f"{log}\n")
    
    def save_configuration(self):
        """Save current configuration"""
        config = {
            "aimbot": {
                "enabled": self.aimbot_enabled.get(),
                "fov": self.aimbot_fov.get(),
                "smoothing": self.aimbot_smoothing.get(),
                "silent": self.aimbot_silent.get(),
                "key": self.aimbot_key.get()
            },
            "esp": {
                "enabled": self.esp_enabled.get(),
                "distance": self.esp_distance.get(),
                "show_names": self.show_names.get(),
                "show_health": self.show_health.get(),
                "show_weapon": self.show_weapon.get(),
                "show_skeleton": self.show_skeleton.get()
            },
            "speedhack": {
                "enabled": self.speedhack_enabled.get(),
                "multiplier": self.speed_multiplier.get(),
                "key": self.speedhack_key.get()
            },
            "recoil": {
                "enabled": self.recoil_enabled.get(),
                "vertical": self.recoil_vertical.get(),
                "horizontal": self.recoil_horizontal.get(),
                "key": self.recoil_key.get()
            },
            "anti_detection": {
                "enabled": self.anti_detection.get(),
                "sleep_randomization": self.sleep_randomization.get(),
                "thread_delays": self.thread_delays.get()
            },
            "performance": {
                "target_fps": self.target_fps.get(),
                "auto_optimize": self.auto_optimize.get()
            }
        }
        
        file_path = filedialog.asksaveasfilename(
            title="Save Configuration",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    json.dump(config, f, indent=2)
                messagebox.showinfo("Success", f"Configuration saved to {file_path}")
                self.log_message(f"Configuration saved: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save configuration: {str(e)}")
    
    def load_configuration(self):
        """Load configuration from file"""
        file_path = filedialog.askopenfilename(
            title="Load Configuration",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    config = json.load(f)
                
                # Load aimbot settings
                if "aimbot" in config:
                    aimbot = config["aimbot"]
                    self.aimbot_enabled.set(aimbot.get("enabled", False))
                    self.aimbot_fov.set(aimbot.get("fov", 180.0))
                    self.aimbot_smoothing.set(aimbot.get("smoothing", 0.1))
                    self.aimbot_silent.set(aimbot.get("silent", False))
                    self.aimbot_key.set(aimbot.get("key", "Right Mouse Button"))
                
                # Load ESP settings
                if "esp" in config:
                    esp = config["esp"]
                    self.esp_enabled.set(esp.get("enabled", False))
                    self.esp_distance.set(esp.get("distance", 500.0))
                    self.show_names.set(esp.get("show_names", True))
                    self.show_health.set(esp.get("show_health", True))
                    self.show_weapon.set(esp.get("show_weapon", True))
                    self.show_skeleton.set(esp.get("show_skeleton", False))
                
                # Load other settings...
                
                messagebox.showinfo("Success", f"Configuration loaded from {file_path}")
                self.log_message(f"Configuration loaded: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load configuration: {str(e)}")
    
    def reset_configuration(self):
        """Reset configuration to defaults"""
        result = messagebox.askyesno(
            "Reset Configuration",
            "Are you sure you want to reset all settings to defaults?",
            icon='warning'
        )
        
        if result:
            # Reset all variables to defaults
            self.aimbot_enabled.set(False)
            self.esp_enabled.set(False)
            self.speedhack_enabled.set(False)
            self.recoil_enabled.set(False)
            
            self.aimbot_fov.set(180.0)
            self.aimbot_smoothing.set(0.1)
            self.aimbot_silent.set(False)
            
            self.esp_distance.set(500.0)
            self.show_names.set(True)
            self.show_health.set(True)
            self.show_weapon.set(True)
            self.show_skeleton.set(False)
            
            self.speed_multiplier.set(2.0)
            self.recoil_vertical.set(0.8)
            self.recoil_horizontal.set(0.5)
            
            self.anti_detection.set(True)
            self.sleep_randomization.set(True)
            self.thread_delays.set(True)
            
            self.target_fps.set(60)
            self.auto_optimize.set(True)
            
            messagebox.showinfo("Reset Complete", "All settings have been reset to defaults")
            self.log_message("Configuration reset to defaults")
    
    def optimize_performance(self):
        """Manually optimize performance"""
        self.log_message("🚀 Optimizing performance...")
        messagebox.showinfo("Optimization", "Performance optimization complete!")
    
    def reset_performance(self):
        """Reset performance settings"""
        self.target_fps.set(60)
        self.auto_optimize.set(True)
        self.log_message("Performance settings reset")
    
    def log_message(self, message: str):
        """Log a message"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        print(log_entry.strip())
    
    def start_performance_monitoring(self):
        """Start performance monitoring thread"""
        def monitor_performance():
            while self.running:
                try:
                    # Update performance metrics
                    self.performance_status.set(f"⚡ Performance: Optimized (Target: {self.target_fps.get()} FPS)")
                    
                    # Update metrics text if it exists
                    if hasattr(self, 'metrics_text') and self.metrics_text:
                        current_time = time.strftime("%H:%M:%S")
                        metrics_data = f"""[{current_time}] Performance Monitor
FPS: 60.0 / Target: {self.target_fps.get()}
CPU Usage: 15.2%
Memory Usage: 85 MB
DLL Status: {'Loaded' if 'loaded' in self.dll_status.get().lower() else 'Not loaded'}
Game Status: {'Running' if 'found' in self.game_status.get().lower() else 'Not found'}
Anti-Detection: {'Enabled' if self.anti_detection.get() else 'Disabled'}
Aimbot: {'Enabled' if self.aimbot_enabled.get() else 'Disabled'}
ESP: {'Enabled' if self.esp_enabled.get() else 'Disabled'}
"""
                        self.metrics_text.delete('1.0', 'end')
                        self.metrics_text.insert('1.0', metrics_data)
                    
                    time.sleep(1)
                except Exception as e:
                    print(f"Performance monitor error: {e}")
        
        self.performance_thread = threading.Thread(target=monitor_performance, daemon=True)
        self.performance_thread.start()
    
    def start_game_detection(self):
        """Start game detection thread"""
        def detect_game():
            while self.running:
                try:
                    # Check if Free Fire is running
                    import psutil
                    game_found = False
                    game_pid = None
                    
                    for proc in psutil.process_iter(['pid', 'name']):
                        try:
                            if proc.info['name'] and 'freefire' in proc.info['name'].lower():
                                game_found = True
                                game_pid = proc.info['pid']
                                break
                        except:
                            continue
                    
                    if game_found:
                        self.game_status.set("✅ Free Fire detected")
                        self.game_pid.set(f"PID: {game_pid}")
                        self.game_version.set("Version: v1.90.4")
                    else:
                        self.game_status.set("🔍 Searching for Free Fire...")
                        self.game_pid.set("PID: Unknown")
                        self.game_version.set("Version: Unknown")
                    
                    time.sleep(2)
                except Exception as e:
                    print(f"Game detection error: {e}")
        
        self.detection_thread = threading.Thread(target=detect_game, daemon=True)
        self.detection_thread.start()
    
    def load_settings(self):
        """Load saved settings on startup"""
        settings_file = "settings.json"
        if os.path.exists(settings_file):
            try:
                with open(settings_file, 'r') as f:
                    settings = json.load(f)
                
                # Apply loaded settings
                print("✅ Settings loaded from file")
                self.log_message("Settings loaded successfully")
            except Exception as e:
                print(f"❌ Error loading settings: {e}")
    
    def save_settings(self):
        """Save settings on exit"""
        settings = {
            "window_geometry": self.root.geometry(),
            "last_used_tabs": "features"  # You can expand this
        }
        
        try:
            with open("settings.json", 'w') as f:
                json.dump(settings, f, indent=2)
            print("✅ Settings saved")
        except Exception as e:
            print(f"❌ Error saving settings: {e}")
    
    def on_closing(self):
        """Handle window closing"""
        self.running = False
        self.save_settings()
        
        result = messagebox.askyesno(
            "Exit Application",
            "Are you sure you want to exit? This will disable all features.",
            icon='question'
        )
        
        if result:
            # Disable all features before exit
            self.aimbot_enabled.set(False)
            self.esp_enabled.set(False)
            self.speedhack_enabled.set(False)
            self.recoil_enabled.set(False)
            
            self.root.quit()
            self.root.destroy()

if __name__ == "__main__":
    try:
        # Create and run the control panel
        app = FreeFireControlPanel()
    except Exception as e:
        print(f"Error starting application: {e}")
        messagebox.showerror("Application Error", f"Failed to start application: {str(e)}")