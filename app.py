import streamlit as st
from random import randint

st.title("ガチャシミュレーションアプリ")#titleは太字
st.caption("ラビットガチャを引くアプリです")#captionは細字

prob = [80,10,7,3]
sum_prob = sum(prob)

with st.form(key='gacha'):
	#ボタン
	gacha_btn = st.form_submit_button('うさぎ様をお迎え')
	if gacha_btn == True:
		st.text("うさぎ様をお迎えします")
		for i in range(10):
			value = randint(1,sum_prob)
			rare = 1
			sum_p = 0
			for p in prob:
				sum_p += p
				if value <= sum_p:
					st.text("うさ度" +( "🐇" * rare) + "をお迎えした！")
					break
				rare += 1