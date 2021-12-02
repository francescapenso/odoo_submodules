# -*- coding: utf-8 -*-

from odoo import models, _
from datetime import datetime


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def create_purchase_orders(self):
        order_line = []
        for sale_order_line_id in self.order_line:
            if not sale_order_line_id.display_type:
                order_line.append((0, 0, {'name': sale_order_line_id.name,
                                          'product_id': sale_order_line_id.product_id.id,
                                          'product_qty': sale_order_line_id.product_uom_qty - sale_order_line_id.qty_delivered,
                                          'date_planned': datetime.today(),
                                          'product_uom': sale_order_line_id.product_id.uom_po_id.id or sale_order_line_id.product_id.uom_id.id,
                                          'x_studio_da_cartoni': sale_order_line_id.x_studio_da_cartoni,
                                          'x_studio_da_n_pezzi': sale_order_line_id.x_studio_da_n_pezzi,
                                          'x_studio_da_pallet': sale_order_line_id.x_studio_da_pallet,
                                          }))
            else:
                order_line.append({'name': sale_order_line_id.name,
                                   'display_type':sale_order_line_id.display_type,
                                   })
        context = {
            'default_origin': self.name,
            'default_x_studio_data_di_carico': self.x_studio_data_carico,
            'default_x_studio_data_di_consegna': self.x_studio_data_consegna,
            'default_x_studio_incoterms_1': self.x_studio_incoterms,
            # 'x_studio_delivery_address': self.name,
            'default_x_studio_customer_ref': self.name,
            'default_order_line': order_line,
        }
        return {
            'name': _('Purchase Orders'),
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_mode': 'form',
            'target': 'new',
            'views': [(self.env.ref('purchase.purchase_order_form').id, 'form')],
            'domain': [],
            'context': context,
        }

