import string
from odoo import models, fields, api

class res_partner(models.Model):
    _inherit = 'res.partner'
    
    #CREACION DEL CAMPO fiscal_address
    # 
    fiscal_address =  fields.Text(string="Dirección Fiscal", store=True)