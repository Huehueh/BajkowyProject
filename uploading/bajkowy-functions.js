

async function ReadRfid()
{
    var rfid_text = document.getElementById("rfid_response");
    rfid_text.innerHTML = "Przyłóż kartę RFID";

    let r = await fetch('hue/read_rfid', {method: "GET"});
    rfid_text.innerHTML = await r.text();
    console.log(r);
}

async function UploadSound(sound)
{
    let formData = new FormData();
    formData.append("music", sound);
    try {
        let r = await fetch('/upload_sound', {method: "POST", body: formData});
        console.log('UploadSound: HTTP response code:', r.status);
        if (r.status != 200)
        {
            return;
        }
    }
    catch(e) {
        console.log("Eeee", e);
    }
}