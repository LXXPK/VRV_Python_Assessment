# Log Analysis Script

## Overview
This script processes web server log files to extract:
- IP request counts.
- Most frequently accessed endpoints.
- Suspicious activity based on failed login attempts.

Results are displayed in the terminal and saved to a CSV file.

---

## Features
1. Counts requests per IP.
2. Identifies the most accessed endpoint.
3. Flags IPs with excessive failed login attempts (`401` errors).

---

## Usage

### Prerequisites
- Python 3.6 or higher.
- Required modules: `re`, `csv`, `collections`.

### Steps to Run
1. Clone the repository and ensure the script and the log file (`sample.log`) are in the same directory.
2. Install Python if not already installed. Use the following command to verify:
   ```bash
   python --version
3. Run the script using:
   ```bash
   python log_analysis.py
4. The results will:
   -Be displayed in the terminal.
   -Be saved to log_analysis_results.csv in the same directory.

##Output
#Terminal Output:

1. IP Request Counts: Shows how many requests were made by each IP.
   -*Most Accessed Endpoint*: Displays the endpoint with the highest access count.
   -*Suspicious Activity*: Lists IPs with failed login attempts exceeding the threshold.
   -CSV File (log_analysis_results.csv):

2. Contains:
   -IP request counts.
   -The most accessed endpoint with its access count.
   -Suspicious IPs with their failed login attempts.

##Configuration
You can customize the following variables in the script:

*log_file*: The name of the log file (default: sample.log).
*failed_threshold*: The number of failed login attempts to consider suspicious (default: 10).

