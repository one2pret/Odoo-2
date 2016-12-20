{
    'name': "PC Backup",
    'version': "0.2.8",
    'author': "Sythil Tech",
    'category': "Tools",
    'summary': "Backs up important files on your desktop computers",
    'description': "Backs up important files on your desktop computers",
    'license':'LGPL-3',
    'data': [
        'data/res.groups.csv',
        'data/ir.cron.csv',
        'security/ir.model.access.csv',
        'views/res_users_views.xml',
        'views/backup_computer_views.xml',
        'views/backup_computer_file_views.xml',
        'views/backup_odoo_views.xml',
        'views/pc_backup_templates.xml',
    ],
    'demo': [],
    'depends': ['web'],
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
}