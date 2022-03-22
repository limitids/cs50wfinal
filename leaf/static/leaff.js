



document.addEventListener('DOMContentLoaded',function()  {

    var map = L.map('map').setView([0,0],13)

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoibGltaXRpZHMiLCJhIjoiY2wxMmhmdTFyMW1udDNjcWg1Yjh6aW9ybCJ9.83KFrSYz5wDG6jmDKmCZRg'
    }).addTo(map);
    var marker = L.marker([30.444740, -91.147400]).addTo(map);
    marker.bindPopup("<a>La careta</a>")


    document.getElementById('coordForm').addEventListener('submit',(e)=> {

        const form = document.getElementById('coordForm')
        const zip = form.elements[0].value

        fetch(`api/coords`, {
            method: 'PUT',
            body: JSON.stringify({
                "zip": `${zip}`
            })
        }).then(response => response.json())
        .then(
            response => {
                map.panTo(new L.LatLng(response.lat,response.long));
            }




        )

        e.preventDefault()

    })

})
