import argparse
import os

from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

# Get user input
parser = argparse.ArgumentParser()
parser.add_argument("--task", default="Return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

# Define Language Model
model = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Define Prompt Templates
code_prompt = PromptTemplate.from_template(
    "Write a very short {language} function that will {task}"
)

test_prompt = PromptTemplate.from_template(
    "Write a unit test for the following {language} code:\n{code}"
)

# define and invoke code generation chain
code_chain = code_prompt | model
code_result = code_chain.invoke({
    "language": args.language, 
    "task": args.task
})

# define and execute test generation chain
test_chain = test_prompt | model

test_result = test_chain.invoke({
    "language": args.language, 
    "code": code_result
})

# print results
print("\n")
print(code_result)
print(test_result)

