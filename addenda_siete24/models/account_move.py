# -*- coding: utf-8 -*-


from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, UserError
from odoo.tools.float_utils import float_repr

import base64
import requests

from lxml import etree
from lxml.objectify import fromstring
from pytz import timezone
from datetime import datetime
from dateutil.relativedelta import relativedelta
CFDI_XSLT_CADENA = 'l10n_mx_edi/data/3.3/cadenaoriginal.xslt'
CFDI_XSLT_CADENA_TFD = 'l10n_mx_edi/data/xslt/3.3/cadenaoriginal_TFD_1_1.xslt'

class AccountMove(models.Model):

	_inherit = 'account.move'

	def _get_rfc_supplier(self):
		for rec in self:
			supplier = rec.company_id.partner_id.commercial_partner_id.vat
			return supplier