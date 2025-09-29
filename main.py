from fastapi import FastAPI
from scanner import scan_breakouts
from alerts import send_alerts
from scheduler import start_scheduler

app = FastAPI()

@app.on_event("startup")
def startup_event():
    start_scheduler()

@app.get("/scan")
def scan():
    results = scan_breakouts()
    send_alerts(results)
    return {"status": "alerts sent", "results": results}

@app.get("/status")
def status():
    return {"status": "running"}