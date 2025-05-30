from cli import show_menu, handle_choice
from database import Base, engine
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    Base.metadata.create_all(bind=engine)

    running = True
    while running:
        clear_screen()
        show_menu()
        choice = input("\nYour choice: ")
        clear_screen()
        running = handle_choice(choice)

if __name__ == "__main__":
    main()
