a_tags = document.getElementsByTagName("a");

index = 0;

while(index < a_tags.length){
	if (a_tags[index].getAttribute("href") !== null){
		if(a_tags[index].getAttribute("href").endsWith(".html")){
			console.log("https://www.parlament.gv.at/" + a_tags[index].getAttribute("href"));
		}
	}

	index += 1;
}

