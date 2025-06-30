# 🛡️ NeuraCam: AI-Powered Real-Time Surveillance System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Built with-Streamlit-ff4b4b.svg)](https://streamlit.io/)
[![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-green)](https://github.com/ultralytics/ultralytics)

---

## Table of Contents
- [Demo](#demo)
- [UI Preview](#ui-preview)
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Deployment on Streamlit](#deployment-on-streamlit)
- [Directory Tree](#directory-tree)
- [Bug / Feature Request](#bug--feature-request)
- [Future Scope](#future-scope)
- [License](#license)
- [Author](#author)

---

## Demo

🚀 **Live App:** [Coming Soon on Streamlit Cloud](https://neuracam.streamlit.app)

> _(Replace with your real link after deployment)_

---

## UI Preview

🎥 [Watch the full walkthrough](https://drive.google.com/your-google-drive-video-link)

> _(Replace with your actual Google Drive video link)_

---

## Overview

**NeuraCam** is a real-time surveillance system that uses AI for object detection, intrusion alerting, heatmap analytics, and real-time tracking — all visualized through an interactive Streamlit dashboard.

Perfect for:
- 🏢 Office and Home Surveillance
- 🧠 ML Learners exploring YOLO + Deep SORT
- 💻 Real-time streaming dashboard builders

---

## Features

- 🎯 **YOLOv8 Person Detection**  
- 🟥 **Restricted Zone Intrusion Alerts**  
- 🔁 **Object Tracking via Deep SORT**  
- 🔥 **Heatmap Overlay** for movement zones  
- 📈 **Live Analytics**: live count, unique count  
- 🚨 **Telegram Alerts** with Snapshots  
- ⚙️ Toggle features live from dashboard  

---

## Installation

> Requires Python 3.10+

### 1. Clone this repo:

```bash
git clone https://github.com/ANUSHKA49282/neuracam.git
cd neuracam
```

### 2. Install all dependencies:

```bash
pip install -r requirements.txt
```

### 3. Add `.env` file for Telegram

```env
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
```

> Replace with your own from @BotFather

---

## How to Use

```bash
streamlit run test_yolo_streamlit.py
```

Then:
1. Allow webcam access  
2. Toggle: Show Dashboard / Enable Alerts / Heatmap  
3. Walk into the restricted zone = 📸 Telegram snapshot sent!

---

## Deployment on Streamlit

1. Push to GitHub  
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)  
3. Choose your repo  
4. Set main file to `test_yolo_streamlit.py`  
5. Add secrets:

```env
BOT_TOKEN=your_token
CHAT_ID=your_chat_id
```

6. Deploy! 🚀

---

## Directory Tree

```text
neuracam/
├── detection/
│   ├── yolo_model.py
│   └── anomaly_detection.py
├── dashboard/
│   ├── analytics.py
│   └── heatmap_visualizer.py
├── alerts/
│   └── telegram_bot.py
├── test_yolo_streamlit.py
├── requirements.txt
├── .env              # (Not pushed)
├── .gitignore
├── LICENSE
└── README.md
```

---

## Bug / Feature Request

Found a bug or want a new feature?  
👉 [Submit here](https://github.com/ANUSHKA49282/neuracam/issues)

---

## Future Scope

1. 📹 Multi-camera input  
2. 🧭 Draw restricted zones via UI  
3. 💾 Alert log history  
4. 🔐 Optional anonymization  
5. 📤 Cloud snapshot storage

---

## License

Distributed under the MIT License.  
See [LICENSE](LICENSE) for details.

---

## Author

**Anushka**  
B.Tech Student, VIT AP University  
GitHub: [@ANUSHKA49282](https://github.com/ANUSHKA49282)

---
