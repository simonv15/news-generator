import sys, os
import logging

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from llmwrpr.openai_wrpr import OpenAIWrapper

class LLMWrapperBase:
    def __init__(self, options):
        self.options = options
        self.logger = logging.getLogger(__name__)

    def text_output_call(self, prompt, options):
        raise NotImplementedError(" text_output_call not implemented")

    def structured_output_call(self, prompt, response_schema, options):
        raise NotImplementedError(" structured_output_call not implemented")

    @staticmethod
    def get_wrapper(options):
        llm_wrapper = None
        _provider = options.get("provider", "openai_api").lower()

        if _provider == "openai_api":
            from ..llmwrpr.openai_wrpr import OpenAIWrapper
            llm_wrapper = OpenAIWrapper(options)

        return llm_wrapper