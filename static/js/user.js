
function createNode(element)
{
    return document.createElementNS(elements);
}
function append(parent,el)
{
    return parent.appendChild(el);
}

const ul = document.getElementsByClassName("SignUp");
const url = "https://127.0.0.1:8080/ap1/v1/users/registration"

fetch(url)

.then(function(data) {
    // Here you get the data to modify as you please
    })


.catch(function(error) {
    // If there is any error you will catch them here
});   