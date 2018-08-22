$(function () {

    $.getJSON("/movies/", function (data) {

        console.log(data);

        if(data["status"] == "200"){

            var movie_data = data["data"];

            var $ul = $("#movie_container");

            for(var i = 0; i < movie_data.length; i++){
                console.log(movie_data[i]);

                var $li = $("<li></li>");

                $li.html(movie_data[i]["m_name"]);

                $li.attr("movie_id", movie_data[i]["m_id"]);

                $li.appendTo($ul);

                $li.click(function () {

                    var li = $(this);

                    var movie_id =  li.attr("movie_id");

                    console.log(movie_id);

                    $.ajax("/movies/" + movie_id + "/", {
                        type: "DELETE",
                        success: function (data) {
                            console.log(data);

                            if(data["status"] == "204"){
                                li.remove();
                            }

                        }
                    });

                })
            }
        }
    })

    $("#add_movie").click(function () {

        var movie_name = $("#movie_name").val();

        $.post("/movies/", {"m_name": movie_name},function (data) {
            console.log(data);
        })

    })

})