import json
import logging
import allure
from allure_commons.types import AttachmentType

def log_and_attach_allure_info(result):
    allure.attach(body=result.request.url,
                  name="Request url",
                  attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.method,
                  name="Request method",
                  attachment_type=AttachmentType.TEXT)
    allure.attach(body=json.dumps(result.request.body, indent=4, ensure_ascii=True),
                  name="Request body",
                  attachment_type=AttachmentType.JSON,
                  extension="json")
    allure.attach(body=str(result.cookies),
                  name="Response cookies",
                  attachment_type=AttachmentType.TEXT,
                  extension="txt")
    logging.info(result.request.url)
    logging.info(result.status_code)
    logging.info(result.cookies)
    logging.info(result.text)
