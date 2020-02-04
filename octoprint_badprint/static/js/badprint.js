$(function() {
	function BadprintViewModel(parameters) {
		var self = this;
		self.settings = parameters[0];
		
		self.cancel = function(){
			showConfirmationDialog({
				message: gettext("This will cancel your print."),
				cancel: gettext("No"),
				proceed: gettext("Yes"),
				onproceed: function() {
					OctoPrint.job.cancel();
				},
				nofade: true
			});
		}
	}

	OCTOPRINT_VIEWMODELS.push([
		BadprintViewModel,
		["settingsViewModel"],
		["#tab_plugin_badprint"]
	]);
});