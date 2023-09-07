# Import the Libraries
import yaml

# Funcion to load the config file
def load(filename, information):
    with open(filename, 'r') as file:
        config = yaml.safe_load(file)
        config = config[information] # Get the information
        return config

# Funcion to save the config file
def save(filename, dicionary, new_info):
    with open(filename, 'r') as file:
        config = yaml.safe_load(file)

        config[dicionary] = new_info # Add the new information

        with open(filename, 'w') as file:
            yaml.dump(config, file)

# to test the code
if __name__ == "__main__":
    print(load("system\config\config.yaml", "test"))
    save("system\config\config.yaml", "test", "test")
    print(load("system\config\config.yaml", "test"))


