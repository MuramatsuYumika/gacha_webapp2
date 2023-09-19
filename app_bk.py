import streamlit as st
from PIL import Image
import datetime

st.title("🐇うさぎ王国🐇")#titleは太字
st.caption("うさぎ王国はうさぎ様絶対の国！入国審査に引っかからずに入国せよ！")#captionは細字
st.subheader("自己紹介")
st.text("うさぎ様はバナナが好物です！")
#Python特有の改行含みの文字列
code = '''
include<stdio.h>
int main(){
	int x = 0;
	printf("%d",x);
	return 0;
}
'''
st.code(code,language='c')

#画像
image = Image.open("LINE_ALBUM_20221110_221124_5.jpg")
st.image(image,width=200)

with st.form(key='profile_form'):
	#テキストボックス
	name = st.text_input('名前')
	
	#セレクトボックス
	#age_category = st.selectbox("種族",("うさぎ","人間"))
	#ラジオボタン
	age_category = st.radio("種族",("うさぎ","人間"))

	#複数選択
	hobby = st.multiselect("持ち物",("バナナ","にんじん","ナイフ","ライフル","小松菜"))

	#チェックボックス
	st.checkbox("うさぎ様に食べ物を捧げます")

	#スライダー
	height = st.slider("満腹度",min_value = 0, max_value = 100)

	#日付
	start_date = st.date_input("誕生した日",datetime.date(2023,9,19))

	#カラーピッカー
	color = st.color_picker("テーマカラー","#FFFFFF")

	#ボタン
	submit_btn = st.form_submit_button('送信')
	if submit_btn == True:
		st.text("ねぇ！"+ name +"！バナナを渡しなさい！")