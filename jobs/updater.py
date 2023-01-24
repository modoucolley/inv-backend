from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import create_pdffile, send_message

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(send_message, 'interval', seconds=5)
	scheduler.start()