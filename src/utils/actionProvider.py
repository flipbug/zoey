from utils.pluginMount import PluginMount

class ActionProvider:
    """
    Mount point for plugins which refer to actions that can be performed.

    Plugins implementing this reference should provide the following attributes:

    ================    =======================================================
    name                The name of the plugin

    commandPatterns     A Dictonary which contains a regex pattern for each
                        Keyword.
    ================    ======================================================
    """
    __metaclass__ = PluginMount
