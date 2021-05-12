# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class AccountantOjkConfigSetting(models.TransientModel):
    _name = "accountant.ojk_config_setting"
    _inherit = "res.config.settings"

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda self: self._default_company_id(),
    )

    accountant_ojk_sequence_id = fields.Many2one(
        string="OJK Sequence",
        comodel_name="ir.sequence",
        related="company_id.accountant_ojk_sequence_id",
    )
    accountant_ojk_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Laporan Kegiatan Pemberian Jasa OJK",
        comodel_name="res.groups",
        related="company_id.accountant_ojk_confirm_grp_ids",
        store=False,
    )
    accountant_ojk_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel OJK",
        comodel_name="res.groups",
        related="company_id.accountant_ojk_cancel_grp_ids",
        store=False,
    )
    accountant_ojk_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart OJK",
        comodel_name="res.groups",
        related="company_id.accountant_ojk_restart_grp_ids",
        store=False,
    )
