#!/usr/bin/env python3
""" Module that contains schools_by_topic function. """

import pymongo


def schools_by_topic(mongo_collection, topic):
    """ Function that returns the list of school having a specific topic. """
    filtered_topics = {"topics": topic}
    return list(mongo_collection.find(filtered_topics))