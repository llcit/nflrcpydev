// site.js
jQuery(function($) {
    $("#sitemap_btn").click(function () {
        $("#sitemap_panel").toggle( "blind", "down", 700 );
        $("#sitemap_btn_toggle").toggleClass("glyphicon-chevron-down glyphicon-chevron-up");
        // $("#sitemap_panel").css( "height", "100%");
    });

    $(document).ready(function() {

    });
})