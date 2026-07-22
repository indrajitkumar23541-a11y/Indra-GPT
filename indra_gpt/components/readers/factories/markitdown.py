from indra_gpt.components.readers.base_reader import IngestionReader
from indra_gpt.components.readers.factories.base import ReaderFactory
from indra_gpt.utils.dependencies import format_missing_dependency_message


class MarkItDownReaderFactory(ReaderFactory):
    def create_reader(self, extension: str | None = None) -> IngestionReader:
        del extension

        try:
            from indra_gpt.components.readers.markitdown.markitdown_reader import (
                MarkItDownReader,
            )
        except ImportError as e:
            raise ImportError(
                format_missing_dependency_message(
                    "MarkItDown reader",
                    extras="ingest-markitdown",
                )
            ) from e

        return MarkItDownReader()
