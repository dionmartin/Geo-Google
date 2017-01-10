# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from itertools import groupby
from datetime import datetime, timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.misc import formatLang

import odoo.addons.decimal_precision as dp
from geopy.geocoders import Nominatim

class history_detail(models.Model):

	_name = "history.detail"
	_description = "History Detail"

	latitute = fields.Float('Latitute' , digits=(16, 5))
	longitude = fields.Float('Longitude' , digits=(16, 5))
	address = fields.Char('Address')
	city = fields.Char('City')
	state = fields.Char('State')
	country = fields.Char('Country')


	@api.multi
	def check(self):
		geolocator = Nominatim()
		lat = self.latitute
		longi = self.longitude
		location = geolocator.reverse((lat, longi))
		self.address = location.raw['display_name']
		self.city = location.raw['address']['city']
		self.state = location.raw['address']['state_district']
		self.country = location.raw['address']['country']
