


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
            const json = JSON.stringify({"gay":"gay"})
            document.cookie = `cart="${json}"`
                fetch(`api/coords`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        "zip": `${zip}`
                    })
                }).then(response => response.json())
                .then(
                    response => {
                        let cookie
                        document.cookie = `lat=${response.lat}`;
                        document.cookie = `long=${response.long}`;
                    }
                )
    
    
    
            location = `${location.href}explore`  // Sadly this reloads
    
    
    
            e.preventDefault()
    
        })
    }


    if (document.getElementById('resturaunt_application')) {
        document.getElementById('resturaunt_app').addEventListener('submit',(e)=> {

            const form = document.getElementById('resturaunt_app')
            const name = form.elements[0].value
            const email = form.elements[1].value
            const website = form.elements[2].value
            const address =  form.elements[3].value
            const longitude =  form.elements[4].value
            const latitude =  form.elements[5].value
            console.log(longitude)
            console.log(latitude)

            console.log('hey')
                fetch(``, {
                    method: 'POST',
                    body: JSON.stringify({
                        "name":name,
                        "email":email,
                        "website":website,
                        "address":address,
                        'longitude':longitude,
                        'latitude':latitude
                    })
                })
    
    
    
                location = `${location.href.replace('apply/','explore/')}`  // Sadly this reloads
    
    
    
            e.preventDefault()
    
        })
    }

    function resturaunt(id) {
        location = `${location.href.replace('explore/',`resturaunt/${id}`)}`  // Sadly this reloads
    }
    
    //----------------------------------------------------------------------

        
    if (document.getElementById('resturaunt_holder')) {
        fetch(`${window.location.origin}/api/resturaunts`,{
            method:'PUT',
            body: JSON.stringify({
                'long':`${getCookie('long')}`,
                'lat':getCookie('lat')
            })
        }).then(response=> response.json())
        .then(response => {
            response.resturaunts.forEach(resturaunt => {
                document.getElementById('resturaunt_holder').innerHTML += `
                
                <div id='resturaunt' data-id="${resturaunt.id}">
                <img id='resuraunt_img' data-id="${resturaunt.id}" src='https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/082012/raising_canes_logo.jpg?itok=YtGVVbR0' heihgt=50 width=150>
                <div id='resturaunt_info' data-id="${resturaunt.id}" >
                    <h1 id='resturaunt_title' data-id="${resturaunt.id}" >${resturaunt.name}</h1>
                    <h6 id='resturaunt_category' data-id="${resturaunt.id}" >Fried Chicken</h6>
                </div>
                <h3 id='resturaunt_eta'data-id="${resturaunt.id}">40-50 min</h3>
                <h3 id='resturaunt_cost'data-id="${resturaunt.id}">$1.49 per delivery</h3>
                </div>
                
                
                `    })    
            })
        .then(response => {
            let resturaunts = document.querySelectorAll('#resturaunt')
            
            resturaunts.forEach(resturaunt => {
                resturaunt.addEventListener('click',(e) => {
                    location = `${location.href.replace('explore/',`resturaunt/${e.target.dataset.id}`)}`  // Sadly this reloads
                })
            })
                  
        })
    }

    })
