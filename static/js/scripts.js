$(document).ready(function() {

    $('#view_filters').hide();
    $('#get_filters').on('click', function() {

        $('#view_filters').slideToggle();

    });
    $('#posts').mouseenter(function() {

        $('#posts').css('border-color', '#2F7320')
    });

    $('#posts').mouseleave(function() {
        
        $('#posts').css('border-color', '#FFFFFF')

    });

});