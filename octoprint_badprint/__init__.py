# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import octoprint.settings


class BadprintPlugin(octoprint.plugin.TemplatePlugin,
                     octoprint.plugin.SettingsPlugin,
                     octoprint.plugin.AssetPlugin):
    def get_settings_defaults(self):
        return dict(
            detect_server_url="http://localhost:3333",

            sender_mail_server='smtp.gmail.com',
            sender_mail_port=465,
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
        return dict(
            js=["js/badprint.js"]
        )


__plugin_name__ = "badprint"
__plugin_implementation__ = BadprintPlugin()
