import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalyst_count.settings')  # Update with your project name
app = Celery('catalyst_count')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# Configure the Celery broker to use Redis
app.conf.broker_url = 'redis://localhost:6379/0'