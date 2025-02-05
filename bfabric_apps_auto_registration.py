from bfabric import Bfabric

def get_user_input():
    """Prompt user for necessary inputs."""
    system = input("In which system do you want to create the app? Input TEST for the test system and PROD for the production system: ").strip().upper()
    if system not in ["TEST", "PROD"]:
        raise ValueError("Invalid system input. Please input either TEST or PROD.")

    name = input("Enter app name: ")
    weburl = input("Enter web URL: ")
    technologyid = input("Enter technology ID: ")
    description = input("Enter description: ")

    return {
        "system": system,
        "name": name,
        "weburl": weburl,
        "type": "WebApp",
        "technologyid": technologyid,
        "supervisorid": "2446",
        "enabled": True,
        "valid": True,
        "hidden": False,
        "description": description
    }

def create_app_in_bfabric():
    """Create an app in B-Fabric using user inputs."""
    # Get user input for parameters
    user_input = get_user_input()

    # Determine configuration environment based on user input
    config_env = user_input.pop("system")

    # Initialize Bfabric instance
    bfabric = Bfabric.from_config(config_env=config_env)

    # Set endpoint for app creation
    endpoint = "application"

    # Make API call to save the app
    try:
        result = bfabric.save(endpoint=endpoint, obj=user_input)
        print("App created successfully:", result)
    except Exception as e:
        print("Failed to create app:", str(e))

if __name__ == "__main__":
    create_app_in_bfabric()
