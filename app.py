import streamlit as st
import random

# 問題データ
questions = [
    {
        "question": "株式は元本保証されている？",
        "options": ["◯", "✘"],
        "answer": "✘",
        "explanation": "株式は価格が変動するから、元本保証はされていないよ"
    },
    {
        "question": "投資信託の運用会社の役割は？",
        "options": ["資産の保管", "運用の指図", "販売", "監査"],
        "answer": "運用の指図",
        "explanation": "運用会社は投資信託の資産をどのように運用するかを決める役割を担っているよ"
    },
    {
        "question": "債券の利子は変動する？",
        "options": ["変動する", "固定されている"],
        "answer": "固定されている",
        "explanation": "一般的な債券は固定利率で発行されいるよ"
    }
]

# セッション状態の初期化
if "current_q" not in st.session_state:
    st.session_state.current_q = random.choice(questions)
    st.session_state.answered = False
    st.session_state.feedback = ""
    st.session_state.explanation = ""

st.title("外務員ニ種クイズアプリ")

q = st.session_state.current_q
st.subheader(q["question"])
user_answer = st.radio("選択肢を選んでね", q["options"], key=q["question"])

if not st.session_state.answered:
    if st.button("答え合わせ"):
        st.session_state.answered = True
        if user_answer == q["answer"]:
            st.session_state.feedback = "✅ 正解！"
        else:
            st.session_state.feedback = "❌ 不正解！"
        st.session_state.explanation = f"💡 解説：{q['explanation']}"

# フィードバックと解説の表示
if st.session_state.answered:
    st.markdown(st.session_state.feedback)
    st.info(st.session_state.explanation)
    if st.button("次へ"):
        st.session_state.current_q = random.choice(questions)
        st.session_state.answered = False
        st.session_state.feedback = ""
        st.session_state.explanation = ""
        st.experimental_rerun()
