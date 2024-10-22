#!/usr/bin/env python3
""" Module that contains update_topics function. """

import pymongo


def update_topics(mongo_collection, name, topics):
    """ Function that changes
    all topics of a school document based on the name. """
    filtered_topics = {"name": name}
    updated_topics = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(filtered_topics, updated_topics)