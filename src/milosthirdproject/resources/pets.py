# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import pet_list5_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.pet import Pet
from ..types.pets import Pets
from .._base_client import make_request_options

__all__ = ["PetsResource", "AsyncPetsResource"]


class PetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PetsResourceWithRawResponse:
        return PetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PetsResourceWithStreamingResponse:
        return PetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Create a pet"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/pets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        pet_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pet:
        """
        Info for a specific pet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pet_id:
            raise ValueError(f"Expected a non-empty value for `pet_id` but received {pet_id!r}")
        return self._get(
            f"/pets/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    def list5(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pets:
        """
        List all pets

        Args:
          limit: How many items to return at one time (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/pets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, pet_list5_params.PetList5Params),
            ),
            cast_to=Pets,
        )


class AsyncPetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPetsResourceWithRawResponse:
        return AsyncPetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPetsResourceWithStreamingResponse:
        return AsyncPetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Create a pet"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/pets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        pet_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pet:
        """
        Info for a specific pet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pet_id:
            raise ValueError(f"Expected a non-empty value for `pet_id` but received {pet_id!r}")
        return await self._get(
            f"/pets/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    async def list5(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pets:
        """
        List all pets

        Args:
          limit: How many items to return at one time (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/pets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"limit": limit}, pet_list5_params.PetList5Params),
            ),
            cast_to=Pets,
        )


class PetsResourceWithRawResponse:
    def __init__(self, pets: PetsResource) -> None:
        self._pets = pets

        self.create = to_raw_response_wrapper(
            pets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pets.retrieve,
        )
        self.list5 = to_raw_response_wrapper(
            pets.list5,
        )


class AsyncPetsResourceWithRawResponse:
    def __init__(self, pets: AsyncPetsResource) -> None:
        self._pets = pets

        self.create = async_to_raw_response_wrapper(
            pets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pets.retrieve,
        )
        self.list5 = async_to_raw_response_wrapper(
            pets.list5,
        )


class PetsResourceWithStreamingResponse:
    def __init__(self, pets: PetsResource) -> None:
        self._pets = pets

        self.create = to_streamed_response_wrapper(
            pets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pets.retrieve,
        )
        self.list5 = to_streamed_response_wrapper(
            pets.list5,
        )


class AsyncPetsResourceWithStreamingResponse:
    def __init__(self, pets: AsyncPetsResource) -> None:
        self._pets = pets

        self.create = async_to_streamed_response_wrapper(
            pets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pets.retrieve,
        )
        self.list5 = async_to_streamed_response_wrapper(
            pets.list5,
        )
