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
		var list = "";
		//var items = JSON.parse(response);
		var items = jQuery.parseJSON(response);
		for(var item in items) {
		   list += item[0] + " - " + item[1] + " " + item[2];
		}
		document.getElementById("listFormDiv").innerHTML = list;
	});
}