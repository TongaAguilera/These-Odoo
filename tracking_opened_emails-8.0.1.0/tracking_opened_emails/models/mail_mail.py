import urllib
import urlparse
from openerp import api, tools,models,fields

class mail_mail(models.Model):
    _inherit = 'mail.mail'

    state = fields.Selection(selection_add=[('opened', 'Opened')])

    def _get_opened_tracking_url(self, cr, uid, mail, partner=None, context=None):
        base_url = self.pool.get('ir.config_parameter').get_param(cr, uid, 'web.base.url')
        track_url = urlparse.urljoin(
            base_url, '/web/dbredirect?%(params)s' % {
                'params': urllib.urlencode({
                    'db': cr.dbname,
                    'redirect': '/mail_opened/track/%s/blank.gif' % mail.id,
                })
            }
        )
        return '<img src="%s" alt="" height="1" width="1" alt="" border="0" />' % track_url

    def send_get_mail_body(self, cr, uid, mail, partner=None, context=None):
        mail.auto_delete = False
        body = super(mail_mail,self).send_get_mail_body(cr, uid, mail, partner=None, context=None)

        tracking_url = self._get_opened_tracking_url(cr, uid, mail, partner, context=context)
        if tracking_url:
            body = tools.append_content_to_html(body, tracking_url, plaintext=False, container_tag='div')
        return body

    def set_opened(self, cr, uid, ids=None, mail_mail_ids=None, mail_message_ids=None, context=None):
        self.write(cr,uid,mail_mail_ids,{'state':'opened'},context=context)
