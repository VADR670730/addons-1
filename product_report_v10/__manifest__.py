# © 2016 Houssine BAKKALI, Open Architects Consulting SPRL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Barcode product report",
    "summary": """
        This module allows to show the print barcode and name of the product.
    """,
    "author": "Coop IT Easy SCRLfs",
    "category": "Product",
    "version": "12.0.1.0.0",
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "depends": ["base", "product", "web"],
    "data": [
        "report/layout.xml",
        "report/product_template_label_repeat.xml",
        "report/product_template_label_repeat_10x4.xml",
        "report/product_template_label_repeat_65.xml",
        "report/product_template_templates.xml",
        "report/product_template_templates_65.xml",
        "report/product_reports.xml",
    ],
}