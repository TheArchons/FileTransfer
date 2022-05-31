document.addEventListener("DOMContentLoaded", onload);

href = window.location.href;

function onload() {
    document.getElementById("fileInput").addEventListener("change", () => {
        file = document.getElementById("fileInput").files[0];
        //replace spaces with underscores
        file.name = file.name.replace(/\s/g, "_");
        console.log(file);
        shareLink = document.getElementById("shareLink");
        shareLink.setAttribute('href', href + "/" + file.name)
        shareLink.innerHTML = href + "/" + file.name;
        document.getElementById("FileUploaded").innerHTML = "File uploaded!";
    });
}