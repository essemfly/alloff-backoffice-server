import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from datetime import datetime, timedelta

from tagger.core.mongo.models.order import Order
from tagger.models import ExtendedOrder

logger = logging.getLogger(__name__)


def my_job():
    max_age = datetime.now() - timedelta(days=1)  # 1 day
    valid_orders = Order.objects(orderstatus__nin=[
        "CREATED",
        "RECREATED",
        "PAYMENT_PENDING"
    ], created__gte=max_age).all()
    for o in valid_orders:
        if ExtendedOrder.objects.filter(order_id=o.id).count() > 0:
            eo = ExtendedOrder.objects.get(order_id=o.id)
            if eo.code != code and code is not None:
                print(f"Changing extended order {o.id} code from {eo.code} to {code}")
                eo.code = code
                eo.save()
            elif eo.code is None:
                new_code = ExtendedOrder.generate_usable_code()
                print(f"Changing extended order {o.id} code from {eo.code} to {new_code}")
                eo.code = new_code
                eo.save()
        else:
            e = ExtendedOrder.make_from(o, code=code)
            print(f"Order {o.id} has been extended with code {e.code}! (Given code: {code})")
    pass


# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after our job has run.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
