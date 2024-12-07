# Log Analysis Script

## Overview
This script processes web server log files to extract:
- IP request counts.
- Most frequently accessed endpoints.
- Suspicious activity based on failed login attempts.

Results are displayed in the terminal and saved to a CSV file.



## Features
1. Counts requests per IP.
2. Identifies the most accessed endpoint.
3. Flags IPs with excessive failed login attempts (`401` errors).



## Usage

### Prerequisites
- Python 3.6 or higher.
- Required modules: `re`, `csv`, `collections`.

### Steps to Run
1. Clone the repository and place your log file (`sample.log`) in the directory.
2. Run the script:
   python log_analysis.py
