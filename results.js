
const nameChamp = document.querySelector("#name");

const counter = document.querySelector("#counters");
const searchPhoto = document.querySelector("#searchPhoto");
const counterPhoto1 = document.querySelector("#counterPhoto1");
const counterPhoto2 = document.querySelector("#counterPhoto2");
const counterPhoto3 = document.querySelector("#counterPhoto3");

const queryParams = new URLSearchParams(window.location.search);
const query = queryParams.get('q');

var requestOptions = {
    method: 'GET',
    redirect: 'follow'
};

fetch('./champion_data.json', requestOptions)
    .then(response => response.json())
    .then(result => {
        let searching = query;
        searching = searching.charAt(0).toUpperCase() + searching.slice(1)
        nameChamp.innerHTML = query;
        // counter.innerHTML = result[searching].TopCounters;
        let champ1 = result[searching].TopCounters[0];
        let champ2 = result[searching].TopCounters[1];
        let champ3 = result[searching].TopCounters[2];
        console.log(searching.toLowerCase());
        
        searchPhoto.src = result[searching].ChampImg;
        counterPhoto1.src = result[champ1].ChampImg;
        counterPhoto2.src = result[champ2].ChampImg;
        counterPhoto3.src = result[champ3].ChampImg;
    });
