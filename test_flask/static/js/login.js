function submit_password() {
    console.log("enter submit_password")
    $.post('/login',
        {'username': $('#inputEmail').val(), 'password': $('#inputPassword').val()}
    ).done(function (data) {
        console.log(data)
        if (data.message.indexOf('successfully') > -1)
        {
            console.log("Successfully login")
            var strs = new Array();
            strs = data.message.split(/[\s\n]/);
            user = strs[4]
//            window.location.href='/mainpage'
            document.write("<form id='login' name='login_mainpage' method='post' action='mainpage'>")
            document.write("<input type='hidden' name='login_user' value='$('#inputEmail').val()'>")
            document.write("</form>")
            document.login_mainpage.submit();
        }
        else
        {
            console.log("Fail to confirm password")
        }
    }).fail(function (data) {

    });
}

function register_account() {
    console.log("enter register_account")
    $.post('/register_account',
        {'username': $('#inputEmail').val(), 'password': $('#inputPassword').val()}
    ).done(function (data) {
        console.log(data)
        if (data.message.indexOf('Successfully') > -1)
        {
            console.log("Successfully register")
            var strs = new Array();
            strs = data.message.split(/[\s\n]/);
            user = strs[4]
            window.location.href='/retype_password/' + user
//            var form = $("<form>");   //定义一个form表单 
//            form.attr('method','post');
//            form.attr('action','/register_account');  
//            $('body').append(form);  //将表单放置在web中  
//            form.submit();  //表单提交 
        }
        else
        {
            console.log("Fail to confirm password")
        }
    }).fail(function (data) {

    });
}

$(document).ready(function () {
    console.log('init')
});
