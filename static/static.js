var key

function USPS(){
    var req = new XMLHttpRequest();
    var tracking_number = document.getElementById('tracking_number').value;
    req.open('GET', 'http://production.shippingapis.com/ShippingAPI.dll?API=TrackV2&XML=<TrackRequest USERID="'+key+'"><TrackID ID="'+tracking_number+'"></TrackID></TrackRequest>', true);
    req.addEventListener('load', function()){
        if (req.status >= 200 && req.status < 400){
        var USPS_file = JSON.parse()}
    }

}

// function FedEx

// function UPS

// function DHL