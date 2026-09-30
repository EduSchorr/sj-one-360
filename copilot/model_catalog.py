from __future__ import annotations

from copilot.providers.base import Model


def serialize_model(model: Model, *, enabled: bool = False, cost_tier: int | None = None) -> dict:
    return {
        "provider": model.provider,
        "model_id": model.model_id,
        "display_name": model.display_name,
        "enabled": enabled,
        "cost_tier": cost_tier,
        "reasoning_levels": list(model.reasoning_levels),
    }


def model_for(models: list[dict], provider: str, model_id: str) -> dict | None:
    return next((m for m in models if m["provider"] == provider and m["model_id"] == model_id), None)
