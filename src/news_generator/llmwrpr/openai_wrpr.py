import sys, os
import traceback

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from sysconf import base as conf
# from llmwrpr.base import LLMWrapperBase

from ..sysconf.base import conf
from ..llmwrpr.base import LLMWrapperBase

import openai

class OpenAIWrapper(LLMWrapperBase):
    def __init__(self, options):
        super().__init__(options)
        _api_key = conf["api_key_dict"].get("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=_api_key)

    def text_output_call(self, prompt, options):
        kwargs = options.copy()
        kwargs.pop("provider", None)
        try:
            response = self.client.responses.create(
                input=prompt,
                **kwargs
            )
            return response.output_text
        except Exception as e:
            self.logger.error(traceback.format_exc())
            raise ValueError(f"OpenAI API call failed: {str(e)}")

    def structured_output_call(self, prompt, response_schema, options):
        kwargs = options.copy()
        kwargs.pop("provider", None)
        try:
            response = self.client.responses.parse(
                input=prompt,
                text_format=response_schema,
                **kwargs
            )
            return response.output_parsed.model_dump()
        except Exception as e:
            self.logger.error(traceback.format_exc())
            raise ValueError(f"OpenAI API call failed: {str(e)}")
