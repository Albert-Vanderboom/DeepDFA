import json
import csv
import os
import sys

# csv format:

# Unnamed: 0
# Access Gained	
# Attack Origin	
# Authentication Required	
# Availability	
# CVE ID	
# CVE Page	
# CWE ID	
# Complexity	
# Confidentiality	
# Integrity	
# Known Exploits	
# Publish Date
# Score	
# Summary	
# Update Date	
# Vulnerability Classification	
# add_lines	
# codeLink	
# commit_id	
# commit_message	
# del_lines	
# file_name	
# files_changed	
# func_after	
# func_before	
# lang	
# lines_after	
# lines_before	
# parentID	
# patch	
# project	
# project_after	
# project_before	
# vul	
# vul_func_with_fix

import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        headers = ["Unnamed: 0", 
                   "CVE ID", 
                   "add_lines", 
                   "del_lines", 
                   "func_after", 
                   "func_before", 
                   "patch",
                   "vul"]
        writer.writerow(headers)

        for i, item in enumerate(data):
            add_lines = len(item["function_modified_lines"]["added"])
            del_lines = len(item["function_modified_lines"]["deleted"])
            func_after = item["code_after_change"]
            func_before = item["code_before_change"]
            patch = item["patch"]
            cve_id = item.get("cve_id", "")
            # vul is 0 if no lines are added or deleted.
            vul = 1 if(add_lines == 0 and del_lines == 0) else 0
            writer.writerow([i, cve_id, add_lines, del_lines, func_after, func_before, 
                             patch, vul])


json_path = "/home/fdse/dwt/LLM4Detection/data/clean_data/test_data_clean.json"
csv_path = "/home/fdse/dwt/DeepDFA/data_conversion/test_data_clean.csv"
json_to_csv(json_path, csv_path)