from odoo import models, fields, api, exceptions
from datetime import datetime
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class InheritCrmModel(models.Model):
    _inherit = 'crm.lead'

    facebook = fields.Char(string='Facebook')
    twitter = fields.Char(string='Twitter')
    instgram = fields.Char(string='Instgram')
    website = fields.Char(string='Website')
    whatsapp = fields.Char(string='Whatsapp')
    social = fields.Selection(
        [('facebook', 'Facebook'), ('twitter', 'Twitter'), ('whatsapp', 'Whatsapp'), ('website', 'Website'),
         ('instgram', 'Instgram'), ], string='Social Media')
