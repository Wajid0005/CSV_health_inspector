import pandas as pd

def load_data(file_path):

    filename = file_path.filename.lower()
    try:
        if filename.endswith(".csv"): 
            return pd.read_csv(file_path.file) 
        elif filename.endswith(".xlsx"): 
            return pd.read_excel(file_path.file) 
        else: 
            raise ValueError("Unsupported file format")
        
    except FileNotFoundError:
        print("File not Found")
    except pd.errors.EmptyDataError:
        print("CSV file is empty")
    except Exception as e:
        print(f"Error: {e}")
