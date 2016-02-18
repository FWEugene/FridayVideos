function ResourceLoader(baseurl) {
  this.BASEURL = baseurl;
}
 
ResourceLoader.prototype.loadResource = function(resource, callback) {
  var url = resource;
  var method = 'GET';
  var xhr = new XMLHttpRequest();
    xhr.responseType = 'xml';
    xhr.onreadystatechange = function() {
      try {
		if (xhr.readyState == 4 && xhr.status == 200)
		      {
		        if (xhr.responseText)
		         {
		             callback(null, xhr.responseText);
	         	
		         }
			 }
      } catch (err) {
        console.error('Aborting request ' + url + '. Error: ' + err);
        xhr.abort();
        callback(new Error("Error making request to: " + url + " error: " + err));
      }
    };

    xhr.open(method, resource, true);
    xhr.send();
}; 
  
 
var createAlert = function(title, description) {

	var alertString = `<?xml version = "1.0" encoding = "UTF-8" ?>
		<document>
			<alertTemplate>
				<title>${title}</title>
				<description>${description}</description>
				<button>
					<text>Ok</text>
				</button>
			</alertTemplate>
		</document> `

 return alertString; 
}