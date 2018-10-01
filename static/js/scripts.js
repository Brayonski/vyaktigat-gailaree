$(document).ready(function () {
    function copyToClipboard(idd) {
        var copyText = document.getElementById(idd);
        text = copyText.src;
        var dummy = document.createElement("input");
        document.body.appendChild(dummy);
        dummy.setAttribute('value', text);
        dummy.select();
        document.execCommand("copy");
        document.body.removeChild(dummy);
        alert("Copied the text: " + copyText.src);
    }
});
