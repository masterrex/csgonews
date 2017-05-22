"""
CSGo
"""

# 126 chars max per message
import os
from os.path import expanduser
import feedparser # https://pythonhosted.org/feedparser/introduction.html

CONFIG_PATH = os.path.join(expanduser("~"),
                            ".steam/steam/userdata/11713211/730/local/cfg/")


class CSGONewsConfig(object):
    """
    Simple Object representing a config to sync with subreddit
    """
    def __init__(self, subreddit):
        self.subreddit = subreddit
        self.keybinds = [
            "kp_slash", "kp_multiply", "kp_minus",
            "kp_home", "kp_uparrow", "kp_pgup", "kp_plus",
            "kp_leftarrow", "kp_5", "kp_rightarrow",
            "kp_end", "kp_downarrow", "kp_pgdn", "kp_enter",
            "kp_ins", "kp_del"]
        self.feed = None
    def write_cfg(self):
        """
        Write config to filesystem
        """
        cfg_file = os.path.join(CONFIG_PATH, self.subreddit + '.cfg')
        with open(cfg_file, 'w') as cfg:
            for i in range(0, len(self.keybinds)):
                cfg.write('\nunbind "{0}"\nbind "{0}" "say #{1}: {2}"'.format(
                    self.keybinds[i],
                    i,
                    self.feed['entries'][i]['title'].encode('utf-8')))
    def get_rss_feed(self):
        """
        Returns rss feed data as a dict
        """
        reddit_rss_feed = 'http://reddit.com/r/%s.rss' % self.subreddit
        self.feed = feedparser.parse(reddit_rss_feed)

CONFIGS = [
    CSGONewsConfig('the_donald'),
    CSGONewsConfig('hillaryforprison'),
    CSGONewsConfig('sorosforprison')]

for c in CONFIGS:
    c.get_rss_feed()
    c.write_cfg()
