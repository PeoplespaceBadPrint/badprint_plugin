# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import octoprint.settings

import flask
import yagmail
from email.utils import formatdate


class BadprintPlugin(octoprint.plugin.TemplatePlugin,
                     octoprint.plugin.SettingsPlugin,
                     octoprint.plugin.AssetPlugin,
                     octoprint.plugin.SimpleApiPlugin):

    def get_settings_defaults(self):
        return dict(
            detect_server_url="http://localhost:3333",

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

    def get_api_commands(self):
        return dict(testmail=[])

    def on_api_command(self, command, data):

        if command == "testmail":
            subject = "Spaghetti has been detected! - Octoprint Plugin Badprint"
            body = [
                "Spaghetti has been detected! Please check the octoprint page."]

            try:
                self.send_notification(subject, body)
            except Exception as e:
                return flask.jsonify(success=False, msg=str(e))

            return flask.jsonify(success=True)
        else:
            return flask.make_response("Unknown command", 400)

    def on_api_get(self, request):
		return flask.jsonify(foo="bar")

    def send_notification(self, subject="OctoPrint notification", body=[""]):
        yagmail.register(self._settings.get(['sender_mail_username']), self._settings.get(['sender_mail_password']))
        mailer = yagmail.SMTP(user={self._settings.get(['sender_mail_username']): self._settings.get(['sender_mail_useralias'])}, host=self._settings.get(
            ['sender_mail_server']), port=self._settings.get(['sender_mail_port']), smtp_starttls=self._settings.get(['sender_use_tls']), smtp_ssl=self._settings.get(['sender_use_ssl']))
        emails = [email.strip()
                  for email in self._settings.get(['recipicent_mail_address']).split(',')]
        mailer.send(to=emails, subject=subject, contents=body,
                    headers={"Date": formatdate()})


__plugin_name__ = "badprint"
__plugin_implementation__ = BadprintPlugin()
