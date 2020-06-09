from apps.products.services.update import UpdateProductPrice, UpdateProduct
from apscheduler.schedulers.background import BackgroundScheduler

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(UpdateProductPrice().execute, 'interval', hours=1)
    scheduler.add_job(UpdateProduct().execute, 'interval', hours=2)
    scheduler.start()