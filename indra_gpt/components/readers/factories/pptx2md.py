from indra_gpt.components.readers.base_reader import IngestionReader
from indra_gpt.components.readers.factories.base import ReaderFactory
from indra_gpt.utils.dependencies import format_missing_dependency_message


class PPTX2MdReaderFactory(ReaderFactory):
    def create_reader(self, extension: str | None = None) -> IngestionReader:
        del extension

        try:
            from indra_gpt.components.readers.pptx2md.pptx2md_reader import (
                PPTX2MdReader,
            )
        except ImportError as e:
            raise ImportError(
                format_missing_dependency_message(
                    "PPTX reader",
                    extras="ingest-documents",
                )
            ) from e

        return PPTX2MdReader(reader_settings=self.settings.transformation.pptx)
