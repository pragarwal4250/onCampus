# onCampus Automation

This repository contains a Python script to automate certain tasks on the On-Campus jobs website at ASU. It simplifies the process of applying for jobs by automating the following steps:

1. **Login to Your On-Campus Jobs Account**: The script uses your ASU username and password stored in a `data.json` file to log in to your account.

2. **Resume and Cover Letter**: You should have your resume and cover letter saved on the On-Campus jobs website. Ensure they are the only Resume(s) and Cover Letter(s) uploaded to your profile. The script assumes these documents are already available.

3. **Complete Your Profile**: The script automates the process of completing your profile by filling out other fields such as gender, race, references, and any other required information.

## Prerequisites

Before you can use this script, make sure you have the following installed:

- Python 3.x
- Selenium: You can install it using `pip install selenium`.
- A compatible web driver for your browser (e.g., ChromeDriver for Google Chrome). https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/

## Usage

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/yourusername/onCampus-automation.git
   ```

2. Navigate to the project directory:

   ```
   cd onCampus-automation
   ```

3. Create a `data.json` file with your ASU username, password, names of resume and cover letter you want to use from the ones which are saved on the job portal:

   ```json
   {
       "username": "your_username",
       "password": "your_password",
       "resume": "resume file name including extension",
       "coverLetter": "cover letter filename inclusing extension",
       "pages": "number of pages",
       "campus": "campus name"
   }
   ```

4. Run ChromeDriver.

5. Run the script:

   ```
   python main.py
   ```

6. The script will automate the login, profile completion, and application process for you.

## Notes

- This script is provided as a starting point and may require customization to work with your specific university's website.
- Ensure that you have the necessary permissions and rights to automate tasks on the On-Campus jobs website.

Feel free to customize and enhance the script as needed for your specific use case. If you encounter any issues or have questions, please don't hesitate to reach out for assistance.

Happy job hunting!
