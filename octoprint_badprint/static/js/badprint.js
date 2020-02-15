$(function () {
	function BadprintViewModel(parameters) {
		var self = this
		self.settings = parameters[0]

		self.cancel = function () {
			showConfirmationDialog({
				message: gettext("This will cancel your print."),
				cancel: gettext("No"),
				proceed: gettext("Yes"),
				onproceed: function () {
					OctoPrint.job.cancel()
				},
				nofade: true
			})
		}

		self.getProbability = function () {
			OctoPrint.ajax("GET", 'api/plugin/badprint',
				{
					dataType: 'json'
				}).done(function (data) {
					console.log(data)
					$('#badprint_gauge').attr('data-value', data.probability)
				}).fail(function (err) {
					console.log("get probability fail.")
				})
		}

		//email notification start
		self.emailsend = function () {

			var payload = {
				command: "testmail"
			}

			OctoPrint.ajax("POST", "api/plugin/badprint",
				{
					dataType: "json",
					data: JSON.stringify(payload),
					contentType: "application/json charset=UTF-8"
				}).done(function(data){
					console.log("email send done")
					console.log(data)
				}).fail(function(err){
					console.log(err)
				})
		}
		//email notification end

		//debugging test function
		self.test = function(){
			$('#badprint_gauge').attr('data-value', 0.88)
			self.emailsend()
		}

		self.onStartupComplete = function () {
			console.log(self.settings)

			var stream_url = self.settings.settings.plugins.badprint.detect_streaming_url() + self.settings.webcam_snapshotUrl() + '&' + Date.now()
			$("#badprint_webcam")
			.append('<img  id=\"bp_img\" src=\'' + stream_url + '\'>')

			setInterval(self.getProbability, 1000)
		}
	}

	OCTOPRINT_VIEWMODELS.push([
		BadprintViewModel,
		["settingsViewModel"],
		["#tab_plugin_badprint"]
	])
})
