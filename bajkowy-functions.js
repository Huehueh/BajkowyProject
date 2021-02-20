

async function ReadRfid()
{
     let r = await fetch('hue/read_rfid', {method: "GET"});
     var rfid_text = document.getElementById("rfid_response");
     rfid_text.innerHTML = await r.text();
     console.log(r);
}