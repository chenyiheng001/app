import streamlit as st
import streamlit.components.v1 as components
import base64

# 设置页面标题及宽屏布局
st.set_page_config(page_title="中航智能体合集", layout="wide")

# ========== 函数：设置背景图（使用 base64 编码） ==========
def set_background(image_file):
    """
    将本地图片转为 base64 并应用为背景。
    """
    with open(image_file, "rb") as f:
        data = f.read()
    encoded_bg = base64.b64encode(data).decode()
    # 在 stApp 的 CSS 里设置背景
    page_bg = f"""
    <style>
    .stApp {{
        background: url("data:image/jpg;base64,{encoded_bg}") no-repeat center cent                                                                                                                                                                                                                                           er fixed;
        background-size: cover;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# ========== 设置背景图 ==========
set_background("background.jpg")

# ========== 在侧边栏放置 LOGO 和导航标题 ==========
st.sidebar.image("logo.jpg", width=300)  # 调整 width 以适配 LOGO 大小
st.sidebar.markdown("<h2>智能体导航</h2>", unsafe_allow_html=True)

# ========== 定义智能体字典（名称: URL） ==========
agents = {
    "中航合规AI工具": "https://www.coze.cn/s/oy4zjwmd9qQ/",
    "中航证券合规部门法规查询智能体": "https://www.coze.cn/s/Az-MSs--WgE/",
    "中航证券政府债券承销团": "https://www.coze.cn/s/wb3B9ds9pPw/",
    "中航回测数据查询":"https://www.coze.cn/s/Mp1OXd3ViNs/"
}

# ========== 侧边栏单选按钮，选择要查看的智能体 ==========
selected_agent = st.sidebar.radio("请选择一个智能体", list(agents.keys()))

# ========== 主页面显示标题和所选智能体的 iframe
st.title("中航智能体合集")
st.markdown(f"### 当前选择：{selected_agent}")

selected_url = agents[selected_agent]
components.iframe(selected_url, height=1000, scrolling=True)
