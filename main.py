from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import pandas as pd
from datetime import datetime
import logic_service

app = FastAPI()

@app.post("/problem-report")
async def problem_report(request: Request):
    data = await request.json()

    response = logic_service.calculate_response(data)

    df = pd.DataFrame(columns = ['input', 'time', 'response_status'])
    row = {'input' : data, 'time' : datetime.now(), 'response_status' : response}
    df = df.append(row, ignore_index=True)
    df.to_csv('data_table.csv', index=False)

    return response
    
                        

    


    
