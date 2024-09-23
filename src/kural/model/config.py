import yaml


class KuralConfig:
    def __init__(self, filepath):
        self.filepath = filepath
        self.conf = self.load_config()

    def load_config(self):
        with open(self.filepath, "r") as file:
            return yaml.safe_load(file)

    def get_database_config(self):
        return self.conf.get("database", {})

    def get_logging_config(self):
        return self.conf.get("logging", {})


# Uso do modelo
if __name__ == "__main__":
    config = KuralConfig("config/config.yaml")

    # Acessando as configurações
    db_config = config.get_database_config()
    log_config = config.get_logging_config()

    print("Database Configuration:")
    print(f"Host: {db_config.get('host')}")
    print(f"Port: {db_config.get('port')}")
    print(f"User: {db_config.get('user')}")

    print("\nLogging Configuration:")
    print(f"Level: {log_config.get('level')}")
    print(f"File: {log_config.get('file')}")
