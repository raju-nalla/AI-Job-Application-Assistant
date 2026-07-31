from config.config_loader import ConfigLoader

config = ConfigLoader()

print(config.get("app.name"))
print(config.get("app.version"))

print(config.get("database.path"))

print(config.get("paths.prompts"))

print(config.get("ai.provider"))
print(config.get("ai.model"))

print(config.get("logging.level"))