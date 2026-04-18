"""Google スプレッドシートへのログ記録 (Apps Script Web App 経由)."""

import json
import requests


def log_to_sheet(
    webhook_url: str,
    timestamp: str,
    temperature: float,
    humidity: float,
    absolute_humidity: float,
    device_name: str,
) -> None:
    """Apps Script の Web App に POST してスプレッドシートに 1 行追加する."""
    payload = {
        "timestamp": timestamp,
        "temperature": temperature,
        "humidity": humidity,
        "absolute_humidity": absolute_humidity,
        "device_name": device_name,
    }
    resp = requests.post(
        webhook_url,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
        timeout=10,
    )
    resp.raise_for_status()
