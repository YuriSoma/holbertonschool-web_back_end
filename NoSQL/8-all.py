#!/usr/bin/env python3
""" List documents in python  """
import pymongo


def list_all(mongo_collection) -> list:
    """ Receives a mongo connection,return document list """
    documents: list = []

    for document in mongo_collection.find():
        documents.append(document)

    return documents
