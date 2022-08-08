function myMap() {
    // 40.75820747253673, -73.9854016173013
    const fenway = { lat: 40.75820747253673, lng: -73.9854016173013 };

    let mapProp= {
      center:fenway,
      zoom:10,
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
        // console.log(panorama.location)
        // send fav pano details
        let data = panorama.location
        
        fetch("http://127.0.0.1:5000/fav", {
          method: "POST",
          headers: {'Content-Type': 'application/json'}, 
          body: JSON.stringify(data)
        }).then(res => {
          console.log(`${data.description} is now faved!`);
        });
    })
      
    }

