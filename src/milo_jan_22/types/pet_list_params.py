# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PetListParams"]


class PetListParams(TypedDict, total=False):
    limit: int
    """How many items to return at one time (max 100)"""
