from dotenv import load_dotenv



def load_environment():
    """
    Load the environment variables from a .env file into the current process.

    This function does nothing if a .env file does not exist. If a .env file does
    exist, it is loaded into the current process using the dotenv library.
    """
    
    load_dotenv(".env")