from __future__ import annotations

from ..http import ApiResponse, WSApiHttp


class MediaClient:
    def __init__(self, http: WSApiHttp) -> None:
        self._http = http

    def download(self, media_id: str) -> bytes:
        return self._http.send_bytes("GET", f"/media/{media_id}/download")

    def try_download(self, media_id: str) -> ApiResponse[bytes]:
        return self._http.try_send_bytes("GET", f"/media/{media_id}/download")
