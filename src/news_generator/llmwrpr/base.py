import os
import sys

from ..utils.base import logger, log_traceback


class LLMWrapperBase:
    """Base class for Large Language Model (LLM) wrappers."""

    def __init__(self, options):
        """
        Initializes the LLMWrapperBase.

        Args:
            options (dict): A dictionary of options for the wrapper.
        """
        self.options = options
        self.logger = logger
        self.log_traceback = log_traceback

    def text_output_call(self, prompt, options):
        """
        Makes a call to the LLM to get a text output.

        Args:
            prompt (str): The prompt to send to the LLM.
            options (dict): A dictionary of options for the call.

        Raises:
            NotImplementedError: This method must be implemented by a subclass.
        """
        raise NotImplementedError("This method must be implemented by a subclass.")

    def structured_output_call(self, prompt, response_schema, options):
        """
        Makes a call to the LLM to get a structured output.

        Args:
            prompt (str): The prompt to send to the LLM.
            response_schema (dict): The schema for the structured response.
            options (dict): A dictionary of options for the call.

        Raises:
            NotImplementedError: This method must be implemented by a subclass.
        """
        raise NotImplementedError("This method must be implemented by a subclass.")

    @staticmethod
    def get_wrapper(options):
        """
        Factory method to get an LLM wrapper instance based on the provider.

        Args:
            options (dict): A dictionary of options, including the 'provider'.

        Returns:
            An instance of an LLMWrapperBase subclass.
        """
        llm_wrapper = None
        _provider = options.get("provider", "openai_api").lower()

        if _provider == "openai_api":
            from .openai_wrpr import OpenAIWrapper
            llm_wrapper = OpenAIWrapper(options)

        return llm_wrapper