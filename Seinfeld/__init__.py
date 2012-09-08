# Copyright (c) 2012 John Reese
# Licensed under the MIT License

"""
Accesses a database of Seinfeld quotes.
"""

import supybot
import supybot.world as world

# Use this for the version of this plugin.  You may wish to put a CVS keyword
# in here if you're keeping the plugin in CVS or some similar system.
__version__ = ""

__author__ = supybot.Author("John Reese", "jreese", "john@noswap.com")

# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = {}

import config
import plugin
reload(plugin) # In case we're being reloaded.
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

if world.testing:
    import test

Class = plugin.Class
configure = config.configure


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
