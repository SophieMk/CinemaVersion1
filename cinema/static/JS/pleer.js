var script = document.querySelector('[magnet]')
magnet = script.getAttribute('magnet')
torrentId = magnet
torrentId = torrentId.replace(/\&amp;/g,'&');

console.log(torrentId)
WebTorrent = require("webtorrent")
const client = new WebTorrent()
client.add(torrentId, onTorrent)

function onTorrent (torrent) {
    torrent.files.forEach(function (file) {
        if (file.name.endsWith('.mp4') || file.name.endsWith('.mkv'))
        {
            file.appendTo('.myVideo')
        }
    })
}
