from __future__ import annotations

from dataclasses import dataclass
from typing import AsyncIterator, Protocol


@dataclass(frozen=True)
class Model:
    provider: str
    model_id: str
    display_name: str
    enabled: bool = True
    cost_tier: int | None = None
    reasoning_levels: tuple[str, ...] = ()


@dataclass(frozen=True)
class GenerationRequest:
    prompt: str
    model: str
    reasoning: str = "low"
    max_output_chars: int = 12000
    mode: str = "atendimento"
    image_paths: tuple[str, ...] = ()
    thread_id: str | None = None


class AIProvider(Protocol):
    provider_id: str

    async def list_models(self) -> list[Model]: ...
    async def stream(self, request: GenerationRequest) -> AsyncIterator[str]: ...
