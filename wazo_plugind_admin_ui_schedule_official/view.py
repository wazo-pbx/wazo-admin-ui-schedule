# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import jsonify, request
from wazo_admin_ui.helpers.classful import LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response


class ScheduleListingView(LoginRequiredView):

    def list_json(self):
        params = extract_select2_params(request.args)
        schedules = self.service.list(**params)
        results = [{'id': schedule['id'], 'text': schedule['name']} for schedule in schedules['items']]
        return jsonify(build_select2_response(results, schedules['total'], params))
