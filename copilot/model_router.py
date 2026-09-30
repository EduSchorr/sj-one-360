from __future__ import annotations


class ModelRouter:
    """Future routing seam. V1 always returns the explicitly configured model."""

    def choose(self, *, action: str, configured_model: str, available_models: list[dict]) -> str:
        del action, available_models
        return configured_model
