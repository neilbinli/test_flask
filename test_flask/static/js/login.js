function submit_password() {
    console.log("enter submit_password")
    $.post('/login',
        {'username': $('#inputEmail').val(), 'password': $('#inputPassword').val()}
    ).done(function (data) {
        console.log(data)
        // window.location.href='/login'
    }).fail(function (data) {

    });
}

function register_account() {
    console.log("enter register_account")
    $.post('/register_password',
        {'username': $('#inputEmail').val(), 'password': $('#inputPassword').val(), 'is_confirm': 'False'}
    ).done(function (data) {
        console.log(data)
    }).fail(function (data) {

    });
}

$(document).ready(function () {
    console.log('init')
});
