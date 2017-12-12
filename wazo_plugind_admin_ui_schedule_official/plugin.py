# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.plugin import create_blueprint
from wazo_admin_ui.helpers.destination import register_listing_url

from .service import ScheduleService
from .view import ScheduleListingView

schedule = create_blueprint('schedule', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        ScheduleListingView.service = ScheduleService()
        ScheduleListingView.register(schedule, route_base='/schedules_listing')

        register_listing_url('schedule', 'schedule.ScheduleListingView:list_json')

        core.register_blueprint(schedule)
