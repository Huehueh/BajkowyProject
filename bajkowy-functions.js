

async function ReadRfid()
{
//     hostname_ = location.protocol + "//" + location.hostname + ":" + location.port;
//     let path = hostname_ + "/read_rfid";
     let r = await fetch('hue/read_rfid', {method: "GET"});
     var rfid_text = document.getElementById("rfid_response");
     console.log(r);
     rfid_text.value = r;
}