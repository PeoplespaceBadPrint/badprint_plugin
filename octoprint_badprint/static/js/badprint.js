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

		self.ajaxtest = function () {
			var snapshot_url = self.settings.webcam_snapshotUrl() + '?' + Date.now()
			var detect_server_url = self.settings.settings.plugins.badprint.detect_server_url()
			var destination = detect_server_url + "/p/?img=" + snapshot_url
			console.log(destination)
			OctoPrint.ajax("GET", destination,
				{
					jsonpCallback: "callback",
					dataType: 'jsonp',
					crossDomain: true
				}).done(function (data) {
					console.log(data)

					var detection_max = data.detections[0]
					if (detection_max == undefined)
						$('#badprint_gauge').attr('data-value', 0)
					else {
						console.log(detection_max)
						$('#badprint_gauge').attr('data-value', detection_max[1])
						
						//if spaghetti detected..
						if(detection_max[1] > 0.6){
							self.emailsend()
						}
					}

					self.ajaxtest()
				}).fail(function (err) {
					console.log("ajax test fail.")
				})
		}

		//get gauge value start
		self.get_gauge_value = function(){
			OctoPrint.ajax("GET", "api/plugin/badprint",
				{
					dataType: "json",
					contentType: "application/json charset=UTF-8"
				}).done(function(data){
					console.log(data)
				}).fail(function(err){
					console.log(err)
				})
		}
		//get gauge value start

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
			// console.log(self)

			var stream_url = self.settings.webcam_streamUrl() + '?' + Date.now()
			$("#badprint_webcam")
			.append('<img  id=\"bp_img\" src=\'' + stream_url + '\'>')

			//self.ajaxtest()
		}
	}

	OCTOPRINT_VIEWMODELS.push([
		BadprintViewModel,
		["settingsViewModel"],
		["#tab_plugin_badprint"]
	])
})
