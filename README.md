# 💥 No4bidden – Advanced 40X Bypass Tool

_No4bidden_ is a powerful penetration-testing utility designed to identify and exploit **HTTP 40X (Forbidden/Unauthorized)** bypass misconfigurations.  
Inspired by **Janus**, the Roman god of gates and transitions, No4bidden sees paths where others only see walls.

<p align="center">
<img src="https://github.com/Debajyoti0-0/No4bidden/blob/main/Images/Logo.png" alt="No4bidden Tool Logo">
</p>

## 🔐 Key Features

### 🚀 Comprehensive Bypass Suite
Attempts dozens of 40X bypass techniques including:
- HTTP Verb Tampering  
- Custom Header Injection  
- Path Normalization & Traversal  
- Double / Multi-Encoding  
- HTTP Version Smuggling  
- Combination Attacks  

### 📂 Request File Support (`-r`)
Load full HTTP requests directly from tools like Burp Suite, ZAP, or cURL.  
Supports **headers, body, cookies, and custom methods**.

### ⚡ Performance & Safety
- Fully multithreaded scanning  
- Safe concurrency with locking  
- Auto-calibration for accurate detection  
- Optional rate-limit auto-stop (`--rate-limit`)  
- Adjustable threads, timeouts, and delays  

### 🧙 Wizard Mode
Interactive guided mode to set up a scan step-by-step.

## 🖼️ Banner
<p align="center">
<img src="https://github.com/Debajyoti0-0/No4bidden/blob/main/Images/Banner.png" alt="Banner-preview">
</p>

## 🛠️ Installation

### Prerequisites
- Python **3.x**
- `requests` library

### 1. Clone the repository

```bash
git clone https://github.com/Debajyoti0-0/No4bidden.git
cd No4bidden
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Run the tool

```bash
python3 No4bidden.py --help
```

### 🚀 Usage

- Basic Scan

```bash
python3 No4bidden.py -u https://example.com/admin
```

- Wizard Mode (Beginner Friendly)

```bash
python3 No4bidden.py --wizard
```

### 🔧 Advanced Examples

| Command                                                 | Description                                         |
| ------------------------------------------------------- | --------------------------------------------------- |
| `python3 No4bidden.py -u URL -v`                        | Verbose mode for debugging and thread-level details |
| `python3 No4bidden.py -u URL --threads 100 --delay 500` | 100 threads + 500ms delay                           |
| `python3 No4bidden.py -u URL -x http://127.0.0.1:8080`  | Route traffic via Burp/ZAP                          |
| `python3 No4bidden.py -u URL --rate-limit`              | Stop when a 429 Too Many Requests appears           |
| `python3 No4bidden.py -r request.txt`                   | Use a full request from a file                      |
| `python3 No4bidden.py -u URL -H "X-Custom: Value"`      | Add custom headers                                  |


### 🧬 Bypass Technique Categories
| Category           | Prefix      | Description                                          |
| ------------------ | ----------- | ---------------------------------------------------- |
| 🔀 VERB TAMPERING  | `method_`   | Tests GET/POST/PUT/DELETE/TRACE/OPTIONS and variants |
| 📋 HEADERS         | `header_`   | Injects headers like X-Forwarded-For, X-Original-URL |
| 🛤️ CUSTOM PATHS   | `path_`     | Path traversal, bypass suffixes, malformed routes    |
| 🔣 DOUBLE-ENCODING | `encoding_` | Tests `%2f`, `%252f`, Unicode, Base64 encoded paths  |
| 🌐 HTTP VERSIONS   | `http_`     | Non-standard or tampered HTTP versions               |


## 🤝 Contributing
We welcome contributions!
#### 1. Fork the repository
#### 2. Create a feature branch
#### 3. Add your improvements
#### 4. Submit a pull request
Areas for contribution:
- More payloads
- Additional bypass techniques
- Improved output formatting
- Enhanced detection heuristics


### ⭐ Support
If this project helps you, consider giving it a ⭐ star on GitHub.


### 🧑‍💻 Author
#### [Debajyoti0-0](https://github.com/Debajyoti0-0)

“Opening gates where others see only walls.” ⚔️
