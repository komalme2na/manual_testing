"""
plm_validate.py

Validation script for Page Language Model JSON files.

Author: Komal Meena  
Role: Manual Tester Intern  
Date: April 2025  
Purpose: Validate structure and keys in PLM JSON files as part of QA test validation.
"""

import json
import sys
import os

def log(msg, status="INFO"):
    tag = f"[{status.upper()}]"
    print(f"{tag} {msg}")

def validate_component(component, errors, path="root"):
    if not isinstance(component, dict):
        errors.append(f"{path}: Component is not a dictionary")
        return

    required_keys = ["id", "type"]
    for key in required_keys:
        if key not in component:
            errors.append(f"{path}: Missing required key '{key}'")
        else:
            log(f"Key '{key}' is present in {path}", "PASS")

    if "children" in component:
        if not isinstance(component["children"], list):
            errors.append(f"{path}: 'children' should be a list")
        else:
            for i, child in enumerate(component["children"]):
                validate_component(child, errors, f"{path}.children[{i}]")

def validate_file(file_path):
    log(f"Validating file: {file_path}")

    if not os.path.isfile(file_path):
        log("File does not exist.", "FAIL")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            log(f"JSON Decode Error: {e}", "FAIL")
            return

    errors = []
    validate_component(data, errors)

    if errors:
        log("Validation completed with errors:", "FAIL")
        for error in errors:
            log(error, "FAIL")
    else:
        log("Validation successful. No issues found.", "PASS")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        log("Usage: python plm_validate.py <path_to_json_file>", "INFO")
    else:
        validate_file(sys.argv[1])
