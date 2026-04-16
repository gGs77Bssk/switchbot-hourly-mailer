"""セットアップ用ユーティリティ: SwitchBot デバイス一覧を表示する."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from switchbot_client import list_devices


def main() -> None:
    token = os.environ["SWITCHBOT_TOKEN"]
    secret = os.environ["SWITCHBOT_SECRET"]

    devices = list_devices(token, secret)
    if not devices:
        print("デバイスが見つかりません。")
        return

    print(f"{'デバイス名':<30} {'デバイスID':<20} {'タイプ'}")
    print("-" * 70)
    for d in devices:
        name = d.get("deviceName", "N/A")
        did = d.get("deviceId", "N/A")
        dtype = d.get("deviceType", "N/A")
        print(f"{name:<30} {did:<20} {dtype}")


if __name__ == "__main__":
    main()
