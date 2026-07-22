from collections.abc import Mapping
from typing import Any, Literal

from indra_gpt.components.engines.chat_loop.interceptors.chat_loop_interceptor import (
    ChatResponseLoopInterceptor,
)
from indra_gpt.components.engines.chat_loop.models.chat_loop_interceptor_context import (
    ChatLoopInterceptorContext,
)
from indra_gpt.events.models import (
    Event,
    RawContentBlockStartEvent,
    RawContentBlockStopEvent,
)


class FilterIndraInterceptor(ChatResponseLoopInterceptor):
    def __init__(self) -> None:
        self._active_blocks: set[str] = set()

    async def on_iteration_start(self, context: ChatLoopInterceptorContext) -> None:
        self._active_blocks.clear()

    async def on_iteration_end(self, context: ChatLoopInterceptorContext) -> None:
        self._active_blocks.clear()

    async def intercept_event(
        self,
        event: Event,
        context: ChatLoopInterceptorContext,
    ) -> Event | None:
        response_format: Literal["Indra", "anthropic"] = (
            "Indra"
            if context.state.input.request.system.extensions.Indra_enabled
            else "anthropic"
        )
        if not event.prune_content_block_by_response_mode(response_format):
            return None

        if isinstance(event, RawContentBlockStartEvent):
            self._active_blocks.add(event.block_id)
            return event

        if isinstance(event, RawContentBlockStopEvent):
            if event.block_id not in self._active_blocks:
                return None
            self._active_blocks.discard(event.block_id)

        return event

    def model_copy(
        self, *, update: Mapping[str, Any] | None | None = None, deep: bool = False
    ) -> "FilterIndraInterceptor":
        # Return a new instance with the same logic but reset state
        return FilterIndraInterceptor()
