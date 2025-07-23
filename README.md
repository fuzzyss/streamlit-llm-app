# 専門家 LLM チャットアプリ

AI専門家と旅行プランナーとして質問に答えるStreamlitアプリです。

## 機能

- **AI専門家モード**: AI技術に関する専門的な質問に回答
- **旅行プランナーモード**: 旅行計画に関するアドバイスを提供
- OpenAI GPT-4o-miniを使用

## ローカル開発

### 前提条件
- Python 3.11+
- OpenAI APIキー

### セットアップ

1. リポジトリのクローン
```bash
git clone <repository-url>
cd streamlit-llm-app
```

2. 仮想環境の作成と有効化
```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

3. パッケージのインストール
```bash
pip install -r requirements.txt
```

4. 環境変数の設定
`.streamlit/secrets.toml`ファイルを作成し、APIキーを設定：
```toml
OPENAI_API_KEY = "your-openai-api-key-here"
```

5. アプリの起動
```bash
streamlit run app.py
```

## Streamlit Community Cloudデプロイ

1. GitHubにリポジトリをプッシュ
2. [Streamlit Community Cloud](https://share.streamlit.io/)にログイン
3. 「New app」をクリック
4. GitHubリポジトリを選択
5. `app.py`を指定
6. 「Advanced settings」で`OPENAI_API_KEY`を設定
7. 「Deploy!」をクリック