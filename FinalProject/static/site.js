var Site = function(){
	this.symbol = "";
};

Site.prototype.Init = function(){
	$("#symbol").on("click", function(){
		$(this).val("");
	});
};

Site.prototype.GetQuote = function(){
	$.ajax({
		url: "/quote?symbol=" + this.symbol,
		method: "GET",
		cache: false
	}).done(function(data) {
		console.log(data);	// console.log logs the data so that it is viewable when inspecting the webpage
		document.getElementById("Company").innerHTML ="Company: " + data.shortName;
		document.getElementById("Ticker").innerHTML = "Symbol: " + data.symbol;
		document.getElementById("Price").innerHTML = "Price: " + data.regularMarketPrice;
		document.getElementById("Volume").innerHTML = "Volume: " + data.regularMarketVolume;
		document.getElementById("Volume Avg").innerHTML = "Volume Avg: " + data.averageVolume;
	});
};

Site.prototype.SubmitForm = function(){
	this.symbol = $("#symbol").val();
	this.GetQuote();
}

var site = new Site();

$(document).ready(()=>{
	site.Init();
})
