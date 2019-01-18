var lastButton = "";
var wrongExt = ['zip', 'rar', 'dll', 'exe', 'pdf', 'iso',
'tar', '7z', 'apk', 'tar.gz'];
var isButtonEnabled = true;
var captchaIsValid = false;
var canChange = false;

function disableButton()
{
	var button = document.getElementsByTagName('button')[0];
	lastButton = button;
	var newButton = document.createElement('a');
	newButton.className = "btn btn-lg btn-light disabled";
	newButton.innerHTML = button.innerHTML;
	button.parentNode.replaceChild(newButton, button);
	isButtonEnabled = false;
}

disableButton();

function enableButton()
{
	var button = document.getElementsByTagName('a')[0];
	var newButton = document.createElement('button');
	newButton = lastButton;
	newButton.innerHTML = button.innerHTML;
	button.parentNode.replaceChild(newButton, button);
	isButtonEnabled = true;
}

function updateInputText()
{
	var inputLabel = document.getElementById("inputLabel");
	var fullPath = $("#id_document").val();

	if(fullPath != "")
	{
		var filename = fullPath.replace(/^.*[\\\/]/, '');
		var ext = filename.slice((filename.lastIndexOf(".") - 1 >>> 0) + 2);

		for(var i = 0; i < wrongExt.length; i++)
		{
			if(ext == wrongExt[i])
			{
				inputLabel.textContent = "Extension non supportée !";

				if(isButtonEnabled)
					disableButton();
				return;
			}
		}

		if(!isButtonEnabled && captchaIsValid)
			enableButton();

		canChange = true;
		inputLabel.textContent = filename;
	}
}

function setVideoFromHour()
{
	var addressTag = document.getElementById("address"); 
	var address = addressTag.className;

	var date = new Date();
	var hour = 9;
	var vid = document.getElementById("vid");

	if(hour >= 8 && hour < 12) //matin
		vid.src = address + "lever.mp4";
	else if(hour >= 12 && hour < 14) //midi
		vid.src = address + "repas.mp4";
	else if(hour >= 14 && hour < 18) //après midi
		vid.src = address + "work.vid";
	else if(hour >= 18 && hour < 22) //soir
		vid.src = address + "coucher.mp4";
	else
		vid.src = address + "nuit.mp4";
}

function recaptchaCallback() 
{
	if(!isButtonEnabled && canChange)
		enableButton();
	captchaIsValid = true;
}

setVideoFromHour();
