"""
gui.py - Graphical User Interface for Phishing Detection Awareness Tool

A Tkinter-based GUI that provides an interactive, user-friendly interface
for detecting phishing emails and URLs with visual risk indicators.
"""

import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from datetime import datetime
import re
from detector.email_checker import check_email
from detector.url_checker import check_url
from detector.validator import validate_input
from utils.score_calculator import calculate_risk_score, calculate_risk_level
from utils.explanation import get_explanations
from utils.statistics import global_stats


class PhishingDetectionGUI:
    """
    Main GUI class for the Phishing Detection Awareness Tool.
    Provides an interactive interface with visual risk indicators and detailed reports.
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("🔒 Phishing Detection Awareness Tool")
        self.root.geometry("1000x800")
        self.root.configure(bg="#0a0e27")  # Dark background
        
        # Configure style
        self.setup_styles()
        
        # Build the GUI
        self.create_widgets()
        
        # Store current results for report saving
        self.current_results = None
        
        # Store detected items for multi-analysis
        self.detected_items = []
        self.current_analysis_index = 0
        
    def setup_styles(self):
        """Configure custom colors and styles for cybersecurity theme."""
        self.bg_color = "#0a0e27"  # Dark blue-black
        self.fg_color = "#00ff88"  # Neon green
        self.accent_color = "#ff1744"  # Neon red
        self.secondary_color = "#2196F3"  # Blue
        self.warning_color = "#ff9800"  # Orange
        
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure button style
        style.configure('TButton', 
                       font=('Courier', 10, 'bold'),
                       padding=10)
        style.map('TButton',
                 background=[('active', '#00cc66')])
    
    def extract_emails(self, text):
        """Extract all email addresses from text."""
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(email_pattern, text)
    
    def extract_urls(self, text):
        """Extract all URLs from text."""
        url_pattern = r'https?://[^\s]+|www\.[^\s]+'
        urls = re.findall(url_pattern, text)
        # Filter out invalid URLs
        return [url for url in urls if len(url) > 10]
    
    def auto_detect_and_extract(self, text):
        """
        Automatically detect emails and URLs in text.
        Returns list of tuples: (type, content)
        """
        items = []
        
        # Extract emails
        emails = self.extract_emails(text)
        for email in emails:
            items.append(("email", email))
        
        # Extract URLs
        urls = self.extract_urls(text)
        for url in urls:
            items.append(("url", url))
        
        return items
    
    def detect_input_type(self, text):
        """Auto-detect if input is email, URL, or mixed content."""
        text = text.strip()
        
        # Check if it's a URL
        if text.startswith('http://') or text.startswith('https://') or text.startswith('www.'):
            if '.' in text and ' ' not in text.split('\n')[0]:
                return "url"
        
        # Check if it's a single email
        if '@' in text and '\n' not in text and text.count('@') == 1:
            if '.' in text.split('@')[1]:
                return "email"
        
        # Check if it's email content with multiple emails/URLs
        if '@' in text or 'http' in text:
            return "mixed"
        
        # Default to email
        return "email"
        
    def create_widgets(self):
        """Build all GUI components."""
        # Header
        self.create_header()
        
        # Input section
        self.create_input_section()
        
        # Analysis button
        self.create_analyze_button()
        
        # Results section
        self.create_results_section()
        
        # Footer with save button
        self.create_footer()
        
    def create_header(self):
        """Create the header with title."""
        header_frame = tk.Frame(self.root, bg=self.bg_color, height=60)
        header_frame.pack(fill=tk.X, padx=0, pady=(0, 20))
        
        title = tk.Label(
            header_frame,
            text="🔒 PHISHING DETECTION AWARENESS TOOL",
            font=('Courier', 18, 'bold'),
            fg=self.fg_color,
            bg=self.bg_color
        )
        title.pack(pady=10)
        
        subtitle = tk.Label(
            header_frame,
            text="Protect yourself from phishing attacks | Analyze emails and URLs",
            font=('Courier', 9),
            fg="#00ddff",
            bg=self.bg_color
        )
        subtitle.pack()
        
    def create_input_section(self):
        """Create the input selection and text area."""
        input_frame = tk.LabelFrame(
            self.root,
            text="📋 INPUT & ANALYSIS OPTIONS",
            font=('Courier', 11, 'bold'),
            fg=self.fg_color,
            bg=self.bg_color,
            labelanchor='nw'
        )
        input_frame.pack(fill=tk.X, padx=15, pady=10)
        
        # Analysis mode selection (Radio buttons)
        mode_frame = tk.Frame(input_frame, bg=self.bg_color)
        mode_frame.pack(anchor=tk.W, padx=10, pady=10)
        
        self.mode = tk.StringVar(value="auto")
        
        auto_radio = tk.Radiobutton(
            mode_frame,
            text="🤖 Auto-Detect (Recommended)",
            variable=self.mode,
            value="auto",
            font=('Courier', 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.bg_color,
            activebackground=self.bg_color,
            activeforeground=self.fg_color
        )
        auto_radio.pack(side=tk.LEFT, padx=20)
        
        email_radio = tk.Radiobutton(
            mode_frame,
            text="📧 Email Only",
            variable=self.mode,
            value="email",
            font=('Courier', 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.bg_color,
            activebackground=self.bg_color,
            activeforeground=self.fg_color
        )
        email_radio.pack(side=tk.LEFT, padx=20)
        
        url_radio = tk.Radiobutton(
            mode_frame,
            text="🔗 URL Only",
            variable=self.mode,
            value="url",
            font=('Courier', 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.bg_color,
            activebackground=self.bg_color,
            activeforeground=self.fg_color
        )
        url_radio.pack(side=tk.LEFT, padx=20)
        
        # Instructions label
        instructions_label = tk.Label(
            input_frame,
            text="💡 Paste email content, URLs, or full email messages. Click 'Auto-Detect' to analyze all emails/URLs found.",
            font=('Courier', 8),
            fg="#00ddff",
            bg=self.bg_color,
            wraplength=900,
            justify=tk.LEFT
        )
        instructions_label.pack(anchor=tk.W, padx=10, pady=(0, 5))
        
        # Text input area
        text_label = tk.Label(
            input_frame,
            text="Paste your content here (email address, URL, or full email content):",
            font=('Courier', 9),
            fg=self.secondary_color,
            bg=self.bg_color
        )
        text_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        
        # Create text widget with scrollbar
        text_frame = tk.Frame(input_frame, bg=self.bg_color)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.text_input = tk.Text(
            text_frame,
            height=8,
            font=('Courier', 9),
            bg="#1a1f3a",
            fg=self.fg_color,
            insertbackground=self.fg_color,
            yscrollcommand=scrollbar.set,
            wrap=tk.WORD
        )
        self.text_input.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.text_input.yview)
        
    def create_analyze_button(self):
        """Create the analyze button."""
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=15)
        
        analyze_btn = tk.Button(
            button_frame,
            text="🔍 ANALYZE",
            command=self.analyze,
            font=('Courier', 12, 'bold'),
            bg=self.fg_color,
            fg=self.bg_color,
            padx=30,
            pady=10,
            cursor="hand2"
        )
        analyze_btn.pack()
        
    def create_results_section(self):
        """Create the results display area."""
        results_frame = tk.LabelFrame(
            self.root,
            text="📊 ANALYSIS RESULTS",
            font=('Courier', 11, 'bold'),
            fg=self.fg_color,
            bg=self.bg_color,
            labelanchor='nw'
        )
        results_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Risk level and score display
        score_frame = tk.Frame(results_frame, bg=self.bg_color)
        score_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.risk_level_label = tk.Label(
            score_frame,
            text="Risk Level: --",
            font=('Courier', 14, 'bold'),
            fg=self.fg_color,
            bg=self.bg_color
        )
        self.risk_level_label.pack(side=tk.LEFT, padx=10)
        
        self.risk_score_label = tk.Label(
            score_frame,
            text="Score: -- / 100",
            font=('Courier', 12),
            fg=self.secondary_color,
            bg=self.bg_color
        )
        self.risk_score_label.pack(side=tk.LEFT, padx=20)
        
        # Risk progress bar
        progress_frame = tk.Frame(results_frame, bg=self.bg_color)
        progress_frame.pack(fill=tk.X, padx=10, pady=10)
        
        progress_label = tk.Label(
            progress_frame,
            text="Risk Meter:",
            font=('Courier', 9),
            fg=self.secondary_color,
            bg=self.bg_color
        )
        progress_label.pack(anchor=tk.W, padx=10, pady=(0, 5))
        
        self.risk_progress = ttk.Progressbar(
            progress_frame,
            length=400,
            maximum=100,
            mode='determinate'
        )
        self.risk_progress.pack(fill=tk.X, padx=10, pady=5)
        
        # Explanation/Issues display
        explain_label = tk.Label(
            results_frame,
            text="Detected Issues & Explanations:",
            font=('Courier', 9),
            fg=self.secondary_color,
            bg=self.bg_color
        )
        explain_label.pack(anchor=tk.W, padx=10, pady=(10, 5))
        
        # Create text widget with scrollbar for explanations
        explain_frame = tk.Frame(results_frame, bg=self.bg_color)
        explain_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(explain_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.explanation_box = tk.Text(
            explain_frame,
            height=6,
            font=('Courier', 9),
            bg="#1a1f3a",
            fg=self.fg_color,
            state=tk.DISABLED,
            yscrollcommand=scrollbar.set,
            wrap=tk.WORD
        )
        self.explanation_box.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.explanation_box.yview)
        
    def create_footer(self):
        """Create footer with save report and chart buttons."""
        footer_frame = tk.Frame(self.root, bg=self.bg_color)
        footer_frame.pack(fill=tk.X, padx=15, pady=10)
        
        save_btn = tk.Button(
            footer_frame,
            text="💾 Save Report",
            command=self.save_report,
            font=('Courier', 10, 'bold'),
            bg=self.warning_color,
            fg="#000",
            padx=15,
            pady=8,
            cursor="hand2"
        )
        save_btn.pack(side=tk.LEFT, padx=5)
        
        chart_btn = tk.Button(
            footer_frame,
            text="📊 Show Chart",
            command=self.show_chart,
            font=('Courier', 10, 'bold'),
            bg="#2196F3",
            fg="#fff",
            padx=15,
            pady=8,
            cursor="hand2"
        )
        chart_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            footer_frame,
            text="🗑️  Clear",
            command=self.clear_input,
            font=('Courier', 10, 'bold'),
            bg=self.accent_color,
            fg="#fff",
            padx=15,
            pady=8,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        info_label = tk.Label(
            footer_frame,
            text="Made to raise phishing awareness | Stay safe online!",
            font=('Courier', 8),
            fg="#666",
            bg=self.bg_color
        )
        info_label.pack(side=tk.RIGHT, padx=10)
        
    def analyze(self):
        """Perform phishing analysis on user input with auto-detection support."""
        user_input = self.text_input.get("1.0", tk.END).strip()
        mode = self.mode.get()
        
        if not user_input:
            messagebox.showwarning("Input Error", "Please enter an email address, URL, or email content to analyze.")
            return
        
        try:
            # Auto-detect mode if selected
            if mode == "auto":
                detected_items = self.auto_detect_and_extract(user_input)
                
                if not detected_items:
                    messagebox.showwarning(
                        "No Items Found",
                        "Could not detect any emails or URLs in the provided content.\n\n"
                        "Please ensure you paste:\n"
                        "• A valid email address (e.g., user@example.com)\n"
                        "• A valid URL (e.g., https://example.com)\n"
                        "• Full email content containing sender info and links"
                    )
                    return
                
                # Store detected items for multi-analysis
                self.detected_items = detected_items
                self.current_analysis_index = 0
                
                # Analyze all detected items and display first one
                self.analyze_and_display_item(0, user_input)
            else:
                # Manual mode - validate and analyze
                is_valid, error_message = validate_input(user_input, mode)
                if not is_valid:
                    messagebox.showerror(
                        "Invalid Input",
                        f"The input is not a valid {mode}:\n\n{error_message}\n\n"
                        "Tip: Try using 'Auto-Detect' mode to analyze full email content."
                    )
                    return
                
                # Perform analysis
                self.analyze_single_item(user_input, mode)
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during analysis:\n{str(e)}")
    
    def analyze_single_item(self, item, item_type):
        """Analyze a single email or URL."""
        try:
            # Detect issues based on type
            if item_type == "email":
                detected_issues = check_email(item)
            else:
                detected_issues = check_url(item)
            
            # Calculate risk metrics
            risk_score = calculate_risk_score(detected_issues)
            risk_level = calculate_risk_level(detected_issues)
            
            # Track this analysis in statistics
            global_stats.add_analysis(risk_level)
            
            # Get detailed explanations
            explanations = get_explanations(detected_issues)
            
            # Store results
            self.current_results = {
                "mode": item_type,
                "input": item,
                "detected_issues": detected_issues,
                "risk_score": risk_score,
                "risk_level": risk_level,
                "explanations": explanations,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Display results
            self.display_results(risk_score, risk_level, explanations, item, item_type)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to analyze {item_type}:\n{str(e)}")
    
    def analyze_and_display_item(self, index, original_content):
        """Analyze and display a specific item from detected items."""
        if index >= len(self.detected_items):
            index = 0
        
        self.current_analysis_index = index
        item_type, item_content = self.detected_items[index]
        
        self.analyze_single_item(item_content, item_type)
        
        # Update status to show which item is being analyzed
        if len(self.detected_items) > 1:
            messagebox.showinfo(
                "Multiple Items Found",
                f"Found {len(self.detected_items)} items to analyze.\n\n"
                f"Currently showing: {index + 1} of {len(self.detected_items)}\n"
                f"Type: {item_type.upper()}\n\n"
                f"Content: {item_content[:60]}{'...' if len(item_content) > 60 else ''}"
            )
    
    def display_results(self, risk_score, risk_level, explanations, item=None, item_type=None):
        """Display analysis results with color coding."""
        # Update risk level label with color coding
        if risk_level == "High":
            color = self.accent_color
            emoji = "⚠️"
        elif risk_level == "Medium":
            color = self.warning_color
            emoji = "⚠️"
        else:
            color = "#00ff00"  # Bright green
            emoji = "✅"
        
        self.risk_level_label.config(
            text=f"Risk Level: {emoji} {risk_level}",
            fg=color
        )
        
        # Update score label
        self.risk_score_label.config(text=f"Score: {risk_score} / 100")
        
        # Update progress bar
        self.risk_progress['value'] = risk_score
        if risk_score > 66:
            self.risk_progress.configure(length=400)
        
        # Update explanation box
        self.explanation_box.config(state=tk.NORMAL)
        self.explanation_box.delete("1.0", tk.END)
        
        # Add item information if provided
        if item and item_type:
            self.explanation_box.insert(tk.END, f"📌 Analyzed {item_type.upper()}:\n{item}\n\n")
            self.explanation_box.insert(tk.END, "=" * 70 + "\n\n")
        
        if explanations:
            for explanation in explanations:
                self.explanation_box.insert(tk.END, f"{explanation}\n\n")
        else:
            self.explanation_box.insert(
                tk.END,
                "✅ No suspicious indicators detected!\n\n"
                "This content appears to be safe. However, always exercise caution "
                "and verify suspicious links or requests directly with the sender."
            )
        
        self.explanation_box.config(state=tk.DISABLED)
    
    def save_report(self):
        """Save analysis report to file."""
        if self.current_results is None:
            messagebox.showinfo("No Results", "Please analyze something first before saving a report.")
            return
        
        try:
            # Ask user for save location
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                initialfile=f"phishing_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            )
            
            if not file_path:
                return
            
            # Generate report content
            report_content = self.generate_report()
            
            # Write to file
            with open(file_path, 'w') as f:
                f.write(report_content)
            
            messagebox.showinfo("Success", f"Report saved to:\n{file_path}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save report:\n{str(e)}")
    
    def generate_report(self):
        """Generate detailed report content."""
        if not self.current_results:
            return ""
        
        results = self.current_results
        
        report = "=" * 60 + "\n"
        report += "PHISHING DETECTION ANALYSIS REPORT\n"
        report += "=" * 60 + "\n\n"
        
        report += f"📅 Generated: {results['timestamp']}\n"
        report += f"🔍 Analysis Type: {results['mode'].upper()}\n\n"
        
        report += "RISK ASSESSMENT\n"
        report += "-" * 60 + "\n"
        report += f"Risk Level: {results['risk_level']}\n"
        report += f"Risk Score: {results['risk_score']} / 100\n\n"
        
        report += "ANALYZED CONTENT\n"
        report += "-" * 60 + "\n"
        report += f"{results['input'][:200]}{'...' if len(results['input']) > 200 else ''}\n\n"
        
        report += "DETECTED ISSUES\n"
        report += "-" * 60 + "\n"
        if results['detected_issues']:
            for issue in results['detected_issues']:
                report += f"• {issue}\n"
        else:
            report += "✅ No suspicious indicators detected\n"
        
        report += "\n" + "EXPLANATIONS\n"
        report += "-" * 60 + "\n"
        for explanation in results['explanations']:
            report += f"{explanation}\n\n"
        
        report += "\n" + "=" * 60 + "\n"
        report += "Safety Tips:\n"
        report += "• Never click links from unsolicited emails\n"
        report += "• Verify sender identity through official channels\n"
        report += "• Check for HTTPS and security indicators in URLs\n"
        report += "• Be suspicious of urgent requests for sensitive information\n"
        report += "=" * 60 + "\n"
        
        return report
    
    def clear_input(self):
        """Clear all input and results."""
        self.text_input.delete("1.0", tk.END)
        self.explanation_box.config(state=tk.NORMAL)
        self.explanation_box.delete("1.0", tk.END)
        self.explanation_box.config(state=tk.DISABLED)
        self.risk_level_label.config(text="Risk Level: --", fg=self.fg_color)
        self.risk_score_label.config(text="Score: -- / 100")
        self.risk_progress['value'] = 0
        self.current_results = None
        self.text_input.focus()
    
    def show_chart(self):
        """Display chart visualization of statistics."""
        stats = global_stats.get_stats()
        
        if stats['total'] == 0:
            messagebox.showinfo("No Data", "Perform at least one analysis to see statistics.")
            return
        
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            messagebox.showerror(
                "Dependency Missing",
                "matplotlib is required for chart visualization.\n\n"
                "Install it using:\n"
                "pip install matplotlib\n\n"
                "Or continue using the tool in console mode to see ASCII charts."
            )
            return
        
        # Generate and display chart
        try:
            fig = global_stats.generate_matplotlib_chart(
                title="Phishing Detection Risk Analysis"
            )
            plt.show()
        except Exception as e:
            messagebox.showerror(
                "Chart Error",
                f"Failed to generate chart:\n{str(e)}"
            )
        self.text_input.focus()


def main():
    """Launch the GUI application."""
    root = tk.Tk()
    app = PhishingDetectionGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
