var id = document.getElementById('claseId').textContent.trim()
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player; 

function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '700',
        width: '1000',
        videoId: id,
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerReady(event) {
    event.target.playVideo();
}

var done = false;

function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING) {
        setInterval(function() {
            var currentTime = player.getCurrentTime();
            console.log('Tiempo transcurrido: ' + currentTime + ' segundos');
        }, 1000);
    }
}
function stopVideo() {
player.stopVideo();
}