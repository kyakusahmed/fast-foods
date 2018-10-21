var sign_in_form = getElementById('sign_in_form')
var sign_up_form = getElementById('sign_up_form')

//Define base_url and base_api_url
var BASE_URL = location.protocol + "//" + location.host
var BASE_API_URL = BASE_URL + "/api/v1/"


if (sign_up_form) {
        
    sign_up_form.addEventListener('submit', function(event){
        //When form data is submitted
        var register_first_name = getElementById('first_name').value
        var register_last_name = getElementById('last_name').value
        var register_email = getElementById('email').value
        var register_password = getElementById('password').value
        var role = getElementById('role').value
        var email_error = getElementById('email-error')
        var password_error = getElementById('password-error')
        var first_name_error = getElementById('first_name-error')
        var last_name_error = getElementById('last_name-error')
        var role = getElementById("role")
        var register_info = getElementById('register-info')
        
        //Empty all error divs
        emptyDivs(first_name_error)
        emptyDivs(last_name_error)
        emptyDivs(email_error)
        emptyDivs(password_error)
        emptyDivs(register_info)
        emptyDivs(role)
        register_info.classList.remove('alert-danger')
        register_info.classList.remove('alert-success')

        //Check if password matches
        if (register_password !== register_confirm_password) {
            //If passwords don't match
            register_info.innerHTML = '<span class="error"> Oops, there was a problem:</span>'
            displayError(confirm_password_error, "Passwords do not match")

        } else {
            //Fetch data from url
            fetch(BASE_API_URL + "users/registration", {
                method: "POST",
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    first_name: register_first_name,
                    last_name: register_last_name,
                    email: register_email,
                    password: register_password,
                    role: register_role
                })
            })
            .then(function(response) {
                //Return response in form of json
                return response.json()
            })
            .then(function(responseJson) {
                //if response has errors
                register_info.classList.add('alert-danger')
                register_info.classList.remove('alert-success')
                if (responseJson.errors) {
                    for (let error of responseJson.errors) {
                        //Display error messages
                        if (error['field'] == "first_name"){
                            displayError(first_name_error, error['message'])
                        }
                        if (error['field'] == "last_name"){
                            displayError(last_name_error, error['message'])
                        }
                        if (error['field'] == "email"){
                            displayError(email_error, error['message'])
                        } 
                        if (error['field'] == "password"){
                            displayError(password_error, error['message'])
                        }
                        if (error['field'] == "role"){
                            displayError(role_error, error['message'])
                        }
                        register_info.innerHTML = '<span class="error"> Ooops... ' + responseJson['message'] +'</span>'
                    }
                } else if (responseJson.error) {
                    //If response has an error
                    register_info.innerHTML = '<span class="error"> Ooops... ' + responseJson.error +'</span>'
                } else if (responseJson.field == 'email') {
                    //If response has duplicate email error
                    register_info.innerHTML = '<span class="error"> Oops, there was a problem:</span>'
                    displayError(email_error, responseJson.message)
                } else if (responseJson.message == "User added successfully") {
                    //User successfully registered
                    register_info.classList.remove('alert-danger')
                    register_info.classList.add('alert-success')
                    register_info.innerHTML = '<span class="success">Registration successful, Please wait while we redirect you...</span>'
                    redirectToUrl('/user/login', 5000)
                } else {
                    //Return generaic error message
                    register_info.innerHTML = '<span class="error"> Ooops... Unable to process your request now.</span>'
                }
            })
            .catch(function(error) {
                // Return error message
                register_info.innerHTML = '<span class="error"> Oops, there was a problem: '+  error +'</span>'
            });
        }
        //Prevent page load
        event.preventDefault()
    })
} // End user Registration
    

