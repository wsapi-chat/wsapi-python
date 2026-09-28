from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AdReferral(BaseModel):
    """Optional attribution supplied by WhatsApp; no field is guaranteed."""

    model_config = ConfigDict(populate_by_name=True)
    ctwa_clid: Optional[str] = Field(None, alias="ctwaClid")
    source_type: Optional[str] = Field(None, alias="sourceType")
    source_id: Optional[str] = Field(None, alias="sourceId")
    source_url: Optional[str] = Field(None, alias="sourceUrl")
    source_app: Optional[str] = Field(None, alias="sourceApp")
    title: Optional[str] = Field(None, alias="title")
    body: Optional[str] = Field(None, alias="body")
    media_type: Optional[str] = Field(None, alias="mediaType")
    thumbnail_url: Optional[str] = Field(None, alias="thumbnailUrl")
    conversion_source: Optional[str] = Field(None, alias="conversionSource")
    show_ad_attribution: Optional[bool] = Field(None, alias="showAdAttribution")
