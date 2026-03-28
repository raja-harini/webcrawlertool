# 🕷️ Web Crawler Tool – URL Parameter Extractor

A lightweight, efficient, and security-focused **Command-Line Web Crawler Tool** built using Python to extract and analyze **URL query parameters** from given web applications.

---

## 📌 Overview

The **Web Crawler Tool** is designed to assist in **web application analysis and cybersecurity reconnaissance** by extracting query parameters from URLs. It helps identify input points in web applications, which is crucial for **testing, debugging, and vulnerability assessment**.

This tool is ideal for:
- 🔐 Cybersecurity enthusiasts  
- 🕵️ Bug bounty hunters  
- 🌐 Web developers & testers  
- 📊 Data analysts  

---

## 🎯 Key Features

- 🔗 Accepts **multiple URLs** via command line  
- 🧠 Extracts **query parameters dynamically**  
- 📄 Stores results in a structured **output file**  
- ⚡ Fast and lightweight (no external dependencies)  
- 🛡 Useful for **parameter discovery in security testing**  
- 📌 Handles both:
  - URLs **with parameters**
  - URLs **without parameters**  

---

## 🏗 System Architecture

The tool follows a simple and efficient flow:

Input URLs → URL Parsing → Parameter Extraction → File Storage


- **Input Layer:** Command-line arguments  
- **Processing Layer:** URL parsing & parameter extraction  
- **Output Layer:** Structured file output (`output.txt`)  

---

## 🧰 Tech Stack

- 🐍 Python 3  
- 📦 argparse (CLI argument handling)  
- 🔗 urllib.parse (URL parsing)  

---

## 🧠 Working Principle

1. User provides one or more URLs as input.  
2. The tool parses each URL using `urlparse`.  
3. Query parameters are extracted using `parse_qs`.  
4. Extracted data is formatted for readability.  
5. Results are stored in an output file (`output.txt`).  

---

## 💻 Program

```python
import argparse
from urllib.parse import urlparse, parse_qs

# Function to extract parameters from a URL
def extract_parameters(url):
    parsed_url = urlparse(url)
    # Parse the query parameters from the URL
    parameters = parse_qs(parsed_url.query)
    return parameters

# Function to save the extracted results to output.txt
def save_results(results, filename='output.txt'):
    with open(filename, 'w') as file:
        for url, params in results.items():
            file.write(f"URL: {url}\n")
            if params:
                file.write("Parameters:\n")
                for param, values in params.items():
                    file.write(f"  {param}: {', '.join(values)}\n")
            else:
                file.write("No parameters found.\n")
            file.write("\n")

# Main function to handle command-line arguments and workflow
def main():
    parser = argparse.ArgumentParser(description='Crawl URLs and extract parameters.')
    parser.add_argument('urls', nargs='+', help='List of URLs to crawl.')
    args = parser.parse_args()

    results = {}
    # Process each URL and extract its parameters
    for url in args.urls:
        params = extract_parameters(url)
        results[url] = params

    # Save the results to output.txt
    save_results(results)

if __name__ == '__main__':
    main()
```
## ▶️ How to Run
```
python webcrawl.py https://example.com?name=harini&age=20 https://test.com?id=123
```
## 📂 Sample Output
```
URL: https://example.com?name=harini&age=20
Parameters:
  name: harini
  age: 20

URL: https://test.com?id=123
Parameters:
  id: 123

URL: https://example.com
No parameters found.
```
## 🔐 Cybersecurity Relevance

This tool plays a crucial role in:

- 🔍 Identifying attack surfaces (input parameters)
- 🧪 Supporting SQL Injection / XSS testing
- 🕵️ Assisting in bug bounty reconnaissance
- 📊 Understanding application data flow
  
## 📊 Use Cases

- Web Application Testing
- Penetration Testing Recon
- URL Analysis & Debugging
- Data Extraction for ML preprocessing

## 🌟 Highlights

- Beginner-friendly yet industry-relevant project
- No external dependencies required
- Clean and modular code structure
- Strong foundation for building advanced crawlers

## 🚧 Future Enhancements

- 🌍 Full website crawling (internal link discovery)
- 📁 Export results to JSON / CSV
- 🖥 GUI-based version
- 🔗 Support for POST request parameters
- 🧠 Parameter filtering & categorization
- ⚡ Multi-threaded crawling for performance

## 👩‍💻 Author

Harini R

B.E. Computer Science and Engineering (Cyber Security)

Saveetha Engineering College

## 📌 Project Details

- 🎓 Academic Mini Project
- 🏫 Saveetha Engineering College, Thandalam
- 🆔 Register Number: 212223100010


⭐ If you found this project useful, consider giving it a star!
