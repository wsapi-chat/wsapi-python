from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class MessageMedia(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    media_type: str = Field(alias="mediaType")
    id: str
    mimetype: Optional[str] = Field(alias="mimeType", default=None)
    file_length: int = Field(alias="fileLength")
    file_sha256: Optional[str] = Field(alias="fileSHA256", default=None)
    file_enc_sha256: Optional[str] = Field(alias="fileEncSHA256", default=None)
    media_key: Optional[str] = Field(alias="mediaKey", default=None)
    caption: Optional[str] = None
    height: int = 0
    width: int = 0
    jpeg_thumbnail: Optional[str] = Field(alias="jpegThumbnail", default=None)
    direct_path: Optional[str] = Field(alias="directPath", default=None)
    duration: int = 0
    page_count: int = Field(alias="pageCount", default=0)
    title: Optional[str] = None
    filename: Optional[str] = None
