function myMap() {
    const fenway = { lat: 42.345573, lng: -71.098326 };

    let mapProp= {
      center:fenway,
      zoom:5,
    };
    let map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
    const panorama = new google.maps.StreetViewPanorama(
        document.getElementById("pano"),
        {
          position: fenway,
          pov: {
            heading: 34,
            pitch: 10,
          },
        }
      );
    
    map.setStreetView(panorama);
    
    let favButton = document.getElementById("favButton").addEventListener("click",()=>{
        console.log(panorama)
        console.log(panorama.location)
        console.log(panorama.location.description+' is now faved!')
    })
      
    }

// send fav pano details
