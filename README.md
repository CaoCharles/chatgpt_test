# Gemini 聊天機器人

此專案示範如何以 FastAPI 結合 MongoDB 與 Gemini 2.5 Pro 模型，
實作簡易的前後端分離聊天系統。

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
pip install fastapi uvicorn pymongo google-generativeai
```

3. 準備 MongoDB 並設定環境變數：

```bash
export GEMINI_API_KEY=你的金鑰
export MONGO_URI=mongodb://localhost:27017
```

## 啟動後端

```bash
uvicorn backend.main:app --reload
```

啟動後端後，開啟 `frontend/index.html` 即可在瀏覽器與機器人互動。

如果想在命令列體驗，可執行：

```bash
python gemini_chatbot.py --api-key 你的金鑰
```

若已設定 `GEMINI_API_KEY`，參數可以省略。
