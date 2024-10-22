#!/usr/bin/env python3
""" Module that contains list_all function. """

import pymongo


def list_all(mongo_collection):
    """ Function that lists all documents in a collection. """
    documents = list(mongo_collection.find())
    return documents