# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import octoprint.settings

import flask
import requests
import yagmail
from email.utils import formatdate
from time import sleep


class BadprintPlugin(octoprint.plugin.StartupPlugin,
                     octoprint.plugin.TemplatePlugin,
                     octoprint.plugin.SettingsPlugin,
                     octoprint.plugin.AssetPlugin,
                     octoprint.plugin.SimpleApiPlugin):

    probability = 0

    def on_after_startup(self, *args, **kwargs):
        self.get_probability()

    def get_settings_defaults(self):
        return dict(
            detect_streaming_url="http://team1pi.local:8000/p?img=",
            detect_probability_url="http://team1pi.local:8000/probability",

            mail_enable=True,
            sender_mail_server='smtp.gmail.com',
            sender_mail_port=465,
            sender_mail_useralias='',
            sender_mail_username='',
            sender_mail_password='',
            sender_use_tls=False,
            sender_use_ssl=True,

            recipicent_mail_address=''
        )

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
        return dict(js=["js/badprint.js"])

    def get_probability(self):
        subject = "Spaghetti has been detected! - Octoprint Plugin Badprint"
        body = ["Spaghetti has been detected! Please check the octoprint page."]
        while True:
            res = requests.get(self._settings.get(['detect_probability_url']))
            self.probability = res.json()['probability']
            if self._settings.get(['mail_enable']):
                self.send_notification(subject, body)
                self._settings.set(['mail_enable'], False)
            sleep(1)

    def on_api_get(self, request):
        return flask.jsonify(probability=self.probability)

    def send_notification(self, subject="OctoPrint notification", body=[""]):
        yagmail.register(self._settings.get(
            ['sender_mail_username']), self._settings.get(['sender_mail_password']))
        mailer = yagmail.SMTP(user={self._settings.get(['sender_mail_username']): self._settings.get(['sender_mail_useralias'])}, host=self._settings.get(
            ['sender_mail_server']), port=self._settings.get(['sender_mail_port']), smtp_starttls=self._settings.get(['sender_use_tls']), smtp_ssl=self._settings.get(['sender_use_ssl']))
        emails = [email.strip()
                  for email in self._settings.get(['recipicent_mail_address']).split(',')]
        mailer.send(to=emails, subject=subject, contents=body,
                    headers={"Date": formatdate()})


__plugin_name__ = "badprint"
__plugin_implementation__ = BadprintPlugin()
