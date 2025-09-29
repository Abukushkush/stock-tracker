from apscheduler.schedulers.background import BackgroundScheduler
from scanner import scan_breakouts
from alerts import send_alerts

def job():
    results = scan_breakouts()
    send_alerts(results)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", minutes=5)
    scheduler.start()
