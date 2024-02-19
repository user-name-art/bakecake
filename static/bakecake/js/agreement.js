function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}
function eraseCookie(name) {
    document.cookie = name+'=; Max-Age=-99999999;';
}



function getCookieNotification(obj) {
    var siteName = obj.siteName;
    var personalInformationLink = obj.personalInformationLink;
    var color = obj.color;
    var d1 = document.getElementsByTagName('body')[0];
    d1.insertAdjacentHTML('beforeend', '<div class="b-answer__form " id="form-accept-cookie" style="position: fixed;z-index: 99999 !important;bottom: -30px; font-family: Arial, \'Helvetica Neue\', Helvetica, sans-serif !important; font-weight: 400 !important;">    <div class="b-form__box b-form__box_custom" style="border-top: 2px solid ' + color + ';">        <fieldset class="b-form__fieldset" style="line-height: 20px !important; font-size: 12px !important;">            <label style="text-transform: none !important;">Оформляя заказы на нашем сайте, вы соглашаетесь с Политикой обработки персональных данных изложенных в <a href="/static/doc/agreement.pdf" id="personalInfoLinkSpan" style="text-decoration: underline; color: black !important;">данном документе.</a>.</label>            <div class="b-checkbox__item">                <button id="b-button-close-cookie" type="button" class="close" data-dismiss="modal" aria-hidden="true" style="cursor: pointer; position: absolute; top: -8px; right: -120px; font-size: 25px; font-weight: bold; border: 0px; color: ' + color + ' !important; background: none !important;">                    ×                </button>                <button id="b-button-submit" type="button " class="button blue button_custom" style="background-color: ' + color + ';"><span>Подтверждаю ознакомление и согласие</span>   </button> <span style="float: right !important; font-size: 12px !important; padding-top: 21px !important; position:relative !important; right: -115px;" id="copyright"><a href=\'https://devman.org/\' title=\'поставить виджет согласия с куки на сайт\'>© Разработано для проекта на курсе Devman</a></span>                </div>        </fieldset>    </div>    <style type="text/css" id="widgetStyles">        #form-accept-cookie :focus:-moz-placeholder,#form-accept-cookie :focus::-moz-placeholder{color:transparent!important;}        #form-accept-cookie :focus::-webkit-input-placeholder{color:transparent!important;}        #form-accept-cookie *,:after,:before{margin:0;padding:0;box-sizing:border-box;}        #form-accept-cookie div{-webkit-tap-highlight-color:transparent;}        #form-accept-cookie a{color:inherit;text-decoration:none;}        #form-accept-cookie a:active,a:focus,a:hover{text-decoration:none;}        #form-accept-cookie fieldset{border:none;}        #form-accept-cookie .button{height:40px;border:none;outline:none;font-size:14px;padding-left:17px;padding-right:17px;cursor:pointer;background:#e2e7f0;position:relative;transition:200ms;}        #form-accept-cookie .button:not(.no-arrow){padding-right:40px;}        #form-accept-cookie .button:not(.no-arrow):before{content:"";width:11px;height:11px;position:absolute;top:0;bottom:0;right:18px;margin:auto;border-right:1px solid #000;border-top:1px solid #000;-webkit-transform:rotate(45deg);-ms-transform:rotate(45deg);transform:rotate(45deg);transition:200ms;}    ' +
        '@media screen and (max-width: 1164px) {\n' +
        '     #b-button-close-cookie { right: -80px !important; }' +
        '#copyright { right: -75px !important; }\n' +
        '   }' +
        '@media screen and (max-width: 655px) {\n' +
        '     #b-button-close-cookie { right: -40px !important; }' +
        '   }' +
        '@media screen and (max-width: 779px) {\n' +
        '#copyright { display: none !important; }\n' +
        '   }' +
        '    #form-accept-cookie .button span{color:#333;font-weight:700;text-transform:uppercase;letter-spacing:1px;transition:200ms;}        #form-accept-cookie .button:not(.gray):hover{background:#178acb;}        #form-accept-cookie .button:not(.gray):hover span{color:#fff;}        #form-accept-cookie .button:not(.gray):hover:before{border-right-color:#fff;border-top-color:#fff;}        #form-accept-cookie .button:not(.gray):active{background:#126b9d;}        #form-accept-cookie .button.blue{background:#41579e;}        #form-accept-cookie .button.blue:hover{background:#178acb;}        #form-accept-cookie .button.blue:active{background:#126b9d;} #form-accept-cookie #b-button-close-cookie:after { content: none;} #form-accept-cookie #b-button-close-cookie:before { content: none;}      #form-accept-cookie .button.blue:before{border-right-color:#fff;border-top-color:#fff;}        #form-accept-cookie .button.blue span{color:#fff;}        #form-accept-cookie .b-form__box{background:#f6f8fa;padding:35px 35px 15px;}   #form-accept-cookie *{font-weight: 400 !important;}     @media screen and (max-width: 767px){            #form-accept-cookie .b-form__box{padding:25px 20px 5px;}        }        #form-accept-cookie .b-form__box .b-checkbox__item{margin:15px 0;}        #form-accept-cookie .b-form__fieldset{position:relative; max-width: 92%;}        @media (min-width: 768px){            #form-accept-cookie .b-form__fieldset{margin-bottom:30px;}        }        @media screen and (max-width: 767px){            #form-accept-cookie .b-form__fieldset{margin-bottom:35px;}        }        /*! CSS Used from: Embedded */        #form-accept-cookie .b-form__box_custom{background:#f6f8fa;padding:15px 35px 5px;border-top:2px solid #41579e;background:#dfe3e3!important;}        #form-accept-cookie .button_custom{font-size:12px;}    </style></div>');


    if (getCookie('cookieLawNotification-' + window.location.hostname) == null){
        document.getElementById('form-accept-cookie').style.display = 'block';
    }else{
        document.getElementById('form-accept-cookie').style.display = 'none';
    }

    document.getElementById('b-button-close-cookie').onclick = function(){
        document.getElementById('form-accept-cookie').style.display = 'none';
    };

    document.getElementById('b-button-submit').onclick = function(){
        setCookie('cookieLawNotification-' + window.location.hostname, '1', 18000);
        document.getElementById('form-accept-cookie').style.display = 'none';
    };
}
