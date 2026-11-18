from odoo import fields, models


class PosOrder(models.Model):
    _inherit = 'pos.order'

    order_type = fields.Selection(
        selection=[
            ('dine_in', 'Dùng tại quán (Dine-in)'),
            ('take_away', 'Mang đi (Take-away)'),
        ],
        string='Hình thức phục vụ',
        default='dine_in',
        required=True,
    )
    barista_status = fields.Selection(
        selection=[
            ('waiting', 'Chờ pha chế'),
            ('preparing', 'Đang pha chế'),
            ('done', 'Đã ra món'),
        ],
        string='Trạng thái quầy Bar',
        default='waiting',
    )
    barista_note = fields.Char(
        string='Ghi chú pha chế (Đường / Đá)',
        help='Ví dụ: 70% đường, ít đá, không lấy ống hút',
    )