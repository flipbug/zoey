from utils.pluginMount import PluginMount

class PluginProvider:
    """
    Mount point for plugins which refer to commands that can be performed.

    Plugins implementing this reference should provide the following attributes:

    ================    =======================================================
    name                The name of the plugin

    commandPatterns     A Dictonary which contains a regex pattern for each
                        keyword.
    ================    ======================================================
    """
    __metaclass__ = PluginMount
