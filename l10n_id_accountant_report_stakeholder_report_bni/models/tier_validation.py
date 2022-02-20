# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class TierValidation(models.Model):
    _inherit = "tier.validation"

    @api.model
    def _get_tier_validation_model_names(self):
        _super = super(TierValidation, self)
        res = _super._get_tier_validation_model_names()
        res.append("accountant.report_stakeholder_report_bni")
        return res
