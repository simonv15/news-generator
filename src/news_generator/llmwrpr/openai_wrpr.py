import os
import sys

import openai

from ..llmwrpr.base import LLMWrapperBase
from ..sysconf.base import conf


class OpenAIWrapper(LLMWrapperBase):
    """A wrapper for the OpenAI API."""

    def __init__(self, options):
        """
        Initializes the OpenAIWrapper.

        Args:
            options (dict): A dictionary of options for the wrapper.
        """
        super().__init__(options)
        _api_key = conf["api_key_dict"].get("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=_api_key)

    def text_output_call(self, prompt, options):
        """
        Makes a call to the OpenAI API to get a text output.

        Args:
            prompt (str): The prompt to send to the API.
            options (dict): A dictionary of options for the API call.

        Returns:
            str: The text output from the API.

        Raises:
            ValueError: If the API call fails.
        """
        kwargs = options.copy()
        kwargs.pop("provider", None)
        try:
            response = self.client.responses.create(
                input=prompt,
                **kwargs
            )
            return response.output_text
        except Exception as e:
            self.log_traceback(e)
            raise ValueError(f"OpenAI API call failed: {str(e)}")

    def structured_output_call(self, prompt, response_schema, options):
        """
        Makes a call to the OpenAI API to get a structured output.

        Args:
            prompt (str): The prompt to send to the API.
            response_schema (dict): The schema for the structured response.
            options (dict): A dictionary of options for the API call.

        Returns:
            dict: The structured output from the API.

        Raises:
            ValueError: If the API call fails.
        """
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
            self.log_traceback(e)
            raise ValueError(f"OpenAI API call failed: {str(e)}")
