# -*- encoding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    "name": "Experience Management",
    "version": "0.1",
    "author": "Savoir-faire Linux",
    "category": "Human Resources",
    "website": "http://www.savoirfairelinux.com",
    "depends": ["hr"],
    "description": """
This module allows you to manage your employee experiences:
* Professional
* Academic
* Certification
    """,
    "demo_xml": [
        "hr_experience_demo.csv",
    ],
    "update_xml": [
        "security/ir.model.access.csv",
        "hr_experience_view.xml",
    ],
    "active": False,
    "installable": True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
