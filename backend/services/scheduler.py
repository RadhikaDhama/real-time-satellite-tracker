from apscheduler.schedulers.background import BackgroundScheduler
from backend.processing.propagate_satellite import save_satellites


def start_scheduler():

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        save_satellites,
        "interval",
        seconds=30
    )

    scheduler.start()