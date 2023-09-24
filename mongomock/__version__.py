if (int(python_version[0]) == 3 and int(python_version[1]) >= 8) or int(python_version[0]) >= 4:
    from importlib.metadata import version
    __version__ = version('mongomock')
else:
    import pkg_resources
    __version__ = pkg_resources.get_distribution('mongomock').version
