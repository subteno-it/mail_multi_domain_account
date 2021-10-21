# -*- coding: utf-8 -*-
# Copyright 2021 Subteno
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    force_alias_domain = fields.Char(
        related='team_id.force_alias_domain',
    )
