

async function ReadRfid()
{
    var rfid_text = document.getElementById("rfid_response");
    rfid_text.innerHTML = "Przyłóż kartę RFID";

    let r = await fetch('hue/read_rfid', {method: "GET"});
    rfid_text.innerHTML = await r.text();
    console.log(r);
}