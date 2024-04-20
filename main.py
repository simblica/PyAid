import os
import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ansi escape codes for colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

def install_pip():
    try:
        print(GREEN + "Installing or upgrading pip..." + RESET)
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    except Exception as e:
        logger.error("Failed to install or upgrade pip: %s", e)

def download_essential_modules():
    try:
        print(GREEN + "Downloading essential modules..." + RESET)
        os.system("pip install numpy pandas matplotlib scikit-learn requests beautifulsoup4 tensorflow pytorch flask django")
        logger.info("Essential modules downloaded successfully.")
    except Exception as e:
        logger.error("Failed to download essential modules: %s", e)

def download_discord_modules():
    try:
        print(GREEN + "Downloading discord modules..." + RESET)
        version_choice = input(CYAN + "What version of discord.py would you like to download?\n[1] discord.py (latest version)\n[2] discord.py 1.7.3 (selfbots)\n[3] discord.py-self (selfbots)\n[4] discum (selfbots)\n" + RESET)
        if version_choice == '1':
            os.system("pip install discord.py asyncio aiohttp dotenv")
        elif version_choice == '2':
            os.system("pip install discord.py==1.7.3 asyncio aiohttp dotenv")
        elif version_choice == '3':
            os.system("pip install discord.py-self asyncio aiohttp dotenv")
        elif version_choice == '4':
            os.system("pip install discum asyncio aiohttp dotenv")
        logger.info("Discord modules downloaded successfully.")
    except Exception as e:
        logger.error("Failed to download discord modules: %s", e)

def download_nlp_modules():
    try:
        print(GREEN + "Downloading Natural Language Processing (NLP) modules..." + RESET)
        os.system("pip install nltk spacy gensim")
        logger.info("NLP modules downloaded successfully.")
    except Exception as e:
        logger.error("Failed to download NLP modules: %s", e)

def download_web_scraping_modules():
    try:
        print(GREEN + "Downloading Web scraping modules..." + RESET)
        os.system("pip install beautifulsoup4 requests lxml scrapy")
        logger.info("Web scraping modules downloaded successfully.")
    except Exception as e:
        logger.error("Failed to download web scraping modules: %s", e)

def download_ml_ai_modules():
    try:
        print(GREEN + "Downloading machine learning and AI modules..." + RESET)
        os.system("pip install scikit-learn tensorflow keras torch")
        logger.info("ML/AI modules downloaded successfully.")
    except Exception as e:
        logger.error("Failed to download ML/AI modules: %s", e)

def download_data_analysis_modules():
    try:
        print(GREEN + "Downloading data analysis modules..." + RESET)
        os.system("pip install pandas numpy scipy matplotlib seaborn")
        logger.info("Data analysis modules downloaded successfully.")
    except Exception as e:
        logger.error("Failed to download data analysis modules: %s", e)

def download_gui_modules():
    try:
        print(GREEN + "Downloading GUI development modules..." + RESET)
        os.system("pip install tk")
        logger.info("GUI development modules downloaded successfully.")
    except Exception as e:
        logger.error("Failed to download GUI development modules: %s", e)

def print_module_options():
    """Print module options."""
    print("""
[1] Essential modules
[2] Discord modules
[3] Natural Language Processing (NLP) modules
[4] Web scraping modules
[5] Machine learning and AI modules
[6] Data analysis modules
[7] GUI development modules
[8] All modules
""")

def provide_learning_guidance():
    print("Well hello there! Here are some good sources to learn Python and how it works:\n")
    print("-> " + GREEN + "https://docs.python.org/" + RESET + " (the official documentation of Python)")
    print("-> " + GREEN + "https://youtu.be/XKHEtdqhLK8?si=9pe8mWr-UdTZAZ3T" + RESET + " (a long tutorial that will turn you from a noob to a pro at coding)")
    print("-> " + GREEN + "https://stackoverflow.com/questions/tagged/python" + RESET + " (got any problems coding and can't fix it? Stack Overflow could help you out with it)")

def main():
    """Main function."""
    print("""
██████╗░██╗░░░██╗░█████╗░██╗██████╗░
██╔══██╗╚██╗░██╔╝██╔══██╗██║██╔══██╗
██████╔╝░╚████╔╝░███████║██║██║░░██║
██╔═══╝░░░╚██╔╝░░██╔══██║██║██║░░██║
██║░░░░░░░░██║░░░██║░░██║██║██████╔╝
╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░

  Empowering Python enthusiasts with assistance and guidance
  
  Made by Simbolica
""")

    # Install or upgrade pip if required
    response = input(CYAN + "Would you like to download or upgrade pip (required for installation of modules)? (y/n): " + RESET).lower()
    if response == 'y':
        install_pip()
    else:
        logger.info("Continuing without installing or upgrading pip.")

    guidance_response = input(CYAN + "Would you like some guidance on learning to code in Python? (y/n): " + RESET).lower()
    if guidance_response == 'y':
        provide_learning_guidance()
    else:
        print("No problem! Let's move on.")

    print_module_options()
    module_type = input(CYAN + "Enter the number corresponding to the type of modules you would like to download: " + RESET)
    if module_type == '1':
        download_essential_modules()
    elif module_type == '2':
        download_discord_modules()
    elif module_type == '3':
        download_nlp_modules()
    elif module_type == '4':
        download_web_scraping_modules()
    elif module_type == '5':
        download_ml_ai_modules()
    elif module_type == '6':
        download_data_analysis_modules()
    elif module_type == '7':
        download_gui_modules()
    elif module_type == '8':
        download_all_modules()
# made by simbolica fr
if __name__ == "__main__":
    main()

input("Press Enter to exit...")  
