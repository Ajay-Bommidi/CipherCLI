import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)  # Reset colors automatically after print


def caesar_cipher(text, shift, mode):
    result = ""

    if mode == 'd':  # Decrypt by reversing the shift
        shift = -shift

    for char in text:
        if char.isalpha():  # Only shift alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-alphabet characters unchanged

    return result


def get_valid_string(prompt):
    """Ensure the user inputs a valid string (not empty, not numbers only)."""
    while True:
        text = input(Fore.CYAN + prompt).strip()
        if text and any(char.isalpha() for char in text):  # Ensures at least one letter
            return text
        print(Fore.RED + "❌ Invalid input! Please enter a valid text message.")


def main():
    print(Fore.CYAN + "\n📜 Welcome to the Caesar Cipher CLI Tool! 🔐")
    print(Fore.YELLOW + "--------------------------------------------")

    print(Fore.GREEN + "\nChoose an option:")
    print(Fore.MAGENTA + "🔹 'e' - Encrypt a message")
    print(Fore.MAGENTA + "🔹 'd' - Decrypt a message\n")

    mode = input(Fore.CYAN + "Enter your choice (e/d): ").strip().lower()

    if mode not in ['e', 'd']:
        print(Fore.RED + "❌ Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")
        return

    print(Fore.YELLOW + "\n🔠 Example message: Hello, World!")
    print(Fore.YELLOW + "🔢 Example shift: 3 (A → D, B → E, etc.)\n")

    text = get_valid_string("Enter your message: ")

    while True:
        try:
            shift = int(input(Fore.CYAN + "Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                break
            else:
                print(Fore.RED + "❌ Shift value must be between 1 and 25.")
        except ValueError:
            print(Fore.RED + "❌ Invalid input! Shift value must be a number.")

    output = caesar_cipher(text, shift, mode)

    print(Fore.GREEN + f"\n✅ Result: {Fore.YELLOW}{output}")
    print(Fore.BLUE + "\n✨ Thanks for using the Caesar Cipher CLI! ✨")


if __name__ == "__main__":
    main()
