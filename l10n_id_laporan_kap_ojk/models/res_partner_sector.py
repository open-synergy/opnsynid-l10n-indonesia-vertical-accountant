# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResPartnerSector(models.Model):
    _inherit = "res.partner.sector"

    ojk_category = fields.Selection(
        string="Category OJK",
        selection=[
            ("pb", "Perbankan"),
            ("pm", "Permodalan"),
            ("iknb", "IKNB"),
        ]
    )
