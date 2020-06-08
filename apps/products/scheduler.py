from apps.products.services.update import UpdateProductPrice, UpdateProduct
from apscheduler.schedulers.background import BackgroundScheduler

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(UpdateProductPrice().execute, 'interval', seconds=30)
    scheduler.add_job(UpdateProduct().execute, 'interval', seconds=30)
    scheduler.start()