import streamlit as st
import pendulum as pdlm
from sxtwl import fromSolar
import pickle
from ephem import Date
from io import StringIO
from contextlib import contextmanager, redirect_stdout

tiangan = '甲乙丙丁戊己庚辛壬癸'
dizhi = '子丑寅卯辰巳午未申酉戌亥'

@contextmanager
def st_capture(output_func):
    with StringIO() as stdout, redirect_stdout(stdout):
        old_write = stdout.write
        def new_write(string):
            ret = old_write(string)
            output_func(stdout.getvalue())
            return ret
        stdout.write = new_write
        yield

def jiazi():
    return [tiangan[x % len(tiangan)] + dizhi[x % len(dizhi)] for x in range(60)]

def multi_key_dict_get(d, k):
    for keys, v in d.items():
        if k in keys:
            return v
    return None

def new_list(olist, o):
    a = olist.index(o)
    res1 = olist[a:] + olist[:a]
    return res1

def find_lunar_month(year):
    fivetigers = {
        tuple(list('甲己')): '丙寅',
        tuple(list('乙庚')): '戊寅',
        tuple(list('丙辛')): '庚寅',
        tuple(list('丁壬')): '壬寅',
        tuple(list('戊癸')): '甲寅'
    }
    if multi_key_dict_get(fivetigers, year[0]) is None:
        result = multi_key_dict_get(fivetigers, year[1])
    else:
        result = multi_key_dict_get(fivetigers, year[0])
    return dict(zip(range(1, 13), new_list(jiazi(), result)[:12]))

def find_lunar_hour(day):
    fiverats = {
        tuple(list('甲己')): '甲子',
        tuple(list('乙庚')): '丙子',
        tuple(list('丙辛')): '戊子',
        tuple(list('丁壬')): '庚子',
        tuple(list('戊癸')): '壬子'
    }
    if multi_key_dict_get(fiverats, day[0]) is None:
        result = multi_key_dict_get(fiverats, day[1])
    else:
        result = multi_key_dict_get(fiverats, day[0])
    return dict(zip(list(dizhi), new_list(jiazi(), result)[:12]))

def lunar_date_d(year, month, day):
    day = fromSolar(year, month, day)
    return {"年": day.getLunarYear(), "月": day.getLunarMonth(), "日": day.getLunarDay()}

def gangzhi(year, month, day, hour, minute):
    if year == 0:
        return ["無效"]
    if year < 0:
        year = year + 1
    if hour == 23:
        d = Date(round((Date("{}/{}/{} {}:00:00.00".format(str(year).zfill(4), str(month).zfill(2), str(day+1).zfill(2), str(0).zfill(2)))), 3))
    else:
        d = Date("{}/{}/{} {}:00:00.00".format(str(year).zfill(4), str(month).zfill(2), str(day).zfill(2), str(hour).zfill(2)))
    dd = list(d.tuple())
    cdate = fromSolar(dd[0], dd[1], dd[2])
    yTG, mTG, dTG, hTG = "{}{}".format(tiangan[cdate.getYearGZ().tg], dizhi[cdate.getYearGZ().dz]), "{}{}".format(tiangan[cdate.getMonthGZ().tg], dizhi[cdate.getMonthGZ().dz]), "{}{}".format(tiangan[cdate.getDayGZ().tg], dizhi[cdate.getDayGZ().dz]), "{}{}".format(tiangan[cdate.getHourGZ(dd[3]).tg], dizhi[cdate.getHourGZ(dd[3]).dz])
    if year < 1900:
        mTG1 = find_lunar_month(yTG).get(lunar_date_d(year, month, day).get("月"))
    else:
        mTG1 = mTG
    hTG1 = find_lunar_hour(dTG).get(hTG[1])
    return [yTG, mTG1, dTG, hTG1]

with open('twogan.pickle', 'rb') as f:
    data = pickle.load(f)

st.set_page_config(layout="wide", page_title="兩頭鉗分定經")

with st.sidebar:
    # Initialize session state for date and time if not already set
    if 'selected_date' not in st.session_state:
        st.session_state.selected_date = pdlm.now(tz='Asia/Shanghai').date()
    if 'selected_time' not in st.session_state:
        st.session_state.selected_time = pdlm.now(tz='Asia/Shanghai').time()

    # Date and time input widgets
    pp_date = st.date_input("日期", value=st.session_state.selected_date, key="date_input")
    pp_time = st.time_input("時間", value=st.session_state.selected_time, key="time_input")

    # Update session state with user selections
    st.session_state.selected_date = pp_date
    st.session_state.selected_time = pp_time

    # Extract year, month, day, hour, minute
    p = str(pp_date).split("-")
    pp = str(pp_time).split(":")
    y = int(p[0])
    m = int(p[1])
    d = int(p[2])
    h = int(pp[0])
    min = int(pp[1])

ertou, links = st.tabs([' 兩頭鉗 ', ' 連接 '])

with ertou:
    st.header('兩頭鉗')
    cctext = gangzhi(y, m, d, h, min)
    two_gan_text = data.get(cctext[0][0] + cctext[3][0])
    output6 = st.empty()
    with st_capture(output6.code):
        print("{}年{}月{}日{}時".format(cctext[0], cctext[1], cctext[2], cctext[3]))
        print(" ")
        print(" ")
        print(cctext[0][0] + cctext[3][0])
        print("判斷")
        print(two_gan_text.get("判斷"))
        print(" ")
        print("命格")
        print(two_gan_text.get("命格")[0])
        print(two_gan_text.get("命格")[1])
        print(" ")
        print("基業")
        print(two_gan_text.get("基業"))
        print(" ")
        print("兄弟")
        print(two_gan_text.get("兄弟"))
        print(" ")
        print("行藏")
        print(two_gan_text.get("行藏"))
        print(" ")
        print("婚姻")
        print(two_gan_text.get("婚姻"))
        print(" ")
        print("子息")
        print(two_gan_text.get("子息"))
        print(" ")
        print("收成")
        print(two_gan_text.get("收成"))

with links:
    st.header('連接')
    links_md = """# 開發者資訊
微信公眾號 "探究三式"

<p align="center">
  <a href="https://iching.streamlit.app/">
    <img src="https://raw.githubusercontent.com/kentang2017/ichingshifa/master/pic/iching.png" style="max-width: 100%; height: auto;">
  </a>
  <a href="https://kintaiyi.streamlit.app/">
    <img src="https://raw.githubusercontent.com/kentang2017/kintaiyi/master/pic/Untitled-1.png" style="max-width: 100%; height: auto;">
  </a>
  <a href="https://kinliuren.streamlit.app/">
    <img src="https://raw.githubusercontent.com/kentang2017/kinliuren/master/pic/Untitled-33.png" style="max-width: 100%; height: auto;">
  </a>
  <a href="https://kinqimen.streamlit.app/">
    <img src="https://raw.githubusercontent.com/kentang2017/kinqimen/master/pic/Untitled-22.png" style="max-width: 100%; height: auto;">
  </a>
  <a href="https://kinwuzhao.streamlit.app/">
    <img src="https://raw.githubusercontent.com/kentang2017/kinwuzhao/refs/heads/main/pic/wuzhao.png" style="max-width: 100%; height: auto;">
  </a>
  <a href="https://kintaixuan.streamlit.app/">
    <img src="https://raw.githubusercontent.com/kentang2017/taixuanshifa/master/pic/taixuan.png" style="max-width: 100%; height: auto;">
  </a>
  <a href="https://kinwangji.streamlit.app/">
    <img src="https://raw.githubusercontent.com/kentang2017/kinwangji/main/pic/kwj.png" style="max-width: 100%; height: auto;">
  </a>
  <a href="https://jingjue.streamlit.app/">
    <img src="https://raw.githubusercontent.com/kentang2017/jingjue/master/pic/jingjue.png" style="max-width: 100%; height: auto;">
  </a>
  <a href="https://liangtouqian.streamlit.app/">
    <img src="https://raw.githubusercontent.com/kentang2017/liangtouqian/master/pic/Untitled-44.png" style="max-width: 100%; height: auto;">
  </a>
  <img src="https://raw.githubusercontent.com/kentang2017/kintaiyi/master/pic/20231205113526.jpg" style="max-width: 100%; height: auto">
</p>

如有任何建議或合作事宜，可加本人微信聯繫
或搜 gnatnek (請註明是在github加我的)

或 加入QQ群組 堅三式軟件交流群 (搜群號 770621021或 "堅三式軟件交流群")
聯繫通訊
"""
    st.markdown(links_md, unsafe_allow_html=True)
