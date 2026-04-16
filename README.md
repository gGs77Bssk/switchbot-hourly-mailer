# switchbot-hourly-mailer

SwitchBot 温湿度計のデータを 1 時間ごとに Gmail で送信する GitHub Actions プロジェクト。

## 仕組み

1. SwitchBot Open API v1.1 で温湿度計のデータを取得
2. 室温・相対湿度から絶対湿度を計算 (Tetens の式)
3. Gmail SMTP でメール送信

GitHub Actions の cron (`0 * * * *`) で毎時自動実行されます。

---

## セットアップ手順

### 1. SwitchBot トークン・シークレットの取得

1. SwitchBot アプリを開く
2. **プロフィール** → **設定** に移動
3. **アプリバージョン** を **10 回タップ** → 「開発者向けオプション」が表示される
4. 開発者向けオプションで **トークン** と **クライアントシークレット** をコピー

### 2. Gmail アプリパスワードの取得

1. Google アカウントの **2 段階認証を有効化** する (まだの場合)
2. https://myaccount.google.com/apppasswords にアクセス
3. アプリ名を入力 (例: `switchbot-mailer`) して「作成」
4. 表示された **16 文字のパスワード** をコピー (スペースは除去)

### 3. デバイス ID の確認

ローカル環境で以下を実行してデバイス ID を確認します。

```bash
# 環境変数をセット
export SWITCHBOT_TOKEN="your_token_here"
export SWITCHBOT_SECRET="your_secret_here"

# 依存インストール & 実行
pip install requests
python tools/list_devices.py
```

温湿度計 (Meter / MeterPlus / WoIOSensor 等) のデバイス ID をメモしてください。

### 4. GitHub Secrets の登録

リポジトリの **Settings → Secrets and variables → Actions → New repository secret** で以下を登録:

| Secret 名 | 値 |
|---|---|
| `SWITCHBOT_TOKEN` | SwitchBot トークン |
| `SWITCHBOT_SECRET` | SwitchBot クライアントシークレット |
| `SWITCHBOT_DEVICE_ID` | 温湿度計のデバイス ID |
| `GMAIL_ADDRESS` | 送信元 Gmail アドレス |
| `GMAIL_APP_PASSWORD` | Gmail アプリパスワード (16文字) |
| `MAIL_TO` | 送信先メールアドレス (自分宛でOK) |

### 5. 手動実行でテスト

1. GitHub リポジトリの **Actions** タブを開く
2. 左側の **Hourly Temperature Report** を選択
3. **Run workflow** ボタンをクリック
4. メールが届くことを確認

成功すれば、以後毎時 00 分 (UTC) に自動実行されます。

---

## 無料枠について

- **Public リポジトリ**: GitHub Actions 無料・無制限
- **Private リポジトリ**: 月 2,000 分の無料枠あり。本ワークフローは 1 回あたり約 30 秒で完了するため、月 720 回 (= 24h × 30日) 実行しても約 360 分で収まります。

## ローカルでのテスト

```bash
pip install requests pytest
pytest tests/
```
