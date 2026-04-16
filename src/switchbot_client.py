"""SwitchBot Open API v1.1 クライアント."""

import base64
import hashlib
import hmac
import time
import uuid
from typing import Any

import requests


def _make_headers(token: str, secret: str) -> dict[str, str]:
    """HMAC-SHA256 署名付き認証ヘッダを生成する."""
    t = str(int(time.time() * 1000))
    nonce = str(uuid.uuid4())
    string_to_sign = f"{token}{t}{nonce}".encode("utf-8")
    sign = base64.b64encode(
        hmac.new(secret.encode("utf-8"), string_to_sign, hashlib.sha256).digest()
    ).decode("utf-8")
    return {
        "Authorization": token,
        "sign": sign,
        "t": t,
        "nonce": nonce,
        "Content-Type": "application/json; charset=utf-8",
    }


_BASE_URL = "https://api.switch-bot.com/v1.1"


def list_devices(token: str, secret: str) -> list[dict[str, Any]]:
    """デバイス一覧を取得する."""
    resp = requests.get(
        f"{_BASE_URL}/devices",
        headers=_make_headers(token, secret),
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()
    if data.get("statusCode") != 100:
        raise RuntimeError(f"SwitchBot API error: {data}")
    return data["body"]["deviceList"]


def get_device_status(token: str, secret: str, device_id: str) -> dict[str, Any]:
    """指定デバイスのステータスを取得する."""
    resp = requests.get(
        f"{_BASE_URL}/devices/{device_id}/status",
        headers=_make_headers(token, secret),
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()
    if data.get("statusCode") != 100:
        raise RuntimeError(f"SwitchBot API error: {data}")
    return data["body"]
