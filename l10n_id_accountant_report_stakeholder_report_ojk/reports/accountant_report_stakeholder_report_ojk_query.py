# -*- coding: utf-8 -*-
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, tools


class DaftarKlienAuditUmumQuery(models.Model):
    _name = "accountant.report_stakeholder_report_ojk_query"
    _description = "Accountat Report Stakeholder Report - Query"
    _auto = False

    signing_accountant_id = fields.Many2one(
        string="Signing Accountant",
        comodel_name="res.partner",
    )
    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
    )
    analytic_account_id = fields.Many2one(
        string="Analytic Account",
        comodel_name="account.analytic.account",
    )
    stakeholder_report_id = fields.Many2one(
        string="# Stakeholder Report",
        comodel_name="accountant.report_stakeholder_report",
    )
    signing_accountant_name = fields.Char(
        string="Signing Accountant Name",
    )
    contract_name = fields.Char(
        string="Contract Title",
    )
    contract_number = fields.Char(
        string="Contract Number",
    )
    contract_date = fields.Date(
        string="Contract Date",
    )
    contract_amount = fields.Float(
        string="Contract Amount",
    )
    contract_payment_amount = fields.Float(
        string="Contract Payment Amount",
    )
    contract_note = fields.Float(
        string="Contract Note",
    )
    ojk_category = fields.Selection(
        string="Category OJK",
        selection=[
            ("pb", "Perbankan"),
            ("pm", "Permodalan"),
            ("iknb", "IKNB"),
        ],
    )

    def _select(self):
        select_str = """
             SELECT a.id AS id,
                    a.signing_accountant_id AS signing_accountant_id,
                    a.project_id AS project_id,
                    c.analytic_account_id AS analytic_account_id,
                    g.id AS stakeholder_report_id,
                    b.name AS signing_accountant_name,
                    e.title AS contract_name,
                    e.name AS contract_number,
                    e.date AS contract_date,
                    0.0 AS contract_amount,
                    0.0 AS contract_payment_amount,
                    e.note AS contract_note,
                    h.ojk_category AS ojk_category
        """
        return select_str

    def _from(self):
        from_str = """
                accountant_report AS a
        """
        return from_str

    def _where(self):
        where_str = """
            WHERE (e.state = 'done' or e.state = 'approve' or e.state = 'open')
        """
        return where_str

    def _join(self):
        join_str = """
        JOIN res_partner AS b ON a.signing_accountant_id = b.id
        JOIN project_project AS c ON a.project_id = c.id
        JOIN account_analytic_account AS d ON c.analytic_account_id = d.id
        JOIN service_contract AS e ON d.id = e.analytic_account_id
        JOIN rel_stakeholder_report_2_accountant_report AS f ON a.id = f.accountant_report_id
        JOIN accountant_report_stakeholder_report AS g ON f.accountant_report_id = g.id
        JOIN res_partner_sector AS h ON b.sector_id = h.id
        """
        return join_str

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        # pylint: disable=locally-disabled, sql-injection
        cr.execute(
            """CREATE or REPLACE VIEW %s as (
            %s
            FROM %s
            %s
            %s
        )"""
            % (self._table, self._select(), self._from(), self._join(), self._where())
        )
