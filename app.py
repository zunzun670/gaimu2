import streamlit as st
import random

# CSSでフォントサイズと太さを統一、さらに可愛く装飾
st.markdown(""" 
    <style> 
    .question-text, .stRadio label { 
        font-size: 18px !important; 
        line-height: 1.3 !important;
        font-weight: bold;
    }
    div[role="radiogroup"] > label {
        line-height: 1.2 !important;
        margin-bottom: 0.2rem !important;
    }
    /* サイドバーや隅に置くキャラクター用 */
    .daruma-text {
        font-size: 50px;
        text-align: center;
    }
    </style> 
""", unsafe_allow_html=True)

# 問題データ（内容は一切変えていないよ！）
questions = [
    {
        "question": "株式は元本保証されている？",
        "options": ["◯", "✕"],
        "answer": "✕",
        "explanation": "株式は価格が変動するから、元本保証はされていないよ",
        "source": "問題：二種外務員",
    },
    {
        "question": "投資信託の運用会社の役割は？",
        "options": ["資産の保管", "運用の指図", "販売", "監査"],
        "answer": "運用の指図",
        "explanation": "運用会社は投資信託の資産をどのように運用するかを決める役割を担っているよ",
        "source": "問題：二種外務員",
    },
    {
        "question": "債券の利子は変動する？",
        "options": ["変動する", "固定されている"],
        "answer": "固定されている",
        "explanation": "一般的な債券は固定利率で発行されいるよ",
        "source": "問題：二種外務員",
    },
    {
        "question": "株式会社が新しく株を発行して、投資家からお金を集める場所のことを流通市場という。",
        "options": ["◯", "✕"],
        "answer": "✕",
        "explanation": "新しく株を発行してお金を集めるのは発行市場。流通市場は、すでに誰かが持っている株を売り買いする場所（証券取引所など）",
        "source": "問題：二種外務員",        
    },
    {
        "question": "上場株式を売買するとき、株価がいくらであっても証券会社が受け取る売買委託手数料の金額は、国によって一律に決められている。",
        "options": ["◯", "✕"],
        "answer": "✕",
        "explanation": "それぞれの証券会社が自分たちで決めていいことになっているよ。だからインターネットの証券会社みたいに「うちは手数料がすごく安いよ！」と競争できるようになったんだね",
        "source": "問題：二種外務員",        
    },
    {
        "question": "会社が倒産したとき、その会社の債券を持っている人は、株式を持っている人よりも優先的に、残ったお金を返してもらう権利がある。",
        "options": ["◯", "✕"],
        "answer": "◯",
        "explanation": "優先順位は1️⃣債権を持っている人（お金を貸している人）2️⃣株式を持っている人（会社のオーナー）。債権者に全部返した後余っていたら、株式を持っている人にももらえるよ",
        "source": "問題：二種外務員",
    },
    {
        "question": "上場会社が、すでに発行している株式をさらに新しく発行して、広く投資家からお金を集めることを「公募増資（こうぼぞうし）」という。",
        "options": ["◯", "✕"],
        "answer": "◯",
        "explanation": "会社はこれでお金を手に入れて、新しい工場を建てたり事業を広げたりするんだ",
        "source": "問題：二種外務員",
    },
    {
        "question": "証券会社が、客から預かっているお金や株を、証券会社自身の財産と混ざらないように分けて管理することを「分別管理（ぶんべつかんり）」という。",
        "options": ["◯", "✕"],
        "answer": "◯",
        "explanation": "万が一、証券会社がつぶれてもお客さんのお金が守られるための大事なルールだよ",
        "source": "問題：二種外務員",
    },
    {
        "question": "次のうち、債券の「格付け」において、一般的に「投資適格（投資しても比較的安全）」とされる最低ラインの格付けはどれか。",
        "options": ["AA", "A","BBB","BB"],
        "answer": "BBB",
        "explanation": "格付けは一般的に「BBB」以上が投資適格、ギリギリ合格ラインと覚えてね。「BB」以下が投機的（リスクが高い）とされているよ",
        "source": "問題：二種外務員",
    },
    {
        "question": "投資家が、証券会社に対して株式の売買を注文する際、価格を指定せずに「その時の市場価格で成立させてほしい」と依頼する方法を「指値注文」という。",
        "options": ["◯", "✕"],
        "answer": "✕",
        "explanation": "価格を指定しない注文は「成行（なりゆき）注文」だよ。指値は「1000円で買って」と値段を指し示す注文のことだね",
        "source": "問題：二種外務員",
    },
    {
        "question": "株式の売買取引において、最も優先して成立する注文は次のうちどれか。",
        "options": ["1,000円の指値買い注文", "成行買い注文","900円の指値買い注文","前日に出された1,050円の指値買い注文"],
        "answer": "成行買い注文",
        "explanation": "取引所では「価格優先の原則」があるよ。価格を指定しない成行注文は、どんな価格の指値注文よりも優先して成立するルールなんだ。",
        "source": "問題：二種外務員",
    },
    {
        "question": "生命保険の保険金は、相続税の課税対象にはならない。",
        "options": ["◯", "✕"],
        "answer": "✕",
        "explanation": "生命保険金は「みなし相続財産」として相続税の課税対象になるよ。ただし「500万円 × 法定相続人の数」まで非課税になる特例がある。たとえば法定相続人が3人なら、1,500万円まで非課税だよ。",
        "source": "問題：日本FP協会 3級ファイナンシャル・プランニング技能検定学科試験 2025年5月公表分",
    },
    {
        "question": "次のうち、所得税の課税対象とならないものはどれ？",
        "options": ["給与所得", "退職所得","宝くじの当せん金","不動産の賃貸収入"],
        "answer": "宝くじの当せん金",
        "explanation": "「非課税所得」として法律で定められているよ。ただし、懸賞金や競馬の払戻金などは課税対象になることがあるので注意！",
        "source": "問題：日本FP協会 3級ファイナンシャル・プランニング技能検定学科試験 2025年5月公表分",
    },
    {
        "question": "税理士の登録を受けていないファイナンシャル・プランナーが、顧客のために反復継続して確定申告書を作成しても、その行為が無償であれば税理士法に抵触しない。 ",
        "options": ["◯", "✕"],
        "answer": "✕",
        "explanation": "反復継続して他人の確定申告書を作成する行為は、税理士法に違反しちゃう。税務書類の作成は原則として税理士の独占業務。FPが行えるのは、あくまで一般的なアドバイスまで！",
        "source": "問題：日本FP協会 3級ファイナンシャル・プランニング技能検定学科試験 2025年5月公表分",
    },
    {
        "question": "雇用保険の高年齢雇用継続基本給付金は、原則として、60歳以上65歳未満の被保険者が、60歳到達時点に比べて賃金月額が85％未満に低下した状態で就労している場合に支給される。",
        "options": ["◯", "✕"],
        "answer": "✕",
        "explanation": "支給の条件は、賃金が60歳到達時点の75％未満に低下した場合。「75％未満」が正しいラインなので注意！",
        "source": "問題：日本FP協会 3級ファイナンシャル・プランニング技能検定学科試験 2025年5月公表分",
    },
     {
        "question": "国民年金の第1号被保険者の収入により生計を維持している配偶者で、20歳以上60歳未満の者は、国民年金の第３号被保険者となる。 ",
        "options": ["◯", "✕"],
        "answer": "✕",
        "explanation": "第3号になれるのは、第2号（会社員や公務員）に扶養されている配偶者だけ。第1号（自営業など）に扶養されている配偶者は、自分で保険料を払う第1号被保険者になるよ。",
        "source": "問題：日本FP協会 3級ファイナンシャル・プランニング技能検定学科試験 2025年5月公表分",
    },
    {
        "question": "国民年金の第3号被保険者は、確定拠出年金の個人型年金に加入することができる。",
        "options": ["◯", "✕"],
        "answer": "◯",
        "explanation": "2017年から第3号もiDeCo（個人型確定拠出年金）に加入OK！ただし、掛金の上限や手続きには注意が必要だよ。",
        "source": "問題：日本FP協会 3級ファイナンシャル・プランニング技能検定学科試験 2025年5月公表分",
    },
    {
        "question": "小規模企業共済の掛金月額は、1,000円から7万円までの範囲内で500円単位で選択することができる。",
        "options": ["◯", "✕"],
        "answer": "◯",
        "explanation": "途中で増減もできるから、事業の状況に合わせて調整できるのが魅力！",
        "source": "問題：日本FP協会 3級ファイナンシャル・プランニング技能検定学科試験 2025年5月公表分",
    },
    {
        "question": "契約転換制度を利用して、現在契約している生命保険を新たな契約に転換する場合、転換後契約の保険料は、転換前契約の加入時の年齢に応じた保険料率により算出される。",
        "options": ["◯", "✕"],
        "answer": "✕",
        "explanation": "転換後の保険料は、転換時の年齢に応じた保険料率で計算されるよ。つまり、年齢が上がるほど保険料も高くなるので、転換のタイミングには注意が必要！",
        "source": "問題：日本FP協会 3級ファイナンシャル・プランニング技能検定学科試験 2025年5月公表分",
    },
]

# セッション状態の初期化 
if "current_q" not in st.session_state: 
    st.session_state.current_q = random.choice(questions) 
    st.session_state.answered = False 
    st.session_state.feedback = "" 
    st.session_state.explanation = ""
    st.session_state.combo = 0 # 連続正解数

q = st.session_state.current_q

# サイドバーに合格祈願キャラクターを表示
with st.sidebar:
    st.write("### 合格祈願！進化するだるま")
    # コンボ数に応じてだるまが豪華になる
    if st.session_state.combo == 0:
        daruma = "⚪️" # まだ白い
    elif st.session_state.combo < 3:
        daruma = "🔴" # 赤くなった
    elif st.session_state.combo < 5:
        daruma = "🏵️🔴🏵️" # ちょっと豪華
    else:
        daruma = "✨👑🔴👑✨" # めちゃくちゃ豪華
    
    st.markdown(f"<div class='daruma-text'>{daruma}</div>", unsafe_allow_html=True)
    st.write(f"現在の連続正解: {st.session_state.combo}")

st.title("二種外務員とFP3級 問題")

# 出典に基づいてアイコンを決定
icon = "💼" if "外務員" in q["source"] else "🏠"

# 3行分のスペースを空ける
st.markdown("<br>", unsafe_allow_html=True)

# 出典の表示（アイコン付き）
if "source" in q: st.caption(f"{icon} {q['source']}")

# 問題文
st.markdown(f"<div class='question-text'>{q['question']}</div>", unsafe_allow_html=True) 
user_answer = st.radio("答えを選んでね", q["options"], key=q["question"])

# 答え合わせボタン
if not st.session_state.answered:
    if st.button("答え合わせ 🔍"):
        st.session_state.answered = True
        if user_answer == q["answer"]:
            st.session_state.feedback = "✅ 正解！すごい！"
            st.session_state.combo += 1
            st.balloons() # 正解時に風船！
        else:
            st.session_state.feedback = "❌ 不正解！どんまい！"
            st.session_state.combo = 0 # 間違えたらコンボリセット
        st.session_state.explanation = f"💡 解説：{q['explanation']}"

# フィードバックと解説の表示
if st.session_state.answered:
    st.divider() # 区切り線
    st.markdown(f"### {st.session_state.feedback}")
    st.info(st.session_state.explanation)

    if st.button("次へ 🐾"):
        st.session_state.current_q = random.choice(questions)
        st.session_state.answered = False
        st.session_state.feedback = ""
        st.session_state.explanation = ""
        st.rerun()
