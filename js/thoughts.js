
$.getJSON('..\\js\\thoughtsHTML.json', function(data) {
    for(let index in data){
        $('#thoughts').append(data[content])
    };
});

