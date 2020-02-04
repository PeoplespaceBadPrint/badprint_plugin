# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import octoprint.settings

class BadprintPlugin(octoprint.plugin.TemplatePlugin,
					   octoprint.plugin.SettingsPlugin,
					   octoprint.plugin.AssetPlugin):
	def get_settings_defaults(self):
		return dict(
			stream = octoprint.settings.Settings().get(["webcam", "stream"])
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