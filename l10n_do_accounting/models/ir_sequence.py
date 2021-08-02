from odoo import api, models, fields


class IrSequence(models.Model):
    _inherit = "ir.sequence"

    expiration_date = fields.Date(
        string="NCF Expiration date",
        default=fields.Date.end_of(
            fields.Date.today().replace(year=fields.Date.today().year + 1), "year"
        ),
    )

    mail_template = fields.Many2one(
        comodel_name='mail.template',
        string='Mail_template',
        required=False)

    warning_ncf = fields.Integer(string="NCF de alerta")

    # TODO: Note for anyone from the future: use l10n_do prefix on v14, for God sake
