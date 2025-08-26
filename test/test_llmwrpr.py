# %%
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.news_generator.llmwrpr.base import LLMWrapperBase

from pydantic import BaseModel

class Animal(BaseModel):
    name: str
    sound: str
    ability: int

options = {
    "provider": "openai_api",
    "temperature": 0.0,
    "model": "gpt-4o-mini"
}
# %%
llm_wrapper = LLMWrapperBase.get_wrapper(options)

prompt = "Generate a description for a fictional animal."

text_output = llm_wrapper.text_output_call(prompt, options)
print(f"Text Output: {text_output}")

structured_output = llm_wrapper.structured_output_call(prompt, Animal, options)
print("Structured Output:")
for k, v in structured_output.items():
    print(f"- {k}: {v}")

# %%
