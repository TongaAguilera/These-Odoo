{
    'name': 'Tracking Opened Emails',
    'version': '1.0',
    'category': 'Email',
    'description': """
Tracking Opened Emails
===============================================
This module lets you know if the emails sent from Odoo were read by the recipients in.
A stage 'opened' was added in the form 'Configuration' => ' Technical ' => 'Email' => ' Emails' and the opened emails are in green in the tree vue.
    """,
    'author': 'Gaston',
    'depends': ['mail'],
    'data': [
             'views/view_mail_form.xml',
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
