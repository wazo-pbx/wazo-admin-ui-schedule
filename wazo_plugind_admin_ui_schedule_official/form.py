# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import pytz

from flask_babel import lazy_gettext as l_
from wtforms.fields import (
    SubmitField,
    StringField,
    SelectField,
    SelectMultipleField,
    FieldList,
    FormField
)
from wtforms.validators import InputRequired

from wazo_admin_ui.helpers.destination import DestinationField
from wazo_admin_ui.helpers.form import BaseForm

week_days = [l_('Monday'), l_('Tuesday'), l_('Wednesday'), l_('Thursday'), l_('Friday'), l_('Saturday'), l_('Sunday')]
month_days = range(1, 31)
months = [l_('January'), l_('February'), l_('March'), l_('April'), l_('May'), l_('June'), l_('July'),
          l_('August'), l_('September'), l_('October'), l_('November'), l_('December')]


def convert_list_to_choices(list_):
    result = []
    for index, item in enumerate(list_, start=1):
        result.append((index, item))
    return result


def list_timezones():
    result = [('', l_('None'))]
    result.extend(list(zip(pytz.all_timezones, pytz.all_timezones)))
    return result


class PeriodForm(BaseForm):
    hours_start = StringField(l_('Hour Start'))
    hours_end = StringField(l_('Hour End'))
    week_days = SelectMultipleField(l_('Weekdays'), choices=convert_list_to_choices(week_days))
    month_days = SelectMultipleField(l_('Monthdays'), choices=convert_list_to_choices(month_days))
    months = SelectMultipleField(l_('Months'), choices=convert_list_to_choices(months))


class ScheduleExceptionalPeriodForm(PeriodForm):
    destination = DestinationField()


class ScheduleOpenPeriodForm(PeriodForm):
    pass


class ScheduleForm(BaseForm):
    name = StringField(l_('Name'), validators=[InputRequired()])
    timezone = SelectField(l_('Timezone'), choices=list_timezones())
    closed_destination = DestinationField()
    exceptional_periods = FieldList(FormField(ScheduleExceptionalPeriodForm))
    open_periods = FieldList(FormField(ScheduleOpenPeriodForm))
    submit = SubmitField(l_('Submit'))
