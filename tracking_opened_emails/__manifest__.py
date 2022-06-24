# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Tracking Opened Emails',
    'version': '1.0',
    'category': 'Email',
    "website": '',
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
    'demo': [],
    'currency': "EUR",
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
