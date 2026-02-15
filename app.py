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
    },
    {
        "question": "株式会社が新しく株を発行して、投資家からお金を集める場所のことを流通市場という。",
        "options": ["◯", "✘"],
        "answer": "✘",
        "explanation": "新しく株を発行してお金を集めるのは発行市場。流通市場は、すでに誰かが持っている株を売り買いする場所（証券取引所など）"
    },
    {
        "question": "上場株式を売買するとき、株価がいくらであっても証券会社が受け取る売買委託手数料の金額は、国によって一律に決められている。",
        "options": ["◯", "✘"],
        "answer": "✘",
        "explanation": "それぞれの証券会社が自分たちで決めていいことになっているよ。だからインターネットの証券会社みたいに「うちは手数料がすごく安いよ！」と競争できるようになったんだね"
    },
    {
        "question": "会社が倒産したとき、その会社の債券を持っている人は、株式を持っている人よりも優先的に、残ったお金を返してもらう権利がある。",
        "options": ["◯", "✘"],
        "answer": "◯",
        "explanation": "優先順位は1️⃣債権を持っている人（お金を貸している人）2️⃣株式を持っている人（会社のオーナー）。債権者に全部返した後余っていたら、株式を持っている人にももらえるよ"
    },


    
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
