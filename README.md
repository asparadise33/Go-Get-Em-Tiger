# Go-Get-Em-Tiger
BE Capstone Project
![image](https://github.com/user-attachments/assets/bd12d154-ec59-487e-83c0-4de7aa1b171d)


# Who the app is for:
As a User who loves tracking their habits, creating new goals, and seeing how far they’ve come or motivation to keep going. This is the application for you. User’s can create custom Habits, Titles, Frequencies, Categories.

# API Docs:
https://documenter.getpostman.com/view/33499624/2sAYk7RiYg

# Tech/Frameworks used, planning materials:
Python and Django
ERD:
https://dbdiagram.io/d/BE-Capstone-67b51f40263d6cf9a0a33704
Data Flowchart:
https://mermaid.live/edit#pako:eNpNj8FqwzAMhl_F6NzQexiDNm7ZYaduvczOQY2VxBDbRbEpo_Td6yYpRCf93_-B0B2aYAhKaIdwa3rkKH6l9iLPTp1H4loUxafYq-_QWV8vzcQqdaLOjjE7M95PWCqJY38JyGbh1cznIMVHUVRMGOlFD-oLLzaKY2BXr4zz1byNFT0Rmq2kgVYVbMARO7Qmf3F_EQ2xJ0cayrwaajENUYP2j6xiiuHn3zdQRk60AQ6p66FscRhzStNVabFjdG_liv4vBLdIjye1bF1H


# Project Setup Instructions for first-time installation

Follow these steps to set up and run the project:

1. Install the required packages using Pipenv:
    ```sh
    pipenv install
    ```

2. Activate the virtual environment:
    ```sh
    pipenv shell
    ```

3. Create the database migrations:
    ```sh
    python manage.py makemigrations
    ```

4. Apply the migrations to the database:
    ```sh
    python manage.py migrate
    ```

5. Start the development server:
    ```sh
    python manage.py runserver
    ```


## HOW TO START THE SERVER FOR FRONT-END
1. Open Terminal:
    ```sh
    pipenv shell
    ```

2. Start Python Interpreter:
    ```sh
    CTRL + Shift + P and click Python: Select Interpreter
    ```    

3. Select the correct Python Interpreter:
    ```sh
    Python (version)(`file_name_server_randomString`:Pipenv) ~.\virtualenvs\sec...
    ```  

4. Open Terminal to Start Server:
    ```sh
    python manage.py runserver
    ```      

5. Verify server is running by clicking to open web page to see data:
    ```sh
    Starting development server at http://127.0.0.1:8000/
    ```
 


## TO LOAD FIXTURES
1. Create the database migrations:
    ```sh
    python manage.py makemigrations
    ```


# Loom Video of Postman Calls:
https://www.loom.com/share/4fcabfb131ed46c4afb2e05558188abf
