
$.getJSON('..\\js\\thoughtsHTML.json', function(data) {
    for(let content in data){
        $('#thoughts').append(content)
    };
});

