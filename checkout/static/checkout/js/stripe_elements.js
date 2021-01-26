// https://stripe.com/docs/api/payment_methods/create#create_payment_method-billing_details
// https://stripe.com/docs/api/payment_intents/confirm#confirm_payment_intent-shipping


var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    // triggers loading page 
    card.update({ 'disabled': true});
    $(".spanner").addClass("show");
    $(".overlay").addClass("show");
    // capture form data
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo, 
    };

    var url = '/checkout/cache_checkout_data/';

    // post that data to the cache view
    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form.full_name.value),
                email: $.trim(form.email.value),
                address:{
                    line1: $.trim(form.address.value),
                    city: $.trim(form.city.value),
                    country: $.trim(form.country.value),
                }
            }
        },
        shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address:{
                    line1: $.trim(form.address.value),
                    postal_code: $.trim(form.postcode.value),
                    city: $.trim(form.city.value),
                    country: $.trim(form.country.value),
            }
        },
    }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $(".spanner").removeClass("show");
                $(".overlay").removeClass("show");

                card.update({ 'disabled': false});
            } else {
                // if everything is ok, post to the form
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function(){
        location.reload();
    })
});