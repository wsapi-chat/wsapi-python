from __future__ import annotations

from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class PagedResponse(BaseModel, Generic[T]):
    model_config = ConfigDict(populate_by_name=True)
    items: Optional[List[T]] = None
    total_count: Optional[int] = Field(None, alias="totalCount")
    page_number: Optional[int] = Field(None, alias="pageNumber")
    page_size: Optional[int] = Field(None, alias="pageSize")
