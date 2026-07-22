from llama_index.core.llms import LLM

from indra_gpt.components.llm.custom.mock import FunctionCallingLLMMock
from indra_gpt.components.llm.factories.base import LLMFactory
from indra_gpt.components.llm.tokenizers.mock import MockTokenizer
from indra_gpt.components.llm.tokenizers.tokenizer_base import TokenizerBase
from indra_gpt.settings.settings import LLMModelConfig


class MockLLMFactory(LLMFactory):
    def _create_llm(
        self, model_config: LLMModelConfig, tokenizer: TokenizerBase | None = None
    ) -> tuple[LLM, str | None]:
        return FunctionCallingLLMMock(), "mock"

    def load_tokenizer(
        self, model_config: LLMModelConfig, raise_exception: bool = True
    ) -> TokenizerBase | None:
        """Mock using Llama Index's default tokenizer."""
        return MockTokenizer()
