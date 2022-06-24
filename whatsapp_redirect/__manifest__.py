{
    'name': 'Send Whatsapp Message',
    'version': '15.0.1.0.0',
    'summary': 'Send Message to partner via Whatsapp web',
    'description': 'Send Message to partner via Whatsapp web',
    'live_test_url': 'https://www.youtube.com/watch?v=7doVs8tDSnU&feature=youtu.be',
    'category': 'Extra Tools',
    'author': 'Cybrosys Techno solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': [
        'base', 'contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/view.xml',
        'wizard/wizard.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
