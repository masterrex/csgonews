import feedparser # https://pythonhosted.org/feedparser/introduction.html

# 126 chars max per message
import os
from os.path import expanduser

CONFIG_PATH = os.path.join(expanduser("~"), ".steam/steam/userdata/11713211/730/local/cfg/")


class CSGONewsConfig(object):
    def __init__(self, subreddit):
        self.subreddit = subreddit
        self.keybinds  =  [
            "kp_slash",  "kp_multiply", "kp_minus",
            "kp_home", "kp_uparrow", "kp_pgup", "kp_plus",
            "kp_leftarrow", "kp_5", "kp_rightarrow",
            "kp_end", "kp_downarrow", "kp_pgdn", "kp_enter",
            "kp_ins", "kp_del"

        ]
    def write_cfg(self):
        with open(os.path.join(CONFIG_PATH, config.subreddit + '.cfg'), 'w') as cfg:
            for i in range(0, len(self.keybinds)):
                cfg.write('\nunbind "{0}"\nbind "{0}" "say #{1}: {2}"'.format(self.keybinds[i], i, self.feed['entries'][i]['title'].encode('utf-8')))
    def get_rss_feed(self):
        self.feed = feedparser.parse('http://reddit.com/r/%s.rss' % self.subreddit)

configs = [ CSGONewsConfig('the_donald'), CSGONewsConfig('hillaryforprison'), CSGONewsConfig('sorosforprison') ]

for config in configs:
    config.get_rss_feed()
    config.write_cfg()
