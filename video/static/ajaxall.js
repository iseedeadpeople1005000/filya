jQuery("document").ready(function(){
    jQuery(".likevideo").on('click', function(){
        console.log("hello2");
            var id = jQuery(this).attr('id');
            console.log(id);
            jQuery.ajax({
                type: "GET",

                url: "/video/addlike/ajax/",

                data:{ "addlike" : id,},

                dataType: "text",

                catch: false,

                success: function(data){
                    console.log(data)
                    jQuery("#" + id + "video").html(data);
                }
            });
    });
});
jQuery("document").ready(function(){
    jQuery(".dislikevideo").on('click', function(){
        console.log("hello5");
            var id = jQuery(this).attr('id');
            console.log(id);
            jQuery.ajax({
                type: "GET",

                url: "/video/dislike/ajax/",

                data:{ "dislike" : id,},

                dataType: "text",

                catch: false,

                success: function(data){
                    console.log(data)
                    jQuery("#" + id + "video").html(data);
                }
            });
    });
});
jQuery("document").ready(function(){
    jQuery(".likecomment").on('click', function(){
        console.log("hello9");
            var id = jQuery(this).attr('id');
            jQuery.ajax({
                type: "GET",

                url: "/video/likecomment/ajax/",

                data:{ "likecomment" : id,},

                dataType: "text",

                catch: false,

                success: function(data){
                    console.log(data)
                    jQuery("#" + id + "com").html(data);
                }
            });
    });
});