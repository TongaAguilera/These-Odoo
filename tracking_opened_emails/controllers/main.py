import werkzeug

from odoo import http, SUPERUSER_ID
from odoo.http import request
from . import logging

logger = logging.getLogger(__name__)


class MailController(http.Controller):
    @http.route('/mail_opened/track/<int:mail_id>/blank.gif', type='http', auth='none')
    def track_mail_open(self, mail_id, **post):
        """ Email tracking. """
        mail_mail = request.registry.get('mail.mail')
        mail_mail.set_opened(request.cr, SUPERUSER_ID, mail_mail_ids=[mail_id])
        response = werkzeug.wrappers.Response()
        response.headers['Cache-Control'] = 'no-cache'
        response.data = 'R0lGODlhAQABAIAAANvf7wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=='.decode('base64')
        return response


