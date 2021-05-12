# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    accountant_ojk_sequence_id = fields.Many2one(
        string="OJK Sequence",
        comodel_name="ir.sequence",
    )
    accountant_ojk_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Laporan Kegiatan Pemberian Jasa OJK",
        comodel_name="res.groups",
        relation="rel_accountant_ojk_allowed_confirm_groups",
        column1="company_id",
        column2="group_id",
    )
    accountant_ojk_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Laporan Kegiatan Pemberian Jasa OJK",
        comodel_name="res.groups",
        relation="rel_accountant_ojk_allowed_cancel_groups",
        column1="company_id",
        column2="group_id",
    )
    accountant_ojk_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Laporan Kegiatan Pemberian Jasa OJK",
        comodel_name="res.groups",
        relation="rel_accountant_ojk_allowed_restart_groups",
        column1="company_id",
        column2="group_id",
    )
