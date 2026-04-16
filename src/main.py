"""エントリーポイント: SwitchBot から温湿度を取得し Gmail で送信する."""

import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

from switchbot_client import get_device_status
from humidity import calc_absolute_humidity
from mailer import send_mail


def main() -> None:
    # --- 環境変数の読み込み ---
    token = os.environ["SWITCHBOT_TOKEN"].strip()
    secret = os.environ["SWITCHBOT_SECRET"].strip()
    device_id = os.environ["SWITCHBOT_DEVICE_ID"].strip()
    gmail_address = os.environ["GMAIL_ADDRESS"].strip()
    gmail_app_password = os.environ["GMAIL_APP_PASSWORD"].strip()
    mail_to = os.environ["MAIL_TO"].strip()

    # --- SwitchBot API からデータ取得 ---
    status = get_device_status(token, secret, device_id)
    temperature: float = status["temperature"]
    relative_humidity: float = status["humidity"]
    device_name: str = status.get("deviceName", device_id)

    # --- 絶対湿度の計算 ---
    absolute_humidity = calc_absolute_humidity(temperature, relative_humidity)

    # --- メール組み立て ---
    now = datetime.now(ZoneInfo("Asia/Tokyo"))
    ts = now.strftime("%Y-%m-%d %H:%M")

    subject = f"[室温ログ] {ts} {temperature}℃ / {relative_humidity}%"
    body = (
        f"室温ログ ({ts} JST)\n"
        f"\n"
        f"室温      : {temperature} ℃\n"
        f"相対湿度  : {relative_humidity} %RH\n"
        f"絶対湿度  : {absolute_humidity} g/m³\n"
        f"\n"
        f"デバイス  : {device_name}\n"
    )

    # --- メール送信 ---
    send_mail(gmail_address, gmail_app_password, mail_to, subject, body)
    print(f"Mail sent: {subject}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
