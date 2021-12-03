# -*- coding: utf-8 -*-

from odoo import models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    def create_sale_orders(self):
        order_line = []
        for purchase_order_line_id in self.order_line:
            if not purchase_order_line_id.display_type:
                order_line.append((0, 0, {'product_id': purchase_order_line_id.product_id.id,
                                          'name': purchase_order_line_id.name,
                                          'product_uom_qty': purchase_order_line_id.qty_received,
                                          'product_uom': purchase_order_line_id.product_id.uom_po_id.id or purchase_order_line_id.product_id.uom_id.id,
                                          'x_studio_da_cartoni': purchase_order_line_id.x_studio_da_cartoni,
                                          'x_studio_da_n_pezzi': purchase_order_line_id.x_studio_da_n_pezzi,
                                          'x_studio_da_pallet': purchase_order_line_id.x_studio_da_pallet,
                                          }))
            else:
                order_line.append({'name': purchase_order_line_id.name,
                                   'display_type': purchase_order_line_id.display_type,
                                   })
        context = {
            'default_order_line': order_line,
            #'default_x_studio_data_carico': self.x_studio_data_di_carico,
            #'default_x_studio_data_consegna': self.x_studio_data_di_consegna,
            #'default_x_studio_incoterms': self.x_studio_incoterms_1,
            # 'x_studio_pickup_address': self.x_studio_data_carico,
            'default_name': self.x_studio_customer_ref,
        }
        return {
            'name': _('Sale Orders'),
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'target': 'current',
            'views': [(self.env.ref('sale.view_order_form').id, 'form')],
            'domain': [],
            'context': context,
        }

