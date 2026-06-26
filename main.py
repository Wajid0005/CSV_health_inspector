from fastapi import FastAPI, UploadFile, File
from loader import load_data
from analyzer import CSVInspector
app = FastAPI()

@app.get("/")
def home():

    return {"message": "CSV Health Inspector API Running."}

@app.post("/analyze")

async def analyze_file(file: UploadFile = File(...)):

    data = load_data(file)

    inspector = CSVInspector(data)
    
    
    
    return  {
        "filename": file.filename,
        "shape": inspector.check_shape(),
        "missing": inspector.check_missing(), 
        "duplicates": inspector.check_duplicates(),
        "dtypes": inspector.check_dtypes(), 
        "suspicious": inspector.check_suspicious_values()
    }