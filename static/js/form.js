var fbtoken = "";

function saveForm() {
	var message = document.getElementById("feedbackmessageTextArea").value;
	var contact = document.getElementById("contactField").value;

	var url = "/saveForm?contact=" + contact 
				+ "&message=" + message 
				+ "&fbtoken=" + fbtoken;
	
	$.post(url, {}, function(response) {
		listForm();
	});
}

function listForm() {
	var url = "/listForm?fbtoken=" + fbtoken;
	
	$.post(url, {}, function(response) {
		document.getElementById("listFormDiv").innerHTML = response;
	});
}