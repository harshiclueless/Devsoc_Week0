LLM API Script

so this is a python script that reads questions from a text file, sends each one to an LLM through the Groq API and saves the answers in a JSON file.



How it works:

1\. 'load\_questions reads `questions.txt` (one question per line).

2\. 'ask\_llm' sends each question to the model and returns the reply.

3\. 'save\_responses' writes all question/response pairs to 'responses.json'.

If a request fails, the script prints the error, stores 'null' for that question, and carries on with the rest.



Files:

\- 'main.py': the script

\- 'questions.txt': input questions, one per line

\- 'responses.json': output, a list of '{"question": ..., "response": ...}' objects



Setup:

1\. Install Python 3.

2\. Install the dependency:

```

&#x20;  pip install groq

```

3\. Get an API key from the Groq console and set it as an environment variable (Windows cmd):

```

&#x20;  set GROQ\_API\_KEY=your\_key\_here

```



Usage:



```

python main.py

```



The answers are saved to 'responses.json'.



\## Notes



\- The API key is read from an environment variable and is never stored in the code.

\- The model is set by 'MODEL\_NAME' in `main.py` (currently `openai/gpt-oss-20b`). Groq changes its model list over time, so update this if you get a "model not found" error.

