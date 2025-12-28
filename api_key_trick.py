import os
from rich import print

API_KEYS: list[str] = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
]


def chat() -> None:
    """Chat"""

    # client.chat.completions.create()

    while True:
        try:
            api_key: str = API_KEYS[api_key_index]
            # client.chat.completions.create()
            pass
        except Exception as error:
            print(f"\n[-] {error}!")
            if error == "Googooli":
                global api_key_index
                api_key_index += 1
                if api_key_index == len(API_KEYS):
                    api_key_index = 0
                continue
            else:
                break


def main():
    """Main of program."""

    os.system(command="cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    try:
        api_key_index: int = 0

        main()

    except KeyboardInterrupt:
        pass

    except Exception as error:
        print(f"\n[-] {error}!")

    print()
