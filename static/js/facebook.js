var fbtoken = "";

window.fbAsyncInit = function() {
	FB.init({
		appId: '158550007562379',
		cookie: true,
		xfbml: true,
		version: 'v3.2'
	});
	FB.AppEvents.logPageView();

	FB.getLoginStatus(function(response) {
		statusChangeCallback(response);
	});

	FB.logout(function(response) {
	});
};

(function(d, s, id) {
	var js, fjs = d.getElementsByTagName(s)[0];
	if (d.getElementById(id)) {
		return;
	}
	js = d.createElement(s);
	js.id = id;
	js.src = "https://connect.facebook.net/en_US/sdk.js";
	fjs.parentNode.insertBefore(js, fjs);
})
(document, 'script', 'facebook-jssdk');


function checkLoginState() {
	FB.getLoginStatus(function(response) {
	  statusChangeCallback(response);
	});
}

function statusChangeCallback(response) {
	console.log(response);
	fbtoken = reponse.accessToken;
	googletoken = "";
	if (response.status === 'connected') {
		testAPI();
	  } else {
	  }
}

function testAPI() {
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me', function(response) {
    	console.log(response);
      	console.log('Successful login for: ' + response.name);
    });
  }