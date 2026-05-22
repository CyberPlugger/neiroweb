import argparse
import sys
import ast

try:
    from . import ask, history, reset_history
    from . import interactive
except ImportError:
    from __init__ import ask, history, reset_history
    import interactive

HELP_TEXT = """
aibot - AI CLI tool

USAGE:
  aibot ask "Hello!"            → send a prompt to the AI
  aibot chat                    → start interactive chat mode
  aibot history                → show conversation history
  aibot history --reset       → clear conversation history
  aibot history --set "[...]" → manually set history

EXAMPLES:
  aibot ask "Hello!"
  aibot chat
  aibot history --reset
"""


def main():
    # If no arguments are provided, show help message
    if len(sys.argv) == 1:
        print(HELP_TEXT)
        return

    # Create argument parser
    parser = argparse.ArgumentParser(prog="aibot")
    subparsers = parser.add_subparsers(dest="command")

    # ---------------- ASK COMMAND ----------------
    ask_parser = subparsers.add_parser("ask")
    ask_parser.add_argument("text", nargs="+", help="Prompt text for the AI")
    ask_parser.add_argument("--model", default="openai", help="AI model name")

    # ---------------- CHAT COMMAND ----------------
    subparsers.add_parser("chat", help="Start interactive chat mode")
    subparsers.add_parser('graphical_chat', help='Activates graphical interface of an AI ChatBot')

    # ---------------- HISTORY COMMAND ----------------
    history_parser = subparsers.add_parser("history", help="Manage chat history")
    history_parser.add_argument("--reset", action="store_true", help="Clear history")
    history_parser.add_argument("--set", dest="set_history", help="Set custom history list")

    args = parser.parse_args()

    # ---------------- ASK HANDLER ----------------
    if args.command == "ask":
        prompt = " ".join(args.text)
        result = ask(prompt, model=args.model)
        print(result)
        return

    # ---------------- CHAT HANDLER ----------------
    if args.command == "chat":
        print("Starting interactive chat mode...")
        interactive.chat()
        return

    if args.command == 'graphical_chat':
        print('Graphical interface should start')
        interactive.GraphicChat().run()
        return

    # ---------------- HISTORY HANDLER ----------------
    if args.command == "history":

        # Reset history
        if args.reset:
            reset_history()
            print("History cleared successfully.")
            return

        # Set history manually
        if args.set_history:
            try:
                new_history = ast.literal_eval(args.set_history)

                if isinstance(new_history, list):
                    history.clear()
                    history.extend(new_history)
                    print("History updated successfully.")
                else:
                    print("Error: history must be a list.")

            except Exception as e:
                print(f"Invalid format: {e}")

            return

        # Print current history
        print(history)
        return

    # Default help fallback
    parser.print_help()

if __name__ == '__main__':
    main()