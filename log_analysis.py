import re
import csv
from collections import defaultdict, Counter


log_file = "sample.log"
output_csv = "log_analysis_results.csv"

ip_request_counts = defaultdict(int)
endpoint_counts = Counter()
failed_login_attempts = defaultdict(int)
failed_threshold = 10 


with open(log_file, "r") as file:
    for line in file:
        match = re.match(r'(\d+\.\d+\.\d+\.\d+) .* "(?:GET|POST) (.+?) HTTP/.*" (\d+)', line)
        if match:
            ip, endpoint, status_code = match.groups()
            ip_request_counts[ip] += 1
            endpoint_counts[endpoint] += 1
            if status_code == "401":
                failed_login_attempts[ip] += 1


sorted_ip_requests = sorted(ip_request_counts.items(), key=lambda x: x[1], reverse=True)

most_accessed_endpoint, max_count = endpoint_counts.most_common(1)[0]


suspicious_ips = {ip: count for ip, count in failed_login_attempts.items() if count > failed_threshold}


print("\nIP Address Request Counts:")
print(f"{'IP Address':<20} {'Request Count':<10}")
for ip, count in sorted_ip_requests:
    print(f"{ip:<20} {count:<10}")

print("\nMost Frequently Accessed Endpoint:")
print(f"{most_accessed_endpoint} (Accessed {max_count} times)")

print("\nSuspicious Activity Detected:")
print(f"{'IP Address':<20} {'Failed Login Attempts':<10}")
for ip, count in suspicious_ips.items():
    print(f"{ip:<20} {count:<10}")


with open(output_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(["IP Address", "Request Count"])
    writer.writerows(sorted_ip_requests)

    
    writer.writerow([])
    writer.writerow(["Most Accessed Endpoint", "Access Count"])
    writer.writerow([most_accessed_endpoint, max_count])

    
    writer.writerow([])
    writer.writerow(["Suspicious IP Address", "Failed Login Attempts"])
    writer.writerows(suspicious_ips.items())

print(f"\nResults saved to {output_csv}")
