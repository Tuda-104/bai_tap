from odoo import models, fields


class SCustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    plan_sale_order = fields.Many2one('plan.sale.order', string='Kế hoạch bán hàng')
    plan_sale_order_id = fields.Many2one('plan.sale.order', string='Mã kế hoạch')

    def action_confirm(self):
        if self.plan_sale_order_id or self.plan_sale_order.state == 'approve':
            return super(SCustomSaleOrder, self).action_confirm()
        else:
            raise models.ValidationError("!!!LỖI!!!")
