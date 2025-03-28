"""
LeetCode Problem: Design Twitter
Problem Number: 355
Difficulty: Medium
Topic: Heap Priority Queue
Link: https://leetcode.com/problems/design-twitter/
"""

from heapq import *
from collections import defaultdict

# Tweet Heap, Timestamp and Follow Map
# Space Complexity: O(u * t + u^2)
# TIME LIMIT EXCEEDED
class Twitter:

    # Initialize the object
    def __init__(self):
        self.timestamp = 0
        self.tweets = []
        self.follows = defaultdict(set)

    # Post a new tweet
    # Time Complexity: O(log t)
    def postTweet(self, userId, tweetId):
        heappush(self.tweets, (self.timestamp, userId, tweetId))
        self.timestamp -= 1

    # Get news feed
    # Time Complexity: O(t log t)
    def getNewsFeed(self, userId):
        feed = []
        temp = []
        while self.tweets and len(feed) < 10:
            tweet = heappop(self.tweets)
            if tweet[1] in self.follows[userId] or tweet[1] == userId:
                feed.append(tweet[2])
            temp.append(tweet)
        while temp:
            heappush(self.tweets, temp.pop())
        return feed

    # Add a new follower
    # Time Complexity: O(1)
    def follow(self, followerId, followeeId):
        self.follows[followerId].add(followeeId)

    # Remove a follower
    # Time Complexity: O(1)
    def unfollow(self, followerId, followeeId):
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# User Tweet Map, Timestamp and Follow Map
# Space Complexity: O(u * t + u^2)
class Twitter:

    # Initialize the object
    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    # Post a new tweet
    # Time Complexity: O(1)
    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    # Get news feed
    # Time Complexity: O(u log u)
    def getNewsFeed(self, userId):
        feed = []
        heap = []

        self.follows[userId].add(userId)
        for uid in self.follows[userId]:
            if uid in self.tweets:
                idx = len(self.tweets[uid]) - 1
                timestamp, tid = self.tweets[uid][idx]
                heappush(heap, (timestamp, tid, uid, idx - 1))

        while heap and len(feed) < 10:
            timestamp, tid, uid, idx = heappop(heap)
            feed.append(tid)
            if idx >= 0:
                timestamp, tid = self.tweets[uid][idx]
                heappush(heap, (timestamp, tid, uid, idx - 1))

        return feed

    # Add a new follower
    # Time Complexity: O(1)
    def follow(self, followerId, followeeId):
        self.follows[followerId].add(followeeId)

    # Remove a follower
    # Time Complexity: O(1)
    def unfollow(self, followerId, followeeId):
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
