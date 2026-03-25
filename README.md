# 🔮 堅兩頭鉗 · Liangtouqian — 兩頭鉗分定經

<p align="center">
  <b>年干時干，兩頭鉗定一生命格 · Pincer the Destiny by Year Stem & Hour Stem</b><br>
  <i>兩頭鉗分定經 | Liǎng Tóu Qián Fēn Dìng Jīng | Two-Headed Pincers Destiny Scripture</i>
</p>

<p align="center">
  <a href="https://github.com/kentang2017/liangtouqian/stargazers"><img src="https://img.shields.io/github/stars/kentang2017/liangtouqian?style=flat" alt="GitHub Stars"></a>
  <a href="https://github.com/kentang2017/liangtouqian/network/members"><img src="https://img.shields.io/github/forks/kentang2017/liangtouqian?style=flat" alt="GitHub Forks"></a>
  <a href="https://t.me/haizhonggum"><img src="https://img.shields.io/badge/chat-Telegram-blue?logo=telegram" alt="Telegram"></a>
  <a href="https://t.me/numerology_coding"><img src="https://img.shields.io/badge/channel-Telegram-red?logo=telegram" alt="Telegram Channel"></a>
  <a href="https://www.paypal.me/kinyeah"><img src="https://img.shields.io/badge/Donate-PayPal-green.svg?logo=paypal&style=flat-square" alt="Donate"></a>
</p>

<p align="center">
  <a href="https://liangtouqian.streamlit.app/">
    <img src="https://img.shields.io/badge/🌐%20線上排盤-Live%20Demo-brightgreen?style=for-the-badge" alt="Live Demo">
  </a>
</p>

---

<p align="center">
  <img width="1978" height="906" alt="image" src="https://github.com/user-attachments/assets/a3155885-6440-495a-b273-53424ec10157" />
</p>

---

## 📖 導讀 · Introduction

### 中文

**兩頭鉗**（又稱「兩頭箝」），出自古籍《堅兩頭鉗分定經》，是中國傳統命理學中一門獨特的論命術數。其核心原理簡潔精妙：以出生八字中的**年干**（年柱天干）與**時干**（時柱天干）兩端為綱，猶如鉗子的兩頭夾定命格，故名「兩頭鉗」。

年干為命之根源，代表先天稟賦與家族背景；時干為命之歸宿，代表晚年境遇與最終成就。兩干相合，便可推斷一個人的**命格**、**基業**、**兄弟**、**行藏**、**婚姻**、**子息**及**收成**等人生各個面向。此法取象直觀、斷語精練，歷來為命理愛好者所重視。

本應用以 Python + Streamlit 實現，只需輸入出生日期與時間，即可自動排出干支四柱，並依據兩頭鉗法則呈現完整的命格分析。

### English

**Liǎng Tóu Qián** (兩頭鉗, literally "Two-Headed Pincers") is a unique destiny analysis method from classical Chinese metaphysics, originating from the ancient text *"Jiān Liǎng Tóu Qián Fēn Dìng Jīng"* (堅兩頭鉗分定經 — *The Scripture of Destiny Classification by the Two-Headed Pincers*).

The method is elegantly simple: it uses only two key elements from a person's **Four Pillars of Destiny** (八字, BaZi) — the **Year Heavenly Stem** (年干) and the **Hour Heavenly Stem** (時干). Like the two jaws of a pincer clamping down on a subject, these two stems "clamp" and define the native's fate — hence the vivid name "Two-Headed Pincers."

- The **Year Stem** represents one's innate endowment and ancestral background.
- The **Hour Stem** represents one's later-life fortune and ultimate achievements.

Together, these two stems reveal readings across seven life dimensions: **Destiny Pattern** (命格), **Career & Foundation** (基業), **Siblings** (兄弟), **Actions & Conduct** (行藏), **Marriage** (婚姻), **Children** (子息), and **Harvest & Outcome** (收成).

This web application is built with **Python** and **Streamlit**. Simply enter a birth date and time, and it automatically calculates the Four Pillars (年月日時) and presents a complete Two-Headed Pincers destiny reading.

---

## ✨ 功能特色 · Features

| 功能 Feature | 說明 Description |
|---|---|
| 📅 自動排四柱 | 輸入日期時間，自動計算年月日時干支 / Auto-calculate Four Pillars from date & time |
| 🔮 兩頭鉗論命 | 年干＋時干組合，鉗定命格 / Year Stem + Hour Stem pincer destiny reading |
| 📜 七大範疇 | 命格、基業、兄弟、行藏、婚姻、子息、收成 / Seven life dimensions analyzed |
| 🌙 農曆支援 | 精確換算公曆與農曆干支 / Accurate solar ↔ lunisolar calendar conversion |
| 🌐 線上使用 | Streamlit 網頁即時互動 / Real-time interactive web app via Streamlit |
| 📱 響應式佈局 | 適配桌面及移動設備 / Responsive layout for desktop and mobile |

---

## 🚀 線上體驗 · Live Demo

無需安裝，直接在瀏覽器中體驗兩頭鉗論命。  
No installation required — try it directly in your browser.

👉 **[https://liangtouqian.streamlit.app/](https://liangtouqian.streamlit.app/)**

---

## 💻 本地運行 · Run Locally

```bash
# 克隆倉庫 / Clone the repository
git clone https://github.com/kentang2017/liangtouqian.git
cd liangtouqian

# 安裝依賴 / Install dependencies
pip install -r requirements.txt

# 啟動應用 / Launch the app
streamlit run app.py
```

> 需要 Python 3.7+ · Requires Python 3.7+

---

## 📚 三式相關項目 · Related Projects

本應用是「堅三式」系列的一部分。  
This app is part of the **Kin Three Styles** (堅三式) series of Chinese metaphysics tools.

| 項目 Project | 說明 Description | 連結 Link |
|---|---|---|
| 🔮 堅大六壬 | 大六壬排盤 Da Liu Ren | [kinliuren.streamlit.app](https://kinliuren.streamlit.app/) |
| ☯️ 堅奇門 | 奇門遁甲 Qi Men Dun Jia | [kinqimen.streamlit.app](https://kinqimen.streamlit.app/) |
| ⭐ 堅太乙 | 太乙神數 Taiyi | [kintaiyi.streamlit.app](https://kintaiyi.streamlit.app/) |
| 🀄 堅易 | 易經 I Ching | [iching.streamlit.app](https://iching.streamlit.app/) |
| 🏮 堅王機 | 皇極經世 Wangji | [kinwangji.streamlit.app](https://kinwangji.streamlit.app/) |
| 🌟 堅太玄 | 太玄 Taixuan | [kintaixuan.streamlit.app](https://kintaixuan.streamlit.app/) |
| 💫 堅五照 | 五照 Wuzhao | [kinwuzhao.streamlit.app](https://kinwuzhao.streamlit.app/) |
| 🎴 金口訣 | 金口訣 Jingjue | [jingjue.streamlit.app](https://jingjue.streamlit.app/) |

---

## 🤝 聯絡與支持 · Contact & Support

- 💬 **Telegram 群組 Chat**: [@haizhonggum](https://t.me/haizhonggum)
- 📢 **Telegram 頻道 Channel**: [@numerology_coding](https://t.me/numerology_coding)
- 💰 **贊助支持 Donate**: [PayPal](https://www.paypal.me/kinyeah)
- 📱 **微信公眾號 WeChat**: 探究三式

<p align="center">
  <img src="https://raw.githubusercontent.com/kentang2017/kinliuren/refs/heads/master/pic/%E5%9C%96%E7%89%87_20260316084147.jpg" alt="微信公眾號二維碼" width="200">
</p>

> 如有任何建議或合作事宜，可加微信 **gnatnek**（請註明是在 GitHub 加的）  
> 或加入 QQ 群組「堅三式軟件交流群」（群號：770621021）
>
> For suggestions or collaboration, add WeChat **gnatnek** (please note you found me on GitHub),  
> or join the QQ group "堅三式軟件交流群" (Group ID: 770621021).

---

<div align="center">

⭐ **覺得有用？請給我一顆星！ · Find it useful? Give us a star!** ⭐

**🙏 如覺有用，歡迎打賞支持 · If you find this useful, donations are welcome 🙏**

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg?logo=paypal&style=for-the-badge)](https://www.paypal.me/kinyeah)

_"年干時干，兩頭鉗定一生。"_  
_"Year Stem and Hour Stem — the Two-Headed Pincers clamp your destiny."_

</div>
