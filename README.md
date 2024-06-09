# Streamlit App for Interactive CSV Analysis and Query Application

We provide a Streamlit application that allows users to:

- upload a data file (CSV, Excel) and view it as a table (s).
- plot scatter (also line) plots  with choosen x and y-axis (axes) to visualize relations between any two features with respect to the target class.
- chat in natural language (english powered by OpenAI's GPT-3.5) on data analysis such as summarizing data, finding specific values, and performing basic statistical operations.

## Directory Structure

interactive_table_explorer/
├── backend/
│   ├── chat.py
│   ├── doc_load.py
│   ├── __init__.py
│   └── util.py
├── frontend/
│   ├── app_st_ui.py
│   └── __init__.py
├── app.py
└── README.md

### Module Descriptions

#### `doc_load.py`

This module provides functions to load data from uploaded files. It supports various file formats including CSV, Excel, and others.

#### `chat.py`

This module sets up a chat interface for data analysis, utilizing OpenAI's language model. Users can interact with the system to summarize data, perform statistical operations, and more.

#### `util.py`

This module contains utility functions for displaying data frames and creating interactive Plotly plots. It provides functions to visualize DataFrame head, tail, or a random sample, as well as to create scatter plots.

#### `app_st_ui.py`

This module sets up the Streamlit UI components for the application. It includes functions to display information about the app and handle user interactions.

#### `app.py`

The main script that integrates backend and frontend functionalities and runs the Streamlit app. It orchestrates the interaction between different modules to provide a seamless user experience.


## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/my_streamlit_app.git
    cd my_streamlit_app
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
    
Or build docker image and run it.

- docker build -t my_app .
- docker run -p 8501:8501 my_app

### Running the App

Please execute below to open the Streamlit app in browser:
```sh
streamlit run app.py
```

## How to Use

- [Example CSV and Excel Files to try out](https://drive.google.com/drive/folders/1x76K-6e06ZSg925vCQ53twlXM0k62Lhy?usp=sharing)

- [Uploading and viewing data file (CSV, Excel sheets)](https://youtu.be/9zxvtiKP59E)

- [Making scatter plots from selected table](https://youtu.be/3xsAyI-vRTI)
  
- [Interact with the data by typing queries in the chat input.](https://youtu.be/2Ywb_1L0ZKY)

Rest assured we have prevented the bot from hallucinating by providing the data and features itself and instructued it to shy away from answering unrelated questions by appropriate system prompt. Please check "basic_instructions" inside setup_chat function of "chat" module.



## Contributions and Feedback

- Looking forward to receive feedback on **pranoy.ghosh.tlp23@plaksha.edu.in**.
- Contributions are welcome! Please submit a pull request for any improvements or bug fixes.

### Good development practises

We pledge to adhere to several aspects as mapped below:

- SOLID:

Single Responsibility Principle (SRP): Each module or class in the backend and frontend directories has a single responsibility, such as loading data files, plotting from DataFrame, or setting up the Streamlit UI.

Open/Closed Principle (OCP): Our project structure allows for enabling the addition of new functionalities or modules without needing to modify existing code.

Interface Segregation Principle (ISP): Each module or class contains only the methods and attributes necessary for its specific responsibility.

Dependency Inversion Principle (DIP): Higher-level modules depend on abstractions rather than concrete implementations. For example, "app" depends on the interfaces provided by modules in backend and frontend, rather than directly depending on their implementations.

- PEP8:

Code Readability through consistent indentation (4 spaces) and spacing.

Naming Conventions for variables, functions, and modules ("lowercase_with_underscores").

Import statements are organized and grouped.

Descriptive comments provide context and explanation for complex parts of the code where necessary.

Functions and modules include docstrings.

**Try executing :**
```
autopep8 --in-place --recursive --aggressive --max-line-length=79 .
```
in CLI to reformat all Python files in the current directory and its subdirectories after modifications.

### MIT License
You are free to **"use, modify, distribute, sublicense, and/or sell copies of the software"** but please include **original copyright/permission notice everywhere**.See the LICENSE file for details.


