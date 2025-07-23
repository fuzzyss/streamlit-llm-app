from dotenv import load_dotenv
import os
load_dotenv()

# app.py
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# OpenAI APIキーの設定（Streamlit Cloud対応）
if "OPENAI_API_KEY" in st.secrets:
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# --- 専門家ごとのシステムメッセージ（日本語版） ------------------------------
ROLE_PROMPTS = {
    "AI専門家": "あなたはAIの専門家です。高度な技術的知見をわかりやすく説明し、詳細かつ実用的な回答を提供してください。",
    "旅行プランナー": "あなたはプロの旅行プランナーです。旅行者の希望に合わせた最適な旅程を提案し、現地で役立つ実践的なアドバイスを提供してください。",
}

# --- LLM インスタンス ---------------------------------------------------------
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# --- 質問を投げて回答を返す関数 ----------------------------------------------
def ask_llm(input_text: str, selected_role: str) -> str:
    """
    input_text   : ユーザーの質問
    selected_role: ラジオボタンで選択した専門家タイプ（'AI専門家' or '旅行プランナー'）
    return       : LLM からの回答文字列
    """
    system_prompt = ROLE_PROMPTS.get(selected_role, "あなたは親切なアシスタントです。")
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=input_text),
    ]
    response = llm(messages)
    return str(response)

# -----------------------------------------------------------------------------#
#                            Streamlit UI                                      #
# -----------------------------------------------------------------------------#
st.title("専門家 LLM チャット")

# ★ アプリ概要と操作方法を明示
st.markdown(
    """
### アプリの概要  
- **ラジオボタン**で「AI専門家」または「旅行プランナー」を選択すると、選んだ専門家として LLM が回答します。  
- **テキスト入力欄**に質問や相談内容を入力し、**送信ボタン**を押してください。  
- OpenAI API キー (`OPENAI_API_KEY`) が環境変数に設定されている必要があります。

### 使い方  
1. サイドバー or 画面中央のラジオボタンで専門家を選択  
2. 質問をテキストエリアに入力  
3. **送信**をクリック — 数秒待つと回答が表示されます
"""
)

# 1. 専門家タイプをラジオボタンで選択
selected_role = st.radio(
    "回答してほしい専門家を選んでください",
    ("AI専門家", "旅行プランナー"),
    horizontal=True,
)

# 2. ユーザー入力欄
user_input = st.text_area("質問を入力してください", height=150)

# 3. 送信ボタン
if st.button("送信"):
    if not user_input.strip():
        st.warning("質問を入力してください。")
    else:
        with st.spinner("LLM に問い合わせ中…"):
            answer = ask_llm(user_input, selected_role)
        st.success("回答が届きました！")
        st.markdown("### 回答")
        st.write(answer)
