function drawLocationOnMap(div, coords) {
    var myLatlng = new google.maps.LatLng(coords.latitude, coords.longitude);
      var mapOptions = {
        zoom: 15,
        center: myLatlng,
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
        },
        zoomControl: true,
        zoomControlOptions: {
          style: google.maps.ZoomControlStyle.SMALL
        },
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        scrollwheel: false
      }
      var map = new google.maps.Map(div, mapOptions);

      var marker = new google.maps.Marker({
          position: myLatlng,
          map: map,
          title: 'EventX!'
      });
}

$(document).ready(function () {
    var divMapa = $("#mapa").get(0);
    var coords = {"latitude": -22.930575, "longitude": -43.2090166666667};
    drawLocationOnMap(divMapa, coords)
});