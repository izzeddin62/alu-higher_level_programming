#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        prev_item = {"high_score": 0, "owner": ""}
        for (key, value) in a_dictionary.items():
            if value > prev_item.get("high_score"):
                prev_item["high_score"] = value
                prev_item["owner"] = key
        if prev_item["high_score"] == 0:
            return None
        else:
            return prev_item["owner"]
