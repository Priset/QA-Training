from browser_factory import DriverFactory

class DriverSingleton:
    _instance = None

    @classmethod
    def get_instance(cls, browser_name="chrome"):
        if cls._instance is None:
            cls._instance = DriverFactory.get_driver(browser_name)
        return cls._instance

    @classmethod
    def close_driver(cls):
        if cls._instance:
            cls._instance.quit()
            cls._instance = None
