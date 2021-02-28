

async function ReadRfid()
{
    var rfid_text = document.getElementById("rfid_response");
    rfid_text.value = "Przyłóż kartę RFID";

    let r = await fetch('hue/read_rfid', {method: "GET"});
    rfid_text.value = await r.text();
    console.log(r);
}
