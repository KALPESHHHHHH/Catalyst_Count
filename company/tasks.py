# company/tasks.py
from celery import shared_task
from .models import CompanyCSVData
import pandas as pd
from django.db import IntegrityError
from io import StringIO
import logging

# Configure logger
logger = logging.getLogger(__name__)

@shared_task
def process_csv(file_content, filename):
    try:
        data = StringIO(file_content)
        df = pd.read_csv(data)

        success_count = 0
        error_count = 0
        error_messages = []

        for index, row in df.iterrows():
            try:
                if pd.notna(row.get('name')) and pd.notna(row.get('domain')):
                    # Adjust id handling according to your needs
                    company = CompanyCSVData.objects.create(
                        name=row.get('name'),
                        domain=row.get('domain'),
                        year_founded=row.get('year_founded'),
                        industry=row.get('industry'),
                        size_range=row.get('size_range'),
                        locality=row.get('locality'),
                        country=row.get('country'),
                        linkedin_url=row.get('linkedin_url'),
                        current_employee_estimate=row.get('current_employee_estimate'),
                        total_employee_estimate=row.get('total_employee_estimate')
                    )
                    success_count += 1
                else:
                    error_count += 1
                    error_messages.append(f"Row {index + 1}: 'name' or 'domain' is required.")
            except IntegrityError as e:
                error_count += 1
                error_messages.append(f"Error inserting Row {index + 1}: {str(e)}")
                logger.error(f"Integrity error on row {index + 1}: {str(e)}")
            except Exception as e:
                error_count += 1
                error_messages.append(f"Unexpected error for Row {index + 1}: {str(e)}")
                logger.error(f"Unexpected error on row {index + 1}: {str(e)}")

        logger.info(f"Successfully processed {success_count} records. {error_count} errors occurred.")
        if error_messages:
            logger.error("Errors: %s", error_messages)

    except Exception as e:
        logger.error(f"Error processing CSV: {str(e)}")