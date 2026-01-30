# __init_subclass__ Examples

class PluginBase:
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)
        cls.name = kwargs.get('name', cls.__name__)

class MyPlugin(PluginBase, name='CustomPlugin'):
    pass

print(PluginBase.plugins)  # [<class '__main__.MyPlugin'>]
print(MyPlugin.name)       # CustomPlugin