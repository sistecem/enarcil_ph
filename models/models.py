# -*- coding: utf-8 -*-

from odoo import models, fields, api


class enarcil_ph(models.Model):
    _name = 'enarcil_ph.enarcil_ph'
    _description = 'enarcil_ph.enarcil_ph'

    name = fields.Char()

    @api.model
    def test(self, key):
        do_something = 'do something'
        print(do_something)
        return {}

    @api.model
    def test2(self, key):
        do_something = 'do something'
        print (do_something)
        if err:
            return {'status': 'error', 'message': 'The error message you want to send to the device'}
        return {'status': 'ok', 'message': 'Optional success message'}

