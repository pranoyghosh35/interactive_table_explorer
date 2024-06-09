import os
import pandas as pd

def load_data(uploaded_file, **kwargs):
    """
    Load data from the uploaded file based on its extension and additional options.
    
    Parameters:
        uploaded_file (file): The file uploaded by the user.
        **kwargs: Additional arguments passed to pandas read functions (pd.read_csv or pd.read_excel).
        
    Returns:
        dict or None: A dictionary with sheet/table names as keys and DataFrames as values, or None if an error occurs.
    """
    file_formats = {
        "csv": pd.read_csv,
        "xls": pd.read_excel,
        "xlsx": pd.read_excel,
        "xlsm": pd.read_excel,
        "xlsb": pd.read_excel,
    }
    
    try:
        # Extract file extension
        ext = os.path.splitext(uploaded_file.name)[1][1:].lower()
    except Error:
        # If uploaded_file does not have a 'name' attribute, handle it as a string
        ext = uploaded_file.split(".")[-1]
    
    tmp_name_df = {}
    
    # Check if the file extension is supported
    if ext in file_formats:
        try:
            if ext in {"xls", "xlsx", "xlsm", "xlsb"}:
                # Read all sheets in the Excel file
                excel_data = pd.read_excel(uploaded_file, sheet_name=None, **kwargs)
                # Store the dictionary of DataFrames
                tmp_name_df = excel_data
                return tmp_name_df
            else:
                # Read CSV file
                dataframe = file_formats[ext](uploaded_file, **kwargs)
                file_name = os.path.basename(uploaded_file.name)
                tmp_name_df[file_name] = dataframe
                return tmp_name_df
        except TypeError as e:
            # Handle errors caused by invalid keyword arguments
            print(f"Error: {e}")
            print("An unexpected keyword argument was passed. Please check the parameters and try again.")
            return None
        except Exception as e:
            # Handle other errors
            print(f"Error: {e}")
            return None
    else:
        # Handle unsupported file extensions
        print(f"Error: Unsupported file extension '{ext}'")
        return None
