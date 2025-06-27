# Gemini 聊天機器人

此專案示範如何以 FastAPI 結合 MongoDB 與 Gemini 2.5 Pro 模型，
實作簡易的前後端分離聊天系統。最新版的 `gemini_chatbot.py`
支援 Gemini、ChatGPT、Azure 以及 Claude 介面，可透過參數切換。

## 專案結構

- `backend/` 後端程式碼
  - `core/` 環境設定、資料庫連線與模型呼叫
  - `routers/` API 路由定義
  - `main.py` FastAPI 入口
- `frontend/` 簡單的網頁介面
- `gemini_chatbot.py` 命令列版聊天腳本

## 安裝步驟

1. 安裝 Python 3.11 以上版本。
2. 安裝必要套件：

```bash
pip install fastapi uvicorn pymongo google-generativeai openai anthropic cryptography
```

3. 準備 MongoDB 並設定環境變數：

```bash
export GEMINI_API_KEY=你的金鑰
export OPENAI_API_KEY_ENC=你的加密金鑰
export CLAUDE_API_KEY_ENC=你的加密金鑰
export AZURE_API_KEY_ENC=你的加密金鑰
export API_SECRET=解密用密鑰
export MONGO_URI=mongodb://localhost:27017
```

若欲加密金鑰，可透過 `cryptography.Fernet` 產生密鑰後加密：

```python
from cryptography.fernet import Fernet
secret = Fernet.generate_key()
cipher = Fernet(secret)
print('ENC:', cipher.encrypt(b'YOUR_KEY').decode())
print('SECRET:', secret.decode())
```

## 啟動後端

```bash
uvicorn backend.main:app --reload
```

啟動後端後，開啟 `frontend/index.html` 即可在瀏覽器與機器人互動。

如果想在命令列體驗，可執行（範例使用 Gemini）：

```bash
python gemini_chatbot.py --provider gemini --secret $API_SECRET
```

`--provider` 可改為 `openai`、`azure` 或 `claude`，並需於環境變數準備相對應的加密金鑰。
