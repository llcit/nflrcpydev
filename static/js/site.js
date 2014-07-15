// site.js
jQuery(function($) {
    $("#sitemap_btn").click(function () {
        $("#sitemap_panel").toggle( "blind", "down", 700 );
        $("#sitemap_btn_toggle").toggleClass("glyphicon-chevron-down glyphicon-chevron-up");
    });

    $(document).ready(function() {

    });
})