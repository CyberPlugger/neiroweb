import os
import sys
import tkinter as tk

from tkinter import ttk, scrolledtext
import threading

try:
    from . import ask, reset_history
except ImportError:
    from __init__ import ask, reset_history

IS_WINDOWS = os.name == 'nt'

class ColorPrinter:

    @staticmethod
    def supports_color():
        if IS_WINDOWS:
            try:
                os.system('')
                return True
            except:
                return False
        return sys.stdout.isatty()

    @staticmethod
    def red(text):
        return f"\033[91m{text}\033[0m" if ColorPrinter.supports_color() else text

    @staticmethod
    def green(text):
        return f"\033[92m{text}\033[0m" if ColorPrinter.supports_color() else text

    @staticmethod
    def yellow(text):
        return f"\033[93m{text}\033[0m" if ColorPrinter.supports_color() else text

    @staticmethod
    def blue(text):
        return f"\033[94m{text}\033[0m" if ColorPrinter.supports_color() else text

    @staticmethod
    def cyan(text):
        return f"\033[96m{text}\033[0m" if ColorPrinter.supports_color() else text

    @staticmethod
    def bold(text):
        return f"\033[1m{text}\033[0m" if ColorPrinter.supports_color() else text

    @staticmethod
    def white(text):
        return text

def chat():

    title = ColorPrinter.bold(ColorPrinter.cyan(r'''
             o          __o__   o__ __o         o__ __o     ____o__ __o____ 
        <|>           |    <|     v\       /v     v\     /   \   /   \  
        / \          / \   / \     <\     />       <\         \o/       
      o/   \o        \o/   \o/     o/   o/           \o        |        
     <|__ __|>        |     |__  _<|   <|             |>      < >       
     /       \       < >    |       \   \\           //        |        
   o/         \o      |    <o>      /     \         /          o        
  /v           v\     o     |      o       o       o          <|        
 />             <\  __|>_  / \  __/>       <\__ __/>          / \       
                                                                                   
    '''))

    os.system('cls' if os.name == 'nt' else 'clear')
    print(title)

    x = {
        'A': 'green',
        'I': 'red',
        'B': 'yellow',
        'O': 'white',
        'T': 'blue',
        ' Interactive ': 'white',
        'chat ': 'yellow',
        '(type ': 'white',
        'exit ': 'red',
        'to exit, ': 'white',
        'reset ': 'red',
        'to reset AI\'s memory and ': 'white',
        'clear ': 'blue',
        'to clear the console)': 'white',
        '\n': 'white'
    }

    for i in x:
        print(
            getattr(
                ColorPrinter,
                x[i]
            )(
                i
            ),
            end=''
        )

    while True:
        user_input = input(ColorPrinter.green("You: "))

        if user_input.lower() == "exit":
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        if user_input.lower() == "reset":
            reset_history()
            print("Memory cleared.")
            continue

        if user_input.lower() == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(title)
            continue

        response = ask(user_input)
        print(ColorPrinter.blue(f'AI: {response}'))


class GraphicChat:
    """
    Graphical AI chat interface using tkinter.
    Similar to aibot.interactive.chat but with GUI support.
    """

    def __init__(self):

        # Create main window
        self.root = tk.Tk()
        self.root.title("AIBOT Chat")
        self.root.geometry("900x650")

        # Theme state
        self.dark_mode = True

        # Configure ttk style
        self.style = ttk.Style()

        # Create all widgets
        self.create_widgets()

        # Apply initial theme
        self.apply_theme()

    # --------------------------------------------------
    # UI CREATION
    # --------------------------------------------------

    def create_widgets(self):

        # Top control frame
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        # Theme switch button
        self.theme_button = ttk.Button(
            self.top_frame,
            text="Switch Theme",
            command=self.toggle_theme
        )
        self.theme_button.pack(side="right", padx=(5, 0))

        # Reset history button
        self.reset_button = ttk.Button(
            self.top_frame,
            text="Reset History",
            command=self.reset_chat_history
        )
        self.reset_button.pack(side="right")

        # Chat display area
        self.chat_box = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Consolas", 11),
            state="disabled"
        )

        self.chat_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        # Bottom input frame
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(fill="x", padx=10, pady=10)

        # User input field
        self.input_box = tk.Entry(
            self.bottom_frame,
            font=("Consolas", 11)
        )

        self.input_box.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        # Send button
        self.send_button = ttk.Button(
            self.bottom_frame,
            text="Send",
            command=self.send_message
        )

        self.send_button.pack(side="right")

        # Send message on Enter key
        self.input_box.bind(
            "<Return>",
            lambda event: self.send_message()
        )

    # --------------------------------------------------
    # THEME SYSTEM
    # --------------------------------------------------

    def apply_theme(self):

        if self.dark_mode:

            bg = "#1e1e1e"
            fg = "#ffffff"
            input_bg = "#2b2b2b"

        else:

            bg = "#f0f0f0"
            fg = "#000000"
            input_bg = "#ffffff"

        # Main window
        self.root.configure(bg=bg)

        # Frames
        self.top_frame.configure(bg=bg)
        self.bottom_frame.configure(bg=bg)

        # Chat box
        self.chat_box.configure(
            bg=input_bg,
            fg=fg,
            insertbackground=fg
        )

        # Input field
        self.input_box.configure(
            bg=input_bg,
            fg=fg,
            insertbackground=fg
        )

    def toggle_theme(self):

        self.dark_mode = not self.dark_mode
        self.apply_theme()

    # --------------------------------------------------
    # CHAT FUNCTIONS
    # --------------------------------------------------

    def add_message(self, sender, message):

        self.chat_box.configure(state="normal")

        self.chat_box.insert(
            tk.END,
            f"{sender}: {message}\n\n"
        )

        self.chat_box.configure(state="disabled")
        self.chat_box.see(tk.END)

    def send_message(self):

        user_message = self.input_box.get().strip()

        if not user_message:
            return

        # Show user message
        self.add_message("You", user_message)

        # Clear input field
        self.input_box.delete(0, tk.END)

        # Run AI request in separate thread
        threading.Thread(
            target=self.get_ai_response,
            args=(user_message,),
            daemon=True
        ).start()

    def get_ai_response(self, message):

        try:

            response = ask(message)

            self.add_message(
                "AI",
                response
            )

        except Exception as e:

            self.add_message(
                "System",
                f"Error: {e}"
            )

    # --------------------------------------------------
    # HISTORY MANAGEMENT
    # --------------------------------------------------

    def reset_chat_history(self):

        # Reset backend history
        reset_history()

        # Clear chat UI
        self.chat_box.configure(state="normal")
        self.chat_box.delete("1.0", tk.END)
        self.chat_box.configure(state="disabled")

        # Show system message
        self.add_message(
            "System",
            "Conversation history has been cleared."
        )

    # --------------------------------------------------
    # APPLICATION START
    # --------------------------------------------------

    def run(self):

        self.root.mainloop()

if __name__ == '__main__':
    chat()