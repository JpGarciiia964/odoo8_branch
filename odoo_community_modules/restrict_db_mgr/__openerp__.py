# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Enterprise Management Solution
#    risk_management Module
#    Copyright (C) 2014 OpenSur (comercial@opensur.com)
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
    'name': 'Restrict access to Manage Databases',
    'version': '1.0',
    'author': 'OpenSur SA',
    'website': 'http://www.opensur.com',
    'category': 'Website',
    'description': """
       Restrict access to Manage Databases feature, only administrator user or technical features group allowed\n
       You can customize error page by editing file: restrict_access.html

    """,
    'depends': ['web', 'base'],
    'update_xml':[
    ],
    'data': [],
    'demo': [],
    'test': [],
    'qweb' : [
                "views/base.xml",
                "views/restrict_access.xml"
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'active': False,
}

