# wom.py - An asynchronous wrapper for the Wise Old Man API.
# Copyright (c) 2023-present Jonxslays
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

import typing as t

from wom import models
from wom import result
from wom import routes

from . import BaseService

__all__ = ("NameChangeService",)

ValueT = t.TypeVar("ValueT")
ResultT = result.Result[ValueT, models.HttpErrorResponse]


class NameChangeService(BaseService):
    __slots__ = ()

    async def search_name_changes(
        self,
        username: str | None = None,
        *,
        status: models.NameChangeStatus | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> ResultT[list[models.NameChangeModel]]:
        params = self._generate_map(
            username=username, status=status, limit=limit, offset=offset
        )

        route = routes.SEARCH_NAME_CHANGES.compile().with_params(params)
        data = await self._http.fetch(route, self._list)

        if isinstance(data, models.HttpErrorResponse):
            return result.Err(data)

        return result.Ok([self._serializer.deserialize_name_change(c) for c in data])

    async def submit_name_change(
        self, old_name: str, new_name: str
    ) -> ResultT[models.NameChangeModel]:
        payload = self._generate_map(oldName=old_name, newName=new_name)
        route = routes.SUBMIT_NAME_CHANGE.compile()
        data = await self._http.fetch(route, self._dict, payload=payload)

        if isinstance(data, models.HttpErrorResponse):
            return result.Err(data)

        return result.Ok(self._serializer.deserialize_name_change(data))

    async def get_name_change_details(self, id: int) -> ResultT[models.NameChangeDetailModel]:
        route = routes.NAME_CHANGE_DETAILS.compile(id)
        data = await self._http.fetch(route, self._dict)

        if isinstance(data, models.HttpErrorResponse):
            return result.Err(data)

        return result.Ok(self._serializer.deserialize_name_change_detail(data))