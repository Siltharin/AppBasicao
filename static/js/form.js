var fbtoken = "";

function saveForm() {
	
	var message = document.getElementById("feedbackmessageTextArea").value;
	var contact = document.getElementById("contactField").value;

	var url = "/saveForm?contact=" + contact + "&message=" + message + "&fbtoken=" + fbtoken;
	
	$.post(url, {} , function(response) {
		document.getElementById("formResponse").innerHTML = "<font color='darkblue'><b>Obrigada pelo Feedback!</b></font>";
	});
}