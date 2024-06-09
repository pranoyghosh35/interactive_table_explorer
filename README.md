# Streamlit App for Interactive CSV Analysis and Query Application

We provide a Streamlit application that allows users to:

- upload a data file (CSV, Excel) and view it as a table (s).
- plot scatter (also line) plots  with choosen x and y-axis (axes) to visualize relations between any two features with respect to the target class.
- chat in natural language (english powered by OpenAI's GPT-3.5) on data analysis such as summarizing data, finding specific values, and performing basic statistical operations.

## Directory Structure

interactive_table_explorer/
│
├── backend/
│ ├── init.py
│ ├── doc_load.py
│ ├── plot_from_dataframe.py
│ └── ...
│
├── frontend/
│ ├── init.py
│ ├── app_st_ui.py
│ ├── file_handling.py
│ ├── display_table.py
│ └── ...
│
├── app.py
└── README.md


### File Descriptions

- **`backend/`**: Contains modules for backend functionalities.
    - **`doc_load.py`**: Contains functions for loading data files.
    - **`plot_from_dataframe.py`**: Contains functions for plotting from DataFrame.
    - Other backend modules...
    
- **`frontend/`**: Contains modules for frontend (Streamlit UI) functionalities.
    - **`app_st_ui.py`**: Contains functions for setting up the Streamlit UI.
    - **`file_handling.py`**: Contains functions for handling file uploads and data loading.
    - **`display_table.py`**: Contains functions for displaying data as a table.
    - Other frontend modules...

- **`app.py`**: The main script that brings everything together and runs the Streamlit app.

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

- [Uploading and viewing data file (CSV, Excel sheets)](https://drive.google.com/drive)
  
- [Enter your OpenAI API key in the sidebar. Interact with the data by typing queries in the chat input.](https://drive.google.com/drive)


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


