# Gmail-cleaning-service-browser
                                 $$$ EXPERIMENTAL PROGRAM $$$
To succesfully use this program, you will have to abide by the steps given by the setup guide to the Gmail API
 - https://developers.google.com/gmail/api/quickstart/python

Retrieve your Credential json file, place into the folder, and enable the Gmail API in your google cloud project.

I will recommend using an environment. I use conda, and will show the steps for setting up the 
correct environment using conda :)

1 - First install conda:
    - [windows](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe) 
    - [Mac M1/M2](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg)  
2 - initialize conda.
   Open cmd as Admin and type
   ```
   conda init
   ```
   close that window
   open a new cmd window in your GmailClean dir (or navigate to the dir) and type
   ```
   conda create -n GmailClean python=3.8 -y
   conda activate GmailClean
   pip install -r requirements.txt
   ```
   If you have correctly placed the credentials.json file in the directory, then you should now be able to launch the site
   and clean up your Gmail inbox :)
