import streamlit as st
import os

# 自动获取文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
img_path = os.path.join(project_root, "img")

st.title("📊 贸易数据图表展示")
st.divider()

# 朝代筛选器（中文提示）
dynasty = st.selectbox("选择查看朝代数据", ["全部数据", "唐代", "宋代"])

# 你的图片列表（已修正繁体“稅”）
all_img = [
    "共现关系图_商.png",
    "共现关系图_市.png",
    "共现关系图_稅.png",
    "关键词对比柱状图（前15）.png",
    "唐代词云图.png",
    "宋代词云图.png",
    "商业主题占比图.png",
    "情感对比柱状图.png"
]

# 根据筛选结果过滤图片
if dynasty == "唐代":
    show_img = [pic for pic in all_img if "唐代" in pic]
elif dynasty == "宋代":
    show_img = [pic for pic in all_img if "宋代" in pic]
else:
    show_img = all_img

# 两列排版，改用新版width参数，彻底消除警告
col1, col2 = st.columns(2)
cols = [col1, col2]

for idx, pic_name in enumerate(show_img):
    full_path = os.path.join(img_path, pic_name)
    with cols[idx % 2]:
        # 用 width="stretch" 替代 use_column_width=True
        st.image(full_path, caption=pic_name.replace(".png",""), width="stretch")