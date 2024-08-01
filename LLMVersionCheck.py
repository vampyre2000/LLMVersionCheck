import requests
import datetime
import pyttsx3
from bs4 import BeautifulSoup

#Set the list of software versions that we want to check for
Software_versions={"LlamaCPP"  :"https://github.com/ggerganov/llama.cpp/releases/latest",
                "Koboldcpp"    :"https://github.com/LostRuins/koboldcpp/releases/latest",
                "KoboldcppROCM":"https://github.com/YellowRoseCx/koboldcpp-rocm/releases/latest",
                "Ollama"       :"https://github.com/ollama/ollama/releases/latest",
                "SillyTavern_M":"https://github.com/SillyTavern/SillyTavern/releases/latest",
                "GPT4All"      :"https://github.com/nomic-ai/gpt4all/releases/latest",
                "Fabric"       :"https://github.com/danielmiessler/fabric/releases"}
#Set the date to when we believe that the singularity will happen.
Singularity_date = datetime.date(2030,9,30)

# Get today's date and time using the datetime.date() function
today = datetime.date.today()
# Print the formatted date in "YYYY-MM-DD" format

# Send an HTTP GET request to retrieve the HTML content
def check_version(PROGRAM,URL): 
    response = requests.get(URL)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        # Locate the element containing the Kobol.cpp version information (e.g., a <span> or <p> tag)
        version_element = soup.find("title")  # Adjust the selector based on the website's HTML structure
        date_element    = soup.find("relative-time")
        Version_f       = soup.find("relative-time")
        # Extract the version number from the element's text content
        version = version_element.text
        version_p= version.find("·")
        #version = version_element.text.strip()
        date    = date_element.text.strip()
        print(f"Release Date {date}:{PROGRAM}:{version[0:version_p]}")
        #engine.say(f"Release Date {date}:{PROGRAM}:{version[0:version_p]}")
        #engine.runAndWait()
    else:
        print(f"Failed to fetch the webpage for {PROGRAM}")

days_until_singularity=(Singularity_date - today)
print("Today's date is the " + today.strftime("%Y-%m-%d"))
print(f"Days until the singularity {days_until_singularity}")
for key in Software_versions:
   check_version(key,Software_versions[key])    
