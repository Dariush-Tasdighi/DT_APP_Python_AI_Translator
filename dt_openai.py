"""
Dariush Tasdighi OpenAI module.
"""

from openai import OpenAI
import dt_llm_utility as utility
from openai.types.chat import ChatCompletion

VERSION: str = "1.2"
TEMPERATURE: float = 0.7
KEY_NAME_OPENAI_API_KEY: str = "OPENAI_API_KEY"
BASE_URL: str = "https://openrouter.ai/api/v1".strip().lower()
MODEL_NAME: str = "google/gemma-3-27b-it:free".strip().lower()

SYSTEM_PROMPT: str = "You are a helpful AI assistant."

SYSTEM_MESSAGE: dict = {
    utility.KEY_NAME_ROLE: utility.ROLE_SYSTEM,
    utility.KEY_NAME_CONTENT: SYSTEM_PROMPT,
}


def chat(
    messages: list[dict],
    notify: bool = False,
    base_url: str = BASE_URL,
    api_key: str | None = None,
    model_name: str = MODEL_NAME,
    temperature: float = TEMPERATURE,
) -> tuple[str | None, int, int]:
    """Chat function."""

    if not api_key:
        api_key = utility.get_key_value(
            key=KEY_NAME_OPENAI_API_KEY,
        )

    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    if notify:
        print(f"OpenAI chat started ({model_name})...")

    response: ChatCompletion = client.chat.completions.create(
        stream=False,
        model=model_name,
        temperature=temperature,
        messages=messages,  # type: ignore
    )

    if notify:
        print(f"OpenAI chat finished ({model_name}).")

    assistant_answer: str | None = response.choices[0].message.content

    prompt_tokens: int = 0
    completion_tokens: int = 0

    if assistant_answer:
        if response.usage:
            prompt_tokens = response.usage.prompt_tokens
        if response.usage:
            completion_tokens = response.usage.completion_tokens

    return assistant_answer, prompt_tokens, completion_tokens


if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!")
