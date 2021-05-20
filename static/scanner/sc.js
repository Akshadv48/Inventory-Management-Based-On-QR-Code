var scanner = new Instascan.Scanner({ video: document.getElementById('preview'), scanPeriod: 5, mirror: false ,backgroundScan: false});
			scanner.addListener('scan',function(content){
				
				//window.location.href=content;
				var x = document.getElementById("error")
				var txt = document.getElementById("owner_id")
				txt.value = content
				var btn = document.getElementById("submit")
				btn.click();

				//x.innerHTML = "Success loading details";
				//url = window.location.href + "store/fullinfo/" + content

				//getapi(url,content)
			});
			Instascan.Camera.getCameras().then(function (cameras){
				if(cameras.length>0){
					if(cameras.length >= 2){
						scanner.start(cameras[1]);

					}
					else{
						scanner.start(cameras[0]);
					}
					
					
				}
				else{
					console.error('No cameras found.');
					var x = document.getElementById("error")
					x.innerHTML = "Cameras Not Found can't start scanner";
				}
			}).catch(function(e){
				console.error(e);
				var x = document.getElementById("error")
					x.innerHTML = "Cameras Not Found can't start scanner";
			});