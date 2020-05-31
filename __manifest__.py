# Copyright 2013 XCG Consulting (http://odoo.consulting)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Py3o Report Engine',
    'summary': 'Reporting engine based on Libreoffice (ODT -> ODT, '
               'ODT -> PDF, ODT -> DOC, ODT -> DOCX, ODS -> ODS, etc.)',
    'version': '11.0.1.0.0',
    'category': 'Reporting',
    'license': 'AGPL-3',
    'author': 'XCG Consulting,'
              'ACSONE SA/NV,'
              'Odoo Community Association (OCA),'
              'Hung Huynh Ngoc (hunghn.qna@gmail.com)',
    'website': 'https://github.com/OCA/reporting-engine',
    'depends': ['web'],
    'external_dependencies': {
        'python': ['py3o.template',
                   'py3o.formats',
                   'PyPDF2']
    },
    'data': [
        'security/ir.model.access.csv',
        'views/ir_actions_report.xml',
        'views/menu.xml',
        'views/py3o_template.xml',
        'views/report_py3o.xml',
    ],
    'demo': [
        'demo/report_py3o.xml',
    ],
    'installable': True,
}
