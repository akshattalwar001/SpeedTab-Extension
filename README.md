# 🌐 Website Load Time Tracker 🚀

A cutting-edge **Chrome extension** paired with a **Flask backend** to measure website load times, deliver **AI-powered performance insights**, and showcase a **webpage preview**


[Download crx file](https://github.com/akshattalwar001/SpeedTab-Extension/blob/main/website-load-time-tracker-extension.crx)
[Download zip file(preffered)](https://github.com/akshattalwar001/SpeedTab-Extension/blob/main/website-load-time-tracker-extension.zip)

## 📋 Overview

Unleash the power of AI with this tool that tracks load times, detects anomalies using `IsolationForest`, and offers a mini-screen preview.

## ✨ Features

- **📏 Load Time Tracking**: Measure website load times in milliseconds.
- **🤖 AI Insights**: Analyze performance with tiers (`<500ms` 🚀, `500-1000ms` ⚡, `1000-2000ms` 🕒, `2000-3000ms` 🐢, `>3000ms` 🦥) and anomaly detection.
- **🖼️ Webpage Preview**: View a scaled-down, scrollable preview in the popup.
- **📜 History Tracking**: Store and display past results in a table.
- **🗑️ Clear History**: Reset data with a single click.

## 🛠️ Requirements

### Chrome Extension
- **Browser**: Google Chrome (latest version recommended).

### Flask Server
- **Python**: `3.x`
- **Packages**: 
  ```bash
  flask
  flask-cors
  requests
  scikit-learn
  numpy
  ```

## 🚀 Installation


**Get the Code:**
Clone or download:
```bash
git clone https://github.com/yourusername/website-load-time-tracker.git
cd website-load-time-tracker
```

**Install Dependencies:**
Create `requirements.txt`:
```text
flask
flask-cors
requests
scikit-learn
numpy
```

Install:
```bash
pip install -r requirements.txt
```

**Run the Server:**
Save `app.py` and start:
```bash
python app.py
```
Server runs at `speedtab-extension-production.up.railway.app/`. Keep it alive!

### 2. 🔧 Install the Chrome Extension

**Grab the File:**
- Download `website-load-time-tracker-extension.zip` from latest release.

**Add to Chrome:**
1. Open `chrome://extensions/`
2. Enable **Developer mode**
3. Drag/drop the `.zip` file or unzip and click **Load unpacked** to select the folder

**Confirm:**
Look for the icon in your toolbar. Click to start!

## 🎮 Usage

**Launch:**
Click the extension icon in your Chrome toolbar.

**Track a Site:**
1. Enter a URL (e.g., `https://example.com`)
2. Hit **Track Load Time**

**Check:**
- **Last Result**: URL, load time, status
- **AI Analysis**: Insights like 🚀 Very fast or ⚠️ Unusual
- **Preview**: Mini-screen view
- **History**: Past entries

**Reset:**
Click **Clear History** to wipe data.

## 🐛 Troubleshooting

### 🔴 "Failed to fetch" Error:
- Ensure the server is running: `python app.py`
- Check terminal for errors; restart if needed
- Inspect console (right-click > Inspect > Console) for network issues

### 🌐 Preview Not Loading:
- Some sites (e.g., `https://google.com`) block iframes. Try another URL
- Use `http://` or `https://` prefixes

### 🤔 No AI Insights:
- Need 5+ entries per domain for anomaly detection. Track repeatedly
- Verify `scikit-learn` and `numpy` are installed


### Project Structure
```
website-load-time-tracker/
├── README.md
├── requirements.txt
├── app.py
├── website-load-time-tracker-extension/
    ├── manifest.json
    ├── popup.html
    ├── popup.js
    ├── icon48.png
    └── icon128.png

```
