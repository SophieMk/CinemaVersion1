var script = document.querySelector('[magnet]')
magnet = script.getAttribute('magnet')
torrentId = magnet
torrentId = torrentId.replace(/\&amp;/g,'&');

console.log(torrentId)
WebTorrent = require("webtorrent")
const client = new WebTorrent()
client.add(torrentId, function (torrent) {
console.log("Here")
// Torrents can contain many files. Let's use the .mp4 file
const file = torrent.files.find(function (file) {
       return file.name.endsWith('.mp4')
})

// Display the file by adding it to the DOM.
// Supports video, audio, image files, and more!
file.appendTo('.myVideo')
})