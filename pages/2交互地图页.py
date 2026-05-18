import streamlit as st
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
map_path = os.path.join(project_root, "maps")

st.title("🗺️ 唐宋商业贸易地域分布地图")
st.divider()

# 左右并列摆放两张地图
col_tang, col_song = st.columns(2)

with col_tang:
    st.subheader("唐代商业贸易地图")
    with open(os.path.join(map_path,"唐代交互式地图.html"),"r",encoding="utf-8") as f:
        tang_map = f.read()
    st.components.v1.html(tang_map, height=550)

with col_song:
    st.subheader("宋代商业贸易地图")
    with open(os.path.join(map_path,"宋代交互式地图.html"),"r",encoding="utf-8") as f:
        song_map = f.read()
    st.components.v1.html(song_map, height=550)