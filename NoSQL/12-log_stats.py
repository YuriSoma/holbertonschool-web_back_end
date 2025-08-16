#!/usr/bin/env python3
"""
12-log_stats.py
Provides stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def _count(col, filt=None):
    """Compatibility helper: prefer count_documents, fall back to find().count()."""
    if filt is None:
        filt = {}
    # Newer/recommended (PyMongo >= 3.7)
    if hasattr(col, "count_documents"):
        return col.count_documents(filt)
    # Older fallback
    return col.find(filt).count()


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # total logs
    total = _count(collection, {})
    print("{} logs".format(total))

    # methods
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        cnt = _count(collection, {"method": method})
        print("\tmethod {}: {}".format(method, cnt))

    # status check: method=GET, path=/status
    status_cnt = _count(collection, {"method": "GET", "path": "/status"})
    print("{} status check".format(status_cnt))
