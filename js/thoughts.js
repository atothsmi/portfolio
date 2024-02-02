function getThoughts(file){
    fetch(file).then((res) => {
        if (!res.ok) {
            throw new Error
                (`HTTP error! Status: ${res.status}`);
        }
        return res.json();
    })
    .then((data) => {
        for(let content in data){
            $('#thoughts').append(content)
        };
    })
    .catch((error) => 
        console.error("Unable to fetch data:", error));
};

getThoughts('..\\js\\thoughtsHTML.json');

