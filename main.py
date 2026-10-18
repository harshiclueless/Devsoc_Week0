import json
import os
import time

from groq import Groq

INPUT_FILE = "questions.txt"
OUTPUT_FILE = "responses.json"
MODEL_NAME = "openai/gpt-oss-20b"  # check the Groq console's models page; names change


def load_questions(path):
    """Read non-empty lines from a text file and return them as a list."""
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def ask_llm(client, question):
    """Send one question to the model and return its text answer."""
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": question}],
    )
    return completion.choices[0].message.content


def save_responses(path, results):
    """Write the list of question/response pairs to a JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2, ensure_ascii=False)


def main():
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    results = []
    for question in load_questions(INPUT_FILE):
        try:
            answer = ask_llm(client, question)
        except Exception as error:
            answer = None
            print(f"Failed on '{question}': {error}")
        results.append({"question": question, "response": answer})
        print(f"Done: {question}")
        time.sleep(1)
    save_responses(OUTPUT_FILE, results)


if __name__ == "__main__":
    main()