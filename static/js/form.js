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
		var items = jQuery.parseJSON(response);
		for(var k in items) {
			var item = items[k];
			var date = new Date((item.timestamp) * 1000).toISOString(); //.toString()
		   	list += date + " - " + 
		   			item.contact + " - " + 
		   			item.message;
		}
		document.getElementById("listFormDiv").innerHTML = list;
	});
}