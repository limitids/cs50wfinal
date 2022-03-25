



document.addEventListener('DOMContentLoaded',function()  {

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }


    icon = L.divIcon({
        className: 'custom-div-icon',
        html: '<img src="https://www.pinclipart.com/picdir/big/62-626990_aaca-information-for-austin-tx-food-allergies-eat.png"height=30 width=30> </img>',
        iconSize: [30, 42],
        iconAnchor: [15, 0]
    });

    if (document.getElementById('map')) {
        const long = getCookie('long')
        const lat = getCookie('lat')

        var map = L.map('map').setView([lat,long],13)
        L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox/streets-v11',
            tileSize: 512,
            zoomOffset: -1,
            accessToken: 'pk.eyJ1IjoibGltaXRpZHMiLCJhIjoiY2wxMmhmdTFyMW1udDNjcWg1Yjh6aW9ybCJ9.83KFrSYz5wDG6jmDKmCZRg'
        }).addTo(map);

    var marker = L.marker([30.444740, -91.147400],{icon:icon}).addTo(map);
    marker.bindPopup("<a>La careta</a>")
    }


    if (document.getElementById('coordForm')) {
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
                        let cookie
                        document.cookie = `long=${response.long}`;
                        document.cookie = `lat=${response.lat}`;
                    }
                )
    
    
    
            location = `${location.href}explore`  // Sadly this reloads
    
    
    
            e.preventDefault()
    
        })
    }

    document.getElementById('resturaunt').addEventListener('click',() => {
        location = `${location.href.replace('explore/','resturaunt/')}`  // Sadly this reloads

    })
    

})

/*
fetch(`api/resturaunts`, {
    method: 'PUT',
    body: JSON.stringify({
        "zip": `${zip}`
    })
}).then(response => response.json())
.then(
    response => {

        document.getElementById('resturauntList').innerHTML = `<h1> ${response.resturaunts} </h1>`

    }
)
*/