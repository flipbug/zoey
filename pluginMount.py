class PluginMount(type):
    def __init__(cls, name, bases, attr):
        if not hasattr(cls, 'plugins'):
            cls.plugins = []
        else:
            cls.plugins.append(cls)

    def getPlugins(cls, *args, **kwargs):
        return [p(*args, **kwargs) for p in cls.plugins]
