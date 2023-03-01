import streamlit as st
import pandas
import pickle
import pandas as pd
import numpy as np
user_sim_df = pickle.load(open('recommend_new_nation.pkl','rb'))
final_ratings=pickle.load(open('data_new_file.pkl','rb'))
st.title('Book recommendation app')

userid= st.selectbox(label="User-ID",options=final_ratings["User-ID"].unique())

try:
    tem=list(user_sim_df.sort_values([userid],ascending=False).head(5).index)
    print(tem)
    book_list=[]
    url_list=[]
    for i in tem:
        book_list=book_list+list(final_ratings[final_ratings["User-ID"]==i]['Book-Title'][1:3])
        url_list=url_list+list(final_ratings[final_ratings["User-ID"]==i]['Image-URL-M'][1:3])
        #print(book_list)
    read_books=list(final_ratings[final_ratings['User-ID']==userid]['Book-Title'][1:8])
    read_urls=list(final_ratings[final_ratings['User-ID']==userid]['Image-URL-M'][1:8])
    for i in read_books:
        if i in book_list:
            book_list.remove(i)
    for i in read_urls:
        if i in url_list:
            url_list.remove(i)
    st.subheader("Books already read by the user")
    for i in enumerate(read_books):
        st.write(i[1])
        st.image(read_urls[i[0]])


    st.subheader("Recommended books")
    for i in enumerate(book_list):
        st.write(i[1])
        st.image(url_list[i[0]])
except:
    st.write("Enter a valid user ID")

