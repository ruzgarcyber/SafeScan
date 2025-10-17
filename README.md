# 🛡️ SafeScan — Quick URL Scanner

Minimal Python tool to quickly check URLs for HTTPS 🔒, HTTP status 📡, and basic blacklist ⚠️ matches. Color-coded console output 🎨.

---

## ✨ Features
- HTTPS check (enabled ✅ / disabled ❌)  
- HTTP GET request & status code 📡  
- Basic domain blacklist ⚠️  
- Single file, dependencies: `requests`, `colorama` 🐍

---

## 🚀 Usage
```bash
pip install requests colorama
python safe_scan.py
```
**Enter a URL when prompted 🌐**

## Example Output:
```bash
HTTPS: ENABLED
No blacklist match
GET request sent - Status: 200
```
