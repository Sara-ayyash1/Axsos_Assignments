let userName = document.getElementById("userName");
let requests = document.getElementById("requests"); 
let connections = document.getElementById("connections"); 

function editName() {
    userName.innerHTML = "Sara Ayyash";
}

function acceptUser(userId) {
    let element = document.getElementById(userId);
    element.remove();      

    requests.innerHTML--;   
    let connectionsCount = parseInt(connections.innerHTML)+1;
    connections.innerHTML = connectionsCount + '+'; 
}

function removeUser(userId) {
    let element = document.getElementById(userId);
    element.remove();      
    
    requests.innerHTML--;  
}