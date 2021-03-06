# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from . import register
from foro.forms.topic_private import TopicPrivateInviteForm


@register.inclusion_tag('foro/topic_private/_private_invite_form.html')
def render_invite_form(topic, next=None):
    form = TopicPrivateInviteForm()
    return {'form': form, 'topic': topic, 'next': next}
