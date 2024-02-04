let nameChamp = document.querySelector("#name");
let counter = document.querySelector("#counters");
let searchPhoto = document.querySelector("#searchPhoto");
let counterPhoto1 = document.querySelector("#counterPhoto1");
let counterPhoto2 = document.querySelector("#counterPhoto2");
let counterPhoto3 = document.querySelector("#counterPhoto3");


const searchInput = document.getElementById('searchInput');

var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

searchInput.addEventListener('keyup', function(event) {
  if (event.key === 'Enter') {
    const query = searchInput.value.trim().toLowerCase();
    fetch('./champion_data.json', requestOptions)
    .then(response => response.json())
    .then(result => {
      let searching = searchInput.value;
      nameChamp.innerHTML = searchInput.value;
      // counter.innerHTML = result.searchInput.TopCounters[1];
      counter.innerHTML = result[searching].TopCounters;
      let champ1 = result[searching].TopCounters[0]; 
      let champ2=result[searching].TopCounters[1];
      let champ3 =result[searching].TopCounters[2];
      console.log(searchInput.value);
      searchPhoto.src = result[searching].ChampImg;
      counterPhoto1.src = result[champ1].ChampImg;
      counterPhoto2.src = result[champ2].ChampImg;
      counterPhoto3.src = result[champ3].ChampImg;
  })}})

