# Translator

## This program was written by

- **Dariush Tasdighi**
  - Cell Phone Number: 09121087461
  - Email Address: <DariushT@GMail.com>
  - LinkedIn: <https://www.linkedin.com/in/tasdighi>
  - Telegram Channel: <https://t.me/IranianExperts>
  - Telegram Channel: <https://t.me/DT_PYTHON_LEARNING>

- **Hossein Rouzbahani**
  - Cell Phone Number: 09383995083
  - Email Address: <HR.Hossein.Rouzbahani@Gmail.com>
  - LinkedIn: <https://www.linkedin.com/in/hossein-rouzbahani>

---

- Package: 'rich'
  - <https://pypi.org/project/rich>
  - <https://github.com/Textualize/rich>
  - <https://rich.readthedocs.io/en/latest>

- Package: 'pypdf'
  - <https://pypi.org/project/pypdf>
  - <https://github.com/py-pdf/pypdf>
  - <https://pypdf.readthedocs.io/en/latest>

- Package: 'openai'
  - <https://pypi.org/project/openai>
  - <https://github.com/openai/openai-python>

- Package: 'cryptography'
  - <https://pypi.org/project/cryptography>
  - <https://github.com/pyca/cryptography>
  - <https://cryptography.io/en/latest>

- Package: 'dotenv-python'
  - <https://pypi.org/project/dotenv-python>
  - <https://github.com/TsuiJie/dotenv-python>

## Setup Environment

```bash
python -m venv .venv
```

```bash
.\.venv\Scripts\activate
```

```bash
python -m pip install -r .\requirements.txt -U
```

```bash
python -m pip list
```

```bash
python -m pip install -U pip
```

```bash
python -m pip install -U rich
```

```bash
python -m pip install -U pypdf
```

```bash
python -m pip install -U openai
```

```bash
python -m pip install -U cryptography
```

```shell
python -m pip install -U python-dotenv
```

```bash
python -m pip list
```

Now! We Create / Modify / Delete / Run the Source Codes...

```bash
deactivate
```

## Create '.env' File (For Saving API Keys)

- In the root of project, create a file, with the name of '.env', and write the key name and value:
  - OPENAI_API_KEY="..."

---

## Road Map

1. Detect the best Model for translation
    - google/gemma-3-27b-it:free
    - moonshotai/kimi-dev-72b:free
    - meta-llama/llama-4-scout:free
    - deepseek/deepseek-chat-v3.1:free
    - google/gemini-2.0-flash-exp:free
    - meta-llama/llama-3.3-70b-instruct:free
2. Find Free Sites for Download E-Books (PDF)
3. Convert PDF to TXT
4. Find Free Sites for Download E-Books (TXT)
    - <https://www.gutenberg.org>
        - <https://www.gutenberg.org/ebooks/categories>
            - <https://www.gutenberg.org/ebooks/bookshelf/638>
                - <https://www.gutenberg.org/ebooks/36>
                    - <https://www.gutenberg.org/cache/epub/36/pg36.txt>
5. Open text file
6. Fix Text of text file
7. Convert text of text file to list of paragraphs
8. Loop in list
9. Note: User can set Start!

---

```txt
می‌خواهم بین چند مدل هوش مصنوعی، بهترین مدل را برای ترجمه انتخاب نمایم.

لطفا یک پاراگراف نسبتا طولانی به زبان انگلیسی، در سطح IELTS 9 برایم بنویس، که آن را به تک تک مدل‌های هوش مصنوعی بدهم، تا ترجمه روان و سلیس آن‌ها را با هم مقایسه نمایم.
```

---

```txt
In an era defined by technological ubiquity and accelerating interdependence, the imperative to reconcile innovation with ethical stewardship has never been more acute. Emerging tools—capable of amplifying human creativity, enhancing diagnostic precision, and optimizing resource allocation—also harbour the latent capacity to exacerbate inequality, obscure accountability, and destabilize labour markets if deployed without prudent governance. Consequently, policymakers, technologists, and civil society must collaboratively cultivate a pluralistic framework that privileges transparency, robust oversight, and iterative risk assessment over unbridled experimentation. Education and lifelong learning should be elevated from peripheral policy footnotes to strategic pillars that enable individuals to navigate structural transitions with dignity. Equally salient is the need to embed epistemic humility into systems design: acknowledge complexity, anticipate unintended consequences, and prioritise fail-safes that attenuate harm without needlessly stifling beneficial innovation. Fragmented regulatory patchworks invite jurisdictional arbitrage and dilute normative consensus, so international cooperation—though difficult—is a corollary necessity. Ultimately, progress ought to be judged not merely by the velocity of technical breakthroughs but by how equitably their benefits are distributed, how human autonomy is preserved, and how resilient our institutions remain in the face of rapid change.
```

---
