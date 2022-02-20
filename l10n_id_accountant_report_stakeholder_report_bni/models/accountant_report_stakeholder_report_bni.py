# -*- coding: utf-8 -*-
# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class AccountantReportStakeholderReportBni(models.Model):
    _name = "accountant.report_stakeholder_report_bni"
    _description = "Accountat Report Stakeholder Report - BNI"
    _inherit = ["accountant.report_stakeholder_report"]
    _table = "accountant_report_stakeholder_report"

    @api.model
    def _default_type_id(self):
        return self.env.ref(
            "l10n_id_accountant_report_stakeholder_report_bni."
            "report_stakeholder_report_bni"
        ).id

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        type_id = (
            self.env.ref(
                "l10n_id_accountant_report_stakeholder_report_bni."
                "report_stakeholder_report_bni",
                False,
            )
            and self.env.ref(
                "l10n_id_accountant_report_stakeholder_report_bni."
                "report_stakeholder_report_bni"
            )
            or self.env["accountant.report_stakeholder_report_type"]
        )
        args.append(("type_id", "=", type_id.id))
        return super(AccountantReportStakeholderReportBni, self).search(
            args=args, offset=offset, limit=limit, order=order, count=count
        )
