from celery.utils.log import get_task_logger
import requests
from requests_ntlm import HttpNtlmAuth

logger = get_task_logger(__name__)


def get_url_with_ntlm(url, ntlm_username, ntlm_password):
    logger.info('Getting JSON from URL: [{}] using NTLM {}:{}'.format(url, ntlm_username, ntlm_password))
    logger.debug('URL        : {}'.format(url))
    logger.debug('domain user: {}'.format(ntlm_username))
    logger.debug('pass       : {}'.format(ntlm_password))
    return requests.get(url, timeout=10, verify=False, auth=HttpNtlmAuth(ntlm_username, ntlm_password))


class UCPApiUrls(object):
    API_ROOT = 'api'
    ABOUT = '{}/about'.format(API_ROOT)
    SERVERS = '{}/servers'.format(API_ROOT)
    CHASSIS = '{}/chassis'.format(API_ROOT)
    ETH_SWITCHES = '{}/ethernetswitches'.format(API_ROOT)
    FAB_SWITCHES = '{}/fibrechannelswitches'.format(API_ROOT)
