<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log Analysis Script - README</title>
</head>
<body>
    <h1>Log Analysis Script</h1>
    <p>This script is designed to analyze server logs and provide insights into request patterns, suspicious activities, and endpoint usage. The evaluation is based on IP requests, endpoint access frequencies, and failed login attempts.</p>

    <h2>Key Features</h2>
    <ul>
        <li>Analyzes log files to count requests per IP address.</li>
        <li>Identifies the most frequently accessed endpoint.</li>
        <li>Detects suspicious IP addresses based on repeated failed login attempts (HTTP 401).</li>
        <li>Exports results into a CSV file for easy reporting.</li>
    </ul>

    <h2>Setup and Prerequisites</h2>
    <p>Follow these steps to set up and run the script:</p>
    <ul>
        <li>Ensure <strong>Python 3.x</strong> is installed on your system.</li>
        <li>Place the log file in the same directory as the script and name it <code>sample.log</code>.</li>
        <li>Required Python libraries: <code>re</code>, <code>csv</code>, <code>collections</code> (all are standard libraries).</li>
    </ul>

    <h2>How to Run</h2>
    <ol>
        <li>Save the script as <code>log_analysis.py</code>.</li>
        <li>Run the script using the following command:
            <pre>python log_analysis.py</pre>
        </li>
        <li>The results will be displayed in the console and saved in <code>log_analysis_results.csv</code>.</li>
    </ol>

    <h2>Script Workflow</h2>
    <p>The script processes the log file in the following steps:</p>
    <ol>
        <li>Reads the log file line by line.</li>
        <li>Uses regular expressions to extract the IP address, endpoint, and status code from each log entry.</li>
        <li>Counts:
            <ul>
                <li>Total requests made by each IP address.</li>
                <li>Access frequencies of endpoints.</li>
                <li>Failed login attempts (status code 401).</li>
            </ul>
        </li>
        <li>Identifies the most accessed endpoint and suspicious IPs.</li>
        <li>Outputs results to both the console and a CSV file.</li>
    </ol>

    <h2>Results and Outputs</h2>
    <h3>Console Output</h3>
    <p>The script generates the following in the console:</p>
    <pre>
IP Address Request Counts:
192.168.1.1          120
10.0.0.1             80

Most Frequently Accessed Endpoint:
/home (Accessed 150 times)

Suspicious Activity Detected:
IP Address            Failed Login Attempts
192.168.1.100         12
    </pre>

    <h3>CSV File</h3>
    <p>The <code>log_analysis_results.csv</code> file contains:</p>
    <ul>
        <li>IP addresses and their request counts.</li>
        <li>The most accessed endpoint and its count.</li>
        <li>Suspicious IPs and their failed login attempts.</li>
    </ul>

    <h2>Customization</h2>
    <p>The script allows for easy customization:</p>
    <ul>
        <li><code>log_file</code>: Change the name of the log file to be analyzed.</li>
        <li><code>failed_threshold</code>: Adjust the threshold for detecting suspicious IPs.</li>
    </ul>

    <h2>Assessment Criteria</h2>
    <p>This script demonstrates:</p>
    <ul>
        <li>Ability to process and extract data from raw logs using Python.</li>
        <li>Proficiency in using Python libraries like <code>re</code>, <code>csv</code>, and <code>collections</code>.</li>
        <li>Attention to detail in identifying and reporting suspicious activities.</li>
    </ul>

    <h2>License</h2>
    <p>This project is submitted as part of an assessment and is for educational purposes only.</p>
</body>
</html>
