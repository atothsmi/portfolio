function getThoughts(file){
    fetch(file).then((res) => {
        if (!res.ok) {
            throw new Error
                (`HTTP error! Status: ${res.status}`);
        }
        return res.json();
    })
    .then((data) => {
        for(let year in data){
            console.log(thing);
            for(let date in year){
                console.log(data[year][date])
            };
        };
    })
    .catch((error) => 
        console.error("Unable to fetch data:", error));
};

getThoughts('..\\js\\thoughts.json');

