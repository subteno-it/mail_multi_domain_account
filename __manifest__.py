# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': "mail_multi_domain_account",
    'summary': "Force alias domain by Sales Team for account.move",
    'description': """
        Long description of module's purpose
    """,
    'author': "Subteno",
    'website': "https://www.subteno.com",
    'category': 'Discuss',
    'version': '0.1',
    'depends': [
        'mail_multi_domain',
        'sale',
        'account',
    ],
    'data': [
        'views/crm_team.xml',
    ],
}
