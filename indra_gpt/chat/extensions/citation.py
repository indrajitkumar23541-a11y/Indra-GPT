from pydantic import BaseModel, Field

from indra_gpt.components.engines.citations.types import Citation


class IndraCitation(BaseModel):
    """IndraCitation represents a citation in the Indra format."""

    id: str | None = Field(
        default=None,
        description="Unique identifier for the citation",
    )
    index: int | None = Field(
        default=None,
        description="Index of the citation in the document",
    )
    artifact_id: str | None = Field(
        default=None,
        description="Identifier of the artifact associated with the citation",
    )
    source_id: str | None = Field(
        default=None,
        description="Identifier of the source document from which the citation is derived",
    )

    @classmethod
    def from_citation(cls, citation: Citation) -> "IndraCitation":
        return cls(
            id=citation.doc_id,
            index=citation.value.get("index") if citation.value else None,
            artifact_id=citation.value.get("artifact_id") if citation.value else None,
            source_id=citation.value.get("source_id") if citation.value else None,
        )

    @classmethod
    def to_citation(cls, Indra_citation: "IndraCitation") -> Citation:
        return Citation(
            text="",
            doc_id=Indra_citation.id,
            artifact_id=Indra_citation.artifact_id,
            source_id=Indra_citation.source_id,
            value={
                "index": Indra_citation.index,
                "artifact_id": Indra_citation.artifact_id,
                "source_id": Indra_citation.source_id,
            }
            if Indra_citation.index is not None
            else None,
        )
