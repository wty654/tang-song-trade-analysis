import os
# 禁用所有弃用警告
os.environ["STREAMLIT_DEPRECATION_WARNING"] = "false"
# 禁用特定的参数警告
os.environ["STREAMLIT_WARNING_USE_COLUMN_WIDTH"] = "false"

import streamlit as st
# 下面是你原来的app.py代码...
import streamlit as st

# 全局页面设置
st.set_page_config(
    page_title="唐宋商业贸易数据分析",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 侧边栏导航说明
st.sidebar.title("📊 唐宋商业贸易分析")
st.sidebar.info("请从左侧菜单选择页面查看")