import os
import time
from rich import print
import dt_openai as openai
import dt_llm_utility as utility

TEMPERATURE: float = 0.2
DELAY_IN_SECONDS: float = 5

TEXT: str = """
"A new challenger has appeared."

In the fiercely competitive world of video games, it's common for new contenders to fade away as quickly as they burst on to the scene.

But Battlefield 6 is hoping to change that.

It's the latest entry in a long-running military shooter series often framed as a grittier, more realistic answer to Call of Duty.

The title's never quite managed to match its most famous rival in terms of sales or players, but there are signs the new installment could close the gap.

A preview weekend giving players a chance to try out the game earlier this year broke records, and the buzz heading into its launch has been huge.

But the project is still a big gamble for publisher Electronic Arts (EA), which has reportedly spent hundreds of millions of dollars making it.

BBC Newsbeat's spoken to some of the makers to find out how they hope it will pay off.

Four EA-owned studios have been working on the game under the Battlefield Studios banner.

They include original series developer Dice, based in Sweden, Canada's Motive Studios and Ripple Effect Studios in LA.

The fourth, Criterion, is based in Guildford in the UK.

Rebecka Coutaz is the VP general manager of the two European studios and tells Newsbeat that, in terms of what it's offering players, "Battlefield 6 is probably unbeatable".
"""

SYSTEM_PROMPT: str = """
تو یک مترجم حرفه‌ای از زبان انگلیسی، به زبان فارسی هستی.

- متن انگلیسی کاربر را با دقت، به زبان فارسی روان ترجمه کن.

- تمام آئین نگارش را در متن فارسی ترجمه شده، با دقت رعایت کن.

- در کلمات فارسی ترجمه شده، نیم فاصله را با دقت رعایت کن. یعنی مثلا به جای کلمه "می شود" بنویس "می‌شود" و یا به جای کلمه "درختها" بنویس "درخت‌ها".
"""

SYSTEM_MESSAGE: dict = {
    utility.KEY_NAME_ROLE: utility.ROLE_SYSTEM,
    utility.KEY_NAME_CONTENT: SYSTEM_PROMPT,
}

MODELS: list[str] = [
    "google/gemma-3-27b-it:free",
    "moonshotai/kimi-dev-72b:free",
    "meta-llama/llama-4-scout:free",
    # "deepseek/deepseek-chat-v3.1:free",  # TODO: Error!
    # "google/gemini-2.0-flash-exp:free",  # TODO: Error!
    "meta-llama/llama-3.3-70b-instruct:free",
]


def main() -> None:
    """Main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    for index, model in enumerate(MODELS, start=1):
        print(f"[{index}]: {model}")

        messages: list[dict] = []
        messages.append(SYSTEM_MESSAGE)

        user_message: dict = {
            utility.KEY_NAME_ROLE: utility.ROLE_USER,
            utility.KEY_NAME_CONTENT: TEXT,
        }
        messages.append(user_message)

        start_time: float = time.time()

        assistant_answer, prompt_tokens, completion_tokens = openai.chat(
            model_name=model,
            messages=messages,
            temperature=TEMPERATURE,
        )

        response_time: float = time.time() - start_time

        # print("-" * 50)
        print()
        print(assistant_answer)
        # print("-" * 50)
        print()
        print("Prompt Tokens (Input):", prompt_tokens)
        # print("-" * 50)
        print("Completion Tokens (Output):", completion_tokens)
        # print("-" * 50)
        print(f"Full response received {response_time:.2f} seconds after request.")
        # print("=" * 50)
        print()

        time.sleep(DELAY_IN_SECONDS)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        pass

    except Exception as error:
        print(f"[-] {error}!")

    print()
