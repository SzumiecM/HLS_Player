(function () {
    'use strict';

    var video = document.getElementById('video');
    var videoSrc = 'http://localhost:5000/get/media/playlist.m3u8';
    if (Hls.isSupported()) {
        var hls = new Hls();
        hls.loadSource(videoSrc);
        hls.attachMedia(video);
        video.controls = true;
    }
})();