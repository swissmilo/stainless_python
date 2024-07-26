# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from milosthirdproject import Milosthirdproject, AsyncMilosthirdproject
from milosthirdproject.types import Pet, Pets

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Milosthirdproject) -> None:
        pet = client.pets.create()
        assert pet is None

    @parametrize
    def test_raw_response_create(self, client: Milosthirdproject) -> None:
        response = client.pets.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert pet is None

    @parametrize
    def test_streaming_response_create(self, client: Milosthirdproject) -> None:
        with client.pets.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Milosthirdproject) -> None:
        pet = client.pets.retrieve(
            "petId",
        )
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Milosthirdproject) -> None:
        response = client.pets.with_raw_response.retrieve(
            "petId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Milosthirdproject) -> None:
        with client.pets.with_streaming_response.retrieve(
            "petId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Milosthirdproject) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pet_id` but received ''"):
            client.pets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list5(self, client: Milosthirdproject) -> None:
        pet = client.pets.list5()
        assert_matches_type(Pets, pet, path=["response"])

    @parametrize
    def test_method_list5_with_all_params(self, client: Milosthirdproject) -> None:
        pet = client.pets.list5(
            limit=0,
        )
        assert_matches_type(Pets, pet, path=["response"])

    @parametrize
    def test_raw_response_list5(self, client: Milosthirdproject) -> None:
        response = client.pets.with_raw_response.list5()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(Pets, pet, path=["response"])

    @parametrize
    def test_streaming_response_list5(self, client: Milosthirdproject) -> None:
        with client.pets.with_streaming_response.list5() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(Pets, pet, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMilosthirdproject) -> None:
        pet = await async_client.pets.create()
        assert pet is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMilosthirdproject) -> None:
        response = await async_client.pets.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert pet is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMilosthirdproject) -> None:
        async with async_client.pets.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMilosthirdproject) -> None:
        pet = await async_client.pets.retrieve(
            "petId",
        )
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMilosthirdproject) -> None:
        response = await async_client.pets.with_raw_response.retrieve(
            "petId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMilosthirdproject) -> None:
        async with async_client.pets.with_streaming_response.retrieve(
            "petId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMilosthirdproject) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pet_id` but received ''"):
            await async_client.pets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list5(self, async_client: AsyncMilosthirdproject) -> None:
        pet = await async_client.pets.list5()
        assert_matches_type(Pets, pet, path=["response"])

    @parametrize
    async def test_method_list5_with_all_params(self, async_client: AsyncMilosthirdproject) -> None:
        pet = await async_client.pets.list5(
            limit=0,
        )
        assert_matches_type(Pets, pet, path=["response"])

    @parametrize
    async def test_raw_response_list5(self, async_client: AsyncMilosthirdproject) -> None:
        response = await async_client.pets.with_raw_response.list5()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(Pets, pet, path=["response"])

    @parametrize
    async def test_streaming_response_list5(self, async_client: AsyncMilosthirdproject) -> None:
        async with async_client.pets.with_streaming_response.list5() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(Pets, pet, path=["response"])

        assert cast(Any, response.is_closed) is True
