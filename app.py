import os
import time
import pathlib
from rich import print

# NEW
import dt_openai as openai
import dt_llm_utility as utility

DELAY_IN_SECONDS: float = 5

# NEW
TEMPERATURE: float = 0.2
BASE_URL: str = "https://api.avalai.ir/v1".strip().lower()

# NEW
# MODEL_NAME: str = "google/gemma-3-27b-it:free".strip().lower()

# NEW
# MODEL_NAME: str = "gpt-oss-120b".strip().lower()
MODEL_NAME: str = "gemini-2.5-flash-lite".strip().lower()
# MODEL_NAME: str = "gemini-2.5-flash".strip().lower()  # خیلی طول می‌کشد
# MODEL_NAME: str = "gemma-3-27b-it".strip().lower()  # Error!
# MODEL_NAME: str = "cf.gemma-sea-lion-v4-27b-it".strip().lower()  # Error!

# NEW
SYSTEM_PROMPT: str = """
تو یک مترجم حرفه‌ای از زبان انگلیسی، به زبان فارسی هستی.

- از نوشتن عبارات مربوط به Markdown اجتناب کن.

- متن انگلیسی کاربر را با دقت، به زبان فارسی روان ترجمه کن.

- تمام آئین نگارش را در متن فارسی ترجمه شده، با دقت رعایت کن.

- از نوشتن جملات و کلمات اضافه اجتناب کن! و صرفا متن داده شده را با دقت ترجمه کن.

- در زمان ترجمه، لحن نویسنده را شناسایی کن و سعی کن صرفا با لحن نویسنده، متن را ترجمه کنی.

- در کلمات فارسی ترجمه شده، نیم فاصله را با دقت رعایت کن. یعنی مثلا به جای کلمه "می شود" بنویس "می‌شود" و یا به جای کلمه "درختها" بنویس "درخت‌ها".
"""
SYSTEM_MESSAGE: dict = {
    utility.KEY_NAME_ROLE: utility.ROLE_SYSTEM,
    utility.KEY_NAME_CONTENT: SYSTEM_PROMPT,
}


def load_text_file(file_path: str) -> str:
    """Load and return the content of a text file."""

    if not os.path.exists(path=file_path):
        print(f"[-] The file '{file_path}' does not exist!\n")
        exit()

    if not os.path.isfile(path=file_path):
        print(f"[-] The file '{file_path}' does not exist!\n")
        exit()

    source_file_extension: str = pathlib.Path(file_path).suffix.lower()

    if source_file_extension != ".txt":
        print(f"[-] The file '{file_path}' is not 'txt' file!\n")
        exit()

    with open(file=file_path, mode="rt", encoding="utf-8") as file:
        file_content = file.read()
        return file_content


def fix_text_content(text: str) -> str:
    """Fix text content."""

    fixed_text: str = text

    fixed_text = fixed_text.strip()
    fixed_text = fixed_text.replace("\r", "")

    # آقای علیرضا ولدخانی
    while "\n\n\n" in fixed_text:
        fixed_text = fixed_text.replace("\n\n\n", "\n\n")

    fixed_text = fixed_text.replace("\n\n", "[NEW_PARAGRAPH]")
    fixed_text = fixed_text.replace("\n", " ")
    fixed_text = fixed_text.replace("[NEW_PARAGRAPH]", "\n")

    return fixed_text


def fix_paragraph(paragraph: str) -> str:
    """Fix paragraph."""

    fixed_paragraph: str = paragraph.strip()
    fixed_paragraph = fixed_paragraph.replace("\ufeff", "")  # TODO

    if not fix_paragraph:
        return ""

    while "  " in fixed_paragraph:
        fixed_paragraph = fixed_paragraph.replace("  ", " ")

    return fixed_paragraph


def convert_text_to_paragraphs(text: str) -> list[str]:
    """Convert text into a list of paragraphs."""

    text = text.strip()

    original_paragraphs: list[str] = text.split(sep="\n")

    fixed_paragraphs: list[str] = []

    for original_paragraph in original_paragraphs:
        fixed_paragraph: str = fix_paragraph(
            paragraph=original_paragraph,
        )

        if fixed_paragraph:
            fixed_paragraphs.append(fixed_paragraph)

    return fixed_paragraphs


def fix_translated_paragraph(paragraph: str | None) -> str:
    """Fix translated paragraph."""

    if not paragraph:
        return ""

    fixed_paragraph: str = paragraph.strip()

    if not fix_paragraph:
        return ""

    fixed_paragraph = fixed_paragraph.replace("_", " ")
    fixed_paragraph = fixed_paragraph.replace("—", "، ")
    fixed_paragraph = fixed_paragraph.replace(" - ", "، ")

    fixed_paragraph = fixed_paragraph.replace("# ", "")
    fixed_paragraph = fixed_paragraph.replace("## ", "")
    fixed_paragraph = fixed_paragraph.replace("### ", "")

    fixed_paragraph = fixed_paragraph.replace("\r", "\n")
    fixed_paragraph = fixed_paragraph.replace("\n", " ")

    while "  " in fixed_paragraph:
        fixed_paragraph = fixed_paragraph.replace("  ", " ")

    fixed_paragraph = fixed_paragraph.strip()

    return fixed_paragraph


def translate_paragraph(paragraph: str) -> str:
    """Translate a paragraph using an AI model."""

    print("-" * 50)
    print(f"[{paragraph}]")
    print("-" * 50)

    # NEW
    messages: list[dict] = []
    messages.append(SYSTEM_MESSAGE)

    # NEW
    user_message: dict = {
        utility.KEY_NAME_ROLE: utility.ROLE_USER,
        utility.KEY_NAME_CONTENT: paragraph,
    }
    messages.append(user_message)

    start_time: float = time.time()

    # NEW
    translated_paragraph, prompt_tokens, completion_tokens = openai.chat(
        messages=messages,
        base_url=BASE_URL,
        model_name=MODEL_NAME,
        temperature=TEMPERATURE,
    )

    response_time: float = time.time() - start_time

    if translate_paragraph:
        translated_paragraph = fix_translated_paragraph(
            paragraph=translated_paragraph,
        )

    print(f"[{translated_paragraph}]")
    print("-" * 50)
    print("Prompt Tokens (Input):", prompt_tokens)
    print("-" * 50)
    print("Completion Tokens (Output):", completion_tokens)
    print("-" * 50)
    print(f"Full response received {response_time:.2f} seconds after request.")
    print("=" * 50)
    print()

    if not translated_paragraph:
        raise ValueError("'translated_paragraph' is None or empty!")

    return translated_paragraph


def append_to_file(file_path: str, text: str) -> None:
    """Append to File"""

    with open(file=file_path, mode="at", encoding="utf-8") as file:
        file.write(text)
        file.write("\n")


def main():
    """Main of program."""

    os.system(command="cls" if os.name == "nt" else "clear")

    # input_text_file_path: str = "./data/pg36.txt"
    # output_text_file_path: str = "./data/pg36_translated.txt"

    input_text_file_path: str = "./data/pg2097.txt"
    output_text_file_path: str = "./data/pg2097_translated.txt"

    text_content: str = load_text_file(
        file_path=input_text_file_path,
    )

    fixed_text_content: str = fix_text_content(
        text=text_content,
    )

    paragraphs: list[str] = convert_text_to_paragraphs(
        text=fixed_text_content,
    )

    global success_index
    start_index: int = success_index + 1
    finish_index: int = len(paragraphs) - 1

    for index in range(start_index, finish_index + 1):
        paragraph: str = paragraphs[index]

        print("=" * 50)
        print(f"({index + 1} of {finish_index + 1})")

        translated_paragraph: str = translate_paragraph(
            paragraph=paragraph,
        )

        append_to_file(
            text=translated_paragraph,
            file_path=output_text_file_path,
        )

        success_index = index

        time.sleep(DELAY_IN_SECONDS)


if __name__ == "__main__":
    # عددی که در آخرین مرحله و با
    # بروز خطا نمایش داده شده است
    success_index: int = -1
    # success_index: int = ?????

    try:
        main()
        print("Finished Successfully.")

    except KeyboardInterrupt:
        pass

    except Exception as error:
        print()
        print(f"[-] {error}!")

    print()
    print("." * 50)
    print(f"Success Index: {success_index}")
    print("." * 50)
