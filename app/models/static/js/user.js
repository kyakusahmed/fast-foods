
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


var signin_form = document.getElementById('signin_form')

signin_form.addEventListener('submit', function(event){
    //prevent pager load
    event.preventDefault()

    var email = document.getElementById('email').value
    var password = document.getElementById('password').value

    fetch('/api/v1/users/login', {
        method:'POST',
        headers: {'Content-Type' : 'application/json'},
        body:JSON.stringify({
            email:email,
            password:password
        })
    })
    .then(function(response){
        return response.json()
    })
    .then(function(response){
        console.log(response)
        if (response.access_token) {
            alert("Login successful " + response.access_token )
        } else if (response.msg) {
            alert(response.msg)
        }
    })
    .catch(function(error){
        console.log(error)
    })

    
})
